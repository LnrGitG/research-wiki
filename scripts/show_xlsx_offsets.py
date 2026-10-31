#!/usr/bin/env python3
"""Сдвиги листа по разметке XLSX (row_lead, col_lead) и первые ячейки."""
import sys

import xlsx_engine

path, sheet = sys.argv[1], sys.argv[2]
print("offsets:", xlsx_engine.xml_sheet_offsets(path, sheet))
wb = xlsx_engine.open_workbook(path, engine="fastexcel")
rows = list(wb[sheet].iter_rows(values_only=True))
wb.close()
print("строк:", len(rows))
for i, r in enumerate(rows[:4]):
    print(f"  {i+1}: {[str(v)[:18] for v in r[:9]]}")
