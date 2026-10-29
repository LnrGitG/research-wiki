#!/usr/bin/env python3
"""refresh_source_sla.py — норматив публикации по источникам как данные.

Считает p90 и медиану лага публикации по derived.v_publication_lag_trusted
(только релизы с настоящей датой публикации; даты, скопированные из времени
приёма, туда не попадают) и складывает результат в catalog.source_sla.
Источники без достаточного числа наблюдений получают basis='assumed'
из scripts/source_sla_assumed.json.

Запуск: weekly (воскресенье 03:00) и вручную после массовых загрузок.
--dry-run не пишет в БД.

Запрос по представлению тяжёлый (минуты), поэтому в сторож его не ставим:
сторож читает готовую таблицу.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DSN = dict(host="127.0.0.1", port=15432, dbname="research_wiki", user="wiki",
           connect_timeout=15)
REPO = Path(__file__).resolve().parent.parent
ASSUMED = REPO / "scripts" / "source_sla_assumed.json"
MIN_OBS = 5


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--statement-timeout", type=int, default=900)
    args = ap.parse_args()

    import psycopg

    assumed = json.loads(ASSUMED.read_text(encoding="utf-8"))
    conn = psycopg.connect(**DSN)
    with conn.cursor() as cur:
        cur.execute(f"set statement_timeout = {args.statement_timeout * 1000}")
        # Лаг считаем по свежести релиза, а не по каждой строке: один выпуск
        # приносит и свежий период, и старые (годовые, пересчётные), поэтому
        # построчный лаг завышает срок публикации в разы — у Росстата выходило
        # 302 дня при реальных 40-45. Берём разницу между датой публикации и
        # самым свежим периодом внутри того же выпуска.
        cur.execute("""
            with rel as (
                select l.release_id, l.source_id,
                       max(l.published_on) as published_on,
                       max(l.period_end) as newest_period_end
                from derived.v_publication_lag_trusted l
                where l.lag_days is not null and l.period_end is not null
                  and l.published_on >= date '2026-10-01'
                group by 1, 2
            )
            select s.source_id, s.source_code, count(*) as n_releases,
                   percentile_cont(0.5) within group (
                       order by (published_on - newest_period_end)),
                   percentile_cont(0.9) within group (
                       order by (published_on - newest_period_end)),
                   min(published_on - newest_period_end),
                   max(published_on - newest_period_end),
                   count(distinct (published_on - newest_period_end))
            from rel join catalog.source s on s.source_id = rel.source_id
            where published_on >= newest_period_end
            group by 1, 2
        """)
        measured = {}
        rejected: dict[str, tuple] = {}
        for sid, code, n, med, p90, lo, hi, distinct_lags in cur.fetchall():
            # отсекаем вырожденные замеры: нулевой лаг (дата публикации
            # скопирована из приёма) и замер по одному значению на весь ряд
            assumed_lag = assumed.get(code)
            # Замер принимается только когда он и представителен, и не
            # противоречит регламенту источника: иначе один выпуск, несущий
            # старые периоды (годовые, пересчётные), снова завысит срок в разы.
            plausible = (n >= MIN_OBS and p90 is not None and 1 <= p90 <= 400
                         and code not in ("derived_internal", "unknown")
                         and (assumed_lag is None or p90 <= 2 * assumed_lag))
            if plausible:
                measured[code] = (sid, n, med, p90)
            else:
                rejected[code] = (n, p90, distinct_lags)
                print(f"refresh_source_sla: замер {code} не принят "
                      f"(выпусков {n}, p90={p90}, разных лагов {distinct_lags}) — "
                      f"остаётся допущение {assumed_lag}", file=sys.stderr)

        cur.execute("select source_id, source_code from catalog.source order by 1")
        sources = cur.fetchall()

        rows = []
        for sid, code in sources:
            if code in measured and measured[code][1] >= MIN_OBS:
                _, n, med, p90 = measured[code]
                rows.append((sid, int(round(p90)), int(round(med)), "measured", n,
                             f"p90 по {n} наблюдениям лага публикации"))
            else:
                lag = assumed.get(code)
                if lag is None:
                    print(f"refresh_source_sla: нет ни замера, ни допущения для {code}",
                          file=sys.stderr)
                    continue
                rej = rejected.get(code)
                if rej:
                    note = (f"запасное значение; замер отклонён: выпусков {rej[0]}, "
                            f"p90 {rej[1]} дн — в выпуск попадают и старые периоды")
                    n = rej[0]
                else:
                    note = "запасное значение: настоящих дат публикации ещё нет"
                    n = 0
                rows.append((sid, int(lag), None, "assumed", n, note))

        if args.dry_run:
            for r in rows:
                print(r)
            print(f"всего источников: {len(rows)}, измерено: "
                  f"{sum(1 for r in rows if r[3] == 'measured')}")
            return 0

        with conn.cursor() as cur:
            for sid, p90, med, basis, n, note in rows:
                cur.execute("""
                    insert into catalog.source_sla
                        (source_id, lag_p90_days, lag_median_days, basis, n_obs,
                         measured_at, note, updated_at)
                    values (%s, %s, %s, %s, %s,
                            case when %s = 'measured' then now() else null end, %s, now())
                    on conflict (source_id) do update
                       set lag_p90_days = excluded.lag_p90_days,
                           lag_median_days = excluded.lag_median_days,
                           basis = excluded.basis,
                           n_obs = excluded.n_obs,
                           measured_at = excluded.measured_at,
                           note = excluded.note,
                           updated_at = now()
                """, (sid, p90, med, basis, n, basis, note))
        conn.commit()
        print(f"catalog.source_sla обновлён: {len(rows)} источников, "
              f"измерено {sum(1 for r in rows if r[3] == 'measured')}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
