#!/usr/bin/env python3
"""Профилировщик региональных публикаций Росстата «Информация для мониторинга».

Источник: https://rosstat.gov.ru/storage/mediabank/info-stat-MM-YYYY.zip
(страница rosstat.gov.ru/folder/11109, печатная версия ?print=1 отдаёт ссылки).
Архив — 15 разделов и ~54 файла xlsx/xls; внутри каждого файла несколько листов,
на каждом листе одна широкая таблица: строка 1–3 — название и единица, строка 4
(иногда 4–5) — шапка периодов (годы объединёнными блоками, ниже месяцы или
кварталы), с 5–6 строки — Российская Федерация, федеральные округа, субъекты.

Задача скрипта — не грузить, а измерить: сколько серий и наблюдений даёт источник,
какой у них горизонт и совпадает ли структура между файлами. Результат — JSON и
markdown-таблица для инвентаризации.

Запуск:
    python3 scripts/rosstat_monitoring_profile.py /tmp/mon/info-stat-09-2026 \
        --out queries/rosstat-monitoring-inventory-20261029
"""
import argparse
import json
import os
import re
import sys

MONTHS = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
          'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11,
          'декабрь': 12}
QUARTERS = {'i квартал': 1, 'ii квартал': 2, 'iii квартал': 3, 'iv квартал': 4,
            '1 квартал': 1, '2 квартал': 2, '3 квартал': 3, '4 квартал': 4}
# «2017 год2», «2018 год 1)» — сноски-надстрочники попадают в текст ячейки,
# поэтому хвост после «год» не должен запрещать совпадение.
YEAR_RE = re.compile(r'^((?:19|20)\d\d)\s*(?:год|г\.?)?\s*[\d\)\s]*$', re.I)
REGION_HINT = re.compile(r'(область|край|Республик|округ|Москва|Петербург|Севастополь)', re.I)


def clean(v):
    if v is None:
        return ''
    return re.sub(r'\s+', ' ', str(v)).strip()


def num(v):
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    return float(s) if re.match(r'^[-+]?\d*\.?\d+$', s) else None


def read_rows(path, max_rows=250, max_cols=250):
    """Список листов: [(имя, список строк значений)] для .xlsx и .xls."""
    if path.lower().endswith('.xls'):
        import xlrd
        book = xlrd.open_workbook(path, on_demand=True)
        out = []
        for name in book.sheet_names():
            sh = book.sheet_by_name(name)
            rows = [[sh.cell_value(r, c) for c in range(min(sh.ncols, max_cols))]
                    for r in range(min(sh.nrows, max_rows))]
            out.append((name, rows))
        book.release_resources()
        return out
    import openpyxl
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out = []
    for name in wb.sheetnames:
        rows = []
        for i, row in enumerate(wb[name].iter_rows(values_only=True)):
            if i >= max_rows:
                break
            rows.append(list(row[:max_cols]))
        out.append((name, rows))
    wb.close()
    return out


def find_header(rows):
    """(индекс строки годов, индексы строк периодов) либо (None, []).

    Годы ищутся как отдельная строка с ≥3 ячейками вида «2021 год»; периоды —
    следующая за ней строка (для месячных шапок их может быть две: месяцы и
    номера графов).
    """
    year_idx = None
    for i, row in enumerate(rows[:12]):
        years = sum(1 for v in row if YEAR_RE.match(clean(v)))
        if years >= 3:
            year_idx = i
            break
    if year_idx is None:
        return None, []
    period_rows = []
    for j in range(year_idx + 1, min(year_idx + 4, len(rows))):
        cells = [clean(v).lower() for v in rows[j]]
        months = sum(1 for c in cells if c.split('-')[0].strip() in MONTHS)
        quarters = sum(1 for c in cells if c in QUARTERS or c in ('год',))
        if months >= 3 or quarters >= 3:
            period_rows.append(j)
        else:
            break
    return year_idx, period_rows


def column_periods(rows, year_idx, period_rows):
    """{индекс колонки: (год, период)} с протяжкой годов вправо (объединённые ячейки)."""
    year_row = rows[year_idx]
    year = None
    years = []
    for v in year_row:
        m = YEAR_RE.match(clean(v))
        if m:
            year = int(m.group(1))
        years.append(year)
    labels = {}
    cols = {}
    if period_rows:
        prow = rows[period_rows[0]]
        for ci, v in enumerate(prow):
            labels[ci] = clean(v).lower()
    else:
        # Годовые листы (например, 07-01 «млн. рублей», 13-01 «2016–2025 гг.»):
        # строки периодов нет, каждый столбец года — самостоятельный период.
        for ci, y in enumerate(years):
            if y is not None:
                cols[ci] = (y, 0)
        return cols
    for ci, label in labels.items():
        y = years[ci] if ci < len(years) else None
        if y is None:
            continue
        if label in QUARTERS:
            cols[ci] = (y, QUARTERS[label] * 3)          # квартал кодируем последним месяцем
        elif label == 'год':
            cols[ci] = (y, 0)
        else:
            first = label.split('-')[0].strip()
            last = label.split('-')[-1].strip()
            if first in MONTHS and last in MONTHS:
                cols[ci] = (y, MONTHS[last])              # накопительный период
    return cols


def profile_file(path):
    sheets = []
    for name, rows in read_rows(path):
        year_idx, period_rows = find_header(rows)
        info = dict(sheet=name, rows=len(rows), header_row=None, periods=0,
                    period_min=None, period_max=None, regions=0, cells=0,
                    title='', unit='', kind=None)
        for r in rows[:3]:
            for v in r:
                s = clean(v)
                if len(s) > 12 and not info['title']:
                    info['title'] = s[:140]
                elif s and not info['unit'] and len(s) <= 40:
                    info['unit'] = s[:40]
        if year_idx is not None:
            cols = column_periods(rows, year_idx, period_rows)
            info['header_row'] = year_idx + 1
            info['periods'] = len(set(cols.values()))
            info['kind'] = 'monthly' if any(m for _, m in cols.values() if m) else 'annual'
            regions, cells = set(), 0
            filled = {}
            start = max(period_rows) + 1 if period_rows else year_idx + 2
            for row in rows[start:]:
                label = clean(row[0]) if row else ''
                if not label or not REGION_HINT.search(label):
                    continue
                regions.add(label)
                for ci in cols:
                    if ci < len(row) and num(row[ci]) is not None:
                        cells += 1
                        filled[ci] = filled.get(ci, 0) + 1
            info['regions'] = len(regions)
            info['cells'] = cells
            # Горизонт считаем по колонкам, где реально есть значения: шапка
            # резервирует месяцы до декабря, но данные доходят только до
            # последнего опубликованного месяца (сентябрь 2026).
            if filled:
                ps = sorted({cols[ci] for ci in filled})
                info['period_min'] = '%04d-%02d' % (ps[0][0], ps[0][1] or 1)
                info['period_max'] = '%04d-%02d' % (ps[-1][0], ps[-1][1] or 1)
        sheets.append(info)
    return sheets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('root', help='каталог распакованного архива info-stat-MM-YYYY')
    ap.add_argument('--out', default=None, help='префикс для .json и .md')
    args = ap.parse_args()

    files = []
    for dirpath, _, names in os.walk(args.root):
        for n in sorted(names):
            if n.lower().endswith(('.xlsx', '.xls')):
                files.append(os.path.join(dirpath, n))
    if not files:
        sys.exit('в %s нет xlsx/xls' % args.root)

    report = []
    for f in files:
        rel = os.path.relpath(f, args.root)
        sheets = profile_file(f)
        report.append(dict(file=rel, sheets=sheets))
        tot = sum(s['cells'] for s in sheets)
        print('%-90s листов %d  ячеек %8d' % (rel[:90], len(sheets), tot), flush=True)

    total_cells = sum(s['cells'] for f in report for s in f['sheets'])
    print('\nфайлов %d, листов %d, непустых наблюдений %d'
          % (len(report), sum(len(f['sheets']) for f in report), total_cells))

    if args.out:
        with open(args.out + '.json', 'w', encoding='utf-8') as fh:
            json.dump(dict(root=args.root, total_cells=total_cells, files=report),
                      fh, ensure_ascii=False, indent=1)
        print('записано', args.out + '.json')


if __name__ == '__main__':
    main()
