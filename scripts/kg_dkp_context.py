# -*- coding: utf-8 -*-
"""
kg_dkp_context.py — сборщик полного коммуникационного стека заседания
dkp_context(meeting_id): решение + пресс-релиз + заявление + Резюме +
прогнозные серии одним вызовом (МВФ-рамка, нативное обогащение контекста).

CLI: --meeting=104 | --date=2026-09-11 | --last
"""
import sys
import json

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query  # noqa: E402


def resolve_meeting(argv):
    for a in argv:
        if a.startswith("--meeting="):
            return int(a.split("=")[1])
        if a.startswith("--date="):
            r = query("SELECT meeting_id FROM dkp.meeting WHERE meeting_date='%s'"
                      % a.split("=")[1])
            return r[0][0] if r else None
    if "--last" in argv:
        r = query("SELECT max(meeting_id) FROM dkp.meeting WHERE meeting_date <= now()")
        return r[0][0]
    return None


def dkp_context(meeting_id):
    """Полный стек заседания: dict с пятью компонентами."""
    ctx = {"meeting_id": meeting_id}

    r = query("SELECT meeting_date::text, decision_kind, notes FROM dkp.meeting WHERE meeting_id=%s" % meeting_id)
    if not r:
        return None
    ctx["meeting_date"], ctx["decision_kind"], ctx["notes"] = r[0]

    # графовый 1-хоп: все компоненты из graph (структурная карта)
    g = query("""
        SELECT n2.node_type, n2.ref_key, e.edge_type
        FROM graph.edge e
        JOIN graph.node n1 ON n1.node_id = e.src_id
        JOIN graph.node n2 ON n2.node_id = e.dst_id
        WHERE n1.node_type='cbr_meeting' AND n1.ref_key='meeting:%s'
        ORDER BY e.edge_type""" % meeting_id)
    ctx["graph_links"] = [{"node": t, "ref": k, "edge": e} for t, k, e in g]

    # решение
    r = query("SELECT decision_id, action, rate_prev, rate_new, delta_bp, signal_kind, headline_ru "
              "FROM dkp.decision WHERE meeting_id=%s" % meeting_id)
    if r:
        d = r[0]
        ctx["decision"] = {"decision_id": d[0], "action": d[1],
                           "rate_prev": float(d[2]) if d[2] is not None else None,
                           "rate_new": float(d[3]) if d[3] is not None else None,
                           "delta_bp": float(d[4]) if d[4] is not None else None,
                           "signal_kind": d[5], "headline": d[6]}

    # пресс-релиз и заявление
    ctx["press_release"] = None
    ctx["chair_statement"] = None
    for kind, key in (("press_release", "press_release"),
                      ("chair_statement", "chair_statement")):
        r = query("SELECT statement_id, event_date::text, url, body FROM dkp.statement "
                  "WHERE meeting_id=%s AND kind='%s'" % (meeting_id, kind))
        if r:
            ctx[key] = {"statement_id": r[0][0], "event_date": r[0][1],
                        "url": r[0][2], "body": r[0][3]}

    # Резюме обсуждения
    r = query("SELECT minutes_id, url, body FROM dkp.minutes WHERE meeting_id=%s" % meeting_id)
    if r:
        ctx["minutes"] = {"minutes_id": r[0][0], "url": r[0][1], "body": r[0][2]}

    # прогнозные серии
    r = query("""
        SELECT scenario, series_code, horizon_year, value_low, value_high, value_point, unit_code
        FROM dkp.forecast WHERE meeting_id=%s ORDER BY series_code, horizon_year""" % meeting_id)
    ctx["forecast"] = [
        {"scenario": x[0], "series": x[1], "year": x[2],
         "low": float(x[3]) if x[3] is not None else None,
         "high": float(x[4]) if x[4] is not None else None,
         "point": float(x[5]) if x[5] is not None else None,
         "unit": x[6]} for x in r]

    # аргументы решения
    r = query("""
        SELECT a.argument_id, a.block, a.direction, a.text_short
        FROM dkp.argument a JOIN dkp.decision d USING (decision_id)
        WHERE d.meeting_id=%s ORDER BY a.block, a.argument_id""" % meeting_id)
    ctx["arguments"] = [
        {"argument_id": x[0], "block": x[1], "direction": x[2], "text_short": x[3]}
        for x in r]

    return ctx


def main():
    mid = resolve_meeting(sys.argv)
    if not mid:
        print("Использование: --meeting=<id> | --date=ГГГГ-ММ-ДД | --last")
        return 1
    ctx = dkp_context(mid)
    if ctx is None:
        print("meeting %s не найден" % mid)
        return 1
    out = {k: v for k, v in ctx.items() if k not in ("press_release", "chair_statement", "minutes")}
    out["press_release_len"] = len(ctx["press_release"]["body"]) if ctx.get("press_release") else 0
    out["chair_statement_len"] = len(ctx["chair_statement"]["body"]) if ctx.get("chair_statement") else 0
    out["minutes_len"] = len(ctx["minutes"]["body"]) if ctx.get("minutes") else 0
    out["n_graph_links"] = len(ctx.get("graph_links", []))
    print(json.dumps(out, ensure_ascii=False, indent=1))
    # полный контекст доступен как python-объект: dkp_context(mid)
    return 0


if __name__ == "__main__":
    sys.exit(main())