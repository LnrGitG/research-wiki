#!/usr/bin/env python3
"""Витрины контекстного слоя.

derived.v_metric_context — одна строка на показатель: код, имя, единица,
источник, частота, тема, синонимы, последнее наблюдение, число наблюдений
и статус свежести. Это то, что читает агент, чтобы выбрать показатель,
не угадывая имена таблиц.

derived.v_observation_recent — последние значения по региону за окно, для
быстрого ответа без обращения ко всей истории.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

CTX = """
CREATE OR REPLACE VIEW derived.v_metric_context AS
SELECT m.metric_id,
       m.metric_code,
       m.name_ru,
       u.unit_code        AS unit,
       s.source_code      AS source,
       f.freq_code        AS frequency,
       tp.topic_code      AS topic,
       al.aliases,
       mc.last_observation,
       coalesce(mc.observations_cnt, 0) AS observations,
       CASE
           WHEN mc.last_observation IS NULL                THEN 'нет данных'
           WHEN mc.last_observation >= now() - interval '45 days'  THEN 'свежие'
           WHEN mc.last_observation >= now() - interval '120 days' THEN 'отстают'
           ELSE 'устарели'
       END AS freshness
FROM catalog.metric m
LEFT JOIN catalog.unit u      ON u.unit_id = m.unit_id
LEFT JOIN catalog.source s    ON s.source_id = m.source_id
LEFT JOIN catalog.frequency f ON f.frequency_id = m.frequency_id
LEFT JOIN derived.metric_card mc ON mc.metric_id = m.metric_id
LEFT JOIN LATERAL (
    SELECT t2.topic_code FROM catalog.metric_topic mt
    JOIN catalog.topic t2 ON t2.topic_id = mt.topic_id
    WHERE mt.metric_id = m.metric_id ORDER BY mt.weight DESC LIMIT 1
) tp ON true
LEFT JOIN LATERAL (
    SELECT array_agg(a.alias ORDER BY a.alias) AS aliases
    FROM catalog.metric_alias a WHERE a.metric_id = m.metric_id
) al ON true
WHERE m.is_active
"""

RECENT = """
CREATE OR REPLACE VIEW derived.v_observation_recent AS
SELECT o.metric_id, m.metric_code, m.name_ru,
       o.region_id, r.region_code, r.name_ru AS region_name,
       o.period_start, o.value, u.unit_code AS unit
FROM data.observation o
JOIN catalog.metric m ON m.metric_id = o.metric_id
JOIN catalog.region r ON r.region_id = o.region_id
LEFT JOIN catalog.unit u ON u.unit_id = m.unit_id
WHERE o.period_start >= now() - interval '30 months'
"""

print("=== создание витрин ===")
for label, sql in (("v_metric_context", CTX), ("v_observation_recent", RECENT)):
    try:
        execute(sql)
        print(f"   OK {label}")
    except Exception as e:
        print(f"   ERR {label}: {str(e)[:250]}")

print("\n=== контроль v_metric_context ===")
print("   всего строк:", query("SELECT count(*) FROM derived.v_metric_context")[0][0])
for r in query("""SELECT freshness, count(*) FROM derived.v_metric_context
                  GROUP BY 1 ORDER BY 2 DESC"""):
    print(f"   {r[0]:10s} {r[1]}")
print("   с темой:", query("SELECT count(*) FROM derived.v_metric_context WHERE topic IS NOT NULL")[0][0])
print("   с синонимами:", query("SELECT count(*) FROM derived.v_metric_context WHERE aliases IS NOT NULL")[0][0])
print("\n   пример строки:")
for r in query("""SELECT metric_code, left(name_ru,34), unit, frequency, topic,
                         last_observation, observations, freshness
                  FROM derived.v_metric_context WHERE observations > 1000
                  ORDER BY observations DESC LIMIT 4"""):
    print("   ", r)

print("\n=== права на витрины ===")
for sql in ("GRANT SELECT ON derived.v_metric_context TO viewer, datalens_ro, agent_ro",
            "GRANT SELECT ON derived.v_observation_recent TO viewer, datalens_ro, agent_ro"):
    try:
        execute(sql); print("   OK")
    except Exception as e:
        print("   ERR", str(e)[:150])