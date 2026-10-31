#!/usr/bin/env python3
"""Что видит регекс ячеек в первых 400 КБ листа."""
import re
import sys
import zipfile

from xlsx_engine import _sheet_xml_names

p, sheet = sys.argv[1], sys.argv[2]
zf = zipfile.ZipFile(p)
head = zf.open(_sheet_xml_names(zf)[sheet]).read(400000)
cell_re = re.compile(rb'<c r="([A-Z]+)(\d+)"([^>]*)(/>|>(.{0,120}))', re.S)
for n, mc in enumerate(cell_re.finditer(head)):
    if n > 6:
        break
    print(mc.group(1), mc.group(2), repr(mc.group(3)[:20]), repr(mc.group(4)[:20]),
          repr(mc.group(5)[:30]) if mc.group(5) else None)
