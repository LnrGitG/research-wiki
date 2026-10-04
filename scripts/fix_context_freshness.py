#!/usr/bin/env python3
"""Переработка derived.v_metric_context: свежесть с порогом по частоте.

Первая версия сравнивала всё с одним окном (45/120 дней) и объявила
«отстают/устарели» 15 738 показателей из 15 818 — включая квартальные и
годовые, для которых возраст последней точки нормален. Правильный порог
зависит от частоты: месячному ряду просрочка в 45 дней нормальна, а
квартальному точка четырёхмесячной давности — свежая.

Ожидаемое отставание публикации берётся как период частоты плюс один
период на публикацию и сверяется с датой последнего наблюдения.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

CTX = """
CREATE OR REPLACE VIEW derived.v_metric_context AS
WITH base AS (
    SELECT m.metric_id, m.metric_code, m.name_ru,
           u.unit_code AS unit, s.source_code AS source, f.freq_code AS frequency,
           mc.last_observation, coalesce(mc.observations_cnt,0) AS observations,
           CASE f.freq_code
               WHEN 'D' THEN 10
               WHEN 'W' THEN 25
               WHEN 'M' THEN 75
               WHEN 'Q' THEN 160
               WHEN 'A' THEN 550
               ELSE 120
           END AS tolerance_days
    FROM catalog.metric m
    LEFT JOIN catalog.unit u      ON u.unit_id = m.unit_id
    LEFT JOIN catalog.source s    ON s.source_id = m.source_id
    LEFT JOIN catalog.frequency f ON f.frequency_id = m.frequency_id
    LEFT JOIN derived.metric_card mc ON mc.metric_id = m.metric_id
    WHERE m.is_active
)
SELECT b.metric_id, b.metric_code, b.name_ru, b.unit, b.source, b.frequency,
       tp.topic_code AS topic, al.aliases,
       b.last_observation, b.observations,
       b.last_observation + (b.tolerance_days || ' days')::interval AS expected_next,
       CASE
           WHEN b.last_observation IS NULL THEN 'нет данных'
           WHEN now()::date <= b.last_observation + (b.tolerance_days || ' days')::interval
                                            THEN 'свежие'
           WHEN now()::date <= b.last_observation + ((b.tolerance_days*2) || ' days')::interval
                                            THEN 'отстают'
           ELSE 'устарели'
       END AS freshness
FROM base b
LEFT JOIN LATERAL (
    SELECT t2.topic_code FROM catalog.metric_topic mt
    JOIN catalog.topic t2 ON t2.topic_id = mt.topic_id
    WHERE mt.metric_id = b.metric_id ORDER BY mt.weight DESC LIMIT 1
) tp ON true
LEFT JOIN LATERAL (
    SELECT array_agg(a.alias ORDER BY a.alias) AS aliases
    FROM catalog.metric_alias a WHERE a.metric_id = b.metric_id
) al ON true
"""

try:
    execute("DROP VIEW IF EXISTS derived.v_metric_context CASCADE")
    execute(CTX)
    print("OK  v_metric_context пересоздано")
except Exception as e:
    print("ERR:", str(e)[:300])

print("\n=== распределение свежести (порог по частоте) ===")
for r in query("""SELECT freshness, count(*) FROM derived.v_metric_context
                  GROUP BY 1 ORDER BY 2 DESC"""):
    print(f"   {r[0]:10s} {r[1]}")

print("\n=== по частотам ===")
for r in query("""SELECT frequency, freshness, count(*)
                  FROM derived.v_metric_context GROUP BY 1,2
                  ORDER BY 1, 3 DESC"""):
    print(f"   {r[0]:3s} {r[1]:10s} {r[2]}")

print("\n=== контроль ключевых показателей ===")
for r in query("""SELECT metric_code, left(name_ru,30), frequency, last_observation,
                         observations, freshness
                  FROM derived.v_metric_context
                  WHERE metric_code IN ('kep1_14','kep1_14_s','kep1_12','kep1_12_m',
                                        'kep4_17','kep4_2','ippsm','vvpi')
                  ORDER BY metric_code"""):
    print("  ", r)

try:
    execute("GRANT SELECT ON derived.v_metric_context TO viewer, datalens_ro, agent_ro")
    print("\n   права выданы")
except Exception as e:
    print("\n   ERR прав:", str(e)[:150])