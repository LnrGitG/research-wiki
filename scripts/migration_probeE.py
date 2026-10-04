#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== 1. дубли (metric_id, region_id, period_start) — их отклонит уникальный индекс ===")
print("   дублирующихся ключей:",
      query("""SELECT count(*) FROM (
                 SELECT metric_id, region_id, period_start
                 FROM core.observation_v2
                 GROUP BY 1,2,3 HAVING count(*) > 1
               ) t""")[0][0])

print("\n=== 2. ссылочная целостность ===")
print("   region_id вне catalog.region:",
      query("""SELECT count(*) FROM core.observation_v2 o
               WHERE NOT EXISTS (SELECT 1 FROM catalog.region r
                                 WHERE r.region_id = o.region_id)""")[0][0])
print("   metric_id вне catalog.metric:",
      query("""SELECT count(*) FROM core.observation_v2 o
               WHERE NOT EXISTS (SELECT 1 FROM catalog.metric m
                                 WHERE m.metric_id = o.metric_id)""")[0][0])
print("   release_id вне catalog.release (не NULL):",
      query("""SELECT count(*) FROM core.observation_v2 o
               WHERE o.release_id IS NOT NULL
                 AND NOT EXISTS (SELECT 1 FROM catalog.release r
                                 WHERE r.release_id = o.release_id)""")[0][0])

print("\n=== 3. типы ===")
print("   quality_flags в источнике:",
      query("""SELECT data_type, udt_name FROM information_schema.columns
               WHERE table_schema='core' AND table_name='observation_v2'
                 AND column_name='quality_flags'""")[0])
print("   quality_flags в приёмнике:",
      query("""SELECT data_type, udt_name FROM information_schema.columns
               WHERE table_schema='data' AND table_name='observation'
                 AND column_name='quality_flags'""")[0])

print("\n=== 4. значения release_id / source_id ===")
print("   release_id NULL:", query("SELECT count(*) FROM core.observation_v2 WHERE release_id IS NULL")[0][0])
print("   source_id NULL:", query("SELECT count(*) FROM core.observation_v2 WHERE source_id IS NULL")[0][0])

print("\n=== 5. obs_id: диапазон (сохранять или нет) ===")
print("   ", query("SELECT min(obs_id), max(obs_id), count(DISTINCT obs_id) FROM core.observation_v2")[0])