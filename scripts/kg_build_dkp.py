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
Оптимизировано: per-meeting lookup'ы заменены dict-кэшами ( тоннель ~0.7с/запрос).
"""
import sys
import time

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query, execute, load_sql_file  # noqa: E402

DRY = "--dry" in sys.argv


def esc(s):
    return str(s).replace("'", "''") if s is not None else ""


def upsert_node(ntype, ref_key, title, props_dict=None, cache=None):
    """INSERT ... ON CONFLICT — idempotent; props_dict -> безопасный jsonb."""
    import json as _json
    if cache is not None and ref_key in cache:
        return cache[ref_key]
    props_sql = _json.dumps(props_dict or {}, ensure_ascii=False).replace("'", "''")
    if DRY:
        return None
    q = ("INSERT INTO graph.node (node_type, ref_key, title, props) "
         "VALUES ('%s','%s','%s','%s'::jsonb) "
         "ON CONFLICT (node_type, ref_key) DO UPDATE SET title=EXCLUDED.title "
         "RETURNING node_id" % (ntype, esc(ref_key), esc(title), props_sql))
    r = query(q)
    nid = r[0][0] if r else None
    if cache is not None:
        cache[ref_key] = nid
    return nid


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

    # Кэш meeting-узлов: meeting_id -> node_id (один SELECT вместо ~300)
    meeting_cache = {}
    for mid, nid in query("SELECT ref_key, node_id FROM graph.node WHERE node_type='cbr_meeting'"):
        meeting_cache[int(mid.split(":")[1])] = nid

    # --- meetings ---------------------------------------------------------
    meetings = query(
        "SELECT meeting_id, meeting_date::text, decision_kind FROM dkp.meeting")
    meeting_node_ids = {}
    for mid, mdate, dkind in meetings:
        nid = upsert_node(
            "cbr_meeting", "meeting:%s" % mid,
            "Заседание СД %s" % mdate,
            {"meeting_date": mdate, "decision_kind": dkind or ""},
            cache=meeting_cache)
        meeting_node_ids[mid] = nid
        stats["cbr_meeting"] = stats.get("cbr_meeting", 0) + 1
    print("meetings:", len(meetings), flush=True)

    # --- decisions + follows + with_signal --------------------------------
    decisions = query(
        "SELECT decision_id, meeting_id, action, rate_prev, rate_new, "
        "signal_kind FROM dkp.decision ORDER BY meeting_id")
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
        mnode_id = meeting_node_ids.get(mid)
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
    print("decisions:", len(decisions), flush=True)
    decision_node_ids = {}
    for ref_key, nid in query("SELECT ref_key, node_id FROM graph.node WHERE node_type='cbr_decision'"):
        decision_node_ids[int(ref_key.split(":")[1])] = nid

    # --- statements (press_release + chair_statement) ----------------------
    stmts = query(
        "SELECT statement_id, meeting_id, kind, event_date::text, url "
        "FROM dkp.statement")
    for sid, mid, kind, edate, url in stmts:
        nid = upsert_node(
            "cbr_statement", "statement:%s" % sid,
            "%s %s" % (kind, edate),
            {"kind": kind, "event_date": edate, "url": url or ""})
        mnode_id = meeting_node_ids.get(mid)
        if mnode_id:
            upsert_edge(mnode_id, nid, "has_statement",
                        {"fk": "dkp.statement.meeting_id=%s" % mid, "kind": kind})
        stats.setdefault("cbr_statement", 0)
        stats["cbr_statement"] += 1
    print("statements:", len(stmts), flush=True)

    # --- minutes ------------------------------------------------------------
    minutes = query(
        "SELECT minutes_id, meeting_id, url FROM dkp.minutes")
    for mnid, mid, url in minutes:
        nid = upsert_node(
            "cbr_minutes", "minutes:%s" % mnid,
            "Резюме обсуждения (meeting %s)" % mid,
            {"url": url or ""})
        mnode_id = meeting_node_ids.get(mid)
        if mnode_id:
            upsert_edge(mnode_id, nid, "has_minutes",
                        {"fk": "dkp.minutes.meeting_id=%s" % mid})
        stats["cbr_minutes"] = stats.get("cbr_minutes", 0) + 1
    print("minutes:", len(minutes), flush=True)

    # --- forecast_series (meeting+series_code) + uses_metric ---------------
    # metric-узлы: один SELECT вместо пер-строчных
    metric_cache = {}
    for ref_key, nid in query("SELECT ref_key, node_id FROM graph.node WHERE node_type='metric'"):
        metric_cache[ref_key.split(":", 1)[1]] = nid
    fs = query("""
        SELECT meeting_id, series_code, min(horizon_year), max(horizon_year), count(*)
        FROM dkp.forecast GROUP BY meeting_id, series_code""")
    for mid, scode, hmin, hmax, cnt in fs:
        ref = "forecast_series:%s:%s" % (mid, scode)
        nid = upsert_node(
            "cbr_forecast_series", ref,
            "Прогноз %s (%s): %s–%s" % (scode, mid, hmin, hmax),
            {"meeting_id": mid, "series_code": scode, "horizons": int(cnt)})
        mnode_id = meeting_node_ids.get(mid)
        if mnode_id:
            upsert_edge(mnode_id, nid, "has_forecast",
                        {"fk": "dkp.forecast.meeting_id=%s" % mid, "series": scode})
        # uses_metric -> metric узел (создаём при отсутствии)
        mn_id = metric_cache.get(scode) or upsert_node(
            "metric", "metric:%s" % esc(scode), scode, cache=metric_cache)
        upsert_edge(nid, mn_id, "uses_metric",
                    {"fk": "dkp.forecast.series_code=%s" % scode})
        stats["cbr_forecast_series"] = stats.get("cbr_forecast_series", 0) + 1
    print("forecast_series:", len(fs), flush=True)

    # --- arguments ----------------------------------------------------------
    args = query(
        "SELECT argument_id, decision_id, block, direction FROM dkp.argument")
    for aid, did, block, direction in args:
        nid = upsert_node(
            "cbr_argument", "argument:%s" % aid,
            "Аргумент %s [%s/%s]" % (aid, block, direction),
            {"decision_id": did, "block": block or "", "direction": direction or ""})
        dnode_id = decision_node_ids.get(did) if did else None
        if dnode_id:
            upsert_edge(dnode_id, nid, "has_argument",
                        {"fk": "dkp.argument.decision_id=%s" % did})
        stats["cbr_argument"] = stats.get("cbr_argument", 0) + 1
    print("arguments:", len(args), flush=True)

    # --- metric nodes для существующих series_code --------------------------
    metrics = query("SELECT DISTINCT series_code FROM dkp.forecast")
    for (scode,) in metrics:
        upsert_node("metric", "metric:%s" % esc(scode), scode, cache=metric_cache)
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