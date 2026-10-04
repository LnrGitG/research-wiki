#!/usr/bin/env python3
"""Доводка: catalog.metric.source_id обязателен, но в старом core.metric его
не было и скрипты его не передают. Ставим значение по умолчанию — служебный
источник 'unknown'. NOT NULL сохраняется."""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

sid = query("SELECT source_id FROM catalog.source WHERE source_code='unknown'")
if not sid:
    print("нет источника 'unknown' — создаю")
    execute("""INSERT INTO catalog.source (source_code, name_ru)
               VALUES ('unknown','Источник не определён')
               ON CONFLICT (source_code) DO NOTHING""")
    sid = query("SELECT source_id FROM catalog.source WHERE source_code='unknown'")
sid = sid[0][0]
print("служебный источник unknown: source_id =", sid)

try:
    execute(f"ALTER TABLE catalog.metric ALTER COLUMN source_id SET DEFAULT {sid}")
    print("OK   DEFAULT проставлен")
except Exception as e:
    print("ERR ", str(e)[:200])

r = query("""SELECT column_name, is_nullable, column_default
             FROM information_schema.columns
             WHERE table_schema='catalog' AND table_name='metric'
               AND column_name='source_id'""")[0]
print("   состояние:", r)

# повторная проверка записи через представление
print("\n--- повторный тест записи в core.metric ---")
try:
    execute("""INSERT INTO core.metric
               (metric_id, metric_code, name_ru, unit_id, frequency_id, status, tags)
               VALUES (999999, 'cutover_test_metric', 'Тест переключения', 1, 5,
                       'active', ARRAY['test'])""")
    print("   INSERT: ок")
    row = query("""SELECT metric_id, source_id, status, tags FROM catalog.metric
                   WHERE metric_code='cutover_test_metric'""")
    print("   легло в catalog.metric:", row[0] if row else "нет")
    execute("DELETE FROM core.metric WHERE metric_code='cutover_test_metric'")
    print("   после удаления:",
          query("SELECT count(*) FROM catalog.metric WHERE metric_code='cutover_test_metric'")[0][0])
except Exception as e:
    print("   ERR:", str(e)[:250])

print("\n--- контрольный счётчик ---")
print("   core.metric:", query("SELECT count(*) FROM core.metric")[0][0])
print("   catalog.metric:", query("SELECT count(*) FROM catalog.metric")[0][0])