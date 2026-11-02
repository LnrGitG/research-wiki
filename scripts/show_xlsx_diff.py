#!/usr/bin/env python3
"""Показать расхождения из отчёта сверки: файл, лист, колонки, примеры."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import bench_xlsx_engine as bench

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    ROOT, "findings", "xlsx-migration-verify-20261031.json")
report = json.load(open(path, encoding="utf-8"))
for entry in report:
    for f in entry["files"]:
        if f["ok"]:
            continue
        print("=" * 70)
        print(entry["script"], "->", f["file"], f.get("error", ""))
        if "error" in f:
            continue
        full = os.path.join(ROOT, f["file"])
        a = bench.scan(full, "openpyxl")
        b = bench.scan(full, "fastexcel")
        print("строк:", a["rows_total"], "vs", b["rows_total"],
              "| sha:", a["sha_book"], "vs", b["sha_book"])
        for d in bench.diff_report(a, b):
            print("  ", json.dumps(d, ensure_ascii=False)[:600])
    p = entry.get("parse")
    if p and p.get("ok") is False:
        print("=" * 70)
        print(entry["script"], "разбор расходится:", p["openpyxl"], p["fastexcel"])
