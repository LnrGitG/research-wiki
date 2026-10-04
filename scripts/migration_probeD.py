#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== core.metric: NULL-и в обязательных для приёмника полях ===")
print(query("""SELECT
    count(*) AS всего,
    count(*) FILTER (WHERE unit_id IS NULL)      AS null_unit,
    count(*) FILTER (WHERE frequency_id IS NULL) AS null_freq,
    count(*) FILTER (WHERE name_ru IS NULL)      AS null_name,
    count(*) FILTER (WHERE metric_code IS NULL)  AS null_code
  FROM core.metric""")[0])

print("\n=== коды, не проходящие новое правило ^[a-z0-9_-]+$ ===")
print("   ", query("SELECT count(*) FROM core.metric WHERE metric_code !~ '^[a-z0-9_-]+$'")[0][0])

print("\n=== дубли кодов в core.metric ===")
rows = query("""SELECT metric_code, count(*) FROM core.metric
                GROUP BY 1 HAVING count(*) > 1 ORDER BY 2 DESC LIMIT 10""")
print("   дублей:", len(rows))
for r in rows:
    print("    ", r[0], r[1])

print("\n=== unit_id метрик: есть ли отсутствующие в catalog.unit ===")
print("   ", query("""SELECT count(DISTINCT m.unit_id)
                       FROM core.metric m
                       WHERE m.unit_id IS NOT NULL
                         AND NOT EXISTS (SELECT 1 FROM catalog.unit u
                                         WHERE u.unit_id = m.unit_id)""")[0][0])

print("\n=== frequency_id метрик: отсутствующие в catalog.frequency ===")
print("   ", query("""SELECT count(DISTINCT m.frequency_id)
                       FROM core.metric m
                       WHERE m.frequency_id IS NOT NULL
                         AND NOT EXISTS (SELECT 1 FROM catalog.frequency f
                                         WHERE f.frequency_id = m.frequency_id)""")[0][0])

print("\n=== вывод source_id из наблюдений: сколько метрик получит источник ===")
print("   ", query("""
    SELECT count(*) FROM (
      SELECT o.metric_id, (SELECT o2.source_id FROM core.observation_v2 o2
                           WHERE o2.metric_id = o.metric_id
                             AND o2.source_id IS NOT NULL
                           GROUP BY o2.source_id
                           ORDER BY count(*) DESC LIMIT 1) AS src
      FROM core.observation_v2 o GROUP BY o.metric_id
    ) t WHERE src IS NOT NULL""")[0][0])

print("\n=== метрики без наблюдений (source_id вывести не из чего) ===")
print("   ", query("""SELECT count(*) FROM core.metric m
                       WHERE NOT EXISTS (SELECT 1 FROM core.observation_v2 o
                                         WHERE o.metric_id = m.metric_id)""")[0][0])

print("\n=== max(source_id) в наблюдениях ===")
print("   ", query("SELECT max(source_id) FROM core.observation_v2")[0][0])