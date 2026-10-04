#!/usr/bin/env python3
"""ops.context_bundle — набор показателей под контекст сессии.

Агент приходит с темой («инфляция»), регионом и глубиной. Функция отдаёт
готовый список показателей этой темы с последним известным значением по
региону и статусом свежести — то, что раньше приходилось угадывать по именам
таблиц.

Две ступени: точная тема (catalog.topic.topic_code) и разговорный термин,
который сначала разрешается через catalog.resolve_metric.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

FN = """
CREATE OR REPLACE FUNCTION ops.context_bundle(
        p_topic text,
        p_region text DEFAULT NULL,
        p_months int DEFAULT 24)
RETURNS TABLE (metric_code text, name_ru text, unit text, frequency text,
               topic text, freshness text, last_observation date,
               region_code text, last_value numeric)
LANGUAGE sql STABLE AS $$
    WITH resolved_topic AS (
        -- тема может прийти кодом темы, названием темы или термином показателя
        SELECT t.topic_code FROM catalog.topic t
        WHERE lower(t.topic_code) = lower(p_topic) OR lower(t.name_ru) = lower(p_topic)
        UNION
        SELECT c.topic FROM derived.v_metric_context c
        WHERE lower(c.metric_code) = lower(p_topic)
        UNION
        SELECT c.topic FROM catalog.resolve_metric(p_topic, 1) r
        JOIN derived.v_metric_context c ON c.metric_id = r.metric_id
        WHERE c.topic IS NOT NULL
        LIMIT 1
    )
    SELECT c.metric_code, c.name_ru, c.unit, c.frequency, c.topic, c.freshness,
           c.last_observation, r.region_code,
           o.value AS last_value
    FROM derived.v_metric_context c
    JOIN resolved_topic rt ON rt.topic_code = c.topic
    LEFT JOIN LATERAL (
        SELECT o2.region_id, o2.period_start, o2.value
        FROM data.observation o2
        WHERE o2.metric_id = c.metric_id
          AND o2.period_start >= (current_date - (p_months || ' months')::interval)
        ORDER BY o2.period_start DESC
        LIMIT 1
    ) o ON true
    LEFT JOIN catalog.region r ON r.region_id = o.region_id
    WHERE p_region IS NULL OR r.region_code = p_region
    ORDER BY c.metric_code
$$;
"""
try:
    execute(FN); print("OK  ops.context_bundle создана")
except Exception as e:
    print("ERR:", str(e)[:350])

try:
    execute("GRANT EXECUTE ON FUNCTION ops.context_bundle(text,text,int) TO viewer, datalens_ro, agent_ro")
    execute("GRANT EXECUTE ON FUNCTION catalog.resolve_metric(text,int) TO viewer, datalens_ro, agent_ro")
    print("OK  права на функции")
except Exception as e:
    print("ERR прав:", str(e)[:150])

print("\n=== проба: тема «инфляция» ===")
try:
    for r in query("SELECT metric_code, left(name_ru,36), unit, frequency, freshness, last_observation, last_value "
                   "FROM ops.context_bundle('инфляция')"):
        print("  ", r)
except Exception as e:
    print("   ERR:", str(e)[:250])

print("\n=== проба: тема inflation, регион RU ===")
try:
    rows = query("SELECT metric_code, frequency, freshness, region_code, last_value "
                 "FROM ops.context_bundle('inflation', 'RU', 36)")
    print("   показателей:", len(rows))
    for r in rows[:6]:
        print("  ", r)
except Exception as e:
    print("   ERR:", str(e)[:250])

print("\n=== проба: тема labour ===")
try:
    rows = query("SELECT metric_code, freshness, region_code, last_value "
                 "FROM ops.context_bundle('labour', NULL, 60)")
    print("   показателей:", len(rows))
    for r in rows[:6]:
        print("  ", r)
except Exception as e:
    print("   ERR:", str(e)[:250])