#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Миграция dkp v1 -> v2: поля сигнала, режима, консенсуса, развилок.

Добавляем: dkp.decision.signal_kind, dkp.meeting.policy_mode,
consensus_scope, degree_snapshot (jsonb); dkp.argument.time_ref, concern,
conditionality. Заполнение для трёх последних решений (2026) по текстам
Резюме и пресс-релизов, прочитанных 23.09.2026.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import execute, query  # noqa: E402

MIGRATIONS = [
    ("dkp.decision", "signal_kind text"),
    ("dkp.meeting", "policy_mode text"),
    ("dkp.meeting", "consensus_scope text"),
    ("dkp.meeting", "degree_snapshot jsonb"),
    ("dkp.argument", "time_ref text"),
    ("dkp.argument", "concern text"),
    ("dkp.argument", "conditionality text"),
]

# (date, policy_mode, consensus_scope, degree_snapshot)
MEETING_V2 = [
    ("2026-04-24", "easing", "broad_consensus",
     {"dku": "умеренно жесткие", "expectations": "снижаются, повышенные",
      "output_gap": "закрылся быстрее прогноза", "confidence": "мягкий сигнал"}),
    ("2026-06-19", "easing", "consensus",
     {"dku": "жесткие, продолжили смягчаться", "expectations": "снизились, повышенные",
      "output_gap": None, "confidence": "направленный мягкий сигнал"}),
    ("2026-07-24", "easing", "consensus",
     {"dku": "умеренно жесткие", "expectations": "выросли",
      "output_gap": "нет данных", "confidence": "формула без направленности"}),
    ("2026-09-11", "pause_in_easing", "broad_consensus",
     {"dku": "умеренно жесткие (спор: отдельные — нейтральные/умеренно мягкие)",
      "expectations": "разнонаправленно, выше уровней 1п2026",
      "output_gap": "обсуждали повторное открытие положительного разрыва",
      "confidence": "осознанный отказ от сигнала"}),
]

# (date, signal_kind, signal_text)
SIGNALS = [
    ("2026-04-24", "soft_dovish",
     "умеренно мягкий сигнал: целесообразность снижения на ближайших заседаниях"),
    ("2026-06-19", "soft_dovish",
     "оценивать целесообразность дальнейшего снижения на ближайших заседаниях"),
    ("2026-07-24", "neutral_formula",
     "решения в зависимости от динамики инфляции и ожиданий и оценки рисков"),
    ("2026-09-11", "none",
     "осознанный отказ от сигнала о направленности (гибкость при значительных рисках)"),
]

# (date, block, условие, следствие) — развилки из Резюме/пресс-релизов
FORKS = [
    ("2026-09-11", "fiscal",
     "Бюджетные проектировки предполагают более высокий структурный первичный дефицит",
     "более жесткая ДКП"),
    ("2026-09-11", "inflation_now",
     "Более длительные ограничения Ормузского пролива — нефть выше прогноза",
     "трактовка рисков вверх"),
    ("2026-09-11", "demand",
     "Рост внутреннего спроса останется сдержанным, мощности восстановятся",
     "жесткость достаточна, снижение устойчивой инфляции возобновится"),
    ("2026-07-24", "rationale",
     "Более значительные вторичные эффекты выбытия мощностей",
     "более плавное снижение ключевой ставки"),
]


def main() -> None:
    for tbl, coldef in MIGRATIONS:
        col = coldef.split()[0]
        cols = query(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_schema='dkp' AND table_name=%s", (tbl.split(".")[1],))
        if col not in {r[0] for r in cols}:
            execute("ALTER TABLE %s ADD COLUMN %s" % (tbl, coldef))
            print("added %s.%s" % (tbl, col))

    for date, mode, scope, snap in MEETING_V2:
        import json as _json
        execute(
            "UPDATE dkp.meeting SET policy_mode=%s, consensus_scope=%s, degree_snapshot=%s "
            "WHERE meeting_date=%s",
            (mode, scope, _json.dumps(snap, ensure_ascii=False), date))
        print("meeting", date, "->", mode, scope)

    for date, kind, text in SIGNALS:
        execute(
            "UPDATE dkp.decision SET signal_kind=%s WHERE meeting_id="
            "(SELECT meeting_id FROM dkp.meeting WHERE meeting_date=%s)",
            (kind, date))
        print("signal", date, "->", kind)

    # развилки: заполнить conditionality у соответствующих аргументов
    for date, block, condition, consequence in FORKS:
        n = execute(
            "UPDATE dkp.argument a SET conditionality=%s "
            "FROM dkp.decision d, dkp.meeting m "
            "WHERE a.decision_id=d.decision_id AND d.meeting_id=m.meeting_id "
            "AND m.meeting_date=%s AND a.block=%s",
            (condition + " => " + consequence, date, block))
        print("fork", date, block, "rows:", n)

    # time_ref: forward для сигналов и прогнозов
    execute(
        "UPDATE dkp.argument SET time_ref='forward' "
        "WHERE block IN ('signal', 'inflation_forecast') AND time_ref IS NULL")
    execute(
        "UPDATE dkp.argument SET time_ref='present' WHERE time_ref IS NULL")
    # concern: surprise где «нечто новое/неожиданное», confirm — «в линию с прогнозом»
    execute(
        "UPDATE dkp.argument SET concern='surprise' "
        "WHERE text_raw ILIKE '%временное выбытие%' OR text_raw ILIKE '%существенное усиление%'"
        " OR text_raw ILIKE '%мог ли положительный разрыв%'")
    execute(
        "UPDATE dkp.argument SET concern='confirm' "
        "WHERE text_raw ILIKE '%в соответствии с%прогнозом%' OR text_raw ILIKE '%как и ожидали%'")

    print("== verify ==")
    for r in query("""SELECT m.meeting_date, d.signal_kind, m.policy_mode, m.consensus_scope
                      FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
                      WHERE m.meeting_date>='2026-04-01' ORDER BY 1"""):
        print("  ", r)
    for r in query("SELECT count(*) FILTER (WHERE conditionality IS NOT NULL), "
                   "count(*) FILTER (WHERE time_ref='forward'), "
                   "count(*) FROM dkp.argument"):
        print("  args (forks, forward, total):", r)


if __name__ == "__main__":
    main()