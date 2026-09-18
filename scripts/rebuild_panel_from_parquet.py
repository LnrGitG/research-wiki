#!/usr/bin/env python3
"""
Пересборка панели регионов из parquet версии 3.0 («Если быть точным»).

Почему пересборка, а не чистка клонов:
- в parquet ДЕДУПЛИКАЦИЯ уже выполнена обработчиком набора (описание, версия
  3.0: «Удалены частичные дубликаты наблюдений»), поэтому 12 419 клонов,
  накопленных в старой панели, там отсутствуют по построению;
- parquet содержит ВСЕ колонки панели плюс четыре: subsection, comment,
  version_date, object_okato — потерь нет;
- множество наблюдений совпадает с панелью полное, в обе стороны:
  296 532 уникальных ключа (код,регион,год,значение,unit,source) — 0 «только
  в панели», 0 «только в parquet»;
- восстановленное измерение subsection заполнено в 100% строк.

Ключ наблюдения: (indicator_code, object_name, year, subsection,
indicator_unit) — единственный вариант из проверенных, дающий уникальность
без остатка (305 130 строк, 0 повторов).

Безопасность: старая таблица не удаляется, а переименовывается в
`regions_panel__panel_collapsed` (откат одной командой RENAME).
"""
import os
import sys

import pyarrow.parquet as pq
import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))

PARQUET = os.environ.get("PANEL_PARQUET", "/home/ubuntu/panel_src.parquet")
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
OLD = "staging.regions_panel__panel"
KEEP = "staging.regions_panel__panel_collapsed"   # прежняя (схлопнутая) под бэкап
NEW = "staging.regions_panel__panel_rebuilt"      # новая до подмены

PARQ_COLS = ["section", "indicator_code", "indicator_name", "subsection",
             "object_name", "object_level", "object_oktmo", "object_okato",
             "year", "indicator_value", "indicator_unit", "comment",
             "source", "version_date"]


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    # --- границы панели: по каким кодам/регионам собирать ---
    cur.execute(f"SELECT DISTINCT indicator_code FROM {OLD}")
    codes = {r[0] for r in cur.fetchall()}
    cur.execute(f"SELECT DISTINCT region_name FROM {OLD}")
    regions = {r[0] for r in cur.fetchall()}
    print(f"границы: {len(codes)} кодов, {len(regions)} регионов", flush=True)

    # --- новая таблица с расширенной схемой ---
    cur.execute(f"DROP TABLE IF EXISTS {NEW}")
    cur.execute(f"""
        CREATE TABLE {NEW} (
            section text, indicator_code text, indicator_name text,
            subsection text, region_name text, region_level text,
            oktmo text, okato text, year integer, value numeric, unit text,
            comment text, source text, version_date text
        )
    """)
    conn.commit()

    f = pq.ParquetFile(PARQUET)
    total = 0
    for b in f.iter_batches(batch_size=50_000, columns=PARQ_COLS):
        d = {c: b.column(c).to_pylist() for c in PARQ_COLS}
        batch = []
        for i in range(b.num_rows):
            if d["indicator_code"][i] not in codes:
                continue
            if d["object_name"][i] not in regions:
                continue
            v = d["indicator_value"][i]
            batch.append((
                d["section"][i], d["indicator_code"][i], d["indicator_name"][i],
                d["subsection"][i], d["object_name"][i], d["object_level"][i],
                d["object_oktmo"][i], d["object_okato"][i], d["year"][i],
                v, d["indicator_unit"][i], d["comment"][i],
                d["source"][i], d["version_date"][i],
            ))
        if batch:
            cur.executemany(
                f"INSERT INTO {NEW} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                batch)
            conn.commit()
        total += len(batch)
        print(f"  загружено {total:,}", flush=True)

    print(f"\nстрок загружено: {total:,}", flush=True)

    # --- проверки ---
    print("\n=== проверки ===", flush=True)
    cur.execute(f"SELECT count(*) FROM {NEW}")
    print(f"  строк в новой: {cur.fetchone()[0]:,}")

    cur.execute(f"""SELECT count(*) FROM (
        SELECT indicator_code, region_name, year, subsection, unit,
               count(*) FROM {NEW} GROUP BY 1,2,3,4,5 HAVING count(*) > 1) x""")
    print(f"  дублей по ключу наблюдения: {cur.fetchone()[0]:,}")

    cur.execute(f"""SELECT count(*) FROM (
        SELECT indicator_code, region_name, year, value, unit, source
        FROM {NEW} EXCEPT
        SELECT indicator_code, region_name, year, value, unit, source
        FROM {OLD}) x""")
    print(f"  наблюдений новой, отсутствующих в старой: {cur.fetchone()[0]:,}")

    cur.execute(f"""SELECT count(*) FROM (
        SELECT indicator_code, region_name, year, value, unit, source
        FROM {OLD} EXCEPT
        SELECT indicator_code, region_name, year, value, unit, source
        FROM {NEW}) x""")
    print(f"  наблюдений старой, отсутствующих в новой: {cur.fetchone()[0]:,}")

    cur.execute(f"SELECT count(DISTINCT indicator_code) FROM {NEW}")
    print(f"  кодов: {cur.fetchone()[0]}")

    cur.execute(f"""SELECT count(*) FROM {NEW}
                    WHERE subsection IS NOT NULL AND subsection <> ''""")
    nsub = cur.fetchone()[0]
    print(f"  с непустым subsection: {nsub:,}")

    print(f"\nследующий шаг (вручную): RENAME {OLD} -> {KEEP}, "
          f"{NEW} -> {OLD}")
    conn.close()


if __name__ == "__main__":
    main()
