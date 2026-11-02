#!/usr/bin/env python3
"""Статический разбор мест чтения xlsx: совместимо ли с scripts/xlsx_engine.py.

Для каждого вызова openpyxl.load_workbook в scripts/ и loader/ смотрит
окружающий код (тело функции, где стоит вызов, плюс 40 строк после) и
ищет конструкции, которых нет в контракте xlsx_engine:

    .max_row / .max_column / .dimensions / .merged_cells
    .cell(...)  .iter_rows(min_col=/max_col=/max_row=)
    wb[0] (лист по индексу), ws.rows, ws.values
    iter_rows(...) без values_only -> кортежи Cell

Вывод — JSON-список мест с вердиктом, чтобы не судить на глаз.

Запуск: python3 scripts/scan_xlsx_sites.py [--json out.json]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ("scripts", "loader")

PATTERNS = [
    (re.compile(r"\.max_row\b"), "ws.max_row"),
    (re.compile(r"\.max_column\b"), "ws.max_column"),
    (re.compile(r"\.dimensions\b"), "ws.dimensions"),
    (re.compile(r"\.merged_cell"), "merged_cells"),
    (re.compile(r"\.cell\s*\("), ".cell()"),
    (re.compile(r"iter_rows\([^)]*(min_col|max_col)"), "iter_rows(min_col/max_col)"),
    (re.compile(r"iter_rows\([^)]*max_row\s*="), "iter_rows(max_row=)"),
    (re.compile(r"\bwb\s*\[\s*\d+\s*\]"), "wb[индекс]"),
    (re.compile(r"\.rows\b(?!\s*=)"), "ws.rows"),
    (re.compile(r"\.values\b"), "ws.values"),
    (re.compile(r"iter_rows\((?![^)]*values_only)[^)]*\)"), "iter_rows без values_only"),
    (re.compile(r"\.sheet_by_index|worksheets\["), "лист по индексу"),
    (re.compile(r"xlrd|\.xls\b|\.xlsb|\.ods\b"), "не-xlsx формат"),
]


def body_for(text: str, pos: int) -> str:
    """Тело объемлющей функции (или модуля) вокруг позиции pos."""
    start = text.rfind("\ndef ", 0, pos)
    if start < 0:
        start = 0
    nxt = text.find("\ndef ", pos)
    end = nxt if nxt > 0 else len(text)
    return text[start:end]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    args = ap.parse_args()

    sites = []
    for d in DIRS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for fn in sorted(os.listdir(base)):
            if not fn.endswith(".py"):
                continue
            if fn.startswith(("xlsx_engine", "test_xlsx", "bench_xlsx", "scan_xlsx")):
                continue
            path = os.path.join(base, fn)
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"(openpyxl\.)?load_workbook\s*\(", text):
                # только вызовы, а не импорты/сообщения
                line = text[:m.start()].count("\n") + 1
                body = body_for(text, m.start())
                hits = []
                for pat, name in PATTERNS:
                    if pat.search(body):
                        hits.append(name)
                # путь: аргумент вызова
                arg = text[m.end():text.find("\n", m.end())].split(",")[0].strip()
                sites.append({
                    "file": f"{d}/{fn}",
                    "line": line,
                    "arg": arg,
                    "features": sorted(set(hits)),
                    "verdict": "skip" if hits else "convert",
                })
    for s in sites:
        print(f"{s['file']}:{s['line']}\t{s['verdict']}\t{','.join(s['features']) or '-'}")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(sites, fh, ensure_ascii=False, indent=1)
        print(f"\nвсего мест: {len(sites)}, к переводу: {sum(1 for s in sites if s['verdict'] == 'convert')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
