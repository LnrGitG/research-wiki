#!/usr/bin/env python3
"""Первые строки листа под двумя движками — для разбора сдвигов."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import xlsx_engine  # noqa: E402

path, sheet, n = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 3
for eng in ("openpyxl", "fastexcel"):
    wb = xlsx_engine.open_workbook(path, engine=eng)
    rows = list(wb[sheet].iter_rows(values_only=True))
    wb.close()
    print(f"--- {eng}: строк {len(rows)}")
    for i, r in enumerate(rows[:n]):
        print(f"  {i+1}: {[str(v)[:22] for v in r[:12]]}")
