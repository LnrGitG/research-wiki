#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Исправление бэкфилла: реальные даты решений 2026 из ленты mp_dec.

Лента подтверждает: 13.02 / 20.03 / 24.04 / 19.06 / 24.07 / 11.09.
В бэкфилле были ошибки: 2026-06-12 (не существует), 2026-03-20 vs 20.03 ok,
2026-02-13 vs 13.02 ok, 2026-04-24 ok.

Перенос даты 2026-06-12 -> 2026-06-19, вставка 19.06 (cut 25 б.п. до 14,25),
обновление rate_prev/rate_new 24.07 (в бэкфилле был prev=14,00 hold, а
фактически было 14,25 -> 14,00 cut).
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402


def main() -> None:
    # 1) перенести дату июньского решения: 2026-06-12 -> 2026-06-19
    rows = query("SELECT meeting_id FROM dkp.meeting WHERE meeting_date='2026-06-12'")
    if rows:
        execute("UPDATE dkp.meeting SET meeting_date='2026-06-19' WHERE meeting_date='2026-06-12'")
        print("moved 2026-06-12 -> 2026-06-19")

    # 2) решить: 19.06 было cut 14,50 -> 14,25 (не hold!)
    rows = query(
        "SELECT d.decision_id, d.rate_prev, d.rate_new "
        "FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id) "
        "WHERE m.meeting_date='2026-06-19'")
    print("decision 19.06:", rows)
    if rows and (rows[0][1] != 14.50 or rows[0][2] != 14.25):
        execute(
            "UPDATE dkp.decision SET rate_prev=14.50, rate_new=14.25, action='cut' "
            "WHERE meeting_id=(SELECT meeting_id FROM dkp.meeting WHERE meeting_date='2026-06-19')")
        print("fixed 19.06 decision 14,50 -> 14,25 cut")

    # 3) каскад rate_level за 2026: пересобрать по исправленным решениям
    rows = query(
        "SELECT m.meeting_date, d.rate_new, d.decision_id "
        "FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id) "
        "WHERE m.meeting_date >= '2026-01-01' ORDER BY m.meeting_date")
    print("2026 decisions:", [(str(r[0]), float(r[1])) for r in rows])
    for i, (mdate, new, dec_id) in enumerate(rows):
        import datetime
        eff_from = (datetime.date.fromisoformat(str(mdate)) +
                    datetime.timedelta(days=1)).isoformat()
        if i + 1 < len(rows):
            eff_to = (datetime.date.fromisoformat(str(rows[i + 1][0])) +
                      datetime.timedelta(days=1)).isoformat()
        else:
            eff_to = None
        # закрыть предыдущий уровень и вставить исправленный
        execute(
            "UPDATE dkp.rate_level SET effective_to=%s WHERE decision_id=%s",
            (eff_from, dec_id))
        execute(
            "UPDATE dkp.rate_level SET effective_from=%s, effective_to=%s "
            "WHERE decision_id=%s AND rate_code='key_rate'",
            (eff_from, eff_to, dec_id))

    # 4) сверить: текущий уровень и разрывы
    cur = query("SELECT value, effective_from FROM dkp.rate_level "
                "WHERE rate_code='key_rate' AND effective_to IS NULL")
    gaps = query("""
        SELECT count(*) FROM (
          SELECT effective_from, lag(effective_to) OVER (ORDER BY effective_from) prev_to
          FROM dkp.rate_level WHERE rate_code='key_rate') x
        WHERE prev_to IS NOT NULL AND effective_from <> prev_to
    """)
    print("current:", cur, "gaps:", gaps[0][0])

    # 5) вставить statement 19.06 (пресс-конференция)
    if not query("SELECT count(*) FROM dkp.statement")[0][0]:
        execute(
            "INSERT INTO dkp.statement (kind, speaker, event_date, meeting_id, "
            "url, body, document_id) "
            "SELECT 'press_conf', 'Эльвира Набиуллина', meeting_date, meeting_id, "
            "'https://www.cbr.ru/press/event/?id=32634', "
            "'Заявление Председателя по итогам заседания 19.06.2026 "
            "(тело загрузить отдельно)', NULL "
            "FROM dkp.meeting WHERE meeting_date='2026-06-19'")
        print("statement inserted")

    # 6) обновить все три пресс-релиза
    for date, url in [
        ("2026-06-19", "https://www.cbr.ru/press/pr/?file=19062026_133000key.htm"),
        ("2026-07-24", "https://www.cbr.ru/press/pr/?file=24072026_133000key.htm"),
        ("2026-09-11", "https://www.cbr.ru/press/pr/?file=11092026_133000key.htm"),
    ]:
        execute("UPDATE dkp.meeting SET press_release_url=%s WHERE meeting_date=%s",
                (url, date))

    # 7) headline_ru по пресс-релизам
    execute(
        "UPDATE dkp.decision SET headline_ru='снизить ключевую ставку на 25 б.п., до 14,25% годовых' "
        "WHERE meeting_id=(SELECT meeting_id FROM dkp.meeting WHERE meeting_date='2026-06-19')")
    execute(
        "UPDATE dkp.decision SET headline_ru='снизить ключевую ставку на 25 б.п., до 14,00% годовых' "
        "WHERE meeting_id=(SELECT meeting_id FROM dkp.meeting WHERE meeting_date='2026-07-24')")

    print("== final ==")
    for r in query("SELECT meeting_date, d.rate_prev, d.rate_new, d.action "
                   "FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id) "
                   "WHERE m.meeting_date>='2026-06-01' ORDER BY meeting_date"):
        print("  ", r)
    print("  statement:", query("SELECT count(*) FROM dkp.statement")[0][0])
    print("  minutes:", query("SELECT count(*) FROM dkp.minutes")[0][0])


if __name__ == "__main__":
    main()