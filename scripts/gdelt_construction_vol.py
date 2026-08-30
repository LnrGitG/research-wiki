#!/usr/bin/env python3
"""Строительный счётчик GDELT v2: только 2 запроса (construction + infrastructure project),
режим timelinevol, окно 2022-2026 (в остальных годах API нестабилен), пауза 12с между запросами.
Цель — помесячный ряд для наукаста ИКВ. Работаем по годам с ретраями черезsaraskip:
- конструкта: construction (широкое понятие, ок для год-на-месяц граф)
- инфраструктура: infrastructure project
Собираем tone И volume. Выход: data/gdelt_construction_vol_monthly.csv"""
import json, time, sys, urllib.request, urllib.parse
from collections import defaultdict

QUERIES = ['construction', 'infrastructure project']
UA = {'User-Agent': 'Mozilla/5.0'}
OUT = '/home/lnr/research-wiki/data/gdelt_construction_vol_monthly.csv'

def fetch(q, sd, ed, tries=3):
    url = ('https://api.gdeltproject.org/api/v2/doc/doc?query=' + urllib.parse.quote(q)
           + '+sourcecountry:RS&mode=timelinevol&format=json&startdatetime=' + sd + '&enddatetime=' + ed)
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                t = r.read().decode('utf-8', 'replace')
            if t.strip().startswith('{'):
                return json.loads(t)
            time.sleep(20 * (i + 1))
        except Exception as e:
            print('  retry', i, e, file=sys.stderr)
            time.sleep(20 * (i + 1))
    return {}

agg = defaultdict(lambda: [0, 0.0])   # (ym, query) -> [days, sum_vol]
years = list(range(2022, 2027))
for q in QUERIES:
    for y in years:
        sd = f'{y}0101000000'
        ed = f'{y}1231235959'
        d = fetch(q, sd, ed)
        time.sleep(12)
        tl = d.get('timeline') or []
        n = sum(len(s.get('data') or []) for s in tl)
        print(f'{q!r} {y}: {n} days', flush=True)
        for s in tl:
            for rec in s.get('data') or []:
                date = rec.get('date', '')
                val = rec.get('value')
                if date and val is not None:
                    ym = date[:4] + '-' + date[4:6]
                    a = agg[(ym, q)]
                    a[0] += 1
                    a[1] += float(val)

rows = []
for (ym, q), (n, s) in sorted(agg.items()):
    rows.append(f'{ym},{q!r},{n},{round(n and s/n, 3)}')
with open(OUT, 'w') as f:
    f.write('month,query,n_days,vol_mean\n')
    f.write('\n'.join(rows))
print('saved', len(rows), 'rows ->', OUT)