#!/usr/bin/env python3
"""Уточнение-2: шина тревог в ops, определения представлений, размеры канона и наследия."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import db_tunnel  # noqa: E402


def rows(sql):
    try:
        return db_tunnel.query(sql)
    except Exception as exc:  # noqa: BLE001
        print(f"  не прошло: {type(exc).__name__}: {str(exc).splitlines()[0]}")
        return None


print("=== ops: шина тревог и конвейер — живы ли данными ===")
r = rows(
    "SELECT 'alert' AS t, count(*) AS n FROM ops.alert "
    "UNION ALL SELECT 'ingest_run', count(*) FROM ops.ingest_run "
    "UNION ALL SELECT 'quality_rule', count(*) FROM ops.quality_rule "
    "UNION ALL SELECT 'quality_result', count(*) FROM ops.quality_result "
    "UNION ALL SELECT 'ingest_queue', count(*) FROM ops.ingest_queue "
    "UNION ALL SELECT 'release_seen', count(*) FROM ops.release_seen "
    "UNION ALL SELECT 'freshness_snapshot', count(*) FROM ops.freshness_snapshot"
)
if r:
    for x in r:
        print(f"  ops.{x[0]:<20} {x[1]}")

print("\n=== ops.alert: структура и последние записи ===")
r = rows(
    "SELECT string_agg(column_name || ':' || data_type, ', ' ORDER BY ordinal_position) "
    "FROM information_schema.columns WHERE table_schema='ops' AND table_name='alert'"
)
if r:
    print(f"  колонки: {r[0][0]}")

print("\n=== ops: свежесть и признак доставки ===")
for col, tbl in (("delivered_at", "alert"), ("last_seen_at", "freshness_snapshot")):
    r = rows(f"SELECT max({col}) FROM ops.{tbl}")
    if r and r[0][0] is not None:
        print(f"  max(ops.{tbl}.{col}) = {r[0][0]}")
    else:
        print(f"  ops.{tbl}.{col} — пусто или колонки нет")

print("\n=== Схема catalog: канон целиком ===")
r = rows(
    "SELECT c.relkind, c.relname, pg_size_pretty(pg_total_relation_size(c.oid)) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
    "WHERE n.nspname='catalog' AND c.relkind IN ('r','v','m','p') ORDER BY 1,2"
)
if r:
    kinds = {"r": "таблица", "v": "представление", "m": "матпредставление", "p": "партиц."}
    for x in r:
        print(f"  [{kinds.get(x[0], x[0]):<15}] {x[1]:<34} {x[2]}")

print("\n=== Определения: чем core.* на самом деле является ===")
r = rows(
    "SELECT c.relname, left(pg_get_viewdef(c.oid, true), 240) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
    "WHERE n.nspname='core' AND c.relkind='v' ORDER BY c.relname"
)
if r:
    for x in r:
        flat = " ".join(x[1].split())
        print(f"  core.{x[0]} = {flat}")
else:
    print("  представлений в core нет")

print("\n=== Размер по слоям: канон против наследия ===")
r = rows(
    "SELECT n.nspname, pg_size_pretty(sum(pg_total_relation_size(c.oid))) "
    "FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
    "WHERE c.relkind IN ('r','m','p') AND n.nspname NOT LIKE 'pg\\_%' "
    "AND n.nspname <> 'information_schema' "
    "GROUP BY n.nspname ORDER BY sum(pg_total_relation_size(c.oid)) DESC"
)
if r:
    for x in r:
        print(f"  {x[0]:<16} {x[1]}")

print("\n=== meta: имена объектов (в прошлый раз потерял имена) ===")
r = rows(
    "SELECT c.relkind, c.relname FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
    "WHERE n.nspname='meta' AND c.relkind IN ('r','v','m') ORDER BY 1,2"
)
if r:
    kinds = {"r": "табл", "v": "предст", "m": "мат"}
    for x in r:
        print(f"  [{kinds.get(x[0], x[0])}] meta.{x[1]}")

print("\n=== Появились ли где-то ещё v3-имена (второй канон?) ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname FROM pg_class c "
    "JOIN pg_namespace n ON n.oid=c.relnamespace "
    "WHERE (c.relname LIKE '%\\_v3' OR c.relname LIKE 'v3%') "
    "AND n.nspname NOT LIKE 'pg\\_%' LIMIT 10"
)
if r is not None:
    if not r:
        print("  отдельных объектов v3 нет — имена v3 живут только внутри core как наследие")
    for x in r:
        print(f"  {x[0]}")

print("\n=== Есть ли у data.observation политика автовакуума по секциям ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname, c.reloptions "
    "FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
    "WHERE c.relname IN ('observation','observation_v2_legacy') "
    "AND n.nspname IN ('data','core') LIMIT 5"
)
if r:
    for x in r:
        print(f"  {x[0]:<42} reloptions={x[1]}")