#!/usr/bin/env python3
"""Поля data.observation и требования к загрузке дневного ряда."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== колонки data.observation ===")
for r in query("""SELECT column_name, data_type, is_nullable, column_default
                  FROM information_schema.columns
                  WHERE table_schema='data' AND table_name='observation'
                  ORDER BY ordinal_position"""):
    print(f"   {r[0]:20s} {r[1]:28s} null={r[2]:3s} default={str(r[3])[:28]}")

print("\n=== значения перечислений (assessment_type, observation_status) ===")
for r in query("""SELECT conname, pg_get_constraintdef(oid)
                  FROM pg_constraint
                  WHERE conrelid = 'data.observation'::regclass AND contype='c'"""):
    print(f"   {r[0]}: {r[1][:150]}")

print("\n=== релизы ЦБ ===")
for r in query("""SELECT release_id, release_code, left(name_ru,40)
                  FROM catalog.release WHERE source_id=7 ORDER BY release_id LIMIT 6"""):
    print("  ", r)

print("\n=== распределение значений assessment_type в наблюдениях ===")
for r in query("""SELECT assessment_type, count(*) FROM data.observation
                  GROUP BY 1 ORDER BY 2 DESC LIMIT 6"""):
    print("  ", r)