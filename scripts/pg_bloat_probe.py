#!/usr/bin/env python3
"""Точная проверка: файл есть, а строк нет — это свободное место внутри файла."""
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


print("=== Страницы файла против числа строк (по каталогу) ===")
print("  relpages=0 при большом размере невозможно; большой relpages при reltuples=0 = свободное место")
r = rows(
    "SELECT n.nspname||'.'||c.relname AS tbl, c.relpages, c.reltuples, "
    "pg_size_pretty(pg_relation_size(c.oid)) AS heap, "
    "pg_size_pretty(pg_total_relation_size(c.oid)) AS total "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relkind = 'r' AND n.nspname IN ('staging','v2_stage','v2','core') "
    "AND pg_total_relation_size(c.oid) > 20*1024*1024 "
    "ORDER BY pg_total_relation_size(c.oid) DESC LIMIT 18"
)
if r:
    for x in r:
        print(
            f"  {x[0]:<50} стр={x[1]:>8} оценка_строк={x[2]:>12} "
            f"куча={x[3]:>9} всего={x[4]:>9}"
        )

print("\n=== Точный COUNT по подозрительным таблицам (контроль) ===")
for tbl in (
    "v2_stage.fns_rows",
    "core.fns_firms_year",
    "staging.rosstat_construction__domrf_indicators",
    "core.observation_v2_old",
    "staging.regions_panel__panel",
    "v2.observation",
):
    r = rows(f"SELECT count(*) FROM {tbl}")
    if r is not None:
        print(f"  {tbl:<50} строк фактически = {r[0][0]}")

print("\n=== Кто крупнее: куча или индексы (по пустым) ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname, "
    "pg_size_pretty(pg_relation_size(c.oid)) AS heap, "
    "pg_size_pretty(pg_indexes_size(c.oid)) AS idx "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relkind = 'r' AND pg_total_relation_size(c.oid) > 20*1024*1024 "
    "AND n.nspname IN ('staging','v2_stage','v2','core') "
    "ORDER BY pg_total_relation_size(c.oid) DESC LIMIT 12"
)
if r:
    for x in r:
        print(f"  {x[0]:<50} куча={x[1]:>9} индексы={x[2]:>9}")

print("\n=== Сколько освободится при пересборке пустых объектов ===")
r = rows(
    "SELECT count(*), pg_size_pretty(sum(pg_total_relation_size(c.oid))) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "LEFT JOIN pg_stat_user_tables s ON s.relid = c.oid "
    "WHERE c.relkind = 'r' AND n.nspname NOT LIKE 'pg\\_%' "
    "AND coalesce(s.n_live_tup,0) = 0"
)
if r:
    print(f"  пустых таблиц: {r[0][0]}, занято {r[0][1]}")

print("\n=== Освободится ли место самим VACUUM: проверка настроек ===")
r = rows(
    "SELECT current_setting('maintenance_work_mem'), "
    "current_setting('max_parallel_maintenance_workers')"
)
if r:
    print(f"  maintenance_work_mem={r[0][0]} параллельных рабочих={r[0][1]}")

print("\n=== Доступные размеры в табличных пространствах ===")
r = rows("SELECT spcname, pg_size_pretty(pg_tablespace_size(oid)) FROM pg_tablespace")
if r:
    for x in r:
        print(f"  {x[0]:<16} {x[1]}")