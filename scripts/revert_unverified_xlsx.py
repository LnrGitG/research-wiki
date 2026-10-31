#!/usr/bin/env python3
"""Вернуть на openpyxl скрипты, которые не прошли сверку.

Правило карточки: без сверки на живом файле скрипт не переводится. Сюда
попадают (а) файлы с расхождением содержимого книги или результата разбора и
(б) скрипты, для которых живого сырья в репозитории нет. Оба случая
возвращаются к `openpyxl.load_workbook` через git checkout — парсер не
переписывается, откат точечный.

Запуск: python3 scripts/revert_unverified_xlsx.py [--apply]
Без --apply печатает список.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT = os.path.join(ROOT, "findings/xlsx-migration-verify-20261031.json")


def verdicts(report):
    keep, revert = [], []
    for e in report:
        script = e["script"]
        files = e.get("files", [])
        bad = [f["file"] for f in files if not f["ok"]]
        parse_ok = (e.get("parse") or {}).get("ok")
        if not files and parse_ok is None:
            revert.append((script, "сырья для сверки нет"))
        elif bad:
            revert.append((script, f"расхождение: {', '.join(os.path.basename(b) for b in bad[:3])}"))
        elif parse_ok is False:
            revert.append((script, "результат разбора расходится"))
        else:
            keep.append((script, len(files)))
    return keep, revert


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    with open(REPORT, encoding="utf-8") as fh:
        report = json.load(fh)
    keep, revert = verdicts(report)
    print(f"остаются на fastexcel: {len(keep)}")
    for s, n in keep:
        print(f"  + {s} (файлов {n})")
    print(f"\nвозвращаются на openpyxl: {len(revert)}")
    for s, why in revert:
        print(f"  - {s}: {why}")
    if args.apply and revert:
        paths = [s for s, _ in revert]
        cp = subprocess.run(["git", "checkout", "--", *paths], cwd=ROOT,
                            capture_output=True, text=True)
        print(cp.stdout or cp.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
