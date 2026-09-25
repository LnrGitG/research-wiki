# -*- coding: utf-8 -*-
"""dkp_uncertainty_briefing.py — паспорт открытых неопределённостей для ОПР.

Функция briefing(as_of=None): открытые/обновлённые uncertainty-к последнему
заседанию + развязки предыдущих items + баланс рисков + degree_snapshot.
CLI: --last | --meeting=<id> | --as-of=ГГГГ-ММ-ДД
"""
import json
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query


def briefing(meeting_id):
    """Паспорт неопределённостей к заседанию meeting_id."""
    out = {"meeting_id": meeting_id}
    r = query("SELECT meeting_date::text FROM dkp.meeting WHERE meeting_id=%s" % meeting_id)
    if not r:
        return None
    out["meeting_date"] = r[0][0]

    # степень/калибровки ЦБ
    r = query("SELECT degree_snapshot FROM dkp.meeting WHERE meeting_id=%s" % meeting_id)
    if r and r[0][0]:
        out["degree_snapshot"] = r[0][0]

    # баланс рисков (risk_balance последнего заседания)
    r = query("""SELECT variable, direction, text_short FROM dkp.uncertainty_item
                 WHERE meeting_id=%s AND kind='risk_balance' ORDER BY item_id""" % meeting_id)
    out["risk_balance"] = [{"variable": x[0], "direction": x[1], "text": x[2]} for x in r]

    # открытые вопросы этого заседания
    r = query("""SELECT item_id, variable, direction, COALESCE(text_short, text_raw),
                        confidence_note
                 FROM dkp.uncertainty_item
                 WHERE meeting_id=%s AND kind='open_question' AND status='open'
                 ORDER BY item_id""" % meeting_id)
    out["open_questions"] = [{"item_id": x[0], "variable": x[1], "direction": x[2],
                              "text": x[3], "confidence": x[4]} for x in r]

    # развилки (conditionality)
    r = query("""SELECT item_id, variable, premise, consequence
                 FROM dkp.uncertainty_item
                 WHERE meeting_id=%s AND kind='conditionality' ORDER BY item_id""" % meeting_id)
    out["conditionality"] = [{"item_id": x[0], "variable": x[1],
                              "if": x[2], "then": x[3]} for x in r]

    # развязки: items с предыдущих заседаний, статусы которых изменились
    r = query("""SELECT i.item_id, i.meeting_id, m.meeting_date::text, i.variable,
                        i.status, COALESCE(i.resolution_note, i.text_short)
                 FROM dkp.uncertainty_item i JOIN dkp.meeting m USING (meeting_id)
                 WHERE i.meeting_id < %s AND i.status != 'open'
                 ORDER BY i.meeting_id DESC LIMIT 8""" % meeting_id)
    out["resolved_context"] = [{"item_id": x[0], "meeting_id": x[1],
                                "meeting_date": x[2], "variable": x[3],
                                "status": x[4], "note": x[5]} for x in r]

    # преемственность: открытые items предыдущих заседаний (возраст)
    r = query("""SELECT i.item_id, i.meeting_id, m.meeting_date::text, i.variable,
                        COALESCE(i.text_short, i.text_raw)
                 FROM dkp.uncertainty_item i JOIN dkp.meeting m USING (meeting_id)
                 WHERE i.meeting_id < %s AND i.status='open'
                 ORDER BY i.meeting_id DESC LIMIT 10""" % meeting_id)
    out["carried_open"] = [{"item_id": x[0], "opened_meeting": x[1],
                            "meeting_date": x[2], "variable": x[3],
                            "text": x[4]} for x in r]
    return out


def main():
    argv = sys.argv
    mid = None
    for a in argv:
        if a.startswith("--meeting="):
            mid = int(a.split("=")[1])
        elif a.startswith("--as-of="):
            r = query("SELECT max(meeting_id) FROM dkp.meeting WHERE meeting_date <= '%s'"
                      % a.split("=", 1)[1])
            mid = r[0][0] if r else None
    if mid is None and "--last" in argv:
        r = query("SELECT max(meeting_id) FROM dkp.meeting WHERE meeting_date <= now()")
        mid = r[0][0] if r else None
    if not mid:
        print("Использование: --meeting=<id> | --as-of=ГГГГ-ММ-ДД | --last")
        return 1
    b = briefing(mid)
    print(json.dumps(b, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())