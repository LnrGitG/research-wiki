#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== расширения ===")
for r in query("SELECT extname, extversion FROM pg_extension ORDER BY 1"):
    print("   ", r[0], r[1])

print("\n=== derived.metric_semantic: структура ===")
for r in query("""SELECT column_name, data_type FROM information_schema.columns
                  WHERE table_schema='derived' AND table_name='metric_semantic'
                  ORDER BY ordinal_position"""):
    print(f"   {r[0]:22s} {r[1]}")
print("   строк:", query("SELECT count(*) FROM derived.metric_semantic")[0][0])

print("\n=== derived.metric_crosswalk ===")
for r in query("""SELECT column_name, data_type FROM information_schema.columns
                  WHERE table_schema='derived' AND table_name='metric_crosswalk'
                  ORDER BY ordinal_position"""):
    print(f"   {r[0]:22s} {r[1]}")
print("   строк:", query("SELECT count(*) FROM derived.metric_crosswalk")[0][0])

print("\n=== v2.freshness (модель свежести) ===")
for r in query("""SELECT column_name, data_type FROM information_schema.columns
                  WHERE table_schema='v2' AND table_name='freshness'
                  ORDER BY ordinal_position"""):
    print(f"   {r[0]:22s} {r[1]}")
print("   строк:", query("SELECT count(*) FROM v2.freshness")[0][0])
for r in query("""SELECT * FROM v2.freshness ORDER BY freshness DESC NULLS LAST LIMIT 5"""):
    print("   ", r)

print("\n=== есть ли таблицы расписаний/свежести в catalog/ops ===")
for r in query("""SELECT table_schema||'.'||table_name FROM information_schema.tables
                  WHERE table_name ~ 'fresh|schedul|watch|run|quality|alert|monitor'
                  ORDER BY 1"""):
    print("   ", r[0])

print("\n=== схема cron ===")
for r in query("""SELECT table_name FROM information_schema.tables
                  WHERE table_schema='cron' ORDER BY 1"""):
    print("   cron.", r[0])

print("\n=== catalog.metric: полный состав колонок ===")
for r in query("""SELECT column_name, data_type, is_nullable FROM information_schema.columns
                  WHERE table_schema='catalog' AND table_name='metric'
                  ORDER BY ordinal_position"""):
    print(f"   {r[0]:18s} {r[1]:26s} null={r[2]}")