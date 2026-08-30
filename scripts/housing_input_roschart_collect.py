#!/usr/bin/env python3
"""Финальная загрузка: 4 датасета ввода жилья + незавершёнка → SQLite (rosreestr_deals.db).
Таблица: housing_input_annual (region, year, value) + housing_backlog_ratio."""
import json, sqlite3, urllib.request, ssl, pandas as pd
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0'}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
        return json.load(r)

DB = 'data/rosreestr_deals.db'
con = sqlite3.connect(DB)
con.execute("""CREATE TABLE IF NOT EXISTS housing_input_annual (
    region TEXT, year INT, value REAL, source TEXT,
    PRIMARY KEY (region, year, source))""")
con.execute("""CREATE TABLE IF NOT EXISTS housing_backlog_ratio_annual (
    region TEXT, year INT, value REAL,
    PRIMARY KEY (region, year))""")

DATASETS = [
    ('pril-invest-2025-7-5-vvod-v-deystvie-zhilyh-domov', 'roschart_pril_invest_2025_7_5'),
    ('stroi-133-2025-vvod-v-deystvie-zhilyh-domov-organizaciyami-r', 'roschart_stroi_133_2025'),
]
BACKLOG = 'stroi-3-2025-otnoshenie-obschey-ploschadi-nezavershennyh-zhi'
LONG_RF = 'ejegod-18-2024-18-8-vvod-v-deystvie-zhilyh-domov'

total = 0
for ds, src in DATASETS:
    d = get(f'https://roschart.ru/api/dataset/{ds}')['dataset']
    periods = d['periods']
    for s in d['series']:
        region = s['label']
        for y, v in zip(periods, s['values']):
            if v is None: continue
            con.execute("INSERT OR REPLACE INTO housing_input_annual VALUES (?,?,?,?)",
                        (region, int(str(y)[:4]), v, src))
            total += 1
    print(f'{ds[:40]}: +{len(d["series"])} series / {len(periods)} yrs')

# незавершёнка
d = get(f'https://roschart.ru/api/dataset/{BACKLOG}')['dataset']
n_back = 0
for s in d['series']:
    for y, v in zip(d['periods'], s['values']):
        if v is None: continue
        con.execute("INSERT OR REPLACE INTO housing_backlog_ratio_annual VALUES (?,?,?)",
                    (s['label'], int(str(y)[:4]), v))
        n_back += 1
print(f'backlog: {n_back} values')

con.commit()
# верификация
v = pd.read_sql("SELECT source, COUNT(*) n, MIN(year) y0, MAX(year) y1, COUNT(DISTINCT region) regs FROM housing_input_annual GROUP BY source", con)
print(v.to_string(index=False))
rf = pd.read_sql("SELECT year, value FROM housing_input_annual WHERE region='Российская Федерация' AND source='roschart_pril_invest_2025_7_5' ORDER BY year", con)
print('\nРФ ввод жилья, млн кв.м (тыс.→млн = /1000):')
rf['mln_m2'] = (rf.value/1000).round(1)
print(rf[['year', 'mln_m2']].to_string(index=False))
con.close()