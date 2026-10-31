#!/usr/bin/env python3
"""Замер и сверка читателей xlsx: openpyxl против fastexcel.

Каждый движок прогоняется в отдельном процессе, чтобы пик RSS был честным
(maxrss процесса не сбрасывается). Сверка идёт по всему содержимому книги:
число строк, sha256 канонической текстовой формы значений, а при
расхождении — отчёт по колонкам (лист, номер колонки, примеры).

Запуск:
    python3 scripts/bench_xlsx_engine.py FILE [FILE ...] [--json out.json]

Внутренний режим одного движка (используется самим замером):
    python3 scripts/bench_xlsx_engine.py FILE --one fastexcel
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import resource
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xlsx_engine import cell_text, open_workbook  # noqa: E402

PY = sys.executable


def _row_text(row) -> str:
    """Канонический текст строки без хвостовых пустых ячеек.

    Ширина строки у openpyxl и fastexcel различается (openpyxl дополняет
    строку до max_column листа нулями), поэтому хвост из пустых ячеек
    отбрасывается — на значения это не влияет.
    """
    cells = [cell_text(v) for v in row]
    while cells and cells[-1] == "":
        cells.pop()
    return "\t".join(cells)


def _is_blank(row) -> bool:
    return all(cell_text(v) == "" for v in row)


def scan(path, engine):
    """Полный проход книги: строки, sha, отпечатки колонок."""
    t0 = time.perf_counter()
    wb = open_workbook(path, engine=engine)
    digest = hashlib.sha256()
    sheets = {}
    try:
        for name in wb.sheetnames:
            rows = [r for r in wb[name].iter_rows(values_only=True)]
            while rows and _is_blank(rows[-1]):
                rows.pop()
            sha = hashlib.sha256()
            cols = {}
            for r in rows:
                sha.update((_row_text(r) + "\n").encode())
                for i, v in enumerate(r):
                    t = cell_text(v)
                    if t == "":
                        continue
                    cols.setdefault(i, hashlib.sha256()).update(
                        (t + "\x1f").encode())
            sheets[name] = {
                "rows": len(rows),
                "width": max((len(r) for r in rows), default=0),
                "sha": sha.hexdigest(),
                "col_sha": {str(k): v.hexdigest() for k, v in cols.items()},
            }
            for k in sorted(sheets[name]["col_sha"]):
                digest.update(sheets[name]["col_sha"][k].encode())
    finally:
        wb.close()
    elapsed = time.perf_counter() - t0
    return {
        "engine": engine,
        "path": os.path.abspath(path),
        "size_bytes": os.path.getsize(path),
        "sheets": len(sheets),
        "rows_total": sum(s["rows"] for s in sheets.values()),
        "sha_book": digest.hexdigest()[:16],
        "seconds": round(elapsed, 3),
        "peak_rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1),
        "_sheets": sheets,
    }


def run_child(path, engine):
    cp = subprocess.run([PY, os.path.abspath(__file__), path, "--one", engine],
                        capture_output=True, text=True)
    if cp.returncode != 0:
        raise RuntimeError(f"{engine} упал на {path}:\n{cp.stderr[-1500:]}")
    return json.loads(cp.stdout.strip().splitlines()[-1])


def diff_report(a, b, limit=8):
    """Сравнить два прохода (openpyxl=a, fastexcel=b) и описать расхождения."""
    rows = []
    only_a = sorted(set(a["_sheets"]) - set(b["_sheets"]))
    only_b = sorted(set(b["_sheets"]) - set(a["_sheets"]))
    if only_a or only_b:
        rows.append({"level": "sheet", "detail": f"только в openpyxl: {only_a}; "
                                                f"только в fastexcel: {only_b}"})
    for name in sorted(set(a["_sheets"]) & set(b["_sheets"])):
        sa, sb = a["_sheets"][name], b["_sheets"][name]
        if sa["sha"] != sb["sha"]:
            bad = [c for c in sa["col_sha"]
                   if sa["col_sha"].get(c) != sb["col_sha"].get(c)]
            rows.append({"level": "sheet", "sheet": name,
                         "rows": [sa["rows"], sb["rows"]],
                         "columns": bad[:limit],
                         "columns_total": len(bad)})
        elif sa["rows"] != sb["rows"]:
            rows.append({"level": "rows-only", "sheet": name,
                         "rows": [sa["rows"], sb["rows"]]})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--one", choices=("openpyxl", "fastexcel"))
    ap.add_argument("--json")
    args = ap.parse_args()

    if args.one:
        print(json.dumps(scan(args.files[0], args.one), ensure_ascii=False))
        return 0

    report = []
    ok = True
    for path in args.files:
        base = run_child(path, "openpyxl")
        fast = run_child(path, "fastexcel")
        diffs = diff_report(base, fast)
        same = base["sha_book"] == fast["sha_book"] and base["rows_total"] == fast["rows_total"]
        ok = ok and same
        rec = {
            "file": os.path.basename(path),
            "size_mb": round(base["size_bytes"] / 1048576, 2),
            "sheets": base["sheets"],
            "rows": base["rows_total"],
            "openpyxl": {"s": base["seconds"], "rss_mb": base["peak_rss_mb"],
                         "sha": base["sha_book"]},
            "fastexcel": {"s": fast["seconds"], "rss_mb": fast["peak_rss_mb"],
                          "sha": fast["sha_book"]},
            "speedup": round(base["seconds"] / fast["seconds"], 2) if fast["seconds"] else None,
            "identical": same,
            "diffs": diffs,
        }
        report.append(rec)
        print(f"{rec['file']:44s} {rec['sheets']:3d} лист {rec['rows']:8d} строк  "
              f"openpyxl {rec['openpyxl']['s']:7.2f} с -> fastexcel "
              f"{rec['fastexcel']['s']:6.2f} с  x{rec['speedup']:5.2f}  "
              f"sha {'=' if same else '!'}")
        for d in diffs:
            print(f"    РАСХОЖДЕНИЕ {d}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"files": report, "identical_all": ok}, fh,
                      ensure_ascii=False, indent=1)
        print(f"отчёт: {args.json}")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
