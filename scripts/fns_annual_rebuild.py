#!/usr/bin/env python3
"""Нормализация через rebuild: сырые таблицы left as-is; annual заново с нормализацией."""
import sqlite3, pandas as pd, re

con = sqlite3.connect('data/rosreestr_deals.db')

def norm(r):
    r = (r or '').strip()
    m = {
        'Г.Санкт-Петербург': 'г. Санкт-Петербург', 'г.Санкт-Петербург': 'г. Санкт-Петербург',
        'город Санкт-Петербург': 'г. Санкт-Петербург',
        'Г.Севастополь': 'г. Севастополь', 'г.Севастополь': 'г. Севастополь',
        'город Севастополь': 'г. Севастополь',
        'Ямало-Hенецкий АО': 'Ямало-Ненецкий АО',
    }
    return m.get(r, r)

con.execute("DROP TABLE IF EXISTS fns_annual_regional")
con.execute("""CREATE TABLE fns_annual_regional (
    form TEXT, region TEXT, year INT, metric TEXT, value REAL,
    PRIMARY KEY (form, region, year, metric))""")

q = pd.read_sql("SELECT region, snapshot_date snap, value FROM fns_1nom_okved_f_quarterly WHERE metric='G53_okved_F'", con)
q['region'] = q.region.map(norm)
q['snap'] = pd.to_datetime(q.snap.astype(str), format='%Y%m%d')
q['rep_year'] = q.snap.dt.year - (q.snap.dt.month == 1).astype(int)
last = q.sort_values('snap').groupby(['region', 'rep_year']).tail(1)
for _, r in last.iterrows():
    con.execute("INSERT OR REPLACE INTO fns_annual_regional VALUES ('1nom_okved_F',?,?, 'G53_okved_F',?)",
                (r.region, int(r.rep_year), r.value))

n2m = pd.read_sql("SELECT region, snapshot snap, value FROM fns_profitorg_key_quarterly WHERE field LIKE 'Доходы от реализации по прибыльным%'", con)
n2m['region'] = n2m.region.map(norm)
n2m['snap'] = pd.to_datetime(n2m.snap.astype(str), format='%Y%m%d')
n2m['year'] = n2m.snap.dt.year - (n2m.snap.dt.month == 1).astype(int)
n2last = n2m.sort_values('snap').groupby(['region', 'year']).tail(1)
for _, r in n2last.iterrows():
    con.execute("INSERT OR REPLACE INTO fns_annual_regional VALUES ('profitorg',?,?,'rev_profit',?)",
                (r.region, int(r['year']), r.value))

n3 = pd.read_sql("SELECT region, snapshot snap, value FROM fns_ndfl_regional WHERE field='G1'", con)
n3['region'] = n3.region.map(norm)
n3['snap'] = pd.to_datetime(n3.snap.astype(str), format='%Y%m%d')
n3['year'] = n3.snap.dt.year - (n3.snap.dt.month == 1).astype(int)
for _, r in n3.iterrows():
    con.execute("INSERT OR REPLACE INTO fns_annual_regional VALUES ('ndfl',?,?,'ndfl',?)",
                (r.region, int(r['year']), r.value))
con.commit()

print(pd.read_sql("""SELECT form, COUNT(*) n, COUNT(DISTINCT region) regs, COUNT(DISTINCT year) yrs
                     FROM fns_annual_regional GROUP BY form""", con).to_string(index=False))
rb = pd.read_sql("""SELECT year, form, value FROM fns_annual_regional
                    WHERE region='Республика Башкортостан' ORDER BY year, form""", con)
print('\nБашкортостан, годовые (тыс. руб.):')
print(rb.pivot_table(index='year', columns='form', values='value').to_string())
con.close()