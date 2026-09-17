#!/usr/bin/env python3
"""
Восстановление потерянного измерения `subsection` в панели регионов.

Задача. Панель `regions_panel` собиралась из сборника «Регионы России 102»,
но при загрузке терялась колонка `subsection` — она различает строки внутри
показателя (направление инвестиций, распределение по полу и т.п.). Из-за
этого под одним кодом оказывалось несколько значений, и они схлопывались:
104 874 строки панели были потеряны.

Решение. Первоисточник хранит `subsection`; по тем же ключам он содержит
413 850 строк против 308 952 в панели. Поэтому восстановление делается
не соединением (оставило бы схлопнутость), а сборкой `staging.panel_expanded`
из первоисточника с ограничением по ключам панели.

Проверки встроены: полнота включения, отсутствие лишних кодов.
Идемпотентно: DROP + CREATE.

Запуск:
    PGPASSFILE=~/.pgpass python3 scripts/expand_panel_subsection.py
"""
import os
import sys

import psycopg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))

DSN = os.environ.get("PGDSN", "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
SRC = "staging.panel_subsection"
PANEL = "staging.regions_panel__panel"
TARGET = "staging.panel_expanded"


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    # --- проверка 1: полнота включения значений панели ---
    cur.execute(f"""
        SELECT count(*) FROM (
          SELECT DISTINCT indicator_code, region_name, year, value FROM {PANEL}) p
        WHERE NOT EXISTS (
          SELECT 1 FROM {SRC} s
          WHERE s.indicator_code = p.indicator_code
            AND s.object_name = p.region_name
            AND s.year = p.year AND s.indicator_value = p.value)
    """)
    orphan_vals = cur.fetchone()[0]
    print(f"значений панели без пары в первоисточнике: {orphan_vals:,}")

    # --- проверка 2: нет кодов панели, отсутствующих в первоисточнике ---
    cur.execute(f"""
        SELECT count(DISTINCT indicator_code) FROM {PANEL} p
        WHERE NOT EXISTS (SELECT 1 FROM {SRC} s
                          WHERE s.indicator_code = p.indicator_code)
    """)
    orphan_codes = cur.fetchone()[0]
    print(f"кодов панели без пары: {orphan_codes}")

    if orphan_codes:
        print("ВНИМАНИЕ: есть коды панели вне первоисточника — сборка неполна",
              file=sys.stderr)

    # --- сборка ---
    cur.execute(f"DROP TABLE IF EXISTS {TARGET}")
    cur.execute(f"""
        CREATE TABLE {TARGET} AS
        SELECT s.indicator_code,
               s.indicator_name,
               s.subsection,
               s.object_name     AS region_name,
               s.year,
               s.indicator_value AS value,
               s.indicator_unit  AS unit,
               s.source,
               s.csv_file
        FROM {SRC} s
        WHERE EXISTS (SELECT 1 FROM {PANEL} p
                      WHERE p.indicator_code = s.indicator_code
                        AND p.region_name = s.object_name
                        AND p.year = s.year)
    """)
    cur.execute(f"CREATE INDEX ON {TARGET} (indicator_code, region_name, year)")
    conn.commit()

    cur.execute(f"SELECT count(*) FROM {TARGET}")
    n = cur.fetchone()[0]
    cur.execute(f"SELECT count(DISTINCT subsection) FROM {TARGET}")
    nsub = cur.fetchone()[0]
    cur.execute(f"SELECT count(*) FROM {PANEL}")
    np = cur.fetchone()[0]

    print(f"\n{PANEL}: {np:,} строк (схлопнуто)")
    print(f"{TARGET}: {n:,} строк (раскрыто)")
    print(f"различных подписей subsection: {nsub:,}")
    print(f"восстановлено строк: {n - np:,}")

    # --- финальный контроль по ключам ---
    cur.execute(f"""
        SELECT count(*) FROM (
          SELECT DISTINCT indicator_code, region_name, year FROM {PANEL}) p
        WHERE NOT EXISTS (SELECT 1 FROM {TARGET} e
                          WHERE e.indicator_code = p.indicator_code
                            AND e.region_name = p.region_name AND e.year = p.year)
    """)
    print(f"ключей панели без раскрытия: {cur.fetchone()[0]:,}")
    conn.close()


if __name__ == "__main__":
    main()
