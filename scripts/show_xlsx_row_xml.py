#!/usr/bin/env python3
"""Разметка строки листа: какие колонки реально есть в XLSX и что отдаёт движок.

Помогает отличить потерю пустой колонки внутри диапазона от сдвига строк.
"""
import re
import sys
import zipfile

from xlsx_engine import _sheet_xml_names

path = sys.argv[1]
sheet = sys.argv[2]
row = sys.argv[3] if len(sys.argv) > 3 else "9"
with zipfile.ZipFile(path) as zf:
    xml_name = _sheet_xml_names(zf).get(sheet)
    data = zf.read(xml_name).decode("utf-8", "replace")
m = re.search(r'<dimension ref="([^"]+)"', data)
print("dimension:", m.group(1) if m else "нет")
rm = re.search(rf'<row r="{row}"[^>]*>(.*?)</row>', data, re.S)
if rm:
    cells = re.findall(r'<c r="([A-Z]+)\d+"([^>]*)(?:/>|>(.*?)</c>)', rm.group(1), re.S)
    print(f"строка {row}: ячеек в XML {len(cells)}")
    for col, attrs, inner in cells:
        has_val = "<v>" in (inner or "") or "<is>" in (inner or "")
        print(f"  {col}: attrs={attrs.strip()[:40]!r} значение={'да' if has_val else 'нет'}")
