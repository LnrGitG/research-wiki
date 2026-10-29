#!/usr/bin/env python3
"""refresh_metric_progress.py — обновление derived.metric_progress.

Материализованное представление прогресса рядов: последний период, объём,
число регионов на последнем периоде. Обновляется за полчаса до прогона
сторожа (11:00 и 19:00 UTC), чтобы сторож не сканировал 7,9 млн строк.

CONCURRENTLY не блокирует чтение, но требует уникального индекса (он есть).
Если индекс потерян или представление пустое, скрипт падает в обычный refresh
и предупреждает в stderr: тихая деградация до блокирующего обновления лучше,
чем устаревший прогресс в отчёте сторожа.
"""
from __future__ import annotations

import argparse
import sys
import time

DSN = dict(host="127.0.0.1", port=15432, dbname="research_wiki", user="wiki",
           connect_timeout=15)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plain", action="store_true",
                    help="обычный refresh вместо CONCURRENTLY")
    args = ap.parse_args()

    import psycopg

    conn = psycopg.connect(**DSN)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("set statement_timeout = '540s'")
        started = time.time()
        stmt = ("refresh materialized view "
                + ("" if args.plain else "concurrently ")
                + "derived.metric_progress")
        try:
            cur.execute(stmt)
        except Exception as exc:  # noqa: BLE001
            print(f"metric_progress: concurrent refresh не прошёл ({exc}); "
                  f"повторяю обычным", file=sys.stderr)
            cur.execute("refresh materialized view derived.metric_progress")
        cur.execute("select count(*), max(built_at) from derived.metric_progress")
        rows, built_at = cur.fetchone()
    print(f"metric_progress обновлён за {time.time() - started:.0f} с: "
          f"{rows} рядов, снимок {built_at:%d.%m %H:%M} UTC")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
