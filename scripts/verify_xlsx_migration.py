#!/usr/bin/env python3
"""Сверка перевода парсеров на xlsx_engine: файлы и разбор, оба движка.

Два уровня проверки для каждого переведённого скрипта:

1. Файловый. Из кода скрипта вытаскиваются пути сырья (строковые литералы с
   `raw/`, `~/yc-wiki/raw`, `/home/lnr/...`), подставляются существующие файлы
   xlsx; для каждого файла книга прогоняется обоими движками и сверяется
   sha256 канонического содержимого (строки + отпечатки колонок) и число строк.
   Совпадение содержимого книги означает совпадение всего, что парсер из неё
   прочитает, — включая iter_rows(min_row=...), отбор листов и порядок строк.

2. Разборный. Для скриптов с чистой функцией разбора (path -> строки) функция
   вызывается в отдельном процессе под каждым движком, результат
   канонизируется в JSON и сверяется по sha256.

Результат — findings/xlsx-migration-verify-20261031.json и таблица в stdout.
Запуск: python3 scripts/verify_xlsx_migration.py [--json out.json] [--limit N]
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from xlsx_engine import cell_text, open_workbook  # noqa: E402

PY = sys.executable

# script -> (модуль, функция разбора, аргументы) для разборного уровня
PARSE_CALLS = {
    "scripts/direct_sezon.py": ("parse", []),
    "scripts/direct_mosh_sub.py": ("parse", []),
    "scripts/direct_vv_zd.py": ("parse_oper", []),
    # direct_ikv_reg: parse() печатает ход разбора в stdout и ожидает именно
    # файл ИЖК-регистра, поэтому в автоматический разборный уровень не входит;
    # sha результата сверен вручную на Inv_reg_kv_2020-2026 (совпал).
    "scripts/backfill_prom_history.py": ("parse_bulletin", []),
    "scripts/rosstat_monitoring_profile.py": ("read_book", []),
    "scripts/direct_rosstat_monitoring.py": ("read_book", []),
    "loader/parse_cbr_vfs.py": (None, []),
}

MAX_FILES_PER_SCRIPT = 6


def script_paths(script: str) -> list[str]:
    """Пути сырья из кода скрипта -> существующие xlsx-файлы.

    Собираются три вида ссылок: строковые литералы с именем файла (одинарные и
    двойные кавычки), каталоги сырья (`raw/...`, включая склейки из BASE/REPO
    через os.path.join) и glob-шаблоны. Каталог даёт до трёх файлов, чтобы
    сверка не разрасталась на весь raw/.
    """
    text = open(os.path.join(ROOT, script), encoding="utf-8", errors="replace").read()
    found: list[str] = []

    def add_file(p: str) -> None:
        p = os.path.normpath(p)
        if os.path.isfile(p) and p.endswith((".xlsx", ".xlsm")):
            found.append(p)

    def add_dir(p: str) -> None:
        p = os.path.normpath(p)
        if os.path.isdir(p):
            found.extend(sorted(glob.glob(os.path.join(p, "*.xlsx")))[:3])

    # 1. имена файлов в литералах (одинарные и двойные кавычки, кроме f-string)
    for m in re.finditer(r"""(?<![fFrbRB])['"]([^'"\n]{4,200}\.xlsx?[a-z]*)['"]""", text):
        raw = m.group(1)
        if "{" in raw or "%" in raw:
            continue
        cand = raw.replace("~/research-wiki-private", ROOT)
        if not cand.startswith(("/", "raw/", "../")):
            cand = os.path.join(ROOT, cand)
        cand = os.path.normpath(cand)
        if os.path.isfile(cand):
            add_file(cand)
        elif os.path.isdir(cand):
            add_dir(cand)
        elif "*" in cand:
            found.extend(sorted(glob.glob(cand))[:3])
    # 2. каталоги сырья: литералы с raw/ и склейки os.path.join(..., 'raw', ...)
    dir_lits: set[str] = set()
    for m in re.finditer(r"""(?<![fFrbRB])['"]([^'"\n]*raw/[^'"\n]*)['"]""", text):
        dir_lits.add(m.group(1))
    for m in re.finditer(r"""os\.path\.join\(([^)]*['"]raw['"][^)]*)\)""", text):
        parts = [p for p in re.findall(r"""['"]([^'"]+)['"]""", m.group(1)) if p != "raw"]
        if parts:
            dir_lits.add(os.path.join("raw", *parts))
    for m in re.finditer(
            r"""Path\(__file__\)\.resolve\(\)\.parent\.parent\s*/\s*['"]([^'"]+)['"]""", text):
        dir_lits.add(m.group(1))
    for lit in sorted(dir_lits):
        cand = lit.replace("~/research-wiki-private", ROOT)
        if not cand.startswith(("/", "raw/", "../")):
            cand = os.path.join(ROOT, cand)
        if "*" in cand:
            found.extend(sorted(glob.glob(os.path.normpath(cand)))[:3])
        else:
            add_dir(cand)
    # 3. glob по константе каталога: glob.glob(os.path.join(RAW, 'шаблон'))
    for m in re.finditer(r"""glob\.glob\(os\.path\.join\(\s*(\w+)\s*,\s*['"]([^'"]+)['"]""", text):
        var, pat = m.group(1), m.group(2)
        dm = re.search(rf"""^{var}\s*=\s*os\.path\.join\(([^)]*)\)""", text, re.M)
        if not dm:
            continue
        parts = [p for p in re.findall(r"""['"]([^'"]+)['"]""", dm.group(1)) if p != "raw"]
        if parts:
            base = os.path.join(ROOT, "raw", *parts)
            found.extend(sorted(glob.glob(os.path.join(base, pat)))[:3])
    out, seen = [], set()
    for f in found:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out[:MAX_FILES_PER_SCRIPT]


def book_sha(path: str, engine: str):
    """Число строк и sha содержимого книги под данным движком."""
    wb = open_workbook(path, engine=engine)
    h = hashlib.sha256()
    rows_total = 0
    try:
        for name in wb.sheetnames:
            rows = [r for r in wb[name].iter_rows(values_only=True)]
            while rows and all(cell_text(v) == "" for v in rows[-1]):
                rows.pop()
            rows_total += len(rows)
            h.update(name.encode())
            for r in rows:
                cells = [cell_text(v) for v in r]
                while cells and cells[-1] == "":
                    cells.pop()
                h.update(("\t".join(cells) + "\n").encode())
    finally:
        wb.close()
    return rows_total, h.hexdigest()


def compare_file(path: str) -> dict:
    import bench_xlsx_engine as bench
    try:
        a = bench.scan(path, "openpyxl")
        b = bench.scan(path, "fastexcel")
    except Exception as exc:  # noqa: BLE001 — сверка не должна падать целиком
        return {"file": path, "ok": False, "error": f"{type(exc).__name__}: {exc}"}
    ok = a["sha_book"] == b["sha_book"] and a["rows_total"] == b["rows_total"]
    return {"file": os.path.relpath(path, ROOT), "ok": ok,
            "rows_openpyxl": a["rows_total"], "rows_fastexcel": b["rows_total"],
            "sha_openpyxl": a["sha_book"], "sha_fastexcel": b["sha_book"],
            "sheets": a["sheets"]}


def canonical(obj) -> str:
    return hashlib.sha256(
        json.dumps(obj, ensure_ascii=False, sort_keys=True, default=str).encode()
    ).hexdigest()[:16]


def run_parse(script: str, func: str, files: list[str], engine: str):
    """Вызвать функцию разбора в отдельном процессе под данным движком."""
    cp = subprocess.run(
        [PY, os.path.join(HERE, "_xlsx_verify_call.py"), script, func,
         json.dumps(files), engine],
        capture_output=True, text=True, cwd=ROOT, timeout=900,
    )
    if cp.returncode != 0:
        return {"error": (cp.stderr or cp.stdout).strip().splitlines()[-1:] or ["?"]}
    return json.loads(cp.stdout.strip().splitlines()[-1])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=os.path.join(
        ROOT, "findings", "xlsx-migration-verify-20261031.json"))
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    scripts = sorted(
        os.path.relpath(os.path.join(HERE, f), ROOT)
        for f in os.listdir(HERE)
        if f.endswith(".py") and "open_workbook" in open(
            os.path.join(HERE, f), encoding="utf-8", errors="replace").read()
        and not f.startswith(("xlsx_engine", "test_xlsx", "bench_xlsx",
                              "codemod_", "scan_xlsx", "show_xlsx",
                              "verify_xlsx", "probe_fast", "probe_xlsx",
                              "_xlsx_verify", "fixup_xlsx", "_fixup",
                              "summarize_xlsx",
                              "load_rosstat_prices_all"))
    )
    loader = "loader/parse_cbr_vfs.py"
    if os.path.exists(os.path.join(ROOT, loader)):
        scripts.append(loader)
    if args.limit:
        scripts = scripts[:args.limit]

    report, bad = [], 0
    for script in scripts:
        files = script_paths(script)
        entry = {"script": script, "files": []}
        for f in files:
            res = compare_file(f)
            entry["files"].append(res)
            if not res["ok"]:
                bad += 1
        if script in PARSE_CALLS and files:
            func, extra = PARSE_CALLS[script]
            if func:
                entry["parse"] = {}
                for eng in ("openpyxl", "fastexcel"):
                    entry["parse"][eng] = run_parse(script, func, files, eng)
                a = entry["parse"]["openpyxl"].get("sha")
                b = entry["parse"]["fastexcel"].get("sha")
                entry["parse"]["ok"] = a is not None and a == b
                if not entry["parse"]["ok"]:
                    bad += 1
        report.append(entry)
        n_ok = sum(1 for f in entry["files"] if f["ok"])
        p = entry.get("parse", {}).get("ok")
        print(f"{script}: файлов {len(files)}, сверка {n_ok}/{len(files)}"
              + ("" if p is None else f", разбор {'ок' if p else 'РАСХОДИТСЯ'}")
              + ("" if files else " — сырьё не найдено (сверка не выполнена)"))

    os.makedirs(os.path.dirname(args.json), exist_ok=True)
    with open(args.json, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)
    total_files = sum(len(e["files"]) for e in report)
    ok_files = sum(1 for e in report for f in e["files"] if f["ok"])
    print(f"\nскриптов {len(report)}, файловых сверок {ok_files}/{total_files},"
          f" расхождений {bad}; отчёт {args.json}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
