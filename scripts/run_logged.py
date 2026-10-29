#!/usr/bin/env python3
"""run_logged.py — обёртка журналирования загрузок (линия A, этап 0).

Запускает дочернюю команду и записывает прогон в ops.ingest_run:
кто, когда начал, когда кончил, чем кончил, сколько строк пришло, хвост вывода.

Контракт с cron-обёртками: обёртка на входе вызывает

    run_logged.py --job <basename обёртки> -- bash <обёртка> "$@"

а сама обёртка под этим флагом (INGEST_LOGGED=1) журнал не дублирует.

Коды выхода: возвращается код дочерней команды. Если упала запись журнала,
прогон всё равно считается успешным — журнал не должен ломать загрузку.

Использование вручную:
    python3 scripts/run_logged.py --job rosstat_housing_job.sh -- bash scripts/rosstat_housing_job.sh
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAP_PATH = REPO / "scripts" / "ingest_jobs.json"
TAIL_LIMIT = 2000
DSN = dict(host="127.0.0.1", port=15432, dbname="research_wiki", user="wiki")


def load_map() -> dict:
    if not MAP_PATH.exists():
        return {}
    try:
        return json.loads(MAP_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"run_logged: карта джобов не читается ({exc})", file=sys.stderr)
        return {}


def connect():
    import psycopg

    return psycopg.connect(**DSN, connect_timeout=10)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True, help="имя обёртки, напр. rosstat_housing_job.sh")
    ap.add_argument("command", nargs=argparse.REMAINDER, help="-- команда")
    args = ap.parse_args()

    cmd = args.command
    if cmd and cmd[0] == "--":
        cmd = cmd[1:]
    if not cmd:
        print("run_logged: не передана команда", file=sys.stderr)
        return 2

    meta = load_map().get(args.job, {})
    endpoint_id = meta.get("endpoint_id")
    # в журнал пишем имя обёртки: это устойчивый ключ расписания;
    # цепочка реальных парсеров остаётся в scripts/ingest_jobs.json
    parser = args.job

    conn = None
    run_id = None
    started = datetime.now(timezone.utc)
    try:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(
                """insert into ops.ingest_run (endpoint_id, parser_script, started_at, status)
                   values (%s, %s, %s, 'running') returning run_id""",
                (endpoint_id, parser, started),
            )
            run_id = cur.fetchone()[0]
        conn.commit()
    except Exception as exc:  # noqa: BLE001
        print(f"run_logged: журнал недоступен ({exc})", file=sys.stderr)
        if conn is not None:
            conn.close()
        conn = None

    t0 = time.time()
    env = dict(os.environ)
    env["INGEST_LOGGED"] = "1"
    proc = subprocess.run(cmd, cwd=str(REPO), env=env, capture_output=True, text=True)
    elapsed = round(time.time() - t0, 1)

    out = (proc.stdout or "") + (proc.stderr or "")
    if out:
        sys.stdout.write(out if out.endswith("\n") else out + "\n")
    sys.stdout.flush()

    if conn is not None and run_id is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "select count(*) from data.observation where created_at >= %s",
                    (started,),
                )
                rows = cur.fetchone()[0]
                cur.execute(
                    """update ops.ingest_run
                          set finished_at = now(),
                              status = %s,
                              rows_written = %s,
                              exit_code = %s,
                              output_tail = %s
                        where run_id = %s""",
                    (
                        "done" if proc.returncode == 0 else "failed",
                        rows,
                        proc.returncode,
                        (out[-TAIL_LIMIT:] if out else None),
                        run_id,
                    ),
                )
            conn.commit()
        except Exception as exc:  # noqa: BLE001
            print(f"run_logged: не удалось закрыть запись журнала ({exc})", file=sys.stderr)
        finally:
            conn.close()

    # тихий режим сохраняется: обёртка сама решает, что печатать
    print(
        f"run_logged[{args.job}]: exit={proc.returncode} elapsed={elapsed}s",
        file=sys.stderr,
    ) if proc.returncode else None
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
