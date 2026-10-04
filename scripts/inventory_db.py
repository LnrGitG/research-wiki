#!/usr/bin/env python3
"""Инвентарь текущего устройства БД: роли, права, объекты, триггеры."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== РОЛИ ===")
for r in query("""SELECT rolname, rolsuper, rolcanlogin, rolcreatedb, rolcreaterole
                  FROM pg_roles WHERE rolname NOT LIKE 'pg_%' ORDER BY 1"""):
    print(f"   {r[0]:16s} super={r[1]} login={r[2]} createdb={r[3]} createrole={r[4]}")

print("\n=== ЧЛЕНСТВО ===")
for r in query("""SELECT m.rolname AS member, g.rolname AS grp
                  FROM pg_auth_members am
                  JOIN pg_roles m ON m.oid=am.member
                  JOIN pg_roles g ON g.oid=am.roleid ORDER BY 1"""):
    print(f"   {r[0]} -> {r[1]}")

print("\n=== ПРАВА НА СХЕМЫ ===")
for r in query("""SELECT nspname, nspacl::text FROM pg_namespace
                  WHERE nspname IN ('catalog','data','derived','core','dkp','v2',
                                    'public','staging','graph','kb','marts','meta')
                  ORDER BY 1"""):
    print(f"   {r[0]:10s} {str(r[1])[:150]}")

print("\n=== ПРАВА РОЛЕЙ НА ТАБЛИЦЫ (сводно) ===")
for r in query("""SELECT grantee, privilege_type, count(*)
                  FROM information_schema.role_table_grants
                  WHERE table_schema IN ('catalog','data','derived')
                  GROUP BY 1,2 ORDER BY 1,2"""):
    print(f"   {r[0]:16s} {r[1]:12s} {r[2]}")

print("\n=== СХЕМЫ И ЧИСЛО ОБЪЕКТОВ ===")
for r in query("""SELECT table_schema,
                         count(*) FILTER (WHERE table_type='BASE TABLE') AS tbl,
                         count(*) FILTER (WHERE table_type='VIEW')       AS vw
                  FROM information_schema.tables
                  WHERE table_schema NOT IN ('pg_catalog','information_schema')
                  GROUP BY 1 ORDER BY 1"""):
    print(f"   {r[0]:12s} таблиц {r[1]:5d}  представлений {r[2]}")

print("\n=== catalog.* содержимое ===")
for t in ("unit", "source", "frequency", "release", "metric", "region"):
    n = query(f"SELECT count(*) FROM catalog.{t}")[0][0]
    print(f"   catalog.{t:10s} {n:>7,}")

print("\n=== data.observation ===")
r = query("""SELECT count(*), count(DISTINCT metric_id), count(DISTINCT region_id),
                    min(period_start), max(period_start) FROM data.observation""")[0]
print(f"   строк {r[0]:,} | метрик {r[1]:,} | регионов {r[2]} | период {r[3]} .. {r[4]}")
print("   партиций:",
      query("""SELECT count(*) FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
               WHERE n.nspname='data' AND c.relispartition AND c.relkind='r'""")[0][0])

print("\n=== ТРИГГЕРЫ ===")
for r in query("""SELECT n.nspname, c.relname, t.tgname, p.proname
                  FROM pg_trigger t
                  JOIN pg_class c ON c.oid=t.tgrelid
                  JOIN pg_namespace n ON n.oid=c.relnamespace
                  JOIN pg_proc p ON p.oid=t.tgfoid
                  WHERE NOT t.tgisinternal ORDER BY 1,2"""):
    print(f"   {r[0]}.{r[1]} -> {r[2]} ({r[3]})")

print("\n=== derived.* ===")
for r in query("""SELECT table_name, table_type FROM information_schema.tables
                  WHERE table_schema='derived' ORDER BY 1"""):
    print(f"   {r[0]:26s} {r[1]}")