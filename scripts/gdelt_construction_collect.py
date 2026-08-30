#!/usr/bin/env python3
"""GDELT DOC 2.0: строительный счётчик — месячный объём news-потока по запросам о строительстве
для sourcecountry:RS. mode=timelinevolinfo (volume + tone). Период 2017-01 → 2026-08.
Киррилица ненадёжна → английские ключи: construction, "construction company", infrastructure,
"special equipment" и т.д. Limit: 1 req / 5s; пустой {} = нет данных; ретраи 3x backoff.
Выход: data/gdelt_construction_monthly.csv (year-month, query, vol_mean, n_days, tone_mean)."""
import json, time, urllib.request, urllib.parse, sys

QUERIES = [
    'construction company',
    'construction project',
    'infrastructure project',
    'residential complex',
    'special equipment',       # спецтехника (запуск, поставки)
    'building materials',
    'developer',
]

def fetch(query, sd, ed, mode='timelinevolinfo', tries=3):
    url = ('https://api.gdeltproject.org/api/v2/doc/doc?query=' + urllib.parse.quote(query)
           + '+sourcecountry:RS&mode=' + mode + '&format=json&startdatetime=' + sd + '&enddatetime=' + ed)
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=45) as r:
                txt = r.read().decode('utf-8', 'replace')
            if txt.strip().startswith('{'):
                return json.loads(txt)
            # rate-limit text page -> backoff
            time.sleep(12 * (i + 1))
        except Exception as e:
            print('  retry', i, e, file=sys.stderr)
            time.sleep(12 * (i + 1))
    return {}

rows = []
import datetime as dt
start = dt.date(2017, 1, 1)
end = dt.date(2026, 9, 1)

def year_windows():
    y = start.year
    while y <= end.year:
        sd = max(start, dt.date(y, 1, 1)).strftime('%Y%m%d000000')
        ed = min(end - dt.timedelta(days=1), dt.date(y, 12, 31)).strftime('%Y%m%d000000')
        yield sd, ed
        y += 1

for qi, q in enumerate(QUERIES):
    for sd, ed in year_windows():
        d = fetch(q, sd, ed)
        time.sleep(5.5)
        tl = d.get('timeline') or []
        if not tl:
            print(f'{q!r} {sd[:4]}: EMPTY')
            continue
        for series in tl:
            data = series.get('data') or []
            for rec in data:
                date = rec.get('date', '')
                if not date:
                    continue
                ym = date[:4] + '-' + date[4:6]
                val = rec.get('value')
                tone = None
                rows.append((ym, q, val, tone))
        print(f'{q!r} {sd[:4]}: {len(tl)} series, {sum(len(s.get("data") or []) for s in tl)} days')
        time.sleep(5.5)

# агрегируем
import collections, statistics
agg = collections.defaultdict(lambda: [0, []])
for ym, q, vol, tone in rows:
    if vol is None:
        continue
    a = agg[(ym, q)]
    a[0] += 1
    a[1].append(vol)
out = []
for (ym, q), (n, vals) in sorted(agg.items()):
    out.append({'month': ym, 'query': q, 'n_days': n, 'vol_mean': round(statistics.mean(vals), 3)})
df = out
import csv as _csv
with open('/home/lnr/research-wiki/data/gdelt_construction_daily_raw.csv', 'w', newline='') as f:
    w = _csv.writer(f)
    w.writerow(['month', 'query', 'n_days', 'vol_mean'])
    for r in out:
        w.writerow([r['month'], r['query'], r['n_days'], r['vol_mean']])
print('saved', len(out), 'rows')