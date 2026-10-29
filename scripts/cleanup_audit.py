#!/usr/bin/env python3
"""cleanup_audit.py — замер мусора в каноне перед чисткой (только SELECT).

Считает четыре категории, которые нельзя смешивать:
  1) точные дубли на одном зерне (одинаковое значение) — излишек без потери смысла;
  2) конфликтующие ревизии (разные значения на одном зерне, raw против validated) —
     это не мусор, а неразобранные версии: их сводят правилом, а не удаляют;
  3) сентинелы (значения-заглушки, помеченные rejected) — проверяется, попадают ли
     они в представление последней ревизии;
  4) строки до 2017 года — исторические и ошибочные даты, решение отдельное.

Пишет markdown-отчёт в путь, указанный --out, и JSON рядом (для машинной сверки).
Ничего не меняет в базе: чистка запускается отдельным скриптом после дампа.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DSN = dict(host="127.0.0.1", port=15432, dbname="research_wiki", user="wiki",
           connect_timeout=15)

GRAIN = "metric_id, region_id, period_start, coalesce(frequency_id,0), coalesce(assessment_type,''), coalesce(sub_dimension,'')"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/home/lnr/personal/findings/cleanup-audit-20261029.md")
    ap.add_argument("--statement-timeout", type=int, default=900)
    args = ap.parse_args()

    import psycopg

    conn = psycopg.connect(**DSN)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"set statement_timeout = {args.statement_timeout * 1000}")
    report: dict = {}

    cur.execute("select observation_status, count(*) from data.observation group by 1 order by 2 desc")
    report["by_status"] = cur.fetchall()
    cur.execute("select count(*) from data.observation")
    total = cur.fetchone()[0]
    report["total"] = total

    # 1. точные дубли: одинаковое значение на одном зерне
    cur.execute(f"""
        with d as (
            select {GRAIN}, value, count(*) as n
            from data.observation
            where observation_status not in ('rejected', 'superseded')
            group by 1,2,3,4,5,6, value
            having count(*) > 1
        )
        select count(*) as groups, sum(n - 1) as excess from d
    """)
    report["exact_dups"] = cur.fetchone()

    # 2. конфликтующие ревизии: разные значения на одном зерне
    cur.execute(f"""
        with g as (
            select {GRAIN}, count(distinct value) as n_values, count(*) as n_rows
            from data.observation
            where observation_status not in ('rejected', 'superseded')
            group by 1,2,3,4,5,6
            having count(distinct value) > 1
        )
        select count(*) as groups, sum(n_rows) as rows_in_conflict from g
    """)
    report["conflicts"] = cur.fetchone()

    # 2b. из конфликтов — сколько групп, где есть и raw и validated
    cur.execute(f"""
        with g as (
            select {GRAIN},
                   count(distinct value) as n_values,
                   count(*) filter (where observation_status = 'raw') as n_raw,
                   count(*) filter (where observation_status = 'validated') as n_val,
                   count(*) as n_rows
            from data.observation
            where observation_status not in ('rejected', 'superseded')
            group by 1,2,3,4,5,6
            having count(distinct value) > 1
        )
        select count(*), sum(n_rows), sum(n_raw), sum(n_val)
        from g where n_raw > 0 and n_val > 0
    """)
    report["conflicts_raw_vs_validated"] = cur.fetchone()

    # 3. сентинелы и попадание rejected в представление последней ревизии
    cur.execute("""
        select count(*) from data.observation
        where observation_status = 'rejected'
          and value is not null
          and value in (-999, -9999, -99999, 99999999, -1)
    """)
    report["sentinel_rejected"] = cur.fetchone()[0]
    cur.execute("select count(*) from derived.v_observation_latest where observation_status = 'rejected'")
    report["rejected_in_latest_view"] = cur.fetchone()[0]

    # 4. строки до 2017 года и мусорные даты
    cur.execute("""
        select count(*) filter (where period_start < date '2017-01-01'),
               count(*) filter (where period_start < date '1990-01-01'),
               min(period_start), max(period_start)
        from data.observation where observation_status not in ('rejected', 'superseded')
    """)
    report["pre2017"] = cur.fetchone()

    # 5. будущие периоды (свежесть ломалась именно ими)
    cur.execute("""
        select count(*) from data.observation
        where observation_status not in ('rejected', 'superseded') and period_start > current_date + interval '90 days'
    """)
    report["future_periods"] = cur.fetchone()[0]

    conn.close()

    lines = ["# Аудит мусора в каноне, 29.10.2026", "",
             f"Всего наблюдений в `data.observation`: **{total:,}**.".replace(",", " "), ""]
    lines.append("| Статус | Строк |")
    lines.append("|---|---|")
    for st, n in report["by_status"]:
        lines.append(f"| {st} | {n:,} |".replace(",", " "))
    g, ex = report["exact_dups"]
    g, ex = (g or 0), (ex or 0)
    lines += ["", f"**Точные дубли** (одно значение на одном зерне): групп {g:,}, "
                  f"излишек строк {ex:,}.".replace(",", " ")]
    g, rows = report["conflicts"]
    g, rows = (g or 0), (rows or 0)
    lines.append(f"**Конфликтующие ревизии** (разные значения на одном зерне): групп {g:,}, "
                 f"строк {rows:,} — сведение правилом, не удаление.".replace(",", " "))
    g, rows, nraw, nval = report["conflicts_raw_vs_validated"]
    g, rows, nraw, nval = (g or 0), (rows or 0), (nraw or 0), (nval or 0)
    lines.append(f"Из них группы со смесью raw и validated: {g:,} групп, {rows:,} строк "
                 f"(raw {nraw:,}, validated {nval:,}).".replace(",", " "))
    lines.append(f"**Сентинелы** среди rejected: {report['sentinel_rejected']:,}."
                 .replace(",", " "))
    lines.append(f"**Rejected в представлении последней ревизии**: "
                 f"{report['rejected_in_latest_view']:,}.".replace(",", " "))
    p17, p90, pmin, pmax = report["pre2017"]
    lines.append(f"**До 2017 года**: {p17:,} строк (до 1990: {p90:,}), период от {pmin} до {pmax}."
                 .replace(",", " "))
    lines.append(f"**Будущие периоды** (>90 дней вперёд): {report['future_periods']:,}."
                 .replace(",", " "))

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    Path(args.out).with_suffix(".json").write_text(
        json.dumps({k: (v if not isinstance(v, tuple) else list(v)) for k, v in report.items()},
                   ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
