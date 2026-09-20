#!/usr/bin/env python3
"""spec_cli.py — запуск спецификаций из specs/ с записью в derived.spec_runs.

Использование:
  python3 scripts/spec_cli.py run <name>            # один прогон
  python3 scripts/spec_cli.py run <name> --grid lags=1..6
  python3 scripts/spec_cli.py list
  python3 scripts/spec_cli.py show <name>

Валидация: specs/schema.json (jsonschema). Подключение: PGHOST/PGPORT/PGUSER/PGDATABASE env
(на ВМ: PGHOST=127.0.0.1 PGPORT=5432 PGUSER=wiki, пароль из ~/.pgpass).
"""
import argparse
import glob
import json
import os
import sys
import time
from datetime import datetime, timezone

import psycopg2
import psycopg2.extras
import psycopg2.sql
import yaml

SPEC_DIR = os.path.join(os.path.dirname(__file__), "..", "specs")
try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


def load_spec(name: str) -> dict:
    path = os.path.join(SPEC_DIR, f"{name}.yaml")
    if not os.path.exists(path):
        sys.exit(f"Spec not found: {path}")
    with open(path) as f:
        spec = yaml.safe_load(f)
    schema_path = os.path.join(SPEC_DIR, "schema.json")
    if HAS_JSONSCHEMA and os.path.exists(schema_path):
        with open(schema_path) as f:
            jsonschema.validate(spec, json.load(f))
    return spec


def db_connect():
    return psycopg2.connect(
        host=os.environ.get("PGHOST", "127.0.0.1"),
        port=int(os.environ.get("PGPORT", "5432")),
        user=os.environ.get("PGUSER", "wiki"),
        dbname=os.environ.get("PGDATABASE", "research_wiki"),
    )


def fetch_series(conn, metric_id: int, freq: str, region_id: int = 1,
                 release: str = "final"):
    """Возвращает [(period_start, value)] для метрики (final-оценки, последний релиз)."""
    release_order = "DESC" if release == "final" else "ASC"
    q = """
    SELECT o.period_start::date, o.value
    FROM core.observation_v2 o
    WHERE o.metric_id = %s AND o.frequency_id = %s AND o.region_id = %s
    ORDER BY o.period_start::date, o.release_id {order}
    """.format(order=release_order)
    with conn.cursor() as cur:
        cur.execute(q, (metric_id, {"m": 5, "q": 6, "a": 3}[freq], region_id))
        rows = cur.fetchall()
    # последний релиз на период
    best = {}
    for period, value in rows:
        best[period] = value
    return sorted(best.items())


def grid_expand(spec: dict, grid_args: list[str]) -> list[dict]:
    """--grid lags=1..6 -> варианты spec с заменой поля (только плоские поля)."""
    if not grid_args:
        return [spec]
    variants = []
    keys = []
    value_lists = []
    for g in grid_args:
        k, v = g.split("=", 1)
        if ".." in v:
            a, b = v.split("..")
            values = list(range(int(a), int(b) + 1))
        else:
            values = [int(x) for x in v.split(",")]
        keys.append(k)
        value_lists.append(values)
    import itertools
    for combo in itertools.product(*value_lists):
        s = json.loads(json.dumps(spec))  # deep copy
        node = s
        # простая замена: только одиночный ключ
        node[keys[0]] = combo[0]
        variants.append(s)
    return variants


def run_variant(spec: dict, conn) -> dict:
    """Прогон одного варианта. Пока — каркас OLS по target/features через metric_code."""
    import numpy as np
    metric_ids = {}
    with conn.cursor() as cur:
        # резолв metric_code -> metric_id
        codes = [spec["target"]["metric_code"]] + [
            f["metric_code"] for f in spec.get("features", [])
        ]
        cur.execute("SELECT metric_id, metric_code FROM core.metric WHERE metric_code = ANY(%s)", ([c for c in set(codes)],))
        metric_ids = dict((c, mid) for mid, c in cur.fetchall())
    missing = [c for c in set(codes) if c not in metric_ids]
    if missing:
        return {"status": "failed", "notes": f"unknown metric_code: {missing}"}

    # загрузка рядов
    freq = spec["target"]["frequency"]
    target_series = fetch_series(conn, metric_ids[spec["target"]["metric_code"]], freq)
    if not target_series:
        return {"status": "failed", "notes": "target series empty"}

    # build dataframe
    import pandas as pd
    df = pd.DataFrame(target_series, columns=["period", "target"])
    for feat in spec.get("features", []):
        s = fetch_series(conn, metric_ids[feat["metric_code"]], feat.get("frequency", freq))
        if s:
            fdf = pd.DataFrame(s, columns=["period", feat["metric_code"]])
            for lag in feat.get("lags", [0]):
                fdf[feat["metric_code"] + f"_l{lag}"] = fdf[feat["metric_code"]].shift(lag)
            df = df.merge(fdf, on="period", how="left")
    df = df.dropna().astype({c: "float64" for c in df.columns if c != "period"})
    df = df.set_index("period")
    df.index = pd.PeriodIndex(df.index.astype(str), freq={"m": "M", "q": "Q", "a": "A"}[freq])
    # sample window
    sm = spec.get("sample", {})
    if sm.get("start"):
        df = df[df.index >= pd.Period(sm["start"], freq=df.index.freq)]
    if sm.get("end"):
        df = df[df.index <= pd.Period(sm["end"], freq=df.index.freq)]
    lag_cols = [c for c in df.columns if c.endswith(tuple(f"_l{n}" for n in range(0, 12)))]
    X = df[lag_cols_fn(df)]
    y = df["target"]
    if len(df) < 20:
        return {"status": "failed", "notes": f"too few obs: {len(df)}"}
    import statsmodels.api as sm
    est = sm.OLS(y, sm.add_constant(X)).fit()
    metrics = {
        "r2": float(est.rsquared),
        "n": int(len(df)),
    }
    # OOS RMSE, если задан
    oos = spec.get("oos", {})
    if oos.get("start"):
        oos_mask = df.index >= pd.Period(oos["start"], freq=df.index.freq)
        if oos_mask.sum() >= 4:
            est_is = sm.OLS(y[~oos_mask], sm.add_constant(X[~oos_mask])).fit()
            pred = est_is.predict(sm.add_constant(X[oos_mask]))
            metrics["rmse_oos"] = float(np.sqrt(((y[oos_mask] - pred) ** 2).mean()))
    return {"status": "ok", "metrics": metrics}


def lag_cols_fn(df):
    return [c for c in df.columns if "_l" in c]


def record_run(conn, spec: dict, result: dict, start_ts):
    with conn.cursor() as cur:
        cur.execute(
            """INSERT INTO derived.spec_runs
               (spec_name, spec_version, status, params, metrics, started_at, finished_at, rmse, mae, r2, notes)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING run_id""",
            (
                spec["name"], spec.get("version", 1), result["status"],
                psycopg2.extras.Json(spec),
                psycopg2.extras.Json(result.get("metrics", {})),
                start_ts, datetime.now(timezone.utc),
                (result.get("metrics", {}) or {}).get("rmse_oos"),
                (result.get("metrics", {}) or {}).get("mae_oos"),
                (result.get("metrics", {}) or {}).get("r2"),
                result.get("notes"),
            ),
        )
        run_id = cur.fetchone()[0]
    conn.commit()
    return run_id


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("name")
    r.add_argument("--grid", nargs="*", default=[])
    sub.add_parser("list")
    s = sub.add_parser("show")
    s.add_argument("name")
    args = ap.parse_args()

    if args.cmd == "list":
        for p in sorted(glob.glob(os.path.join(SPEC_DIR, "*.yaml"))):
            s = yaml.safe_load(open(p))
            print(f"{s['name']:30s} v{s.get('version',1)} {s.get('model','?'):8s} {s.get('notes','')[:50]}")
        return

    spec = load_spec(args.name)
    conn = db_connect()
    start = datetime.now(timezone.utc)
    result = run_variant(spec, conn)
    run_id = record_run(conn, spec, result, start)
    print(f"run_id={run_id} status={result['status']} metrics={json.dumps(result.get('metrics', {}), ensure_ascii=False)}")


if __name__ == "__main__":
    main()