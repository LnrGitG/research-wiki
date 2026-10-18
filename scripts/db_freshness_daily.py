#!/usr/bin/env python3
"""Обёртка cron-джоба «DB freshness daily check» (no_agent).

Запускает репозиторный сторож scripts/db_freshness_check.py из
~/research-wiki-private. Тот двухслойный: ops.check_freshness()
снимает снимок в ops.freshness_snapshot, скрипт сводит снимок по
источникам и печатает JSON с разбивкой по catalog.source.

Режим watchdog: если _summary.status == 'ok' — молчим (пустой stdout,
снапшот всё равно снят движком); если 'issues' — печатаем по одной
строке на проблемный источник. Восстановлена 15.10.2026 (джоб
0210941406c7 потерян при переезде ВМ).
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

REPO = "/home/lnr/research-wiki-private"
TARGET = os.path.join(REPO, "scripts", "db_freshness_check.py")

PY = "/home/lnr/.hermes/hermes-agent/venv/bin/python3"
if not os.path.exists(PY):
    PY = sys.executable

if not os.path.exists(TARGET):
    print("freshness: скрипт не найден: %s" % TARGET)
    raise SystemExit(1)

env = dict(os.environ)
env.setdefault("PGDSN", "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")

r = subprocess.run([PY, TARGET], cwd=REPO, capture_output=True, text=True, env=env)
if r.returncode != 0:
    sys.stderr.write(r.stderr or "")
    print("freshness: сторож вернул код %d" % r.returncode)
    raise SystemExit(r.returncode)

try:
    data = json.loads(r.stdout)
except Exception:
    # не распарсили — отдаём как есть, лучше шум, чем тишина
    sys.stdout.write(r.stdout)
    raise SystemExit(0)

# Сторож магических заглушек «нет данных» (−99 999 999 / −77 777 777):
# они портят средние и суммы, если попадают в выборку как обычные значения.
sent = subprocess.run([PY, os.path.join(REPO, "scripts", "reject_sentinels.py"),
                       "--check"], cwd=REPO, capture_output=True, text=True, env=env)
sent_alarm = sent.stdout.strip() if sent.returncode != 0 else ""

# Раз в месяц — сводка по активным карточкам без наблюдений (A-6): карточка есть,
# ряда нет. Это план, а не мусор, поэтому не тревога, а раз в месяц одна строка
# с разбивкой по тегам (stage6 — промпродукция и т. д.).
orphan_line = ""
if datetime.now(timezone.utc).day == 1 or os.environ.get("ORPHAN_FORCE") == "1":
    oc = subprocess.run([PY, os.path.join(REPO, "scripts", "orphan_cards_report.py"), "--check"],
                        cwd=REPO, capture_output=True, text=True, env=env)
    if oc.returncode == 0 and oc.stdout.strip():
        orphan_line = oc.stdout.strip()

summary = data.get("_summary", {})
if summary.get("status") == "ok":
    if sent_alarm:
        print(sent_alarm)
    if orphan_line:
        print(orphan_line)
    raise SystemExit(0)  # watchdog: всё свежее — молчим

lines = ["Свежесть БД: проблемных источников %s" % summary.get("problem_sources", "?")]
for src, v in data.items():
    if src.startswith("_") or not isinstance(v, dict):
        continue
    if v.get("status") != "ok":
        lines.append(
            "%s: метрик %s, свежих %s, отстают %s, устарели %s, нет данных %s; "
            "последний период %s, худший лаг %s дн."
            % (src, v.get("metrics"), v.get("fresh"), v.get("lagging"),
               v.get("stale"), v.get("nodata"), v.get("last_period"),
               v.get("worst_lag_days"))
        )
if sent_alarm:
    lines.append(sent_alarm)
if orphan_line:
    lines.append(orphan_line)
print("\n".join(lines))
