#!/usr/bin/env python3
"""Этап D: перенос метрик core.metric -> catalog.metric.

Решения:
 - правило на код ослаблено до латиницы обоих регистров, цифр, подчёркивания,
   дефиса и кириллицы: 522 кода содержат заглавные буквы или кириллицу, а
   переименование сломало бы ссылки в скриптах и навыках;
 - source_id в core.metric отсутствует, он выводится как самый частый
   источник наблюдений метрики; для 474 метрик без наблюдений заводится
   отдельный источник-заглушка 'unknown'.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

# 1) ослабить правило на код
try:
    execute("ALTER TABLE catalog.metric DROP CONSTRAINT IF EXISTS catalog_metric_code_chk")
    execute("""ALTER TABLE catalog.metric
               ADD CONSTRAINT catalog_metric_code_chk
               CHECK (metric_code ~ '^[a-zA-Z0-9_\\-а-яёА-ЯЁ]+$')""")
    print("OK   правило на код: латиница/кириллица, цифры, подчёркивание, дефис")
except Exception as e:
    print("ERR  правило:", str(e)[:160])

# 2) источник-заглушка для метрик без наблюдений
try:
    execute("""INSERT INTO catalog.source (source_code, name_ru, url)
               VALUES ('unknown', 'Источник не определён', NULL)
               ON CONFLICT (source_code) DO NOTHING""")
    print("OK   источник 'unknown' заведён")
except Exception as e:
    print("ERR  unknown:", str(e)[:160])

# 3) перенос метрик
print("\n--- перенос 16 342 метрик ---")
SQL = """
WITH msrc AS (
    SELECT metric_id, source_id,
           row_number() OVER (PARTITION BY metric_id
                              ORDER BY count(*) DESC, source_id) AS rn
    FROM core.observation_v2
    WHERE source_id IS NOT NULL
    GROUP BY metric_id, source_id
)
INSERT INTO catalog.metric
    (metric_id, metric_code, name_ru, unit_id, source_id, frequency_id,
     tags, released_at, version, is_active,
     short_name_ru, description, metric_type, index_base, is_derived,
     formula_text, status)
SELECT m.metric_id, m.metric_code, m.name_ru, m.unit_id,
       COALESCE(ms.source_id,
                (SELECT source_id FROM catalog.source WHERE source_code='unknown')),
       m.frequency_id,
       to_jsonb(m.tags), m.created_at, 1, (m.status = 'active'),
       m.short_name_ru, m.description, m.metric_type, m.index_base,
       m.is_derived, m.formula_text, m.status
FROM core.metric m
LEFT JOIN msrc ms ON ms.metric_id = m.metric_id AND ms.rn = 1
ON CONFLICT (metric_id) DO NOTHING
"""
try:
    n = execute(SQL)
    print(f"OK   вставлено: {n}")
except Exception as e:
    print("ERR ", str(e)[:400])

# 4) выровнять последовательность
try:
    execute("""SELECT setval('catalog.metric_metric_id_seq',
               COALESCE((SELECT max(metric_id) FROM catalog.metric), 1))""")
    print("OK   последовательность metric_id выровнена")
except Exception as e:
    print("ERR  setval:", str(e)[:140])

# 5) контроль
print("\n=== контроль ===")
a = query("SELECT count(*) FROM core.metric")[0][0]
b = query("SELECT count(*) FROM catalog.metric")[0][0]
print(f"   core.metric {a} -> catalog.metric {b}  {'OK' if a == b else 'РАСХОЖДЕНИЕ'}")
print("   без источника:",
      query("SELECT count(*) FROM catalog.metric WHERE source_id IS NULL")[0][0])
print("   на 'unknown':",
      query("""SELECT count(*) FROM catalog.metric m
               JOIN catalog.source s USING(source_id)
               WHERE s.source_code='unknown'""")[0][0])
print("   уникальных кодов:",
      query("SELECT count(DISTINCT metric_code) FROM catalog.metric")[0][0])