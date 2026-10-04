#!/usr/bin/env python3
"""Кто владелец крупных объектов и что роль wiki может с ними делать."""
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


print("=== Владельцы крупных объектов и права wiki ===")
r = rows(
    "SELECT n.nspname||'.'||c.relname, pg_get_userbyid(c.relowner) AS owner, "
    "has_table_privilege(current_user, c.oid, 'SELECT') AS sel, "
    "has_table_privilege(current_user, c.oid, 'INSERT') AS ins, "
    "has_table_privilege(current_user, c.oid, 'DELETE') AS del "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE c.relkind IN ('r','m','p') AND n.nspname IN "
    "('core','data','derived','meta','marts','v2','kb','catalog','dkp') "
    "ORDER BY pg_total_relation_size(c.oid) DESC LIMIT 16"
)
if r:
    for x in r:
        flag = "СВОЯ" if x[1] == "wiki" else "чужая"
        print(
            f"  {x[0]:<44} {flag:<6} owner={x[1]:<9} "
            f"select={x[2]} insert={x[3]} delete={x[4]}"
        )

print("\n=== Функции: кто владелец и можем ли править ===")
r = rows(
    "SELECT p.proname, pg_get_userbyid(p.proowner) "
    "FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace "
    "WHERE n.nspname = 'public' ORDER BY 1"
)
if r is not None:
    for x in r:
        print(f"  {x[0]:<40} владелец={x[1]}")

print("\n=== Мёртвые строки: где накопилось ===")
r = rows(
    "SELECT schemaname||'.'||relname, n_dead_tup, n_live_tup, "
    "round(100.0*n_dead_tup/nullif(n_live_tup+n_dead_tup,0),1) AS pct_dead, "
    "last_autovacuum "
    "FROM pg_stat_user_tables WHERE n_dead_tup > 10000 "
    "ORDER BY n_dead_tup DESC LIMIT 10"
)
if r is not None:
    if not r:
        print("  крупных залежей нет")
    for x in r:
        print(f"  {x[0]:<42} мёртвых={x[1]:>9} живых={x[2]:>9} {x[3]}% последний autovac={x[4]}")

print("\n=== Настройки автоочистки по крупнейшей таблице ===")
r = rows(
    "SELECT c.relname, "
    "coalesce((SELECT option_value FROM pg_options_to_table(c.reloptions) "
    "  WHERE option_name='autovacuum_vacuum_scale_factor'),'наследует') AS vsf, "
    "coalesce((SELECT option_value FROM pg_options_to_table(c.reloptions) "
    "  WHERE option_name='autovacuum_analyze_scale_factor'),'наследует') AS asf "
    "FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
    "WHERE n.nspname='core' AND c.relname LIKE 'observation%' "
    "ORDER BY pg_total_relation_size(c.oid) DESC LIMIT 5"
)
if r is not None:
    for x in r:
        print(f"  {x[0]:<40} vacuum_scale={x[1]} analyze_scale={x[2]}")

print("\n=== Глобальные пороги автоочистки ===")
for k in (
    "autovacuum_vacuum_scale_factor",
    "autovacuum_analyze_scale_factor",
    "autovacuum_vacuum_threshold",
    "autovacuum_max_workers",
    "autovacuum_vacuum_cost_limit",
):
    r = rows("SELECT current_setting(%s)", (k,))
    if r:
        print(f"  {k} = {r[0][0]}")

print("\n=== Есть ли расширение для управления партициями ===")
r = rows(
    "SELECT name FROM pg_available_extensions "
    "WHERE name LIKE 'pg_partman%' OR name LIKE 'pg_repack%'"
)
if r is not None:
    if not r:
        print("  ни pg_partman, ни pg_repack не доступны на этом сервере")
    for x in r:
        print(f"  {x[0]}")