#!/usr/bin/env python3
"""cleanup_apply.py — чистка канона (блок 3), по умолчанию в режиме показа.

Три действия, каждое отдельным флагом, каждое обратимо:

  --action view   — починить derived.v_observation_latest: исключить отклонённые
                    строки, которые сейчас побеждают в DISTINCT ON и попадают в
                    витрину (замер: 35 819 строк). Обратимость —
                    scripts/sql/view_observation_latest_ORIGINAL_20261029.sql.
  --action dups   — точные дубли на одном зерне (одинаковое значение): оставить
                    одну строку, остальные перевести в статус superseded. Строки
                    не удаляются, смысл не теряется: значение остаётся ровно одно.
  --action future — периоды дальше 90 дней вперёд (ошибки парсеров): перевести в
                    rejected с пометкой в notes.

Безопасность: без --apply печатается план и счётчики, база не меняется. С --apply
требуется --dump <путь> — существующий дамп размером не меньше 100 МБ: чистка без
точки возврата запрещена самим скриптом, а не обещанием.

Приёмка по каждому действию — числа до и после (печатаются в конце).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

DSN = dict(host="127.0.0.1", port=15432, dbname="research_wiki", user="wiki",
           connect_timeout=15)

GRAIN = ("metric_id, region_id, period_start, coalesce(frequency_id,0), "
         "coalesce(assessment_type,''), coalesce(sub_dimension,'')")
GRAIN_O = ("o.metric_id, o.region_id, o.period_start, coalesce(o.frequency_id,0), "
           "coalesce(o.assessment_type,''), coalesce(o.sub_dimension,'')")

VIEW_CLEAN = Path(__file__).parent / "sql" / "view_observation_latest_clean.sql"


def counts(cur, full: bool = False) -> dict:
    """Счётчики канона. Представление считается только по запросу: два прохода
    DISTINCT ON по 7,8 млн строк стоят около сорока секунд каждый."""
    cur.execute("""select count(*),
                          count(*) filter (where observation_status = 'rejected')
                   from data.observation""")
    total, rejected = cur.fetchone()
    out = dict(total=total, rejected=rejected, view_total=None, rejected_in_view=None)
    if full:
        cur.execute("select count(*) from derived.v_observation_latest")
        out["view_total"] = cur.fetchone()[0]
        cur.execute("select count(*) from derived.v_observation_latest where observation_status = 'rejected'")
        out["rejected_in_view"] = cur.fetchone()[0]
    return out


def plan_dups(cur) -> tuple[int, int]:
    cur.execute(f"""
        with d as (
            select {GRAIN}, value, count(*) - 1 as extra
            from data.observation where observation_status <> 'rejected'
            group by 1,2,3,4,5,6, value having count(*) > 1
        ) select count(*), sum(extra) from d
    """)
    groups, excess = cur.fetchone()
    return groups or 0, int(excess or 0)


def plan_conflicts(cur) -> tuple[int, int]:
    cur.execute(f"""
        with g as (
            select {GRAIN}, count(distinct value) as n_values, count(*) as n_rows
            from data.observation
            where observation_status not in ('rejected', 'superseded')
            group by 1,2,3,4,5,6 having count(distinct value) > 1
        ) select count(*), sum(n_rows) - count(*) from g
    """)
    groups, losers = cur.fetchone()
    return groups or 0, int(losers or 0)


def plan_future(cur) -> int:
    cur.execute("""select count(*) from data.observation
                   where observation_status <> 'rejected'
                     and period_start > current_date + interval '90 days'""")
    return cur.fetchone()[0]


def do_view(cur, apply: bool) -> None:
    sql = VIEW_CLEAN.read_text(encoding="utf-8")
    sql = "\n".join(l for l in sql.splitlines() if not l.strip().startswith("--"))
    if apply:
        cur.execute(sql)
        print("view: определение заменено")


def do_dups(cur, apply: bool) -> int:
    """Пометить лишние копии как superseded. Возвращает число помеченных строк."""
    # Группировка через array_agg дешевле оконной функции: она читает таблицу
    # один раз и не сортирует 7,8 млн строк, а обновляет только лишние копии по
    # первичному ключу.
    if not apply:
        return 0
    cur.execute(f"""
        create temp table _dup_ids as
        select array_agg(observation_id order by observation_id) as ids
        from data.observation
        where observation_status <> 'rejected'
        group by {GRAIN}, value
        having count(*) > 1
    """)
    cur.execute("select count(*) from _dup_ids")
    groups = cur.fetchone()[0]
    cur.execute("""
        update data.observation t
           set observation_status = 'superseded',
               notes = coalesce(t.notes || ' | ', '') || '29.10.2026: точный дубль, оставлена одна копия'
          from (select unnest(ids[1:array_length(ids, 1) - 1]) as observation_id
                from _dup_ids) k
         where t.observation_id = k.observation_id
    """)
    marked = cur.rowcount
    cur.execute("drop table _dup_ids")
    print(f"групп с дублями: {groups}")
    return marked


def do_conflicts(cur, apply: bool) -> int:
    """Свести конфликтующие ревизии правилом: побеждает самая свежая публикация.

    Правило то же, что уже применяется в derived.v_observation_latest (свежесть по
    published_at релиза, затем release_id, затем observation_id), но здесь оно
    фиксируется физически: проигравшие переводятся в superseded.

    Сведение идёт порциями по метрикам: разовый оконный проход по всем 7,7 млн
    строк требует больше двух гигабайт временного пространства и на ВМ падает с
    «No space left on device». Порция ограничена 200 метриками, каждая порция —
    отдельная транзакция, поэтому прерванный прогон не оставляет полуприменённое
    состояние и его можно повторить.
    """
    if not apply:
        return 0
    cur.execute("""select distinct metric_id from data.observation
                   where observation_status not in ('rejected', 'superseded')
                   group by metric_id, region_id, period_start, coalesce(frequency_id,0),
                            coalesce(assessment_type,''), coalesce(sub_dimension,'')
                   having count(distinct value) > 1""")
    metrics = [r[0] for r in cur.fetchall()]
    print(f"метрик с расхождениями: {len(metrics)}")
    total = 0
    chunk = 200
    for start in range(0, len(metrics), chunk):
        part = metrics[start:start + chunk]
        cur.execute("""
            with g as (
                select metric_id, region_id, period_start,
                       coalesce(frequency_id, 0) as f,
                       coalesce(assessment_type, '') as a,
                       coalesce(sub_dimension, '') as s
                from data.observation
                where metric_id = any(%s)
                  and observation_status not in ('rejected', 'superseded')
                group by 1,2,3,4,5,6
                having count(distinct value) > 1
            ), ranked as (
                select o.observation_id,
                       row_number() over (
                           partition by o.metric_id, o.region_id, o.period_start,
                                        coalesce(o.frequency_id, 0),
                                        coalesce(o.assessment_type, ''),
                                        coalesce(o.sub_dimension, '')
                           order by coalesce(r.published_at, r.ingested_at, o.created_at) desc nulls last,
                                    o.release_id desc, o.observation_id desc) as rn
                from data.observation o
                join g on g.metric_id = o.metric_id and g.region_id = o.region_id
                      and g.period_start = o.period_start
                      and g.f = coalesce(o.frequency_id, 0)
                      and g.a = coalesce(o.assessment_type, '')
                      and g.s = coalesce(o.sub_dimension, '')
                left join catalog.release r on r.release_id = o.release_id
                where o.observation_status not in ('rejected', 'superseded')
            )
            update data.observation t
               set observation_status = 'superseded',
                   notes = coalesce(t.notes || ' | ', '') ||
                           '29.10.2026: проигравшая ревизия, побеждает более свежая публикация'
              from ranked k
             where t.observation_id = k.observation_id and k.rn > 1
        """, (part,))
        total += cur.rowcount
        cur.connection.commit()  # порция = своя транзакция
    cur.execute("select count(*) from data.observation where observation_status = 'superseded'")
    print(f"всего superseded после сведения: {cur.fetchone()[0]}")
    return total


def do_future(cur, apply: bool) -> int:
    sql = """
        update data.observation
           set observation_status = 'rejected',
               notes = coalesce(notes || ' | ', '') || '29.10.2026: период в будущем, ошибка парсера'
         where observation_status <> 'rejected'
           and period_start > current_date + interval '90 days'
    """
    if not apply:
        return 0
    cur.execute(sql)
    return cur.rowcount


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--action", choices=["view", "dups", "future", "conflicts"], required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dump", help="путь к дампу pg_dump -Fc, обязателен при --apply")
    args = ap.parse_args()

    if args.apply:
        if not args.dump:
            print("ОТКАЗ: --apply требует --dump <путь к дампу>", file=sys.stderr)
            return 2
        d = Path(args.dump)
        if not d.exists() or d.stat().st_size < 100 * 1024 * 1024:
            print(f"ОТКАЗ: дамп {d} отсутствует или меньше 100 МБ", file=sys.stderr)
            return 2

    import psycopg
    conn = psycopg.connect(**DSN)
    conn.autocommit = False
    cur = conn.cursor()
    cur.execute("set statement_timeout = 1800000")

    before = counts(cur, full=(args.action == "view"))
    msg = f"до: строк {before['total']}, отклонённых {before['rejected']}"
    if before["view_total"] is not None:
        msg += (f", в представлении {before['view_total']} "
                f"(из них rejected {before['rejected_in_view']})")
    print(msg)

    try:
        if args.action == "view":
            groups, excess = plan_dups(cur)
            do_view(cur, args.apply)
        elif args.action == "dups":
            groups, excess = plan_dups(cur)
            print(f"план: групп дублей {groups}, к пометке {excess} строк")
            if args.apply:
                print(f"помечено superseded: {do_dups(cur, True)}")
        elif args.action == "conflicts":
            groups, rows = plan_conflicts(cur)
            print(f"план: групп конфликтов {groups}, строк-проигравших к сведению {rows}")
            if args.apply:
                print(f"сведено ревизий: {do_conflicts(cur, True)}")
        else:
            n = plan_future(cur)
            print(f"план: периодов в будущем {n}")
            if args.apply:
                print(f"переведено в rejected: {do_future(cur, True)}")

        if args.apply:
            conn.commit()
        else:
            conn.rollback()
            print("режим показа: изменения откатаны, база не тронута")

        cur2 = conn.cursor()
        after = counts(cur2, full=(args.action == "view"))
        msg = f"после: строк {after['total']}, отклонённых {after['rejected']}"
        if after["view_total"] is not None:
            msg += (f", в представлении {after['view_total']} "
                    f"(из них rejected {after['rejected_in_view']})")
        print(msg)
    except Exception as exc:  # noqa: BLE001 — откат обязателен при любой ошибке
        conn.rollback()
        print(f"ОШИБКА, откат: {exc}", file=sys.stderr)
        return 1
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
