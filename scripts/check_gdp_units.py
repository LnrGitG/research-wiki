#!/usr/bin/env python3
"""Проверка единиц и последнего периода в официальном файле Росстата по ВВП (.xls, нужен xlrd).

Зачем: метрики ВВП в базе не имеют единиц (unit_id = unknown), а значения в таблице использования
(около 36,5 трлн за квартал) не похожи на номинальный объём. Скрипт читает первоисточник и печатает
шапку, строку с наименованием единиц и последние значения строки «Валовой внутренний продукт».
"""
import sys

import xlrd

path = sys.argv[1] if len(sys.argv) > 1 else '/tmp/GDP-quarters-of-use-1995_1kv-2026.xls'
wb = xlrd.open_workbook(path)
print('файл:', path)
print('листов:', wb.nsheets, [wb.sheet_by_index(i).name for i in range(min(4, wb.nsheets))])

for sheet_idx in range(min(3, wb.nsheets)):
    sh = wb.sheet_by_index(sheet_idx)
    print(f'\n=== лист {sheet_idx} «{sh.name}»: {sh.nrows} x {sh.ncols}')
    for r in range(min(10, sh.nrows)):
        cells = [str(sh.cell_value(r, c))[:30] for c in range(min(5, sh.ncols))]
        if any(c.strip() for c in cells):
            print(f'  {r}:', ' | '.join(cells))
    for r in range(sh.nrows):
        v0 = str(sh.cell_value(r, 0))
        if 'Валовой внутренний продукт' in v0:
            vals = [sh.cell_value(r, c) for c in range(max(0, sh.ncols - 5), sh.ncols)]
            print(f'  строка «{v0[:52]}», последние значения: {vals}')
            break
    # строка периодов: ищем последние ячейки с датами
    for r in range(min(8, sh.nrows)):
        row = [str(sh.cell_value(r, c)) for c in range(sh.ncols)]
        tail = [x for x in row if x and ('кв' in x.lower() or '/' in x or '.' in x)]
        if len(tail) >= 4:
            print('  периоды (хвост):', tail[-5:])
            break