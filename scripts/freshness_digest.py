#!/usr/bin/env python3
"""freshness_digest.py — сторож контура данных (линия B).

Отвечает на три вопроса и молчит, когда отвечать нечего:
  1) какой загрузчик упал или молчит (ops.ingest_run);
  2) какой ряд отстал против норматива публикации своего источника
     (derived.metric_progress + catalog.source_sla);
  3) какие алерты никто не подтвердил и сколько рядов пора свести в архив.

Тяжёлых запросов внутри нет: агрегат прогресса лежит в материализованном
представлении derived.metric_progress (обновляется за полчаса до прогона),
нормативы — в catalog.source_sla. Оба объекта читаются за миллисекунды,
поэтому сторож можно ставить дважды в день без нагрузки на базу.

Правила вывода:
  * при норме печатает пустую строку, код 0 (тихий cron);
  * при отклонении печатает отчёт, код 1 (видно в истории джоба);
  * --verbose печатает состояние и при норме (для ручного запуска).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

DSN = dict(host="127.0.0.1", port=15432, dbname="research_wiki", user="wiki",
           connect_timeout=15)
REPO = Path(__file__).resolve().parent.parent
JOBS = REPO / "scripts" / "ingest_jobs.json"
STAMP = Path("/home/lnr/personal/tasks/.freshness_digest_last")

SILENT_HOURS = 72        # загрузчик считается молчащим
ARCHIVE_DAYS = 548       # 18 месяцев без нового периода — кандидат в архив
MIN_OBS = 12             # ряд короче 12 наблюдений не судим
TOP = 8                  # сколько примеров показывать в отчёте


def load_jobs() -> dict:
    return {k: v for k, v in json.loads(JOBS.read_text(encoding="utf-8")).items()
            if not k.startswith("_")}


def loaders(cur) -> tuple[list[str], int, int]:
    """Упавшие и молчащие загрузчики. Возвращает (проблемы, прогонов, упало)."""
    cur.execute("""
        select parser_script, max(started_at)
        from ops.ingest_run group by 1
    """)
    last_by_job = {r[0]: r[1] for r in cur.fetchall()}

    cur.execute("""
        select endpoint_id, max(started_at) from ops.ingest_run
        where endpoint_id is not null group by 1
    """)
    last_by_endpoint = {r[0]: r[1] for r in cur.fetchall()}

    cur.execute("""
        select count(*), count(*) filter (where status = 'failed')
        from ops.ingest_run
        where started_at > now() - interval '24 hours'
    """)
    runs_24h, failed_24h = cur.fetchone()

    cur.execute("""
        select parser_script, exit_code, started_at
        from ops.ingest_run
        where status = 'failed' and started_at > now() - interval '24 hours'
        order by started_at desc limit 5
    """)
    problems = [f"упал {r[0]} (код {r[1]}, {r[2]:%d.%m %H:%M})" for r in cur.fetchall()]

    for job, meta in load_jobs().items():
        endpoint_id = meta.get("endpoint_id")
        last = last_by_job.get(job) or (last_by_endpoint.get(endpoint_id)
                                       if endpoint_id else None)
        if last is None:
            problems.append(f"нет ни одного прогона в журнале: {job}")
            continue
        hours = (datetime.now(last.tzinfo) - last).total_seconds() / 3600
        if hours > SILENT_HOURS:
            problems.append(f"молчит {hours:.0f} ч: {job} (последний {last:%d.%m %H:%M})")
    return problems, runs_24h, failed_24h


def rows_health(cur) -> tuple[dict, dict]:
    """Отставание и архив по данным derived.metric_progress + catalog.source_sla."""
    cur.execute("""
        select coalesce(s.source_code, 'unknown') as src,
               count(*) filter (where overdue_days > 0) as n_late,
               count(*) as n_total
        from (
            select p.source_id,
                   (current_date - (p.last_period_end
                       + (f.months_per_period * 30)
                       + coalesce(sla.lag_p90_days, 45))) as overdue_days
            from derived.metric_progress p
            left join catalog.frequency f on f.frequency_id = p.frequency_id
            left join catalog.source_sla sla on sla.source_id = p.source_id
            where p.n_obs >= %s
              and p.status = 'active'
              and p.last_period_end >= current_date - %s
        ) t
        left join catalog.source s on s.source_id = t.source_id
        group by 1 order by 2 desc
    """, (MIN_OBS, ARCHIVE_DAYS))
    by_source = [r for r in cur.fetchall() if r[1]]

    cur.execute("""
        select distinct on (t.name_ru) t.name_ru, t.last_period_end, t.overdue_days
        from (
            select p.name_ru, p.last_period_end,
                   current_date - (p.last_period_end
                       + (f.months_per_period * 30)
                       + coalesce(sla.lag_p90_days, 45)) as overdue_days
            from derived.metric_progress p
            left join catalog.frequency f on f.frequency_id = p.frequency_id
            left join catalog.source_sla sla on sla.source_id = p.source_id
            where p.n_obs >= %s and p.status = 'active'
              and p.last_period_end >= current_date - %s
        ) t
        where t.overdue_days > 0
        order by t.name_ru, t.overdue_days desc
    """, (MIN_OBS, ARCHIVE_DAYS))
    examples = sorted(cur.fetchall(), key=lambda r: r[2], reverse=True)[:TOP]

    cur.execute("""
        select count(*) from derived.metric_progress
        where status = 'active' and last_period_end < current_date - %s
    """, (ARCHIVE_DAYS,))
    archive = cur.fetchone()[0]

    cur.execute("""
        select count(*) from ops.alert
        where delivered_at is null and acknowledged_at is null
          and raised_at < now() - interval '1 day'
    """)
    undelivered = cur.fetchone()[0]
    return dict(by_source=by_source, examples=examples, archive=archive,
                undelivered=undelivered), {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    import psycopg

    conn = psycopg.connect(**DSN)
    with conn.cursor() as cur:
        cur.execute("set statement_timeout = '60s'")
        loader_problems, runs_24h, failed_24h = loaders(cur)
        health, _ = rows_health(cur)

    total = sum(r[2] for r in health["by_source"])
    late = sum(r[1] for r in health["by_source"])
    fresh_share = 100.0 * (total - late) / total if total else 100.0

    problems = list(loader_problems)
    if late:
        problems.append(f"отстают {late} рядов из {total} "
                        f"(свежих {fresh_share:.1f} %)")
    if health["undelivered"]:
        problems.append(f"алертов без доставки и подтверждения: {health['undelivered']}")

    stamp_ok = True
    if STAMP.exists():
        prev = date.fromisoformat(STAMP.read_text().strip())
        gap = (date.today() - prev).days
        if gap > 2:
            problems.append(f"сторож не запускался {gap} дн (отметка {prev})")

    if not problems:
        if args.verbose:
            print(f"Сторож: норма. Прогонов за сутки {runs_24h}, "
                  f"свежих рядов {fresh_share:.1f} % из {total}.")
        return 0

    out = [f"Сторож контура данных, {date.today():%d.%m.%Y}. "
           f"Прогонов за сутки: {runs_24h}" + (f", упало: {failed_24h}" if failed_24h else "")]
    if loader_problems:
        out.append("Загрузчики:")
        out += [f"  - {p}" for p in loader_problems]
    if late:
        out.append(f"Ряды против норматива публикации (отстают {late} из {total}, "
                   f"свежих {fresh_share:.1f} %):")
        for src, n_late, n_total in health["by_source"]:
            out.append(f"  - {src}: {n_late} из {n_total}")
        out.append("  примеры:")
        for name, last_end, overdue in health["examples"]:
            label = (name or "")[:70]
            out.append(f"    {label} — последний период {last_end:%m.%Y}, "
                       f"просрочка {overdue} дн")
    if health["archive"]:
        out.append(f"Кандидатов в архив (нет нового периода >18 мес): {health['archive']} "
                   f"— разбирать в этапе 3, не авария.")
    if health["undelivered"]:
        out.append(f"Алертов без доставки и подтверждения: {health['undelivered']}.")

    print("\n".join(out))
    try:
        STAMP.parent.mkdir(parents=True, exist_ok=True)
        STAMP.write_text(date.today().isoformat())
    except OSError:
        pass
    return 1


if __name__ == "__main__":
    sys.exit(main())
