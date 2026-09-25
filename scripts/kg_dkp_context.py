# -*- coding: utf-8 -*-
"""
kg_dkp_context.py — сборщик полного коммуникационного стека заседания
dkp_context(meeting_id): решение + пресс-релиз + заявление + Резюме +
прогнозные серии + шок-аннотации одним вызовом (МВФ-рамка, нативное
обогащение контекста).

Шок-раздел (вариант A, семантика запросов без DDL):
- jk_mix: информационная vs чистая компонента по block×direction
  аргументов (Jarociński–Karadi 2020);
- sentiment_residual: остаток OLS delta_bp ~ hawk_share
  (Aruoba–Drechsel 2024), параметры регрессии — по всей выборке;
- path_deviation: факт против траектории последнего прогноза
  (Bu et al. 2021) — заполняется, когда есть прогнозный раунд,
  предшествующий решению.

CLI: --meeting=104 | --date=2026-09-11 | --last

См. также: scripts/dkp_shock_queries.py (полный отчёт трёх методов
по всем заседаниям; OLS-параметры и остатки), queries/
dkp-shock-identification-graph-design.md (дизайн варианта A).
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
        r = query("SELECT meeting_id FROM dkp.meeting WHERE meeting_date <= now() "
                  "ORDER BY meeting_date DESC LIMIT 1")
        return r[0][0] if r else None
    return None


def _shock_annotations(decision_id):
    """Шок-аннотации одного решения (вариант A)."""
    ann = {}

    # jk_mix: распределение аргументов факт/инфо + тональность
    r = query("""
        SELECT
            COUNT(*) FILTER (WHERE a.block IN ('demand','credit','labour','output','inflation_now')),
            COUNT(*) FILTER (WHERE a.block IN ('risk_infl','inflation_expect','signal','transmission')),
            COUNT(*) FILTER (WHERE a.direction='hawkish'),
            COUNT(*) FILTER (WHERE a.direction='dovish'),
            COUNT(*)
        FROM dkp.argument a WHERE a.decision_id=%s""" % decision_id)
    if r and (r[0][4] or 0) > 0:
        fact, info, hawk, dov, total = r[0]
        info_share = info / (info + fact) if (info + fact) else 0.0
        if info_share >= 0.40:
            jk = "informational"
        elif hawk >= 2 * dov and dov < total / 4 and total > 0:
            jk = "pure_tightening_bias"
        elif dov > hawk:
            jk = "pure_easing_bias"
        else:
            jk = "mixed"
        ann["jk_mix"] = {
            "kind": jk, "info_share": round(info_share, 2),
            "fact": fact, "info": info, "hawkish": hawk, "dovish": dov}

    # sentiment_residual: регрессия по всей выборке, остаток для решения
    rows = query("""
        SELECT d.delta_bp,
            COUNT(*) FILTER (WHERE a.direction='hawkish')::float
              / NULLIF(COUNT(*), 0) AS hawk_share
        FROM dkp.argument a JOIN dkp.decision d USING (decision_id)
        GROUP BY d.decision_id, d.delta_bp
        HAVING COUNT(*) > 0""")
    pts = [(float(x[1]), float(x[0] or 0)) for x in rows]
    n = len(pts)
    if n >= 3:
        mx = sum(p[0] for p in pts) / n
        my = sum(p[1] for p in pts) / n
        sxx = sum((p[0] - mx) ** 2 for p in pts)
        sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
        beta = sxy / sxx if sxx else 0.0
        alpha = my - beta * mx
        rh = query("""SELECT d.delta_bp,
                      COUNT(*) FILTER (WHERE a.direction='hawkish')::float
                      / NULLIF(COUNT(*), 0)
                  FROM dkp.argument a JOIN dkp.decision d USING (decision_id)
                  WHERE d.decision_id=%s GROUP BY d.delta_bp""" % decision_id)
        if rh and rh[0][0] is not None and rh[0][1] is not None:
            bp, hs = float(rh[0][0] or 0), float(rh[0][1])
            ann["sentiment_residual"] = {
                "residual_bp": round(bp - (alpha + beta * hs), 1),
                "ols": {"alpha": round(alpha, 1), "beta": round(beta, 1), "n": n}}

    # path_deviation: решение против траектории последнего прогноза
    rp = query("""
        WITH last_fc AS (
            SELECT f.horizon_year,
                   COALESCE(f.value_point, (f.value_low + f.value_high)/2) AS rate_mid,
                   m2.meeting_date AS fc_date,
                   ROW_NUMBER() OVER (PARTITION BY f.horizon_year
                                      ORDER BY m2.meeting_date DESC) AS rn
            FROM dkp.forecast f JOIN dkp.meeting m2 ON m2.meeting_id = f.meeting_id
            WHERE f.series_code='key_rate_avg' AND f.scenario='base')
        SELECT ROUND((d.rate_new - fc.rate_mid)*100, 1), fc.horizon_year, fc.fc_date::text
        FROM dkp.decision d
        JOIN dkp.meeting m ON m.meeting_id = d.meeting_id
        JOIN last_fc fc ON fc.horizon_year = EXTRACT(YEAR FROM m.meeting_date) AND fc.rn=1
        WHERE d.decision_id=%s AND fc.fc_date < m.meeting_date""" % decision_id)
    if rp:
        ann["path_deviation"] = {
            "deviation_bp": float(rp[0][0]) if rp[0][0] is not None else None,
            "horizon_year": int(rp[0][1]), "forecast_date": rp[0][2]}

    return ann


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

    # шок-аннотации (вариант A: семантика запросов)
    rd = query("SELECT decision_id FROM dkp.decision WHERE meeting_id=%s" % meeting_id)
    if rd:
        ctx["shocks"] = _shock_annotations(rd[0][0])

    # неопределённости заседания (вариант B: слой uncertainty)
    ru = query("""SELECT kind, variable, direction, COALESCE(text_short, text_raw)
                  FROM dkp.uncertainty_item
                  WHERE meeting_id=%s ORDER BY item_id""" % meeting_id)
    if ru:
        ctx["uncertainty"] = [
            {"kind": x[0], "variable": x[1], "direction": x[2], "text": x[3]}
            for x in ru]

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
    if "shocks" in ctx:
        out["shocks"] = ctx["shocks"]
    print(json.dumps(out, ensure_ascii=False, indent=1))
    # полный контекст доступен как python-объект: dkp_context(mid)
    return 0


if __name__ == "__main__":
    sys.exit(main())