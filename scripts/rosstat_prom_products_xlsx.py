#!/usr/bin/env python3
"""Парсер месячного бюллетеня Росстата Prom_MM_YYYY.xlsx (производство важнейших видов продукции).

Заменяет прежний парсер по markdown-кэшу страницы: тот читал текст через web_extract и был
жёстко привязан к одному месяцу. Здесь разбирается сам xlsx (листы Н-П_NN): для каждого продукта
берётся строка «Российская Федерация без учета…» с тремя графами — отчетный месяц, предыдущий
месяц, период с начала года.

Запись: data/rosstat_construction.db, таблица prom_products_monthly.
"""
import argparse
import datetime
import os
import re
import sqlite3
import sys

import openpyxl

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
from yc_sync import ensure_db  # noqa: E402

CODE_RE = re.compile(r'^\d{2}(\.\d+)+$')
RF_PREFIX = 'Российская Федерация'


def num(v):
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        s = v.strip().replace(' ', '').replace(',', '.')
        try:
            return float(s)
        except ValueError:
            return None
    return None


def parse_sheet(ws):
    """(продукт, единица, okpd2, месяц, предыдущий, накопленный) для строк РФ."""
    out = []
    product, okpd2, unit = None, None, None
    for row in ws.iter_rows(values_only=True):
        a = row[0] if len(row) > 0 else None
        b = row[1] if len(row) > 1 else None
        if isinstance(a, str) and isinstance(b, str) and CODE_RE.match(b.strip()) and len(a.strip()) > 3:
            product, okpd2, unit = a.strip(), b.strip(), None
            continue
        if product and unit is None and isinstance(a, str) and a.strip():
            bs = str(b).strip() if b is not None else ''
            if bs.isdigit() and len(bs) <= 6:  # строка единицы измерения с кодом ОКЕИ
                unit = a.strip()
                continue
        if isinstance(a, str) and a.strip().startswith(RF_PREFIX) and product:
            vals = [num(row[i]) if len(row) > i else None for i in (2, 3, 4)]
            if any(v is not None for v in vals):
                out.append((product, unit, okpd2, vals[0], vals[1], vals[2]))
            product, okpd2, unit = None, None, None  # один РФ-ряд на блок продукта
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('path', nargs='?', default=None, help='Prom_MM_YYYY.xlsx; по умолчанию — свежий в raw/prom/')
    args = ap.parse_args()

    if args.path:
        path = args.path
    else:
        files = []
        for d in (os.path.join(REPO, 'raw', 'prom'), os.path.join(REPO, 'raw', 'rosstat', 'operational')):
            if os.path.isdir(d):
                files += [os.path.join(d, f) for f in os.listdir(d) if re.match(r'Prom_\d{2}_\d{4}\.xlsx$', f)]
        if not files:
            sys.exit('не найден Prom_MM_YYYY.xlsx в raw/prom')
        path = sorted(files)[-1]

    m = re.search(r'Prom_(\d{2})_(\d{4})', os.path.basename(path))
    if not m:
        sys.exit('не разобрать месяц/год из имени файла: ' + os.path.basename(path))
    month, year = int(m.group(1)), int(m.group(2))
    print('файл:', os.path.basename(path), '| период: %04d-%02d' % (year, month))

    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    con = sqlite3.connect(str(ensure_db('rosstat_construction.db')))
    con.execute('''CREATE TABLE IF NOT EXISTS prom_products_monthly (
        product TEXT, year INTEGER, month INTEGER,
        value_month REAL, value_prev_month REAL, value_ytd REAL,
        source TEXT, ingested_at TEXT DEFAULT (datetime('now')),
        PRIMARY KEY (product, year, month))''')
    have = {r[0] for r in con.execute("PRAGMA table_info(prom_products_monthly)")}
    for col in ('unit', 'okpd2'):
        try:
            con.execute(f'ALTER TABLE prom_products_monthly ADD COLUMN {col} TEXT')
        except sqlite3.OperationalError:
            pass  # колонка уже есть

    rows, now = [], datetime.datetime.now().isoformat()
    for sheet in wb.sheetnames:
        if sheet in ('Содержание', 'Лист1'):
            continue
        for product, unit, okpd2, vm, vp, vytd in parse_sheet(wb[sheet]):
            rows.append((product, year, month, vm, vp, vytd,
                         f'rosstat_Prom_{month:02d}_{year}', now, unit, okpd2))
    wb.close()

    con.executemany('''INSERT OR REPLACE INTO prom_products_monthly
        (product, year, month, value_month, value_prev_month, value_ytd, source, ingested_at, unit, okpd2)
        VALUES (?,?,?,?,?,?,?,?,?,?)''', rows)
    con.commit()
    n = con.execute('SELECT count(*) FROM prom_products_monthly WHERE year=? AND month=?', (year, month)).fetchone()[0]
    print('разобрано продуктов:', len(rows), '| в таблице за %04d-%02d: %d' % (year, month, n))

    # строительный срез как контроль
    keys = ('цемент', 'бетон', 'кирпич', 'блоки', 'стекло', 'плитки', 'трубы', 'прокат',
            'лифты', 'пески', 'конструкции и детали', 'окна', 'двери', 'фанера')
    print('\n=== строительный срез (отчетный месяц / предыдущий / с начала года) ===')
    for r in con.execute('''SELECT product, value_month, value_prev_month, value_ytd, unit
                            FROM prom_products_monthly WHERE year=? AND month=? ORDER BY product''', (year, month)):
        low = r[0].lower()
        if any(k in low for k in keys):
            print(f'  {r[0][:62]:62} {r[1]} / {r[2]} / {r[3]}  [{r[4] or "—"}]')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())