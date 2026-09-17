#!/usr/bin/env python3
"""Парсинг Точно-ст RFSD-срезов ОКВЭД F (Строительство) и L (Недвижимость) 2021-2025
в SQLite-панель firm-level: sectoral агрегаты + фирменный длинный столбец.
Выход: data/fns_tochno_sectors.db (tables: firms_<SECTION>_<YEAR> колонки-выборка; sector_aggregate).
"""
import openpyxl, sqlite3, os, sys
from pathlib import Path
from gcs_sync import ensure_db

DB = str(ensure_db('fns_tochno_sectors.db'))
RAW = str(Path(__file__).resolve().parent.parent / 'raw' / 'fns' / 'tochno-st' / 'by_section')
# Колонки для long-формата: идентификаторы + ключевые фин. строки
KEEP = ['year', 'inn', 'okved', 'region', 'filed', 'financial', 'simplified',
        'line_1600', 'line_2110', 'line_2120', 'line_2200', 'line_2400',
        'line_1300', 'line_1230', 'line_1520', 'line_1150', 'line_1210',
        'line_2210', 'line_2220']

def parse(fn, section, year):
    wb = openpyxl.load_workbook(os.path.join(RAW, fn), read_only=True)
    ws = wb['data']
    hdr = [c.value for c in next(ws.iter_rows(min_row=1, max_row=1))]
    idx = {h: i for i, h in enumerate(hdr) if h in KEEP}
    missing = [k for k in KEEP if k not in idx]
    if missing:
        print(f'{fn}: missing {missing}')
    con = sqlite3.connect(DB)
    table = f'firms_{section}_{year}'
    con.execute(f'''CREATE TABLE IF NOT EXISTS {table} (
        year INTEGER, inn TEXT, okved TEXT, region TEXT,
        filed INT, financial INT, simplified INT,
        line_1600 REAL, line_2110 REAL, line_2120 REAL, line_2200 REAL, line_2400 REAL,
        line_1300 REAL, line_1230 REAL, line_1520 REAL, line_1150 REAL, line_1210 REAL,
        line_2210 REAL, line_2220 REAL)''')
    n = 0
    for row in ws.iter_rows(min_row=2, values_only=True):
        con.execute(f'INSERT INTO {table} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    tuple(row[idx.get(k)] if k in idx else None for k in
                          ['year','inn','okved','region','filed','financial','simplified',
                           'line_1600','line_2110','line_2120','line_2200','line_2400',
                           'line_1300','line_1230','line_1520','line_1150','line_1210',
                           'line_2210','line_2220']))
        n += 1
    con.commit()
    print(f'{table}: {n} rows')
    con.close()

if __name__ == '__main__':
    for fn in sorted(os.listdir(RAW)):
        if not fn.endswith('.xlsx') or 'rfsd' not in fn:
            continue
        parts = fn.split('_')
        section, year = parts[3], parts[4]
        try:
            parse(fn, section, year)
        except Exception as e:
            print(f'{fn}: ERR {str(e)[:80]}')
    print('DONE')