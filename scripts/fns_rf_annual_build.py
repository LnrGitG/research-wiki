#!/usr/bin/env python3
"""Нашёл: старые снимки 5-П в cp1251! Декодировать как cp1251 при неудаче utf-8.
Пересобираем длинные ряды с кодировочной поддержкой."""
import csv, io, re, glob
import pandas as pd

def parse_snap(s):
    y = int(s[:4])
    if 2000 <= y <= 2030 and 1 <= int(s[4:6]) <= 12:
        return s
    return f'{s[4:]}{s[2:4]}{s[:2]}'

def read_fns_csv(path):
    raw = open(path, 'rb').read()
    for enc in ('utf-8', 'cp1251'):
        try:
            txt = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    first = txt.splitlines()[0]
    delim = ';' if first.count(';') > first.count(',') else ','
    return list(csv.reader(io.StringIO(txt), delimiter=delim))

def is_region(s):
    s = (s or '').strip()
    if len(s) < 5 or s == 'nan': return False
    if re.search(r'^[\d\s.,—\-Xx]+$', s): return False
    if 'данные по' in s: return False
    if not re.search(r'[А-Яа-яA-Za-z]{4,}', s): return False
    return True

def rf_sum(rows, hdr, col):
    if col not in hdr: return None
    idx = hdr.index(col); tot = 0.0; n = 0
    for r in rows[1:]:
        if len(r) <= idx: continue
        if not is_region(r[0]): continue
        try:
            tot += float((r[idx] or '0').replace(' ', '').replace(',', '.') or 0); n += 1
        except ValueError: pass
    return tot if n >= 60 else None

METRICS = {
    'profitorg': {'GB': 'rev_profit', 'G1': 'rev_loss', 'G2': 'nonop_inc_profit', 'G4': 'exp_sales_profit', 'G6': 'nonop_exp_profit'},
    'taxagent': {'GB': 'income_total', 'G1': 'ndfl_withheld'},
    '1nds': {'GB': 'nds_accrued_total'},
    'usn': {'GB': 'usn_income', 'G1': 'usn_expense'},
    'ttorg': {'GB': 'tnpayers'},
}
CODE_LABEL = {'profitorg': '5-П', 'taxagent': '5-НДФЛ', '1nds': '1-НДС', 'usn': '5-УСН', 'ttorg': '5-ТН'}

out = []
for code, mets in METRICS.items():
    iso2file = {}
    for f in glob.glob(f'raw/fns/{code}_????????.csv'):
        raw = re.search(code + r'_(\d{8})\.csv', f).group(1)
        iso2file[parse_snap(raw)] = f
    by_year = {}
    for iso in sorted(iso2file):
        rows = read_fns_csv(iso2file[iso])
        hdr = rows[0]
        y = int(iso[:4]) - (1 if iso.endswith('0101') else 0)
        vals = {mm: rf_sum(rows, hdr, c) for c, mm in mets.items()}
        if any(v is not None for v in vals.values()):
            by_year[y] = (iso, vals)
    for y, (iso, vals) in sorted(by_year.items()):
        for m, v in vals.items():
            if v is not None:
                out.append({'form': CODE_LABEL[code], 'metric': m, 'year': y,
                            'rf_value_bln_rub': round(v / 1e6, 1), 'snapshot': iso})

df = pd.DataFrame(out).drop_duplicates(subset=['form', 'metric', 'year'], keep='last').sort_values(['form', 'metric', 'year'])
df['partial'] = (df.year == 2026).astype(int)
df.to_csv('data/fns_rf_annual_long.csv', index=False)
piv = df.pivot_table(index='year', columns=['form', 'metric'], values='rf_value_bln_rub')
pd.set_option('display.float_format', lambda v: f'{v:,.1f}')
print('записей:', len(df)); print(piv.to_string())
import sqlite3
con = sqlite3.connect('data/rosreestr_deals.db')
df.to_sql('fns_rf_annual', con, if_exists='replace', index=False)
con.commit(); con.close()