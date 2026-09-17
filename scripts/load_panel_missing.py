#!/usr/bin/env python3
"""
Точечная догрузка: только те CSV, где есть коды, которым ещё не хватает
subsection. Вместо прогона всех 40 файлов — адресная выборка.

Процесс, запускавшийся полным перебором, погибал при перезапуске шлюза,
не доходя до нужных томов «Регионов России».
"""
import zipfile, csv, io, os, sys
from collections import defaultdict
import psycopg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))

ZIP = 'raw/rosstat/regions_collection_102/data_regions_collection_102_v20260313_csv.zip'
DSN = os.environ.get("PGDSN", "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
TABLE = 'staging.panel_subsection'


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    # коды, у которых строка панели ещё не находит subsection
    cur.execute("""
        SELECT DISTINCT p.indicator_code
        FROM staging.regions_panel__panel p
        WHERE NOT EXISTS (
          SELECT 1 FROM staging.panel_subsection s
          WHERE s.indicator_code = p.indicator_code
            AND s.object_name = p.region_name AND s.year = p.year
            AND s.indicator_value = p.value)
    """)
    missing = {r[0] for r in cur.fetchall()}
    print(f"кодов без subsection: {len(missing)}", flush=True)

    cur.execute(f"SELECT DISTINCT csv_file FROM {TABLE}")
    done = {r[0] for r in cur.fetchall()}

    z = zipfile.ZipFile(ZIP)
    # какой файл содержит какие из недостающих кодов
    file_codes = defaultdict(set)
    for fn in z.namelist():
        if not fn.endswith('.csv') or 'MACOSX' in fn or fn in done:
            continue
        with z.open(fn) as f:
            txt = io.TextIOWrapper(f, encoding='utf-8-sig')
            for r in csv.DictReader(txt, delimiter=';'):
                c = r.get('indicator_code')
                if c in missing and (r.get('subsection') or '').strip():
                    file_codes[fn].add(c)

    todo = sorted(file_codes, key=lambda x: -len(file_codes[x]))
    print(f"файлов с нужными кодами: {len(todo)}", flush=True)
    for fn in todo:
        print(f"  {len(file_codes[fn]):>4} кодов  {fn}", flush=True)

    total = 0
    for fn in todo:
        with z.open(fn) as f:
            txt = io.TextIOWrapper(f, encoding='utf-8-sig')
            batch = []
            for r in csv.DictReader(txt, delimiter=';'):
                if not (r.get('subsection') or '').strip():
                    continue
                if r.get('indicator_code') not in missing:
                    continue           # берём только нужные коды
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
                cur.executemany(
                    f'INSERT INTO {TABLE} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', batch)
                conn.commit()
            total += len(batch)
            print(f"  {fn[:50]:52} {len(batch):>7,}", flush=True)

    print(f"\nдогружено строк: {total:,}", flush=True)
    cur.execute(f'SELECT count(*) FROM {TABLE}')
    print(f"всего в таблице: {cur.fetchone()[0]:,}", flush=True)

    cur.execute("""
        SELECT count(*) FROM staging.regions_panel__panel p
        WHERE EXISTS (SELECT 1 FROM staging.panel_subsection s
          WHERE s.indicator_code=p.indicator_code AND s.object_name=p.region_name
            AND s.year=p.year AND s.indicator_value=p.value)
    """)
    m = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM staging.regions_panel__panel")
    t = cur.fetchone()[0]
    print(f"СХОДИМОСТЬ: {m:,}/{t:,} ({100*m/t:.1f}%)", flush=True)
    conn.close()


if __name__ == '__main__':
    main()
