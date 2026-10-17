#!/usr/bin/env python3
"""Разовая сверка после слияния релизов ИКВ (см. merge_ikv_releases.py)."""
import csv
import gzip
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as t  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("=== состояние группы ===")
for r in t.query("""SELECT m.metric_code, m.status, o.release_id, r.release_label, count(*) n
  FROM data.observation o JOIN core.metric m USING(metric_id)
  JOIN core.release r USING(release_id)
  WHERE m.metric_code IN ('iokmrrk','iokmrrkri','iokspr') GROUP BY 1,2,3,4"""):
    print(r)
print("карточка 59561:", t.query(
    "SELECT metric_id, metric_code, status, right(coalesce(description,''),70) "
    "FROM core.metric WHERE metric_id=59561"))
print("release 77 существует:", t.query(
    "SELECT count(*) FROM catalog.release WHERE release_id=77"))
print("release 1 несёт 482:", t.query(
    "SELECT count(*) FROM data.observation WHERE metric_id=482 AND release_id=1"))
print("release 1 всего строк:", t.query(
    "SELECT count(*) FROM data.observation WHERE release_id=1"))

print("=== сверка значений с дампом точки возврата ===")
names = sorted(f for f in os.listdir(os.path.join(REPO, 'attic'))
               if f.startswith('ikv_reg_merge_before_'))
path = os.path.join(REPO, 'attic', names[-1])
print("дамп:", names[-1])
old = {}
with gzip.open(path, 'rt', encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        old[(int(row['metric_id']), int(row['region_id']), row['period_start'],
             row['sub_dimension'])] = float(row['value'])
print("в дампе строк:", len(old))
cur = {(int(m), int(r), str(p), s): float(v) for m, r, p, s, v in t.query(
    "SELECT metric_id, region_id, period_start, sub_dimension, value "
    "FROM data.observation WHERE metric_id IN (482,1927)")}
print("в каноне строк (482+1927):", len(cur))
kept = {k: v for k, v in old.items() if k[0] in (482, 1927)}
lost = set(kept).difference(cur)
added = set(cur).difference(kept)
print("потеряно ключей:", len(lost), "добавлено:", len(added))
diff = [k for k in set(kept).intersection(cur) if abs(kept[k] - cur[k]) > 1e-6]
print("расхождений значений:", len(diff))
print("снято строк дубля:", len([k for k in old if k[0] == 59561]))
print("контроль сумм: до", round(sum(kept.values()), 3), "после", round(sum(cur.values()), 3))

print("=== остались ли дубли в семействе ИКВ ===")
rows = t.query("""SELECT a.metric_code, b.metric_code, count(*) n FROM data.observation x
  JOIN core.metric a ON a.metric_id=x.metric_id
  JOIN data.observation y ON y.region_id=x.region_id AND y.period_start=x.period_start
    AND y.value=x.value
  JOIN core.metric b ON b.metric_id=y.metric_id
  WHERE a.metric_code ~ '^(iokm|ikv|iok)' AND b.metric_code ~ '^(iokm|ikv|iok)'
    AND x.metric_id<y.metric_id GROUP BY 1,2 ORDER BY 3 DESC""")
print(rows if rows else "нет")
print("=== канон целиком ===",
      t.query("SELECT count(*) FROM data.observation")[0][0], "наблюдений,",
      t.query("SELECT count(*) FROM catalog.metric")[0][0], "метрик")
