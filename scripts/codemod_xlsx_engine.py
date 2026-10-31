#!/usr/bin/env python3
"""Кодмод: перевод мест чтения xlsx с openpyxl на scripts/xlsx_engine.py.

Только чтение: `openpyxl.load_workbook(path, read_only=True, data_only=True)`
-> `open_workbook(path)` плюс импорт `from xlsx_engine import open_workbook`.
Схему БД, разбор и формат наблюдений не трогает. Файлы берутся из списка
FILES, чтобы не задеть места, которые сознательно остаются на openpyxl
(min_col/max_col, .cell(), шаблоны xlsx для записи).

Запуск: python3 scripts/codemod_xlsx_engine.py [--dry]
"""
from __future__ import annotations

import re
import sys

FILES = [
    "scripts/b3_vintage_revision.py",
    "scripts/backfill_prom_2023.py",
    "scripts/backfill_prom_history.py",
    "scripts/bud1.py",
    "scripts/bud2.py",
    "scripts/cbr_banking_canon.py",
    "scripts/cbr_mortgage_vfs_sync.py",
    "scripts/direct_domrf_sales.py",
    "scripts/direct_ikv_reg.py",
    "scripts/direct_ind_prod.py",
    "scripts/direct_mosh.py",
    "scripts/direct_mosh_sub.py",
    "scripts/direct_rosstat_operativ_construction.py",
    "scripts/direct_rosstat_prom.py",
    "scripts/direct_sezon.py",
    "scripts/direct_stroit_pril.py",
    "scripts/direct_vv_zd.py",
    "scripts/kep_collect.py",
    "scripts/load_cbr_primary_market.py",
    "scripts/parse_cbr_lending.py",
    "scripts/rosstat_cpi_mom_ingest.py",
    "scripts/transfer_cbr_vfs.py",
    "scripts/update_cbr_lending.py",
    "scripts/verify_cbr_izhk_definitions.py",
    "scripts/rosstat_prom_products_xlsx.py",
    "scripts/rosstat_sezon_parse.py",
    "scripts/rosstat_vv_zd_files_update.py",
    "scripts/rosstat_prom_files_update.py",
    "scripts/rosstat_inv_files_update.py",
    "scripts/ingest_cbr_pf_fo.py",
    "scripts/ingest_grp.py",
    "scripts/cbr_infom_canon.py",
    "scripts/cbr_lending_update.py",
    "scripts/cbr_mo_canon.py",
    "scripts/cbr_monitoring_canon.py",
    "scripts/ingest_expectations.py",
    "scripts/bashkortostan_smr_story.py",
    "scripts/rosstat_operativ_construction_files_update.py",
    "scripts/direct_rosstat_monitoring.py",
    "scripts/rosstat_monitoring_profile.py",
    "scripts/update_rosstat.py",
    "loader/parse_cbr_vfs.py",
]

IMPORT_BLOCK = (
    "try:\n"
    "    from xlsx_engine import open_workbook  # noqa: E402\n"
    "except ImportError:  # запуск из другого каталога\n"
    "    import os as _os\n"
    "    import sys as _sys\n"
    "    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))\n"
    "    from xlsx_engine import open_workbook  # noqa: E402\n"
)


def patch_text(text: str) -> tuple[str, list[str]]:
    log = []
    # 1. локальные импорты внутри функций больше не нужны
    text, n = re.subn(r"\n[ \t]+import openpyxl\n", "\n", text)
    if n:
        log.append(f"убрано локальных import openpyxl: {n}")
    # 2. `from openpyxl import load_workbook`
    text, nloc = re.subn(r"\n[ \t]+from openpyxl import load_workbook[^\n]*\n", "\n", text)
    if nloc:
        log.append(f"убрано локальных from openpyxl: {nloc}")
    if re.search(r"^from openpyxl import load_workbook", text, re.M):
        text = re.sub(r"^from openpyxl import load_workbook.*$",
                      "from xlsx_engine import open_workbook  # noqa: E402",
                      text, count=1, flags=re.M)
        log.append("from openpyxl import load_workbook -> xlsx_engine")
    # 3. блок try/except вокруг import openpyxl
    text = re.sub(
        r"try:\n    import openpyxl\nexcept ImportError:[^\n]*\n(?:[ \t]+[^\n]*\n)+",
        IMPORT_BLOCK, text, count=1)

    # 4. модульный import openpyxl (в т.ч. `import openpyxl, sqlite3, csv`)
    def repl_module(m):
        names = [x.strip() for x in m.group(1).split(",") if x.strip()]
        names = [x for x in names if x != "openpyxl"]
        out = IMPORT_BLOCK
        if names:
            out = "import " + ", ".join(names) + "\n" + IMPORT_BLOCK
        return out

    text, n = re.subn(r"^import openpyxl((?:,[ \t]*\w+)*)[ \t]*(?:#.*)?$",
                      repl_module, text, count=1, flags=re.M)
    if n:
        log.append("модульный import openpyxl -> xlsx_engine")
    if not n:
        text, n = re.subn(r"^import openpyxl[ \t]*(?:#.*)?$", IMPORT_BLOCK, text,
                          count=1, flags=re.M)
        if n:
            log.append("модульный import openpyxl -> xlsx_engine")
    # 5. вызовы чтения: openpyxl.load_workbook(path, read_only=..., data_only=...)
    text, n = re.subn(r"openpyxl\.load_workbook\(", "open_workbook(", text)
    if n:
        log.append(f"вызовов openpyxl.load_workbook: {n}")
    # 6. параметры openpyxl, которых нет у читателя
    text, n = re.subn(r",\s*read_only\s*=\s*(?:True|False)", "", text)
    text2, n2 = re.subn(r",\s*data_only\s*=\s*(?:True|False)", "", text)
    text = text2
    if n or n2:
        log.append(f"убрано read_only/data_only: {n + n2}")
    # 7. байтовые источники: fastexcel принимает bytes, не BytesIO
    text, n = re.subn(r"open_workbook\(io\.BytesIO\((\w+)\)", r"open_workbook(\1", text)
    if n:
        log.append(f"BytesIO -> bytes: {n}")
    # 8. если модульного импорта не было (openpyxl импортировался только в ветке
    #    функции — смешанные xls/xlsx читатели), вставляем блок перед первым
    #    импортом верхнего уровня
    if "from xlsx_engine import open_workbook" not in text:
        lines = text.splitlines(keepends=True)
        for i, line in enumerate(lines):
            if re.match(r"^(?:import|from) \w", line):
                lines.insert(i, IMPORT_BLOCK + "\n")
                log.append("добавлен импорт читателя")
                break
        text = "".join(lines)
    return text, log



def main() -> int:
    dry = "--dry" in sys.argv
    for f in FILES:
        text = open(f, encoding="utf-8").read()
        new, log = patch_text(text)
        leftover = [l for l in new.splitlines() if "openpyxl" in l]
        print(f"{f}: " + ("; ".join(log) or "без изменений"))
        if leftover:
            print("   ОСТАЛОСЬ: " + " | ".join(l.strip() for l in leftover[:4]))
        if not dry and new != text:
            open(f, "w", encoding="utf-8").write(new)
    return 0


if __name__ == "__main__":
    sys.exit(main())
