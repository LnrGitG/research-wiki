#!/usr/bin/env python3
"""
Представление для Yandex DataLens: наблюдения с человекочитаемыми названиями.

Зачем: core.observation_v2 хранит числовые идентификаторы (metric_id, region_id),
а в графиках нужны названия («Вологодская область», «Инвестиции в жилые здания»).
Представление соединяет наблюдения со справочниками, чтобы датасет в DataLens
строился без ручной настройки связей.

Запуск: venv/bin/python make_datalens_view.py
Идемпотентно: CREATE OR REPLACE VIEW.
"""
import os
import sys

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")

VIEW = "core.v_datalens_observations"

SQL = f"""
CREATE OR REPLACE VIEW {VIEW} AS
SELECT
    o.obs_id,
    -- когда
    o.period_start,
    o.period_end,
    EXTRACT(YEAR  FROM o.period_start)::int  AS year,
    EXTRACT(MONTH FROM o.period_start)::int  AS month,
    EXTRACT(QUARTER FROM o.period_start)::int AS quarter,
    f.frequency_code,
    f.name_ru          AS frequency_name,
    -- что
    m.metric_code,
    m.name_ru          AS metric_name,
    m.short_name_ru    AS metric_short_name,
    m.metric_type,
    m.is_derived,
    m.tags             AS metric_tags,
    u.unit_code,
    u.name_ru          AS unit_name,
    -- где
    r.region_code,
    r.name_ru          AS region_name,
    r.level            AS region_level,
    r.oktmo,
    -- значение
    o.value,
    o.value_str,
    o.sub_dimension,
    o.assessment_type,
    o.observation_status,
    o.quality_flags,
    -- откуда
    s.source_code,
    s.name_ru          AS source_name,
    rl.release_label,
    rl.published_at
FROM core.observation_v2 o
LEFT JOIN core.metric    m  ON m.metric_id    = o.metric_id
LEFT JOIN core.region    r  ON r.region_id    = o.region_id
LEFT JOIN core.frequency f  ON f.frequency_id = o.frequency_id
LEFT JOIN core.unit      u  ON u.unit_id      = m.unit_id
LEFT JOIN core.source    s  ON s.source_id    = o.source_id
LEFT JOIN core.release   rl ON rl.release_id  = o.release_id
"""


def main():
    conn = psycopg.connect(DSN)
    conn.autocommit = True
    cur = conn.cursor()

    print("=== создаю представление ===", flush=True)
    cur.execute(SQL)
    print(f"  {VIEW} создано", flush=True)

    # права на чтение для DataLens
    cur.execute(f"GRANT SELECT ON {VIEW} TO datalens_ro")
    print("  права выданы роли datalens_ro", flush=True)

    print("\n=== проверки ===", flush=True)
    cur.execute(f"SELECT count(*) FROM {VIEW}")
    n = cur.fetchone()[0]
    print(f"  строк: {n:,}")

    cur.execute(f"""SELECT count(*) FROM {VIEW}
                    WHERE metric_name IS NULL OR region_name IS NULL""")
    print(f"  строк без названия метрики или региона: {cur.fetchone()[0]:,}")

    cur.execute(f"SELECT count(DISTINCT metric_code) FROM {VIEW}")
    print(f"  метрик: {cur.fetchone()[0]:,}")
    cur.execute(f"SELECT count(DISTINCT region_code) FROM {VIEW}")
    print(f"  регионов: {cur.fetchone()[0]:,}")
    cur.execute(f"SELECT count(DISTINCT source_code) FROM {VIEW}")
    print(f"  источников: {cur.fetchone()[0]:,}")

    print("\n=== контрольный пример: 6 направлений инвестиций ===", flush=True)
    cur.execute(f"""
        SELECT value, sub_dimension, region_name, year, source_name
        FROM {VIEW}
        WHERE metric_code = 'y477050017' AND region_name = 'Вологодская область'
          AND year = 2024
        ORDER BY value DESC""")
    rows = cur.fetchall()
    print(f"  строк: {len(rows)}")
    for v, sd, rn, y, sn in rows:
        print(f"    {v:>7}  [{y}] {str(sd)[:58]}")

    print("\n=== структура представления ===", flush=True)
    cur.execute("""SELECT column_name, data_type FROM information_schema.columns
                   WHERE table_schema='core' AND table_name='v_datalens_observations'
                   ORDER BY ordinal_position""")
    for c, d in cur.fetchall():
        print(f"    {c:22} {d}")

    conn.close()
    print("\nГОТОВО")


if __name__ == "__main__":
    main()
