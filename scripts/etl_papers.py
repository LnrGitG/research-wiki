#!/usr/bin/env python3
"""Оркестратор ETL-пайплайна: одна команда вместо четырёх ручных запусков.

До 19.09.2026 шаги запускались вручную, и два из них регулярно забывались:
`build_paper_details.py` (после инжеста файл не содержал новой статьи, пока
его не запускали руками) и пересборка поискового индекса. Здесь это одна
последовательность с единым отчётом и записью метрик.

Порядок стадий — по зависимостям:

    1. metadata   — фронтматтер, авторы, год, DOI
    2. methods    — методы, данные, выводы (зависит от paper-details.json)
    3. references — список литературы
    4. storage    — связка с PDF в бакете
    5. details    — docs/paper-details.json (нужен для стадии 2)
    6. index      — поисковый индекс для сайта
    7. cards      — сборка карточек и SQL для core.paper_card
    8. publish    — публикация базы знаний в публичный репозиторий

Стадии details, index, publish включаются флагом `--with-derived`: они
пишут в отслеживаемые git файлы, поэтому при обычном добавлении статьи
запускать их не нужно — только перед коммитом или публикацией.

Примеры:

    python3 scripts/etl_papers.py --since 2026-09-19     # после инжеста
    python3 scripts/etl_papers.py --only papers/new.md  # одна статья
    python3 scripts/etl_papers.py --with-derived        # плюс индексы и карточки
    python3 scripts/etl_papers.py --report              # только метрики
"""
import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
sys.path.insert(0, os.path.join(REPO, "scripts"))
import etl_common

PY = sys.executable

# Стадия -> (скрипт, дополнительные аргументы)
STAGES = [
    ("metadata",   "extract_metadata.py",   []),
    ("details",    "build_paper_details.py", []),   # paper-details.json
    ("methods",    "extract_methods.py",    []),
    ("references", "extract_references.py", []),
    ("storage",    "link_storage.py",       []),
    ("index",      "build_search_index.py", []),
    ("cards",      "load_papers.py",        ["--build"]),
]

# Что считается «производным» — пишет в git-файлы, нужен перед коммитом
DERIVED = {"details", "index", "cards"}


def run_stage(name, script, extra, passthrough):
    """Запустить стадию. Возвращает (успех, секунды, вывод)."""
    if not os.path.exists(os.path.join("scripts", script)):
        return False, 0.0, "скрипт не найден: scripts/%s" % script
    cmd = [PY, os.path.join("scripts", script)] + list(extra) + list(passthrough)
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
    dt = time.time() - t0
    out = (r.stdout or "") + (r.stderr or "")
    return r.returncode == 0, dt, out


def main():
    ap = argparse.ArgumentParser(description="ETL-пайплайн корпуса публикаций")
    ap.add_argument("--only", nargs="*", default=None,
                    help="обработать только указанные файлы/стемы")
    ap.add_argument("--since", default=None, help="только файлы новее YYYY-MM-DD")
    ap.add_argument("--force", action="store_true", help="полный пересчёт")
    ap.add_argument("--with-derived", action="store_true",
                    help="включить стадии, пишущие в git (details, index, cards)")
    ap.add_argument("--sign", action="store_true",
                    help="обновить presigned-ссылки (флаг по умолчанию включён "
                         "для storage, т.к. карточки идут в БД со ссылками)")
    ap.add_argument("--no-sign", action="store_true",
                    help="не считать presigned-ссылки (быстрее, но в БД уйдут "
                         "пустые ссылки)")
    ap.add_argument("--report", action="store_true",
                    help="показать метрики прошлых прогонов и выйти")
    ap.add_argument("--dry-run", action="store_true",
                    help="показать план стадий, ничего не запуская")
    args = ap.parse_args()

    if args.report:
        return report()

    # Общие флаги, которые передаются всем стадиям, понимающим инкремент
    passthrough = []
    if args.only:
        passthrough += ["--only"] + list(args.only)
    if args.since:
        passthrough += ["--since", args.since]
    if args.force:
        passthrough += ["--force"]

    # --force опасен для производных: полный пересчёт 314 статей займёт
    # минуты там, где нужны секунды. Производным он не передаётся.
    derived_flags = [f for f in passthrough if f != "--force"]

    # storage по умолчанию считает presigned-ссылки: без них карточки уходят
    # в БД с пустым полем presigned_url. Отключается флагом --no-sign.
    sign_flag = [] if args.no_sign else ["--sign"]

    stages = []
    for n, s, e in STAGES:
        if not args.with_derived and n in DERIVED:
            continue
        pf = list(derived_flags if n in DERIVED else passthrough)
        if n == "storage":
            pf += sign_flag
        stages.append((n, s, e, pf))

    print("=== ETL-пайплайн корпуса публикаций ===")
    print("Стадии: %s" % ", ".join(n for n, _, _, _ in stages))
    print("Режим:  %s" % ("полный пересчёт" if args.force else
                          ("только: %s" % ", ".join(args.only) if args.only else
                           ("новее %s" % args.since if args.since else "инкремент"))))
    print()

    if args.dry_run:
        for n, s, e, pf in stages:
            print("  %-12s -> scripts/%s %s" % (n, s, " ".join(list(e) + list(pf))))
        return 0

    t_all = time.time()
    results = []
    for name, script, extra, pf in stages:
        print("--- %s (%s) ---" % (name, script))
        ok, dt, out = run_stage(name, script, extra, pf)
        # показать только содержательные строки, не весь вывод
        keys = ("к обработке", "без изменений", "ВСЕГО найдено", "Время",
                "Артефакт", "OK:", "готово", "Готово", "публикуется", "ERROR",
                "Ошибка", "Traceback", "Карточек собрано")
        for line in out.split("\n"):
            if any(k in line for k in keys):
                print("    %s" % line.strip()[:150])
        print("    -> %s за %.1f с" % ("OK" if ok else "СБОЙ", dt))
        results.append((name, ok, dt, out))
        if not ok:
            print("\nСтадия %s упала. Последние строки:" % name)
            print("\n".join(out.split("\n")[-8:]))
            print("\nПайплайн остановлен — дальше идти нет смысла.")
            break

    total = time.time() - t_all
    ok_n = sum(1 for _, ok, _, _ in results if ok)
    print("\n=== ИТОГ ===")
    print("Стадий успешно: %d из %d" % (ok_n, len(stages)))
    print("Общее время: %.1f с" % total)
    slow = sorted(((d, n) for n, _, d, _ in results), reverse=True)[:3]
    print("Самые долгие: %s" % ", ".join("%s %.1f с" % (n, d) for d, n in slow))

    etl_common.record_run("etl_papers.py", "pipeline", t_all, time.time(),
                          rows=ok_n, status="ok" if ok_n == len(stages) else "failed",
                          extra={"stages": [n for n, _, _, _ in results],
                                 "mode": "force" if args.force else "incremental"})
    failed = [n for n, ok, _, _ in results if not ok]
    return 1 if failed else 0


def report():
    """Сводка метрик прошлых прогонов по стадиям."""
    log = etl_common.run_log()
    if not log:
        print("Метрик нет: %s пуст" % etl_common.PIPELINE_LOG)
        return 0
    print("Метрик прогонов: %d\n" % len(log))
    by = {}
    for e in log:
        st = e.get("stage", "?")
        d = by.setdefault(st, {"n": 0, "ms": 0, "rows": 0, "fail": 0})
        d["n"] += 1
        d["ms"] += e.get("duration_ms", 0)
        d["rows"] += e.get("rows_affected", 0)
        if e.get("status") != "ok":
            d["fail"] += 1
    print("%-14s %5s %10s %9s %6s" % ("стадия", "runs", "сред. мс", "строк", "сбоев"))
    for st, d in sorted(by.items(), key=lambda x: -x[1]["ms"]):
        print("%-14s %5d %10d %9d %6d"
              % (st, d["n"], d["ms"] // max(1, d["n"]), d["rows"], d["fail"]))

    print("\nПоследние 10 прогонов:")
    for e in log[-10:]:
        print("  %s %-14s %7d мс  строк=%-4d %s"
              % (e.get("started_at", "")[5:16], e.get("stage", "?"),
                 e.get("duration_ms", 0), e.get("rows_affected", 0), e.get("status", "")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
