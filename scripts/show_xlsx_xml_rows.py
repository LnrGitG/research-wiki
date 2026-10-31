#!/usr/bin/env python3
"""Сырая разметка первых строк листа (что реально лежит в XML)."""
import re
import sys
import zipfile

from xlsx_engine import _sheet_xml_names

path, sheet = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(path) as zf:
    data = zf.read(_sheet_xml_names(zf)[sheet]).decode("utf-8", "replace")
m = re.search(r'<dimension ref="([^"]+)"', data)
print("dimension:", m.group(1) if m else "нет")
head = data[:data.find("</sheetData>")][:3000]
for rm in re.finditer(r'<row [^>]*>', head):
    print(rm.group(0))
cells = re.findall(r'<c r="([A-Z]+\d+)"[^>]*(?:/>|>)', head)
print("первые ячейки:", cells[:12])
