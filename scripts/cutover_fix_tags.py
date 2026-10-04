#!/usr/bin/env python3
"""Выровнять catalog.metric.tags под core (text[] вместо jsonb).

ALTER ... TYPE ... USING с подзапросом PostgreSQL не принимает
(«cannot use subquery in transform expression»), поэтому делаем в четыре шага:
новая колонка -> заполнение -> удаление старой -> переименование.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

t = query("""SELECT data_type FROM information_schema.columns
             WHERE table_schema='catalog' AND table_name='metric'
               AND column_name='tags'""")[0][0]
print("текущий тип tags:", t)

if t == "jsonb":
    steps = [
        ("добавить tags_new", "ALTER TABLE catalog.metric ADD COLUMN IF NOT EXISTS tags_new text[]"),
        ("заполнить", """UPDATE catalog.metric
                         SET tags_new = CASE WHEN tags IS NULL THEN NULL
                            ELSE ARRAY(SELECT jsonb_array_elements_text(tags)) END"""),
        ("удалить старую", "ALTER TABLE catalog.metric DROP COLUMN IF EXISTS tags"),
        ("переименовать", "ALTER TABLE catalog.metric RENAME COLUMN tags_new TO tags"),
    ]
    for label, sql in steps:
        try:
            n = execute(sql)
            print(f"   OK {label}" + (f" ({n} строк)" if n else ""))
        except Exception as e:
            print(f"   ERR {label}: {str(e)[:200]}")
else:
    print("   тип уже", t)

print("\nконтроль:")
r = query("""SELECT data_type, udt_name FROM information_schema.columns
             WHERE table_schema='catalog' AND table_name='metric'
               AND column_name='tags'""")[0]
print("   catalog.metric.tags:", r)
print("   пример:", query("SELECT metric_id, tags FROM catalog.metric WHERE tags IS NOT NULL LIMIT 3"))
print("   всего с тегами:", query("SELECT count(*) FROM catalog.metric WHERE tags IS NOT NULL")[0][0])