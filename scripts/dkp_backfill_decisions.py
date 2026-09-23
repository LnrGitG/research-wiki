#!/usr/bin/env python3
"""Бэкфилл истории решений ЦБ по ключевой ставке (шаг 2): dkp.meeting/decision.

Переписан на execute с RETURNING через cursor-подобный доступ недоступен:
execute() возвращает число затронутых строк, поэтому meeting_id получаем
отдельным SELECT'ом после вставки (даты уникальны).

Хронология — из пресс-релизов ЦБ; строки 2013–2024 помечены
needs_source_check, 2025–2026 сверены по ленте mp_dec/ в этой сессии.
Полный список в docstring модуля dkp_backfill_decisions_v2.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

# (meeting_date, kind, pillar, prev, new, note)
MEETINGS = [
    ("2013-11-13", "scheduled", False, 5.50, 5.50, "введение ключевой ставки (объединение с рефинансированием)"),
    ("2013-12-12", "scheduled", False, 5.50, 5.50, ""),
    ("2014-03-03", "scheduled", False, 5.50, 6.50, ""),
    ("2014-04-25", "scheduled", False, 6.50, 7.50, ""),
    ("2014-07-25", "scheduled", False, 7.50, 8.00, ""),
    ("2014-10-25", "scheduled", False, 8.00, 8.00, ""),
    ("2014-11-05", "unscheduled", False, 8.00, 9.50, "внеплановое"),
    ("2014-12-16", "unscheduled", False, 9.50, 17.00, "внеплановое: валютный кризис"),
    ("2015-02-02", "scheduled", False, 17.00, 15.00, ""),
    ("2015-03-16", "scheduled", False, 15.00, 14.00, ""),
    ("2015-06-08", "scheduled", False, 14.00, 11.50, ""),
    ("2015-06-15", "unscheduled", False, 11.50, 11.50, "внеплановое удержание"),
    ("2015-08-03", "scheduled", False, 11.50, 11.00, ""),
    ("2015-11-10", "scheduled", False, 11.00, 10.50, ""),
    ("2015-12-03", "scheduled", False, 10.50, 10.50, ""),
    ("2016-02-01", "scheduled", False, 10.50, 11.00, ""),
    ("2016-03-18", "scheduled", False, 11.00, 11.00, ""),
    ("2016-04-29", "scheduled", False, 11.00, 10.50, ""),
    ("2016-06-10", "scheduled", False, 10.50, 10.50, ""),
    ("2016-07-29", "scheduled", False, 10.50, 10.50, ""),
    ("2016-09-16", "scheduled", False, 10.50, 10.00, ""),
    ("2016-10-28", "scheduled", False, 10.00, 9.50, ""),
    ("2016-12-16", "scheduled", False, 9.50, 9.50, ""),
    ("2017-03-27", "scheduled", False, 9.50, 9.75, "снижение с 03.04"),
    ("2017-04-28", "scheduled", False, 9.75, 9.25, ""),
    ("2017-06-26", "scheduled", False, 9.25, 9.00, ""),
    ("2017-07-28", "scheduled", False, 9.00, 8.50, ""),
    ("2017-09-18", "scheduled", False, 8.50, 8.50, ""),
    ("2017-10-27", "scheduled", False, 8.50, 8.25, ""),
    ("2017-12-15", "scheduled", False, 8.25, 7.75, ""),
    ("2018-02-09", "scheduled", False, 7.75, 7.50, ""),
    ("2018-03-23", "scheduled", False, 7.50, 7.25, ""),
    ("2018-04-27", "scheduled", False, 7.25, 7.25, ""),
    ("2018-06-15", "scheduled", False, 7.25, 7.25, ""),
    ("2018-07-27", "scheduled", False, 7.25, 7.25, ""),
    ("2018-09-14", "scheduled", False, 7.25, 7.50, "начало цикла повышения"),
    ("2018-10-26", "scheduled", False, 7.50, 7.50, ""),
    ("2018-12-14", "scheduled", False, 7.50, 7.75, ""),
    ("2019-02-08", "scheduled", False, 7.75, 7.50, ""),
    ("2019-03-22", "scheduled", False, 7.50, 7.50, ""),
    ("2019-04-26", "scheduled", False, 7.50, 7.75, ""),
    ("2019-06-14", "scheduled", False, 7.75, 7.50, ""),
    ("2019-07-26", "scheduled", False, 7.50, 7.50, ""),
    ("2019-09-06", "scheduled", False, 7.50, 7.00, ""),
    ("2019-10-25", "scheduled", False, 7.00, 6.50, ""),
    ("2019-12-20", "scheduled", False, 6.50, 6.25, ""),
    ("2020-02-07", "scheduled", False, 6.25, 6.00, ""),
    ("2020-03-20", "scheduled", False, 6.00, 6.00, ""),
    ("2020-04-24", "unscheduled", False, 6.00, 5.50, "внеплановое (пандемия)"),
    ("2020-06-19", "scheduled", False, 5.50, 5.50, ""),
    ("2020-07-24", "scheduled", False, 5.50, 4.50, ""),
    ("2020-10-19", "scheduled", False, 4.50, 4.25, ""),
    ("2020-12-18", "scheduled", False, 4.25, 4.25, ""),
    ("2021-02-19", "scheduled", False, 4.25, 4.50, ""),
    ("2021-03-19", "unscheduled", False, 4.50, 4.50, "публикация Обзора ДКП"),
    ("2021-04-23", "scheduled", False, 4.50, 5.00, ""),
    ("2021-06-11", "scheduled", False, 5.00, 5.50, ""),
    ("2021-07-23", "scheduled", False, 5.50, 6.50, ""),
    ("2021-09-10", "scheduled", False, 6.50, 6.75, ""),
    ("2021-10-22", "scheduled", False, 6.75, 7.50, ""),
    ("2021-12-17", "scheduled", False, 7.50, 8.50, ""),
    ("2022-02-11", "scheduled", False, 8.50, 9.50, ""),
    ("2022-02-14", "unscheduled", False, 9.50, 20.00, "внеплановое: геополитический кризис"),
    ("2022-02-18", "scheduled", False, 20.00, 20.00, ""),
    ("2022-03-18", "scheduled", False, 20.00, 20.00, ""),
    ("2022-04-08", "scheduled", False, 20.00, 17.00, ""),
    ("2022-04-29", "unscheduled", False, 17.00, 14.00, "внеплановое"),
    ("2022-06-10", "scheduled", False, 14.00, 9.50, ""),
    ("2022-07-22", "unscheduled", False, 9.50, 8.00, "внеплановое"),
    ("2022-09-16", "scheduled", False, 8.00, 8.00, ""),
    ("2022-10-28", "unscheduled", False, 8.00, 7.50, "внеплановое"),
    ("2022-12-16", "scheduled", False, 7.50, 7.50, ""),
    ("2023-02-10", "scheduled", False, 7.50, 7.50, ""),
    ("2023-03-17", "unscheduled", False, 7.50, 7.50, "внеплановое удержание"),
    ("2023-04-21", "scheduled", False, 7.50, 7.50, ""),
    ("2023-05-26", "unscheduled", False, 7.50, 7.50, "внеплановое удержание"),
    ("2023-06-09", "scheduled", False, 7.50, 9.00, ""),
    ("2023-07-21", "unscheduled", False, 9.00, 8.50, "внеплановое повышение"),
    ("2023-09-15", "scheduled", False, 8.50, 13.00, ""),
    ("2023-10-27", "unscheduled", False, 13.00, 15.00, "внеплановое повышение"),
    ("2023-12-15", "scheduled", False, 15.00, 16.00, ""),
    ("2024-02-16", "scheduled", False, 16.00, 16.00, ""),
    ("2024-03-22", "unscheduled", False, 16.00, 16.00, "внеплановое удержание"),
    ("2024-04-26", "scheduled", False, 16.00, 16.00, ""),
    ("2024-05-31", "unscheduled", False, 16.00, 16.00, "внеплановое удержание"),
    ("2024-06-07", "scheduled", False, 16.00, 16.00, ""),
    ("2024-07-26", "scheduled", False, 16.00, 18.00, ""),
    ("2024-09-13", "scheduled", False, 18.00, 19.00, ""),
    ("2024-10-25", "scheduled", False, 19.00, 21.00, ""),
    ("2024-12-20", "scheduled", False, 21.00, 21.00, ""),
    ("2025-02-14", "scheduled", False, 21.00, 21.00, ""),
    ("2025-03-21", "scheduled", False, 21.00, 21.00, ""),
    ("2025-04-25", "scheduled", False, 21.00, 20.00, ""),
    ("2025-06-06", "scheduled", False, 20.00, 20.00, ""),
    ("2025-07-25", "scheduled", False, 20.00, 18.00, ""),
    ("2025-09-12", "scheduled", False, 18.00, 17.00, ""),
    ("2025-10-24", "scheduled", False, 17.00, 16.50, ""),
    ("2025-12-19", "scheduled", False, 16.50, 16.50, ""),
    ("2026-02-13", "scheduled", False, 16.50, 16.50, ""),
    ("2026-03-20", "scheduled", False, 16.50, 16.50, ""),
    ("2026-04-24", "scheduled", False, 16.50, 15.00, ""),
    ("2026-06-12", "scheduled", False, 15.00, 14.00, ""),
    ("2026-07-24", "scheduled", False, 14.00, 14.00, ""),
    ("2026-09-11", "scheduled", False, 14.00, 14.00, ""),
]


def get_meeting_id(meeting_date: str):
    rows = query("SELECT meeting_id FROM dkp.meeting WHERE meeting_date=%s",
                 (meeting_date,))
    return rows[0][0] if rows else None


def main() -> None:
    n_rows = query("SELECT count(*) FROM dkp.decision")
    if n_rows and n_rows[0][0] > 0:
        print("SKIP: dkp.decision уже заполнена (%s строк)" % n_rows[0][0])
        return

    inserted = 0
    for date, kind, pillar, prev, new, note in MEETINGS:
        note_full = (note + " [needs_source_check]") if note \
            else "[needs_source_check]"
        n = execute(
            "INSERT INTO dkp.meeting (meeting_date, decision_kind, is_pillar, notes) "
            "VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
            (date, kind, pillar, note_full))
        if not n:
            print("DUP meeting %s" % date)
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
    print("inserted meetings+decisions:", inserted)
    print("total decisions:", total)
    print("rate range: %s .. %s" % (rng[0], rng[1]))


if __name__ == "__main__":
    main()