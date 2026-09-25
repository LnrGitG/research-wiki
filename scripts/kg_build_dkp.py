# -*- coding: utf-8 -*-
"""
kg_build_dkp.py — сборка dkp-подграфа в graph.node/graph.edge.

Узлы: cbr_meeting, cbr_decision, cbr_statement (2 kind), cbr_minutes,
cbr_forecast_series, cbr_argument, metric (v2.metric).
Рёбра (по FK dkp — верифицируемое происхождение):
  meeting—has_decision→decision; meeting—has_statement→statement(2 kind);
  meeting—has_minutes→minutes; meeting—has_forecast→forecast_series;
  decision—has_argument→argument; decision—follows→decision(prev);
  decision—with_signal→signal_kind-узел; forecast_series—uses_metric→metric.
Dry-run: --dry. Отчёт: счётчики узлов/рёбер.
"""
import sys
import time

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query, execute, load_sql_file  # noqa: E402

DRY = "--dry" in sys.argv


def esc(s):
    return str(s).replace("'", "''") if s is not None else ""


def upsert_node(ntype, ref_key, title, props_dict=None):
    """INSERT ... ON CONFLICT — idempotent; props_dict -> безопасный jsonb."""
    import json as _json
    props_sql = _json.dumps(props_dict or {}, ensure_ascii=False).replace("'", "''")
    if DRY:
        return None
    q = ("INSERT INTO graph.node (node_type, ref_key, title, props) "
         "VALUES ('%s','%s','%s','%s'::jsonb) "
         "ON CONFLICT (node_type, ref_key) DO UPDATE SET title=EXCLUDED.title "
         "RETURNING node_id" % (ntype, esc(ref_key), esc(title), props_sql))
    r = query(q)
    return r[0][0] if r else None


def upsert_edge(src, dst, etype, prov_dict=None):
    import json as _json
    if DRY or src is None or dst is None:
        return
    prov_sql = _json.dumps(prov_dict or {}, ensure_ascii=False).replace("'", "''")
    q = ("INSERT INTO graph.edge (src_id, dst_id, edge_type, provenance) "
         "VALUES (%s,%s,'%s','%s'::jsonb) ON CONFLICT DO NOTHING"
         % (src, dst, etype, prov_sql))
    execute(q)


def main():
    t0 = time.time()
    stats = {}

    # --- meetings ---------------------------------------------------------
    meetings = query(
        "SELECT meeting_id, meeting_date::text, decision_kind FROM dkp.meeting")
    for mid, mdate, dkind in meetings:
        upsert_node(
            "cbr_meeting", "meeting:%s" % mid,
            "Заседание СД %s" % mdate,
            {"meeting_date": mdate, "decision_kind": dkind or ""})
        stats["cbr_meeting"] = stats.get("cbr_meeting", 0) + 1
    print("meetings:", len(meetings))

    # --- decisions + follows + with_signal --------------------------------
    decisions = query(
        "SELECT decision_id, meeting_id, action, rate_prev, rate_new, "
        "signal_kind FROM dkp.decision ORDER BY meeting_id")
    prev_by_meeting = {}
    prev_dec = None
    prev_meeting = None
    for did, mid, action, rprev, rnew, sig in decisions:
        title = "Решение %s: %s" % (mid, action)
        nid = upsert_node(
            "cbr_decision", "decision:%s" % did,
            title,
            {"meeting_id": mid, "action": action,
             "rate_prev": float(rprev) if rprev is not None else None,
             "rate_new": float(rnew) if rnew is not None else None})
        mnode = query("SELECT node_id FROM graph.node WHERE node_type='cbr_meeting' AND ref_key='meeting:%s'" % mid)
        mnode_id = mnode[0][0] if mnode else None
        upsert_edge(mnode_id, nid, "has_decision",
                    {"fk": "dkp.decision.meeting_id=%s" % mid})
        # follows: предыдущее решение по хронологии заседаний
        if prev_dec is not None and prev_meeting is not None:
            upsert_edge(nid, prev_dec, "follows",
                        {"rule": "prev meeting chronology", "prev_meeting": prev_meeting})
        prev_dec = nid
        prev_meeting = mid
        # with_signal: узел-атрибут
        if sig:
            snid = upsert_node("cbr_signal", "signal:%s" % sig,
                               "Сигнал: %s" % sig)
            upsert_edge(nid, snid, "with_signal",
                        {"fk": "dkp.decision.signal_kind"})
        stats["cbr_decision"] = stats.get("cbr_decision", 0) + 1
    print("decisions:", len(decisions))

    # --- statements (press_release + chair_statement) ----------------------
    stmts = query(
        "SELECT statement_id, meeting_id, kind, event_date::text, url "
        "FROM dkp.statement")
    for sid, mid, kind, edate, url in stmts:
        nid = upsert_node(
            "cbr_statement", "statement:%s" % sid,
            "%s %s" % (kind, edate),
            {"kind": kind, "event_date": edate, "url": url or ""})
        mnode = query("SELECT node_id FROM graph.node WHERE node_type='cbr_meeting' AND ref_key='meeting:%s'" % mid)
        if mnode:
            upsert_edge(mnode[0][0], nid, "has_statement",
                        {"fk": "dkp.statement.meeting_id=%s" % mid, "kind": kind})
        stats.setdefault("cbr_statement", 0)
        stats["cbr_statement"] += 1
    print("statements:", len(stmts))

    # --- minutes ------------------------------------------------------------
    minutes = query(
        "SELECT minutes_id, meeting_id, url FROM dkp.minutes")
    for mnid, mid, url in minutes:
        nid = upsert_node(
            "cbr_minutes", "minutes:%s" % mnid,
            "Резюме обсуждения (meeting %s)" % mid,
            {"url": url or ""})
        mnode = query("SELECT node_id FROM graph.node WHERE node_type='cbr_meeting' AND ref_key='meeting:%s'" % mid)
        if mnode:
            upsert_edge(mnode[0][0], nid, "has_minutes",
                        {"fk": "dkp.minutes.meeting_id=%s" % mid})
        stats["cbr_minutes"] = stats.get("cbr_minutes", 0) + 1
    print("minutes:", len(minutes))

    # --- forecast_series (meeting+series_code) + uses_metric ---------------
    fs = query("""
        SELECT meeting_id, series_code, min(horizon_year), max(horizon_year), count(*)
        FROM dkp.forecast GROUP BY meeting_id, series_code""")
    for mid, scode, hmin, hmax, cnt in fs:
        ref = "forecast_series:%s:%s" % (mid, scode)
        nid = upsert_node(
            "cbr_forecast_series", ref,
            "Прогноз %s (%s): %s–%s" % (scode, mid, hmin, hmax),
            {"meeting_id": mid, "series_code": scode, "horizons": int(cnt)})
        mnode = query("SELECT node_id FROM graph.node WHERE node_type='cbr_meeting' AND ref_key='meeting:%s'" % mid)
        if mnode:
            upsert_edge(mnode[0][0], nid, "has_forecast",
                        {"fk": "dkp.forecast.meeting_id=%s" % mid, "series": scode})
        # uses_metric -> metric узел (создаём при отсутствии)
        mn = query("SELECT node_id FROM graph.node WHERE node_type='metric' AND ref_key='metric:%s'" % esc(scode))
        if not mn:
            mn = [upsert_node("metric", "metric:%s" % esc(scode), scode)]
        upsert_edge(nid, mn[0], "uses_metric",
                    {"fk": "dkp.forecast.series_code=%s" % scode})
        stats["cbr_forecast_series"] = stats.get("cbr_forecast_series", 0) + 1
    print("forecast_series:", len(fs))

    # --- arguments ----------------------------------------------------------
    args = query(
        "SELECT argument_id, decision_id, block, direction FROM dkp.argument")
    for aid, did, block, direction in args:
        nid = upsert_node(
            "cbr_argument", "argument:%s" % aid,
            "Аргумент %s [%s/%s]" % (aid, block, direction),
            {"decision_id": did, "block": block or "", "direction": direction or ""})
        dnode = query("SELECT node_id FROM graph.node WHERE node_type='cbr_decision' AND ref_key='decision:%s'" % did)
        if dnode:
            upsert_edge(dnode[0][0], nid, "has_argument",
                        {"fk": "dkp.argument.decision_id=%s" % did})
        stats["cbr_argument"] = stats.get("cbr_argument", 0) + 1
    print("arguments:", len(args))

    # --- metric nodes для существующих series_code --------------------------
    metrics = query("SELECT DISTINCT series_code FROM dkp.forecast")
    for (scode,) in metrics:
        upsert_node("metric", "metric:%s" % esc(scode), scode)
        stats["metric"] = stats.get("metric", 0) + 1

    nn = query("SELECT count(*) FROM graph.node")[0][0] if not DRY else sum(
        v for k, v in stats.items() if k != "metric")
    ne = query("SELECT count(*) FROM graph.edge")[0][0] if not DRY else 0
    print("\nИТОГ: nodes=%s edges=%s stats=%s in %.1fs"
          % (nn, ne, stats, time.time() - t0))
    if not DRY:
        execute("INSERT INTO graph.ingest_log (started_at, finished_at, pipeline_v, n_nodes, n_edges, notes) "
                "VALUES (now(), now(), 'kg_build_dkp_v1', %s, %s, 'dkp subgraph')"
                % (nn, ne))
    return 0


if __name__ == "__main__":
    sys.exit(main())