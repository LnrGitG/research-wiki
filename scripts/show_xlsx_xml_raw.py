#!/usr/bin/env python3
"""Первые 900 байт sheetData и блок mergeCells."""
import re
import sys
import zipfile

from xlsx_engine import _sheet_xml_names

p, sheet = sys.argv[1], sys.argv[2]
zf = zipfile.ZipFile(p)
d = zf.read(_sheet_xml_names(zf)[sheet]).decode("utf-8", "replace")
i = d.find("<sheetData>")
print(d[i:i + 900])
j = d.find("<mergeCells")
print("----- mergeCells:", d[j:j + 300] if j != -1 else "нет")
