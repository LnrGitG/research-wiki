#!/usr/bin/env python3
"""
Загрузка только тех CSV сборника, где есть колонка subsection для
показателей с коллизиями (8 файлов из 40 вместо полного прогона).

Полный список файлов — /tmp/needed_csv.txt (определён по пересечению
кодов с коллизиями и содержимого архива).
"""
import zipfile, csv, io, os, sys
import psycopg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))

ZIP = 'raw/rosstat/regions_collection_102/data_regions_collection_102_v20260313_csv.zip'
DSN = os.environ.get("PGDSN", "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
TABLE = 'staging.panel_subsection'

NEEDED = [n.strip() for n in open('/tmp/needed_csv.txt') if n.strip()]


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()
    cur.execute(f'DROP TABLE IF EXISTS {TABLE}')
    cur.execute(f"""
        CREATE TABLE {TABLE} (
            indicator_code text, indicator_name text, subsection text,
            object_name text, year integer, indicator_value numeric,
            indicator_unit text, source text, csv_file text
        )
    """)
    cur.execute(f'CREATE INDEX ON {TABLE} (indicator_code, object_name, year, source)')
    conn.commit()

    z = zipfile.ZipFile(ZIP)
    total = 0
    for fn in NEEDED:
        with z.open(fn) as f:
            txt = io.TextIOWrapper(f, encoding='utf-8-sig')
            batch = []
            for r in csv.DictReader(txt, delimiter=';'):
                if not (r.get('subsection') or '').strip():
                    continue          # без subsection строка бесполезна
                try:
                    y = int(r.get('year')) if r.get('year') else None
                except ValueError:
                    y = None
                try:
                    v = float(str(r.get('indicator_value')).replace(',', '.')) \
                        if r.get('indicator_value') else None
                except ValueError:
                    v = None
                batch.append((r.get('indicator_code'), r.get('indicator_name'),
                              r['subsection'].strip(), r.get('object_name'), y, v,
                              r.get('indicator_unit'), r.get('source'), fn))
            if batch:
                cur.executemany(f'INSERT INTO {TABLE} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                batch)
                conn.commit()
            total += len(batch)
        print(f"  {fn[:52]:54} {len(batch):>7,}", flush=True)

    print(f"\nвсего строк с subsection: {total:,}")
    cur.execute(f'SELECT count(*) FROM {TABLE}')
    print(f"в базе: {cur.fetchone()[0]:,}")

    cur.execute(f"""SELECT count(DISTINCT indicator_code) FROM {TABLE}""")
    print(f"кодов: {cur.fetchone()[0]}")

    print("\nY477050017 — подразделы:")
    cur.execute(f"""SELECT subsection, count(*) FROM {TABLE}
                    WHERE indicator_code='Y477050017'
                    GROUP BY 1 ORDER BY 2 DESC""")
    for s, n in cur.fetchall():
        print(f"  {n:>6,}  {s[:66]}")
    conn.close()


if __name__ == '__main__':
    main()
