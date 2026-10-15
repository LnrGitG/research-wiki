#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-034: разрыв «цена новостройки минус стоимость строительства» и банковский клин.

Дизайн зафиксирован в queries/h034-price-cost-gap-spec-20261015.md.
Запуск: локально (тоннель 127.0.0.1:15432) и на ВМ (localhost:5432) — без правок логики,
отличие только в DSN. Зависимости: numpy, scipy, psycopg2 (statsmodels не нужен).

Выход: JSON (stdout и, при --out, в файл).
"""
import argparse
import json
import os
import sys

import numpy as np
import psycopg2

DSN_LOCAL = "host=127.0.0.1 port=15432 dbname=research_wiki user=wiki"
DSN_VM = "host=127.0.0.1 port=5432 dbname=research_wiki user=wiki"

SERIES = {
    "price": "domrf_price_index_m",
    "icpp": "kep3_34",
    "balance": "cbrmon__stroitelstvo__vse__ishodnye_dannye__kak_izmenilis_usloviya_kreditovaniya_balans_otvetov",
}


def fetch(dsn, code, region=1):
    """Ряд метрики: список (period_start, value) по возрастанию даты."""
    sql = """
        select m.metric_id from catalog.metric m where m.metric_code = %s limit 1
    """
    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (code,))
            row = cur.fetchone()
            if row is None:
                raise SystemExit("метрика не найдена: %s" % code)
            mid = row[0]
            cur.execute(
                """select period_start, value from data.observation
                   where metric_id = %s and region_id = %s
                   order by period_start""",
                (mid, region),
            )
            return [(p, float(v)) for p, v in cur.fetchall()]


def fetch_key_rate(dsn):
    """Ключевая ставка: среднее по месяцу из дневного ряда."""
    sql = """
        select date_trunc('month', o.period_start)::date, avg(o.value)
        from data.observation o join catalog.metric m on m.metric_id = o.metric_id
        where m.metric_code = 'cbr_key_rate' and o.region_id = 1
        group by 1 order by 1
    """
    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return [(p, float(v)) for p, v in cur.fetchall()]


def to_month_index(rows):
    """{YYYY-MM: value}"""
    out = {}
    for p, v in rows:
        k = p.strftime("%Y-%m") if hasattr(p, "strftime") else str(p)[:7]
        out[k] = v
    return out


def chain_icpp(rows):
    """Цепной месячный индекс ИЦП -> уровень, база = первому наблюдению (100).

    Дубли наблюдений по месяцу схлопываются (в базе встречаются пары строк
    с одинаковым значением): без этого каждый месяц умножается дважды и
    накопленный индекс завышается вдвое по темпу.
    """
    dedup = {}
    for p, v in rows:
        k = p.strftime("%Y-%m") if hasattr(p, "strftime") else str(p)[:7]
        dedup[k] = v
    out, level = [], 100.0
    first = True
    for k in sorted(dedup):
        if first:
            out.append((k, level))
            first = False
            continue
        level *= dedup[k] / 100.0
        out.append((k, level))
    return out


def align(*series):
    """Выравнивание по общим месяцам: список dict'ов {label: value} + список меток."""
    keys = None
    for rows in series:
        k = set(p.strftime("%Y-%m") if hasattr(p, "strftime") else p for p, _ in rows)
        keys = k if keys is None else (keys & k)
    keys = sorted(keys)
    maps = [to_month_index(rows) for rows in series]
    return keys, maps


def ols_hac(y, X, lags):
    """OLS + HAC (Newey-West) стандартные ошибки, малая выборка."""
    y = np.asarray(y, float)
    X = np.asarray(X, float)
    n, k = X.shape
    XtX_inv = np.linalg.pinv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    e = y - X @ beta
    # HAC
    S = (X * e[:, None]).T @ (X * e[:, None])
    for l in range(1, lags + 1):
        w = 1.0 - l / (lags + 1.0)
        G = (X[l:] * e[l:, None]).T @ (X[:-l] * e[:-l, None])
        S += w * (G + G.T)
    V = XtX_inv @ S @ XtX_inv
    se = np.sqrt(np.maximum(np.diag(V), 1e-30))
    tss = float(np.sum((y - y.mean()) ** 2))
    rss = float(np.sum(e ** 2))
    return {
        "beta": beta.tolist(),
        "se": se.tolist(),
        "t": (beta / se).tolist(),
        "r2": 1.0 - rss / tss if tss > 0 else None,
        "n": int(n),
        "k": int(k),
        "lags_hac": int(lags),
    }


def adf(x, max_lag=1):
    """Простой ADF с константой: t-статистика коэффициента при x_{t-1}."""
    x = np.asarray(x, float)
    dx = np.diff(x)
    y = dx[max_lag:]
    cols = [np.ones(len(y)), x[max_lag:-1]]
    for i in range(1, max_lag + 1):
        cols.append(dx[max_lag - i:-i])
    X = np.column_stack(cols)
    XtX_inv = np.linalg.pinv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    e = y - X @ beta
    dof = len(y) - X.shape[1]
    s2 = float(e @ e) / dof
    se = np.sqrt(np.maximum(np.diag(XtX_inv) * s2, 1e-30))
    return {"t_adf": float(beta[1] / se[1]), "n": int(len(y)), "lag": int(max_lag)}


def build_dataset(dsn, start="2021-01"):
    price = fetch(dsn, SERIES["price"])
    icpp = chain_icpp(fetch(dsn, SERIES["icpp"]))
    bal = fetch(dsn, SERIES["balance"])
    kr = fetch_key_rate(dsn)
    keys, maps = align(price, icpp, bal, kr)
    keys = [k for k in keys if k >= start]
    P = np.array([maps[0][k] for k in keys], float)
    C = np.array([maps[1][k] for k in keys], float)
    B = np.array([maps[2][k] for k in keys], float)
    R = np.array([maps[3][k] for k in keys], float)
    G = np.log(P / P[0]) - np.log(C / C[0])
    return {"months": keys, "P": P, "C": C, "G": G, "B": B, "R": R}


def ecm(ds, fin="both", hac_lags=6, maxlag=2, mask=None):
    """ECM: dG_t = a + rho*G_{t-1} + phi*dG + theta*dR + psi*dB (+ лаги)."""
    G, R, B = ds["G"], ds["R"], ds["B"]
    dG = np.diff(G)
    dR = np.diff(R)
    dB = np.diff(B)
    T = len(dG)
    idx = np.arange(maxlag, T)
    if mask is not None:
        keep = np.array([bool(mask[i + 1]) for i in idx])
        idx = idx[keep]
    y = dG[idx]
    cols = [np.ones(len(idx)), G[idx]]
    for i in range(1, maxlag + 1):
        cols.append(dG[idx - i])
    if fin in ("rate", "both"):
        cols.append(dR[idx])
        cols.append(dR[idx - 1])
    if fin in ("balance", "both"):
        cols.append(dB[idx])
        cols.append(dB[idx - 1])
    X = np.column_stack(cols)
    res = ols_hac(y, X, hac_lags)
    names = ["const", "G_lag1"] + ["dG_lag%d" % i for i in range(1, maxlag + 1)]
    if fin in ("rate", "both"):
        names += ["dR", "dR_lag1"]
    if fin in ("balance", "both"):
        names += ["dB", "dB_lag1"]
    res["names"] = names
    res["months"] = [ds["months"][i + 1] for i in idx]
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dsn", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--start", default="2021-01")
    args = ap.parse_args()
    dsn = args.dsn or os.environ.get("H034_DSN") or (
        DSN_VM if os.environ.get("H034_ON_VM") else DSN_LOCAL
    )
    out = {"dsn_class": "vm" if dsn == DSN_VM else "local", "start": args.start}
    ds = build_dataset(dsn, args.start)
    out["sample"] = {
        "n": len(ds["months"]),
        "first": ds["months"][0],
        "last": ds["months"][-1],
        "gap_first": float(ds["G"][0]),
        "gap_last": float(ds["G"][-1]),
        "price_last": float(ds["P"][-1]),
        "icpp_last": float(ds["C"][-1]),
    }
    out["adf"] = {"G": adf(ds["G"]), "dG": adf(np.diff(ds["G"]))}
    m = ds["months"]
    dates = np.array([x + "-01" for x in m])
    def mask_range(a, b):
        return np.array([(a <= x <= b) for x in dates])
    out["models"] = {
        "M1_rate": ecm(ds, "rate"),
        "M2_balance": ecm(ds, "balance"),
        "M3_both": ecm(ds, "both"),
    }
    # M4: уровни (ADL с трендом)
    G, R, B = ds["G"], ds["R"], ds["B"]
    t = np.arange(len(G), dtype=float)
    X = np.column_stack([np.ones(len(G)), t, R, B])
    out["models"]["M4_levels"] = ols_hac(G, X, 6)
    out["models"]["M4_levels"]["names"] = ["const", "trend", "R", "B"]
    # подпериоды на базовой спецификации
    for a, b, tag in (("2021-01", "2023-12", "sub_2021_2023"),
                      ("2024-01", "2026-12", "sub_2024_2026")):
        mk = mask_range(a + "-01", b + "-01")
        try:
            out["models"][tag] = ecm(ds, "both", mask=mk)
        except Exception as exc:  # noqa: BLE001
            out["models"][tag] = {"error": str(exc)}
    # сценарии по длине лага HAC
    out["hac_sensitivity"] = {}
    for L in (3, 6, 9, 12):
        r = ecm(ds, "both", hac_lags=L)
        i = r["names"].index("dR")
        out["hac_sensitivity"]["hac_%d" % L] = {
            "theta_dR": r["beta"][i], "t_dR": r["t"][i],
        }
    txt = json.dumps(out, ensure_ascii=False, indent=2, default=float)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(txt)
    else:
        sys.stdout.write(txt + "\n")


if __name__ == "__main__":
    main()
