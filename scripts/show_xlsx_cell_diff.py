#!/usr/bin/env python3
"""Диагностика расхождений движков на конкретных файлах сырья.

Печатает первый лист/строку/колонку, где содержимое книг разошлось, и
типы значений в этой колонке под каждым движком.
"""
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import xlsx_engine  # noqa: E402
from xlsx_engine import cell_text  # noqa: E402


def scan(path, engine):
    wb = xlsx_engine.open_workbook(path, engine=engine)
    out = {}
    try:
        for name in wb.sheetnames:
            rows = []
            for r in wb[name].iter_rows(values_only=True):
                cells = list(r)
                while cells and cell_text(cells[-1]) == "":
                    cells.pop()
                rows.append(tuple(cells))
            while rows and not rows[-1]:
                rows.pop()
            out[name] = rows
    finally:
        wb.close()
    return out


def main():
    path = sys.argv[1]
    try:
        a = scan(path, "openpyxl")
    except Exception:
        print("openpyxl упал:"); traceback.print_exc(); return 1
    try:
        b = scan(path, "fastexcel")
    except Exception:
        print("fastexcel упал:"); traceback.print_exc(); return 1
    names = sorted(set(a) | set(b))
    diff = 0
    for name in names:
        ra, rb = a.get(name, []), b.get(name, [])
        if len(ra) != len(rb):
            print(f"лист {name!r}: строк openpyxl {len(ra)}, fastexcel {len(rb)}")
        for i in range(min(len(ra), len(rb))):
            for j in range(max(len(ra[i]), len(rb[i]))):
                va = ra[i][j] if j < len(ra[i]) else "<нет>"
                vb = rb[i][j] if j < len(rb[i]) else "<нет>"
                if cell_text(va) != cell_text(vb):
                    diff += 1
                    if diff <= 15:
                        print(f"лист {name!r} строка {i+1} колонка {j+1}: "
                              f"openpyxl {va!r} ({type(va).__name__}) vs "
                              f"fastexcel {vb!r} ({type(vb).__name__})")
    print(f"расхождений ячеек: {diff}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
