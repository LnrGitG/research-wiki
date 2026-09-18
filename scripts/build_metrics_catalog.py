#!/usr/bin/env python3
"""
Генерация каталога метрик для GitHub Pages.

Собирает статистику по каждой метрике из витрины core.v_datalens_observations
и пишет docs/metrics-catalog.json (страница docs/metrics-catalog.html читает
его на клиенте).

Две оценки полезности:
- op  (оперативный анализ, 0–10): частота ряда (месячные весят больше),
  свежесть данных, широта географии, доля свежих наблюдений.
- res (исследования, 0–10): длина ряда в годах, панельная структура
  (число регионов), объём наблюдений, отсутствие накопительного характера.

Запуск:  python3 scripts/build_metrics_catalog.py
"""
import json
import os
from collections import Counter

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs",
                   "metrics-catalog.json")

SQL = """
SELECT metric_code, metric_name, min(source_name), min(unit_name),
       min(year), max(year), count(*),
       count(*) FILTER (WHERE year >= 2025),
       count(DISTINCT year), count(DISTINCT region_code),
       string_agg(DISTINCT frequency_code, ',' ORDER BY frequency_code),
       count(DISTINCT release_label), count(DISTINCT sub_dimension)
FROM core.v_datalens_observations
WHERE value > 0
GROUP BY metric_code, metric_name
"""


def score_operational(freqs, y1, recent, total, nreg):
    """Пригодность для оперативного анализа: свежесть и частота важнее всего."""
    s = 3 if "M" in freqs else (2 if "Q" in freqs else 0)
    s += 3 if y1 >= 2026 else (1 if y1 >= 2025 else 0)
    if total:
        s += min(2, int(3 * recent / total))
    s += 2 if nreg >= 60 else (1 if nreg >= 20 else 0)
    return s


def score_research(freqs, y0, y1, nyears, nreg, total):
    """Пригодность для исследований: длина ряда и панельная структура."""
    s = 3 if nyears >= 20 else (2 if nyears >= 10 else (1 if nyears >= 5 else 0))
    s += 3 if nreg >= 60 else (2 if nreg >= 20 else (1 if nreg >= 5 else 0))
    s += 2 if total >= 5000 else (1 if total >= 1000 else 0)
    s += 1 if (y1 - y0 + 1) >= 20 else 0
    s += 1 if not ("M" in freqs or "Q" in freqs) else 0
    return s


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()
    cur.execute(SQL)
    rows = cur.fetchall()
    conn.close()

    recs = []
    for (code, name, src, unit, y0, y1, n, recent, nyears, nreg,
         freqs, nrel, nsubd) in rows:
        y0, y1 = int(y0 or 0), int(y1 or 0)
        n, recent, nyears, nreg = int(n), int(recent), int(nyears), int(nreg)
        fl = [f for f in (freqs or "").split(",") if f]
        recs.append({
            "c": code, "n": name, "s": src or "—", "u": unit or "—",
            "y0": y0, "y1": y1, "sp": (y1 - y0 + 1) if y0 else 0,
            "r": n, "rec": recent, "ny": nyears, "nr": nreg, "f": fl,
            "rel": int(nrel), "sd": int(nsubd),
            "op": score_operational(fl, y1, recent, n, nreg),
            "res": score_research(fl, y0, y1, nyears, nreg, n),
        })

    recs.sort(key=lambda x: (-x["res"], -x["r"]))
    path = os.path.abspath(OUT)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(recs, f, ensure_ascii=False)

    print("метрик: %s" % format(len(recs), ","))
    print("файл: %s (%.0f КБ)" % (path, os.path.getsize(path) / 1024))
    for s, cnt in Counter(r["s"] for r in recs).most_common():
        tot = sum(r["r"] for r in recs if r["s"] == s)
        print("  %-14s %5d метрик  %s наблюдений" % (s, cnt, format(tot, ",")))


if __name__ == "__main__":
    main()
