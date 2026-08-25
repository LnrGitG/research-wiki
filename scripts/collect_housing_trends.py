#!/usr/bin/env python3
"""Housing sentiment index via pytrends (Google Trends, RU) following QUIET recipe.
Collect monthly series 2018-2026 for housing dictionary, validate, PCA -> index."""
import time, json
import pandas as pd
import numpy as np
from pytrends.request import TrendReq

DICT = {
    'ипотека': 'mortgage',
    'ключевая ставка': 'key_rate',
    'купить квартиру': 'buy_flat',
    'новостройки': 'new_build',
    'вторичное жильё': 'secondary',
    'снять квартиру': 'rent',
    'цены на квартиры': 'flat_prices',
    'инфляция': 'inflation',
    'курс доллара': 'usd',
}

pt = TrendReq(hl='ru-RU', tz=180, timeout=(10, 25))

# Google Trends caps 5 terms per payload; batch and splice via overlapping anchor term
TF = '2018-01-01 2026-08-31'
series = {}
anchor = 'ипотека'

terms = list(DICT.keys())
batches = []
# first batch: anchor + up to 4; subsequent batches: anchor + next (anchor overlaps for rescaling)
i = 0
while i < len(terms):
    batch = [anchor] + [t for t in terms[i:i+4] if t != anchor]
    if len(batch) == 1:
        break
    batches.append(batch)
    if anchor in terms[i:i+4]:
        i += 4
    else:
        i += 4

print("batches:", batches)
for b in batches:
    ok = False
    for attempt in range(3):
        try:
            pt.build_payload(b, timeframe=TF, geo='RU')
            df = pt.interest_over_time()
            if df is None or df.empty:
                raise RuntimeError("empty")
            for col in b:
                s = df[col].dropna()
                s = s[s.index <= pd.Timestamp('2026-08-01')]
                series[col] = s.astype(float)
            print(f"OK {b}: {len(df)} rows")
            ok = True
            break
        except Exception as e:
            print(f"retry {attempt+1} {b}: {str(e)[:80]}")
            time.sleep(8 * (attempt + 1))
    if not ok:
        print(f"FAILED {b}")
    time.sleep(5)

# Splice: each batch scaled within itself 0-100 with ипотека common. Rescale all to ипотека's series.
base = series[anchor]
result = {'ипотека': base}
for col, s in series.items():
    if col == anchor:
        continue
    # correlation window overlap check
    joined = pd.concat([base.rename('a'), s.rename('b')], axis=1).dropna()
    if len(joined) < 24:
        print(f"SKIP {col}: overlap {len(joined)}")
        continue
    # ratio of medians over full period (both cover same TF so directly comparable scale-wise? No -
    # each payload is normalized independently. Use regression on overlap: b = k*a -> rescale.
    # Simplest robust: k = median(b/a) over points where a>1
    mask = (joined['a'] > 1) & (joined['b'] > 0)
    if mask.sum() < 12:
        mask = joined['b'] > 0
    k = (joined.loc[mask, 'b'] / joined.loc[mask, 'a']).median()
    result[col] = s / k

df_all = pd.DataFrame(result)
df_all.to_csv('/home/lnr/research-wiki/data/search_trends_housing_raw.csv', float_format='%.2f')
print("\ncollected:", df_all.shape)
print(df_all.describe().round(1).loc[['mean', 'min', 'max']].to_string())
