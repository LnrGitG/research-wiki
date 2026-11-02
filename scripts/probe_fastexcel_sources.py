#!/usr/bin/env python3
"""Проверка: что принимает fastexcel.read_excel — путь, bytes, BytesIO, tmp-файл .tmp."""
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fastexcel
from xlsx_engine import open_workbook

SRC = "raw/cbr/bulletin/mortgage_lending_market_2608_76.xlsx"
if not os.path.exists(SRC):
    print("нет файла", SRC)
    sys.exit(1)
raw = open(SRC, "rb").read()
print("размер", len(raw))
for label, obj in (("bytes", raw), ("BytesIO", io.BytesIO(raw))):
    try:
        r = fastexcel.read_excel(obj)
        print(label, "-> ok, листов", len(r.sheet_names))
    except Exception as e:
        print(label, "-> FAIL", type(e).__name__, str(e)[:120])
# путь с расширением .tmp (скрипты иногда качают во временный файл)
tmp = tempfile.mkdtemp(prefix="xlsxprobe-")
p = os.path.join(tmp, "book.tmp")
open(p, "wb").write(raw)
try:
    wb = open_workbook(p, engine="fastexcel")
    print("путь .tmp -> ok, листов", len(wb.sheetnames))
    wb.close()
except Exception as e:
    print("путь .tmp -> FAIL", type(e).__name__, str(e)[:120])
try:
    wb = open_workbook(p, engine="openpyxl")
    print("путь .tmp openpyxl -> ok, листов", len(wb.sheetnames))
except Exception as e:
    print("путь .tmp openpyxl -> FAIL", type(e).__name__, str(e)[:120])
shutil.rmtree(tmp)
