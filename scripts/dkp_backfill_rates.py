#!/usr/bin/env python3
"""Загрузка решётки ключевой ставки dkp.rate_level из решений (ступени).

Логика простая и проверяемая: для каждого решения (по хронологии)
уровень key_rate со значением rate_new; effective_from = день после
заседания; effective_to предыдущего уровня = effective_from нового.
Последний уровень открыт (effective_to IS NULL).
"""
import sys
import os
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402


def next_day(date_str: str) -> str:
    d = datetime.date.fromisoformat(str(date_str)) + datetime.timedelta(days=1)
    return d.isoformat()


def main() -> None:
    n = query("SELECT count(*) FROM dkp.rate_level")[0][0]
    if n:
        print("SKIP: rate_level уже заполнена (%s)" % n)
        return

    rows = query(
        "SELECT m.meeting_date, d.rate_new, d.decision_id "
        "FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id) "
        "ORDER BY m.meeting_date")

    inserted = 0
    for i, (mdate, new, dec_id) in enumerate(rows):
        eff_from = next_day(mdate)
        if i + 1 < len(rows):
            eff_to = next_day(rows[i + 1][0])
        else:
            eff_to = None
        # закрыть предыдущий уровень
        execute(
            "UPDATE dkp.rate_level SET effective_to=%s "
            "WHERE rate_code='key_rate' AND effective_to IS NULL",
            (eff_from,))
        execute(
            "INSERT INTO dkp.rate_level (decision_id, rate_code, rate_group, "
            "value, effective_from, effective_to) VALUES (%s, 'key_rate', 'key', %s, %s, %s)",
            (dec_id, new, eff_from, eff_to))
        inserted += 1

    cnt = query("SELECT count(*) FROM dkp.rate_level")[0][0]
    cur = query(
        "SELECT value, effective_from FROM dkp.rate_level "
        "WHERE rate_code='key_rate' AND effective_to IS NULL")
    holes = query(
        "SELECT count(*) FROM dkp.rate_level "
        "WHERE rate_code='key_rate' AND effective_from IS NULL")
    print("levels:", cnt, "open:", len(cur), "holes:", holes[0][0])
    print("current level:", cur)


if __name__ == "__main__":
    main()