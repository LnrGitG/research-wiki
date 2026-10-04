#!/usr/bin/env python3
"""Сколько поколений таблиц наблюдений живёт одновременно и не дублируют ли они друг друга."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import db_tunnel  # noqa: E402


def rows(sql, params=None):
    try:
        return db_tunnel.query(sql, params)
    except Exception as exc:  # noqa: BLE001
        print(f"  не прошло: {type(exc).__name__}: {str(exc).splitlines()[0]}")
        return None


print("=== Все таблицы, похожие на хранилище наблюдений ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname AS tbl, c.reltuples::bigint, "
    "pg_size_pretty(pg_relation_size(c.oid)) AS heap, "
    "pg_size_pretty(pg_indexes_size(c.oid)) AS idx, "
    "pg_size_pretty(pg_total_relation_size(c.oid)) AS total, "
    "pg_total_relation_size(c.oid) AS bytes "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relkind IN ('r','p') AND (c.relname LIKE '%observation%' "
    "   OR c.relname LIKE '%obs%') AND n.nspname NOT LIKE 'pg\\_%' "
    "ORDER BY bytes DESC LIMIT 20"
)
if r:
    tot = 0
    for x in r:
        tot += x[5]
        print(f"  {x[0]:<42} ~строк={x[1]:>9} куча={x[2]:>9} инд={x[3]:>9} всего={x[4]:>9}")
    print(f"  ИТОГО по таблицам наблюдений: {tot/1024**3:.2f} ГБ")

print("\n=== Сколько строк в каждой генерации (точно) ===")
gens = [
    ("core.observation_v2", "текущая"),
    ("core.observation_v2_legacy", "наследие"),
    ("core.observation_v2_old", "ещё древнее"),
    ("v2.observation", "v2"),
]
for tbl, label in gens:
    r = rows(f"SELECT count(*) FROM {tbl}")
    if r is not None:
        print(f"  {tbl:<32} ({label:<12}) строк = {r[0][0]:>9}")

r = rows("SELECT count(*) FROM data.observation")
if r is not None:
    print(f"  {'data.observation':<32} ({'партиции':<12}) строк = {r[0][0]:>9}")

print("\n=== Совпадают ли наборы: сравнение по ключам ядра ===")
r = rows(
    "SELECT (SELECT count(*) FROM core.observation_v2) AS cur, "
    "(SELECT count(*) FROM core.observation_v2_legacy) AS leg, "
    "(SELECT count(DISTINCT (metric_id, region_id, period_start)) FROM core.observation_v2) AS cur_uniq, "
    "(SELECT count(DISTINCT (metric_id, region_id, period_start)) FROM core.observation_v2_legacy) AS leg_uniq"
)
if r:
    x = r[0]
    print(f"  текущая:    строк={x[0]:>9} уникальных ключей={x[2]:>9}")
    print(f"  наследие:   строк={x[1]:>9} уникальных ключей={x[3]:>9}")

print("\n=== Есть ли строки в наследии, которых нет в текущей ===")
r = rows(
    "SELECT count(*) FROM core.observation_v2_legacy l "
    "WHERE NOT EXISTS (SELECT 1 FROM core.observation_v2 c "
    "WHERE c.metric_id = l.metric_id AND c.region_id = l.region_id "
    "AND c.period_start = l.period_start)"
)
if r is not None:
    print(f"  строк наследия, отсутствующих в текущей: {r[0][0]}")

print("\n=== Индексы на таблице наследия (почему 2 ГБ) ===")
r = rows(
    "SELECT indexrelname, pg_size_pretty(pg_relation_size(indexrelid)), "
    "idx_scan FROM pg_stat_user_indexes "
    "WHERE relname = 'observation_v2_legacy' ORDER BY pg_relation_size(indexrelid) DESC"
)
if r:
    for x in r:
        print(f"  {x[0]:<62} {x[1]:>9} прочтений={x[2]}")

print("\n=== Статистика: сколько таблиц вообще не анализировалось ===")
r = rows(
    "SELECT count(*) AS total, "
    "count(*) FILTER (WHERE last_analyze IS NULL AND last_autoanalyze IS NULL) AS never, "
    "coalesce(pg_size_pretty(sum(pg_total_relation_size(relid)) "
    "  FILTER (WHERE last_analyze IS NULL AND last_autoanalyze IS NULL)), '0') AS never_bytes "
    "FROM pg_stat_user_tables"
)
if r:
    print(f"  всего таблиц: {r[0][0]}, никогда не анализировались: {r[0][1]}, их объём: {r[0][2]}")

print("\n=== Дублируется ли FNS ===")
for tbl in ("core.fns_firms_year", "v2_stage.fns_rows"):
    r = rows(f"SELECT count(*) FROM {tbl}")
    if r is not None:
        print(f"  {tbl:<32} строк = {r[0][0]:>9}")