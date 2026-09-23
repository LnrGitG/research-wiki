#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Загрузка последних 3 решений СД (июнь, июль, сентябрь 2026) + Резюме.

Источники - пресс-релизы cbr.ru, проверены 23.09.2026:
- 19.06.2026: снижение 25 б.п. до 14,25; сигнал - оценивать
  целесообразность дальнейшего снижения на ближайших заседаниях.
- 24.07.2026: снижение 25 б.п. до 14,00; формула без направленности.
- 11.09.2026: удержание 14,00; Резюме 23.09: не давать сигнала.

Также: press_release_url, dkp.statement (пресс-конференция 19.06),
dkp.minutes (05.05.2026 за заседание 24.04; 23.09.2026 за 11.09).
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

DECISIONS = [
    {
        "date": "2026-06-19",
        "headline": "снизить ключевую ставку на 25 б.п., до 14,25% годовых",
        "url": "https://www.cbr.ru/press/pr/?file=19062026_133000key.htm",
        "signal": "оценивать целесообразность дальнейшего снижения на ближайших заседаниях",
        "notes": None,
    },
    {
        "date": "2026-07-24",
        "headline": "снизить ключевую ставку на 25 б.п., до 14,00% годовых",
        "url": "https://www.cbr.ru/press/pr/?file=24072026_133000key.htm",
        "signal": "решения в зависимости от динамики инфляции и ожиданий и оценки рисков (без направленности)",
        "notes": "среднесрочный прогноз обновлен (к опорному заседанию)",
    },
    {
        "date": "2026-09-11",
        "headline": "сохранить ключевую ставку на уровне 14,00% годовых",
        "url": "https://www.cbr.ru/press/pr/?file=11092026_133000key.htm",
        "signal": "решения в зависимости от динамики инфляции и ожиданий и оценки рисков (без направленности)",
        "notes": "Резюме 23.09.2026: не давать сигнала о направленности дальнейших шагов",
    },
]

MINUTES = [
    {
        "meeting": "2026-04-24",
        "published": "2026-05-07",
        "url": "https://cbr.ru/dkp/mp_dec/decision_key_rate/summary_key_rate_07052026",
        "consensus": "широкий консенсус за снижение 50 б.п. до 14,50%; некоторые - за сохранение 15,00%",
        "signal_discussion": "все предложили умеренно мягкий сигнал о целесообразности снижения на ближайших заседаниях",
    },
    {
        "meeting": "2026-09-11",
        "published": "2026-09-23",
        "url": "https://cbr.ru/dkp/mp_dec/decision_key_rate/summary_key_rate_23092026",
        "consensus": "широкий консенсус за сохранение 14,00%",
        "signal_discussion": "не давать сигнала о направленности дальнейших шагов (сохранить гибкость)",
    },
]


def main() -> None:
    for d in DECISIONS:
        execute(
            "UPDATE dkp.meeting SET press_release_url=%s "
            "WHERE meeting_date=%s",
            (d["url"], d["date"]))
        execute(
            "UPDATE dkp.decision SET headline_ru=%s WHERE meeting_id="
            "(SELECT meeting_id FROM dkp.meeting WHERE meeting_date=%s)",
            (d["headline"], d["date"]))
        if d["notes"]:
            execute(
                "UPDATE dkp.meeting SET notes=%s WHERE meeting_date=%s",
                (d["notes"], d["date"]))
        print("decision", d["date"], "updated")

    # dkp.statement для 19.06 (URL пресс-конференции известен)
    if not query("SELECT count(*) FROM dkp.statement")[0][0]:
        execute(
            "INSERT INTO dkp.statement (kind, speaker, event_date, meeting_id, "
            "url, body, document_id) "
            "SELECT 'press_conf', 'Эльвира Набиуллина', meeting_date, meeting_id, "
            "'https://www.cbr.ru/press/event/?id=32634', "
            "'Заявление Председателя по итогам заседания 19.06.2026 "
            "(тело загрузить отдельно)', NULL "
            "FROM dkp.meeting WHERE meeting_date='2026-06-19'")
        print("statement 2026-06-19 inserted")

    for m in MINUTES:
        if query("SELECT count(*) FROM dkp.minutes WHERE url=%s",
                 (m["url"],))[0][0]:
            continue
        rows = query("SELECT meeting_id FROM dkp.meeting WHERE meeting_date=%s",
                     (m["meeting"],))
        if not rows:
            print("NO meeting for minutes", m["meeting"])
            continue
        execute(
            "INSERT INTO dkp.minutes (meeting_id, published_at, url, body) "
            "VALUES (%s, %s, %s, %s)",
            (rows[0][0], m["published"] + "T12:00:00+03:00", m["url"],
             m["consensus"] + " || СИГНАЛ: " + m["signal_discussion"]))
        print("minutes", m["meeting"], "inserted")

    print("== verify ==")
    for r in query("SELECT meeting_date, press_release_url IS NOT NULL "
                   "FROM dkp.meeting WHERE meeting_date>='2026-06-01' "
                   "ORDER BY meeting_date"):
        print("  meeting", r)
    print("  minutes rows:", query("SELECT count(*) FROM dkp.minutes")[0][0])
    print("  statement rows:", query("SELECT count(*) FROM dkp.statement")[0][0])


if __name__ == "__main__":
    main()