#!/usr/bin/env python3
"""freshness_digest.py — сторож контура данных (линия B).

Три класса сигналов вместо одного:
  1) загрузчик упал или молчит (ops.ingest_run);
  2) ряд отстал против норматива публикации источника, а не против
     произвольного допуска в днях (derived.v_observation_latest + лаг из
     derived.v_publication_lag_trusted);
  3) сам сторож не отработал дольше ожидаемого (файл-отметка).

Тихий режим: при норме не печатает ничего и выходит с кодом 0. Любое
отклонение — печать отчёта и код 1, чтобы cron-джоба была помечена сбойной.

Только чтение. Никаких записей в БД, кроме файла-отметки рядом со скриптом.

Запуск: python3 scripts/freshness_digest.py [--verbose]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

DSN = dict(host="127.0.0.1", port=15432, dbname="research_wiki", user="wiki",
           connect_timeout=15)
REPO = Path(__file__).resolve().parent.parent
MARK = REPO / "logs" / ".freshness_digest_last"
JOBS_MAP = REPO / "scripts" / "ingest_jobs.json"

# Норматив публикации по источнику, дни: p90 наблюдённого лага там, где он есть,
# иначе — запасное значение по частоте (используется только до накопления данных).
FALLBACK_NORM = {
    "rosstat": 45, "fedstat_emiss": 45, "cbr": 30, "fns": 45, "domrf": 40,
    "reestr": 40, "minfin": 30, "iminfin": 40, "smartlab": 45, "moex": 5,
    "yandex": 30, "trudvsem": 30, "hh": 30, "kep": 10, "worldbank": 365,
    "derived_internal": 0,
}
SCHEDULED_JOB_MAX_SILENCE_H = 72          # джоб считается молчащим после 72 ч
STALE_METRIC_MIN_OBS = 12                 # мелкие ряды в отчёт не берём
TOP = 15


def connect():
    import psycopg
    return psycopg.connect(**DSN)


def load_jobs_map() -> dict:
    try:
        return {k: v for k, v in json.loads(JOBS_MAP.read_text(encoding="utf-8")).items()
                if not k.startswith("_")}
    except Exception:  # noqa: BLE001
        return {}


def norms(cur) -> dict:
    """Норматив = p90 лага, посчитанного по данным, пришедшим после 01.10.2026."""
    cur.execute("""
        select s.source_code,
               percentile_cont(0.9) within group (order by l.lag_days)
        from derived.v_publication_lag_trusted l
        join catalog.source s on s.source_id = l.source_id
        where l.published_from_ingest and l.lag_days is not null
        group by 1
        having count(*) >= 20
    """)
    measured = {code: int(round(v)) for code, v in cur.fetchall()}
    out = {}
    for code, fb in FALLBACK_NORM.items():
        out[code] = max(measured.get(code, fb), 0)
    out["_measured"] = measured
    return out


def loaders(cur, jobs_map) -> list[str]:
    problems = []
    cur.execute("""
        select parser_script, status, exit_code, started_at::date, left(coalesce(output_tail,''), 160)
        from ops.ingest_run
        where started_at > now() - interval '48 hours' and status = 'failed'
        order by started_at desc
    """)
    for parser, status, code, day, tail in cur.fetchall():
        first = (tail or "").strip().splitlines()
        problems.append(f"загрузчик упал: {parser} ({day}), код {code}"
                        + (f", вывод: {first[-1][:120]}" if first else ""))

    cur.execute("select parser_script, max(started_at) from ops.ingest_run group by 1")
    last_by_parser = {p: t for p, t in cur.fetchall()}
    cur.execute("""select endpoint_id, max(started_at) from ops.ingest_run
                    where endpoint_id is not null group by 1""")
    last_by_endpoint = {e: t for e, t in cur.fetchall()}

    now = datetime.now(timezone.utc)
    for job, meta in jobs_map.items():
        seen = last_by_parser.get(job)
        if seen is None and meta.get("endpoint_id") is not None:
            seen = last_by_endpoint.get(meta["endpoint_id"])
        if seen is None:
            problems.append(f"загрузчик не журналирует ни одного прогона: {job}")
        elif now - seen > timedelta(hours=SCHEDULED_JOB_MAX_SILENCE_H):
            hrs = int((now - seen).total_seconds() // 3600)
            problems.append(f"загрузчик молчит {hrs} ч: {job} (последний {seen:%d.%m %H:%M})")
    return problems


def stale_rows(cur, norms_by_source) -> list[str]:
    """Ряд отстал: ожидаемый следующий период плюс норматив источника уже прошёл."""
    cur.execute("""
        with last as (
            select o.metric_id,
                   count(*) as n,
                   max(o.period_end) as last_end,
                   max(o.period_start) as last_start,
                   max(o.frequency_id) as freq,
                   max(o.source_id) as source_id
            from data.observation o
            where o.observation_status <> 'rejected'
            group by o.metric_id
        )
        select m.metric_code, left(m.name_ru, 60), c.freq_code,
               (c.months_per_period * 30) as step, s.source_code,
               l.last_start, l.last_end, l.n
        from last l
        join catalog.metric m on m.metric_id = l.metric_id
        join catalog.source s on s.source_id = l.source_id
        left join catalog.frequency c on c.frequency_id = l.freq
        where l.n >= %s and c.months_per_period > 0 and l.last_end is not null
          and m.status = 'active'
          and l.last_end >= current_date - interval '18 months'
        """, (STALE_METRIC_MIN_OBS,))
    today = date.today()
    out = []
    for code, name, fcode, step, source_code, last_start, last_end, n in cur.fetchall():
        norm = norms_by_source.get(source_code, FALLBACK_NORM.get(source_code, 45))
        step = step or 1
        nxt_end = last_end + timedelta(days=step)
        overdue = (today - (nxt_end + timedelta(days=norm))).days
        if overdue > 0:
            out.append((overdue, code, name, fcode, source_code, last_end, n))
    out.sort(reverse=True)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true", help="печатать сводку даже при норме")
    args = ap.parse_args()

    jobs_map = load_jobs_map()
    conn = connect()
    cur = conn.cursor()

    try:
        norms_by_source = norms(cur)
        loader_problems = loaders(cur, jobs_map)
        stale = stale_rows(cur, norms_by_source)

        cur.execute("""
            with last as (
                select metric_id, count(*) n, max(period_end) last_end
                from data.observation where observation_status <> 'rejected'
                group by 1
            )
            select count(*) from last l join catalog.metric m using(metric_id)
            where l.n >= %s and m.status = 'active'
              and l.last_end < current_date - interval '18 months'
        """, (STALE_METRIC_MIN_OBS,))
        closed_series = cur.fetchone()[0]

        cur.execute("""select count(*) from ops.alert
                        where delivered_at is null
                          and acknowledged_at is null
                          and raised_at < now() - interval '1 day'""")
        pending_alerts = cur.fetchone()[0]

        cur.execute("select count(*) from ops.ingest_run where started_at > now() - interval '24 hours'")
        runs_24h = cur.fetchone()[0]
    finally:
        conn.close()

    lines = []
    if loader_problems:
        lines.append("Загрузчики:")
        lines += [f"  - {p}" for p in loader_problems[:TOP]]

    if stale:
        groups = {}
        for overdue, code, name, fcode, source_code, last_end, n in stale:
            groups.setdefault(source_code, []).append((overdue, code, name, last_end, n))
        lines.append(f"Ряды отстали против норматива ({len(stale)} метрик):")
        for source_code, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            norm = norms_by_source.get(source_code, 45)
            sample = items[:3]
            tail = "; ".join(f"{c} «{nm}» до {le:%m.%Y} (+{od} дн)" for od, c, nm, le, _ in sample)
            lines.append(f"  - {source_code} (норматив {norm} дн): {len(items)} метрик; {tail}")

    if closed_series:
        lines.append(f"Рядов без движения более 18 месяцев (кандидаты в архив): {closed_series}")

    if pending_alerts:
        lines.append(f"Алерты без доставки старше суток: {pending_alerts}")

    if runs_24h == 0:
        lines.append("Журнал загрузок пуст за сутки: ни один загрузчик не отработал")

    mark_ok = True
    try:
        if MARK.exists():
            prev = datetime.fromisoformat(MARK.read_text().strip())
            gap = (datetime.now(timezone.utc) - prev).total_seconds() / 3600
            if gap > 36:
                lines.append(f"Сторож не отрабатывал {gap:.0f} ч (пропущены прогоны)")
        MARK.parent.mkdir(parents=True, exist_ok=True)
        MARK.write_text(datetime.now(timezone.utc).isoformat())
    except Exception:  # noqa: BLE001
        mark_ok = False

    measured = norms_by_source.get("_measured", {})
    if not lines:
        if args.verbose:
            tail = ", ".join(f"{k} {v} дн" for k, v in sorted(measured.items())) or "нет замеров"
            print(f"Сторож: норма. Прогонов за сутки {runs_24h}, алертов без доставки 0. "
                  f"Нормативы: {tail}.")
        return 0
        return 0

    header = (f"Сторож контура данных, {datetime.now(timezone.utc):%d.%m.%Y %H:%M} UTC. "
              f"Прогонов за сутки: {runs_24h}.")
    print(header)
    print("\n".join(lines))
    if measured:
        print("Нормативы (p90 наблюдённого лага, дни): "
              + ", ".join(f"{k} {v}" for k, v in sorted(measured.items())))
    if not mark_ok:
        print("Отметка о прогоне не записана — проверьте права на logs/")
    return 1


if __name__ == "__main__":
    sys.exit(main())
