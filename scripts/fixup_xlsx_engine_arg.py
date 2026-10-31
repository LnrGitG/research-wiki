#!/usr/bin/env python3
"""Доводка перевода на xlsx_engine: движок из --xlsx-engine в каждом скрипте.

Кодмод первого прохода заменил `openpyxl.load_workbook(...)` на
`open_workbook(...)`, но не протащил выбор движка: откат работал только через
переменную окружения. Здесь в каждый скрипт добавляется

    ENGINE = engine_from_argv()          # --xlsx-engine или XLSX_ENGINE

и каждый вызов чтения получает `engine=ENGINE`. Для скриптов с argparse
дополнительно регистрируется сам флаг `--xlsx-engine`.

Запуск: python3 scripts/fixup_xlsx_engine_arg.py [файл ...]
Без аргументов — все скрипты, где уже есть `open_workbook(`.
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKIP = {"xlsx_engine.py", "test_xlsx_engine.py", "bench_xlsx_engine.py",
        "codemod_xlsx_engine.py", "verify_xlsx_migration.py",
        "_xlsx_verify_call.py", "probe_fastexcel_sources.py",
        "scan_xlsx_sites.py", "show_xlsx_diff.py", "show_xlsx_sites.py",
        "fixup_xlsx_engine_arg.py"}

IMPORT_RE = re.compile(r"from xlsx_engine import open_workbook  # noqa: E402")
CALL_RE = re.compile(r"open_workbook\(([^,()]*)\)")
ENGINE_LINE = ("ENGINE = engine_from_argv()  # --xlsx-engine openpyxl|fastexcel, "
               "резерв — XLSX_ENGINE\n")


def convert(path: str) -> str:
    text = open(path, encoding="utf-8").read()
    if "open_workbook(" not in text or "xlsx_engine import" not in text:
        return "не переведён"
    needs_arg = "parse_args(" in text
    log = []

    if "engine=ENGINE" not in text:
        # 1. инженерный выбор движка на уровне модуля
        if "engine_from_argv" not in text:
            new_imp = ("from xlsx_engine import add_engine_arg, engine_from_argv, "
                       "open_workbook  # noqa: E402" if needs_arg else
                       "from xlsx_engine import engine_from_argv, open_workbook  "
                       "# noqa: E402")
            text, n = IMPORT_RE.subn(new_imp, text)
            log.append(f"импорт x{ (n) }")
        idx = text.rfind("xlsx_engine import")
        if idx == -1:
            return "импорта xlsx_engine нет"
        eol = text.index("\n", idx) + 1
        if "ENGINE = engine_from_argv()" not in text:
            text = text[:eol] + ENGINE_LINE + text[eol:]
            log.append("ENGINE")

        # 2. каждый вызов читает выбранным движком
        text, n = CALL_RE.subn(r"open_workbook(\1, engine=ENGINE)", text)
        log.append(f"вызовов {n}")

    # 3. argparse должен принять флаг, иначе скрипт падает до чтения
    if needs_arg and "add_engine_arg(" not in text.replace(
            "from xlsx_engine import add_engine_arg", ""):
        m = re.search(r"^(\s*)(\w+)\.parse_args\(", text, re.M)
        if m:
            var, indent = m.group(2), m.group(1)
            text = text[:m.start()] + f"{indent}add_engine_arg({var})\n" + text[m.start():]
            log.append(f"add_engine_arg({var})")

    open(path, "w", encoding="utf-8").write(text)
    return ", ".join(log) or "без изменений"


def main(argv: list[str]) -> int:
    if argv:
        targets = [os.path.abspath(p) for p in argv]
    else:
        targets = []
        for d in ("scripts", "loader"):
            for f in sorted(os.listdir(os.path.join(ROOT, d))):
                if not f.endswith(".py") or f in SKIP:
                    continue
                p = os.path.join(ROOT, d, f)
                if "open_workbook(" in open(p, encoding="utf-8", errors="replace").read():
                    targets.append(p)
    for p in targets:
        print(f"{os.path.relpath(p, ROOT)}: {convert(p)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
