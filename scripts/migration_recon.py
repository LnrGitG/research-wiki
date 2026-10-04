#!/usr/bin/env python3
"""Разведка перед переездом: структура источника и приёмника, распределение периодов."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query


def cols(schema, table):
    return [(r[0], r[1]) for r in query(
        "SELECT column_name, data_type FROM information_schema.columns "
        "WHERE table_schema=%s AND table_name=%s ORDER BY ordinal_position",
        (schema, table))]


print("=== core.observation_v2 ===")
for c, t in cols("core", "observation_v2"):
    print(f"   {c:20s} {t}")
print("   строк:", query("SELECT count(*) FROM core.observation_v2")[0][0])

print("\n=== data.observation (приёмник) ===")
for c, t in cols("data", "observation"):
    print(f"   {c:20s} {t}")

print("\n=== распределение наблюдений по годам ===")
for r in query("""SELECT date_part('year', period_start)::int AS yr, count(*) AS n
                  FROM core.observation_v2 GROUP BY 1 ORDER BY 1"""):
    print(f"   {r[0]}: {r[1]:>9,}")

print("\n=== период: min/max ===")
print("  ", query("SELECT min(period_start), max(period_start), "
                   "count(DISTINCT date_trunc('month', period_start)) "
                   "FROM core.observation_v2")[0])

print("\n=== core.metric ===")
for c, t in cols("core", "metric"):
    print(f"   {c:20s} {t}")

print("\n=== core.source / release / unit / frequency ===")
for tbl in ("source", "release", "unit", "frequency"):
    print(f"  {tbl}: " + ", ".join(c for c, _ in cols("core", tbl)))

print("\n=== region_id: сколько различных, диапазон ===")
print("  ", query("SELECT count(DISTINCT region_id), min(region_id), max(region_id) "
                   "FROM core.observation_v2")[0])

print("\n=== core.region (если есть) ===")
try:
    print("   строк:", query("SELECT count(*) FROM core.region")[0][0])
    print("   колонки:", [c for c, _ in cols("core", "region")])
except Exception as e:
    print("   ERR", str(e)[:100])

print("\n=== NULL-и в ключевых полях ===")
print("  ", query("""SELECT
      count(*) FILTER (WHERE metric_id IS NULL) AS null_metric,
      count(*) FILTER (WHERE region_id IS NULL) AS null_region,
      count(*) FILTER (WHERE period_start IS NULL) AS null_period,
      count(*) FILTER (WHERE value IS NULL) AS null_value
    FROM core.observation_v2""")[0])