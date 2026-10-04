#!/usr/bin/env python3
"""Функция catalog.resolve_metric — поиск показателя по слову контекста.

Четыре ступени: точный код, точный синоним, триграммная близость синонима,
триграммная близость имени. Возвращает код, имя, тему, единицу, частоту и
оценку совпадения, отсортированные по убыванию.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

FN = """
CREATE OR REPLACE FUNCTION catalog.resolve_metric(term text, lim int DEFAULT 10)
RETURNS TABLE (metric_id int, metric_code text, name_ru text,
               topic text, unit text, freq text,
               match_kind text, score numeric)
LANGUAGE sql STABLE AS $$
    WITH t AS (SELECT lower(btrim(term)) AS q)
    SELECT m.metric_id, m.metric_code, m.name_ru,
           tp.topic_code AS topic,
           u.unit_code AS unit, f.freq_code AS freq,
           src.kind AS match_kind, src.score
    FROM catalog.metric m
    LEFT JOIN catalog.unit u      ON u.unit_id = m.unit_id
    LEFT JOIN catalog.frequency f ON f.frequency_id = m.frequency_id
    LEFT JOIN LATERAL (
        SELECT t2.topic_code FROM catalog.metric_topic mt
        JOIN catalog.topic t2 ON t2.topic_id = mt.topic_id
        WHERE mt.metric_id = m.metric_id
        ORDER BY mt.weight DESC LIMIT 1
    ) tp ON true
    JOIN LATERAL (
        SELECT 'code'::text AS kind, 1.00::numeric AS score
        WHERE lower(m.metric_code) = (SELECT q FROM t)
        UNION ALL
        SELECT 'alias', 0.95
        WHERE EXISTS (SELECT 1 FROM catalog.metric_alias a
                      WHERE a.metric_id = m.metric_id
                        AND lower(a.alias) = (SELECT q FROM t))
        UNION ALL
        SELECT 'alias_fuzzy', similarity(a.alias, (SELECT q FROM t))
        FROM catalog.metric_alias a
        WHERE a.metric_id = m.metric_id
          AND similarity(a.alias, (SELECT q FROM t)) > 0.45
        UNION ALL
        SELECT 'name_fuzzy', similarity(m.name_ru, (SELECT q FROM t)) * 0.9
        WHERE similarity(m.name_ru, (SELECT q FROM t)) > 0.35
        ORDER BY 2 DESC LIMIT 1
    ) src ON true
    WHERE m.is_active
    ORDER BY src.score DESC, m.metric_id
    LIMIT lim
$$;
"""
try:
    execute(FN)
    print("OK  функция catalog.resolve_metric создана")
except Exception as e:
    print("ERR:", str(e)[:400])

print("\n=== проба на разговорных терминах ===")
for term in ("инфляция", "ИПЦ", "ключевая ставка", "безработица", "зарплата",
             "промпроизводство", "инвестиции", "розница", "СМР", "ВВП"):
    try:
        rows = query("SELECT metric_code, left(name_ru,38), topic, match_kind, score "
                     "FROM catalog.resolve_metric(%s, 3)", (term,))
        if rows:
            top = rows[0]
            print(f"   «{term}» -> {top[0]} | {top[1]} | тема={top[2]} | {top[3]} {top[4]:.2f}")
        else:
            print(f"   «{term}» -> не найдено")
    except Exception as e:
        print(f"   «{term}» ERR {str(e)[:120]}")