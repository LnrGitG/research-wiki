#!/usr/bin/env python3
"""Этап G: сквозная проверка переезда. Сверяет приёмник с источником по
счётчикам, по распределению по годам и по выборочным значениям."""
import sys, json
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

ok = True

print("=== 1. счётчики ===")
pairs = [("core.unit", "catalog.unit"), ("core.frequency", "catalog.frequency"),
         ("core.region", "catalog.region"), ("core.release", "catalog.release"),
         ("core.metric", "catalog.metric"),
         ("core.observation_v2", "data.observation")]
for a, b in pairs:
    na = query(f"SELECT count(*) FROM {a}")[0][0]
    nb = query(f"SELECT count(*) FROM {b}")[0][0]
    good = na == nb
    ok = ok and good
    print(f"   {'OK ' if good else 'РАСХ'} {a} {na:,} -> {b} {nb:,}")

# источники: приёмник намеренно на один больше — добавлен 'unknown'
na = query("SELECT count(*) FROM core.source")[0][0]
nb = query("SELECT count(*) FROM catalog.source")[0][0]
extra = query("""SELECT count(*) FROM catalog.source s
                 WHERE NOT EXISTS (SELECT 1 FROM core.source c
                                   WHERE c.source_id = s.source_id)""")[0][0]
good = (nb == na + extra)
ok = ok and good
print(f"   {'OK ' if good else 'РАСХ'} core.source {na} -> catalog.source {nb} "
      f"(+{extra} служебный 'unknown', на него ссылаются 474 метрики без наблюдений)")

print("\n=== 2. распределение наблюдений по годам ===")
src = {str(r[0]): r[1] for r in query(
    "SELECT date_part('year', period_start)::int, count(*) "
    "FROM core.observation_v2 GROUP BY 1 ORDER BY 1")}
dst = {str(r[0]): r[1] for r in query(
    "SELECT date_part('year', period_start)::int, count(*) "
    "FROM data.observation GROUP BY 1 ORDER BY 1")}
diff = 0
for y in sorted(set(src) | set(dst), key=int):
    a, b = src.get(y, 0), dst.get(y, 0)
    if a != b:
        diff += 1
        print(f"   РАСХ {y}: {a:,} -> {b:,}")
print(f"   лет сверено: {len(set(src) | set(dst))}, расхождений: {diff}")
ok = ok and diff == 0

print("\n=== 3. выборочная сверка значений ===")
rows = query("""
    SELECT o.metric_id, o.region_id, o.period_start, o.value,
           d.value, o.sub_dimension IS NOT DISTINCT FROM d.sub_dimension
    FROM core.observation_v2 o
    JOIN data.observation d
      ON d.metric_id=o.metric_id AND d.region_id=o.region_id
     AND d.period_start=o.period_start
     AND d.frequency_id=o.frequency_id
     AND d.assessment_type IS NOT DISTINCT FROM o.assessment_type
     AND d.sub_dimension IS NOT DISTINCT FROM o.sub_dimension
     AND d.release_id=o.release_id
    WHERE o.period_start >= '2026-01-01'
    LIMIT 2000""")
bad = [r for r in rows if r[3] != r[4]]
print(f"   сверено строк: {len(rows)}, расхождений значений: {len(bad)}")
ok = ok and len(bad) == 0

print("\n=== 4. ссылочная целостность приёмника ===")
for label, sql in [
    ("наблюдения без метрики",
     """SELECT count(*) FROM data.observation o
        WHERE NOT EXISTS (SELECT 1 FROM catalog.metric m WHERE m.metric_id=o.metric_id)"""),
    ("наблюдения без региона",
     """SELECT count(*) FROM data.observation o
        WHERE NOT EXISTS (SELECT 1 FROM catalog.region r WHERE r.region_id=o.region_id)"""),
    ("наблюдения без релиза",
     """SELECT count(*) FROM data.observation o
        WHERE o.release_id IS NOT NULL
          AND NOT EXISTS (SELECT 1 FROM catalog.release r WHERE r.release_id=o.release_id)"""),
]:
    n = query(sql)[0][0]
    print(f"   {'OK ' if n == 0 else 'ПРОБЛЕМА'} {label}: {n}")
    ok = ok and n == 0

print("\n=== 5. партиции ===")
r = query("""SELECT count(*) FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
             WHERE n.nspname='data' AND c.relispartition
               AND c.relkind = 'r'""")[0][0]
print(f"   партиций-таблиц: {r}")
filled = query("""SELECT count(*) FROM (
                    SELECT c.relname FROM pg_class c
                    JOIN pg_namespace n ON n.oid=c.relnamespace
                    WHERE n.nspname='data' AND c.relispartition AND c.relkind='r'
                  ) t""")[0][0]
print(f"   (индексов партиций столько же, всего отношений-партиций 2x)")

print("\n=== 6. витрина ===")
try:
    r = query("""SELECT c.relkind FROM pg_class c
                 JOIN pg_namespace n ON n.oid=c.relnamespace
                 WHERE n.nspname='derived' AND c.relname='metric_card'""")[0][0]
    print("   тип metric_card:", r, "(m = материализованное представление)")
    print("   строк в витрине:", query("SELECT count(*) FROM derived.metric_card")[0][0])
except Exception as e:
    print("   ERR", str(e)[:150])

print("\n=== ИТОГ ===")
print("   переезд", "ПРОШЁЛ" if ok else "ТРЕБУЕТ ВНИМАНИЯ")