#!/usr/bin/env python3
"""Этап F: починить derived.metric_card.

Сейчас это обычная таблица (в неё молча не создалось представление, потому
что имя было занято). Переименовываем её в metric_card_legacy и создаём
настоящее материализованное представление под прежним именем, чтобы читатели
не пострадали.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

print("=== текущий тип derived.metric_card ===")
r = query("""SELECT c.relkind FROM pg_class c
             JOIN pg_namespace n ON n.oid=c.relnamespace
             WHERE n.nspname='derived' AND c.relname='metric_card'""")
print("   ", r[0][0] if r else "нет")
print("   строк:", query("SELECT count(*) FROM derived.metric_card")[0][0])
print("   колонки:", [x[0] for x in query(
    "SELECT column_name FROM information_schema.columns "
    "WHERE table_schema='derived' AND table_name='metric_card' ORDER BY ordinal_position")])

# 1) переименовать старую таблицу, освободив имя
try:
    execute("ALTER TABLE derived.metric_card RENAME TO metric_card_legacy")
    print("\nOK   старая таблица -> derived.metric_card_legacy")
except Exception as e:
    print("\n(переименование пропущено)", str(e)[:160])

# 2) создать материализованное представление
try:
    execute("""CREATE MATERIALIZED VIEW IF NOT EXISTS derived.metric_card AS
               SELECT m.metric_id,
                      m.metric_code,
                      m.name_ru,
                      u.unit_code,
                      s.source_code,
                      f.freq_code,
                      MAX(o.period_start) AS last_observation,
                      COUNT(o.*)          AS observations_cnt
               FROM catalog.metric    m
               JOIN catalog.unit      u ON u.unit_id      = m.unit_id
               JOIN catalog.source    s ON s.source_id    = m.source_id
               JOIN catalog.frequency f ON f.frequency_id = m.frequency_id
               LEFT JOIN data.observation o ON o.metric_id = m.metric_id
               GROUP BY m.metric_id, m.metric_code, m.name_ru,
                        u.unit_code, s.source_code, f.freq_code""")
    print("OK   представление создано")
except Exception as e:
    print("ERR  создание:", str(e)[:250])

try:
    execute("CREATE UNIQUE INDEX IF NOT EXISTS ux_metric_card ON derived.metric_card (metric_id)")
    print("OK   уникальный индекс для REFRESH CONCURRENTLY")
except Exception as e:
    print("ERR  индекс:", str(e)[:160])

print("\n=== контроль ===")
r = query("""SELECT c.relkind FROM pg_class c
             JOIN pg_namespace n ON n.oid=c.relnamespace
             WHERE n.nspname='derived' AND c.relname='metric_card'""")
print("   тип теперь:", r[0][0] if r else "нет", "(m = материализованное представление)")
try:
    print("   строк:", query("SELECT count(*) FROM derived.metric_card")[0][0])
except Exception as e:
    print("   строк: ERR", str(e)[:120])
print("   legacy-таблица:", query(
    "SELECT count(*) FROM derived.metric_card_legacy")[0][0] if query(
    """SELECT 1 FROM information_schema.tables
       WHERE table_schema='derived' AND table_name='metric_card_legacy'""") else "нет")