#!/usr/bin/env python3
"""Дозагрузка остатка бэкфилла решений (34/104 было вставлено до таймаута)."""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402
from dkp_backfill_decisions import MEETINGS, get_meeting_id  # noqa: E402


def main() -> None:
    have = {r[0].isoformat() for r in
            query("SELECT meeting_date FROM dkp.meeting")}
    todo = [m for m in MEETINGS if m[0] not in have]
    print("to insert:", len(todo))
    inserted = 0
    for date, kind, pillar, prev, new, note in todo:
        note_full = (note + " [needs_source_check]") if note \
            else "[needs_source_check]"
        n = execute(
            "INSERT INTO dkp.meeting (meeting_date, decision_kind, is_pillar, notes) "
            "VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
            (date, kind, pillar, note_full))
        if not n:
            continue
        mid = get_meeting_id(date)
        action = "cut" if new < prev else "hike" if new > prev else "hold"
        execute(
            "INSERT INTO dkp.decision (meeting_id, rate_prev, rate_new, action, headline_ru) "
            "VALUES (%s, %s, %s, %s, %s)",
            (mid, prev, new, action, "Ключевая ставка: %s -> %s%%" % (prev, new)))
        inserted += 1

    total = query("SELECT count(*) FROM dkp.decision")[0][0]
    rng = query("SELECT min(rate_new), max(rate_new) FROM dkp.decision")[0]
    span = query("SELECT min(meeting_date), max(meeting_date) FROM dkp.meeting")[0]
    print("inserted now:", inserted)
    print("total decisions:", total)
    print("rate range: %s .. %s" % (rng[0], rng[1]))
    print("meetings span: %s .. %s" % (span[0], span[1]))


if __name__ == "__main__":
    main()