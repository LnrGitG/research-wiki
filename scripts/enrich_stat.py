#!/usr/bin/env python3
"""enrich_stat.py — шаг 1 разметки: статистические характеристики метрик.

Для каждого ряда (final-оценки, последний релиз, region_id=1):
- flow/stock эвристика (AC1, монотонность, имя);
- value_kind из имени;
- stationarity: ADF/KPSS level+diff;
- transforms: diff, log, yoy, z-score, MA(3/6/12), SAR(STL), 3MMA, 3SAAR —
  стационарность, AC1, signal/noise каждой;
- иерархия: префикс кода/имени (КЭП), кандидаты-родители;
- quality_flags: константа, умерший, короткий.

Запуск на ВМ: PGHOST=127.0.0.1 PGUSER=wiki python3 ~/specs/enrich_stat.py [--limit N]
Запись: derived.metric_enrichment (UPSERT).
"""
import json
import os
import sys

import numpy as np
import pandas as pd
import psycopg2
import psycopg2.extras
from statsmodels.tsa.stattools import adfuller, kpss, acf
from statsmodels.tsa.seasonal import STL

FREQ = {3: "a", 5: "m", 6: "q"}
PERIOD_FREQ = {"m": "M", "q": "Q", "a": "Y"}


def load_series(conn, limit=None):
    """Все метрики РФ: список (metric_id, code, name, tags, freq, series)."""
    q = """
    SELECT m.metric_id, m.metric_code, m.name_ru, m.tags::text, m.frequency_id,
           o.period_start::date, o.value
    FROM core.metric m
    JOIN LATERAL (
        SELECT DISTINCT ON (o.period_start) o.period_start, o.value
        FROM core.observation_v2 o
        WHERE o.metric_id = m.metric_id AND o.region_id = 1
        ORDER BY o.period_start::date, o.release_id DESC
    ) o ON true
    ORDER BY m.metric_id, o.period_start
    """
    if limit:
        q += f" LIMIT {int(limit)}"
    with conn.cursor() as cur:
        cur.execute(q)
        rows = cur.fetchall()
    by_metric = {}
    for mid, code, name, tags, fid, period, value in rows:
        by_metric.setdefault((mid, code, name, tags, fid), []).append((str(period), value))
    return by_metric


def adf_p(s):
    try:
        return float(adfuller(s, autolag="AIC")[1])
    except Exception:
        return None


def kpss_p(s):
    try:
        return float(kpss(s, regression="c", nlags="auto")[1])
    except Exception:
        return None



def _clean(o):
    """None вместо NaN/inf — для JSONB."""
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(x) for x in o]
    if isinstance(o, float) and (np.isnan(o) or np.isinf(o)):
        return None
    return o


def series_char(s: pd.Series, freq: str) -> dict:
    """Стационарность + AC1 + сезонность одного ряда."""
    s = s.dropna().astype(float)
    out = {"n": int(len(s))}
    if len(s) < 12:
        return out
    out["adf_level"] = adf_p(s)
    out["adf_diff"] = adf_p(s.diff().dropna())
    out["kpss_level"] = kpss_p(s)
    ac = acf(s, nlags=min(len(s) - 1, 24), fft=True)
    out["ac1"] = float(ac[1])
    season_lag = {"m": 12, "q": 4}.get(freq)
    if season_lag and len(s) >= season_lag * 2 + 4:
        out["acf_seasonal"] = float(ac[season_lag])
        out["seasonal_significant"] = bool(abs(ac[season_lag]) > 2 / np.sqrt(len(s)))
    out["cv"] = float(s.std() / abs(s.mean())) if abs(s.mean()) > 1e-9 else None
    return out


def ma_profile(s: pd.Series, window: int) -> dict:
    sma = s.rolling(window, center=True).mean()
    ratio = float((sma / s).std()) if len(s) > window else None
    corr = float(s.corr(sma)) if sma.notna().sum() > 10 else None
    return {"corr_raw": corr, "signal_ratio": ratio}


def sar_profile(s: pd.Series, freq: str) -> dict:
    """STL-разложение: амплитуда сезонной компоненты, доля сезонной дисперсии, фаза пика."""
    s = s.dropna().astype(float)
    period = 12 if freq == "m" else 4
    if len(s) < period * 2 + 8:
        return {}
    try:
        from statsmodels.tsa.seasonal import STL
        res = STL(s, period=period, robust=True).fit()
        seas = res.seasonal
        amp = float((seas.max() - seas.min()) / max(abs(s.mean()), 1e-9))
        share = float(seas.var() / (seas.var() + res.resid.var())) if res.resid.var() > 0 else None
        peak_idx = int(seas.groupby(seas.index.month if freq == "m" else seas.index.quarter).mean().idxmax())
        return {"amplitude": amp, "season_share": share, "peak_period": int(peak_idx)}
    except Exception:
        return {}


def mma_saar(s: pd.Series, freq: str) -> dict:
    """3MMA и 3SAAR (для месячных): сглаженный SA-ряд в годовом выражении."""
    s = s.dropna().astype(float)
    out = {}
    if freq == "m" and len(s) >= 15:
        mma = s.rolling(3).mean()
        out["mma3_corr_raw"] = float(s.corr(mma))
        try:
            from statsmodels.tsa.seasonal import STL
            res = STL(s, period=12, robust=True).fit()
            sa = s - res.seasonal  # seasonally adjusted
            # 3SAAR: SA за 3 мес → годовой темп: (SA_t / SA_{t-3})^4 - 1
            saar = (sa / sa.shift(3)) ** 4 - 1
            saar = saar.replace([np.inf, -np.inf], np.nan).dropna()
            if len(saar) >= 12:
                out["saar_ac1"] = float(acf(saar, nlags=1, fft=True)[1])
                out["saar_cv"] = float(saar.std() / abs(saar.mean())) if abs(saar.mean()) > 1e-9 else None
                out["saar_adf"] = adf_p(saar)
            # SA vs raw стационарность
            sa_clean = sa.dropna()
            if len(sa_clean) >= 12:
                out["sa_adf_level"] = adf_p(sa_clean)
                out["sa_ac1"] = float(acf(sa_clean, nlags=1, fft=True)[1])
        except Exception:
            pass
    if freq == "q" and len(s) >= 8:
        mma = s.rolling(2).mean()
        out["mma2_corr_raw"] = float(s.corr(mma)) if mma.notna().sum() > 6 else None
    return out


def flow_stock_heuristic(s: pd.Series, name: str, freq: str) -> tuple:
    """(flow_stock, value_kind) — эвристика по динамике и имени."""
    name_l = (name or "").lower()
    if any(w in name_l for w in ["темп", "% к соотв", "yoy", "% к пред", "процент", "индекс", "ставка"]):
        return "ratio", "temp"
    if any(w in name_l for w in ["остат", "задолжен", "действующ", "запас", "на счетах", "портфель"]):
        return "stock", "point"
    if any(w in name_l for w in ["выдач", "объём", "объем", "количество", "сделк", "введено", "выдано", "числ"]):
        return "flow", "cumulative"
    # AC1: монотонно растущий с AC1>0.98 — вероятный stock
    s = s.dropna().astype(float)
    if len(s) >= 24:
        ac = acf(s, nlags=1, fft=True)[1]
        if ac > 0.985 and s.diff().dropna().ge(0).mean() > 0.9:
            return "stock", "point"
    return None, None


def hierarchy_from_name(name: str, code: str):
    """КЭП-номер из имени ('1.1.1 …'), глубина; [подтаблица N]."""
    import re
    m = re.match(r"^(\d+(?:\.\d+)+)\s", name or "")
    parent = depth = None
    if m:
        parts = m.group(1).split(".")
        depth = len(parts)
        if depth > 1:
            parent = ".".join(parts[:-1])
    return parent, depth


def enrich_one(mid, code, name, tags, fid, obs, conn):
    freq = FREQ.get(fid, "m")
    df = pd.DataFrame(obs, columns=["period", "value"])
    df["period"] = pd.PeriodIndex(df["period"], freq=PERIOD_FREQ[freq])
    s = df.set_index("period")["value"].astype(float)

    values = s.dropna()
    if len(values) < 3:
        return None

    flow_stock, value_kind = flow_stock_heuristic(s, name, freq)
    parent, depth = hierarchy_from_name(name, code)

    # stationarity
    stat = series_char(s, freq)

    # transforms: diff/log/yoy/z-score/MA/SAR/3MMA/3SAAR
    tr = {}
    def tstat(t):
        t = t.dropna()
        if len(t) < 12:
            return None
        return {"n": int(len(t)), "adf": adf_p(t), "ac1": float(acf(t, nlags=1, fft=True)[1])}
    tr["diff"] = tstat(s.diff())
    pos = s[s > 0]
    if len(pos) >= 12:
        tr["log"] = tstat(np.log(pos))
    if len(s) >= 25:
        tr["yoy"] = tstat(s / s.shift(12 if freq == "m" else 4) - 1)
    z = (s - s.mean()) / s.std()
    tr["zscore"] = {"range": [float(z.min()), float(z.max())]}
    # MA
    for w in (3, 6, 12):
        if len(s) >= w + 6:
            tr[f"ma{w}"] = ma_profile(s, w)
    # SAR + 3MMA + 3SAAR
    sar = sar_profile(s, freq)
    if sar:
        tr["sar"] = sar
    tr["mma"] = mma_saar(s, freq)
    smoothed = [k for k, v in tr.items() if v]
    mma_d = tr.get("mma") or {}
    if "saar_cv" in mma_d:
        tr["saar"] = {"cv": mma_d["saar_cv"], "ac1": mma_d["saar_ac1"], "adf": mma_d["saar_adf"]}
    if "sa_ac1" in mma_d:
        tr["sa"] = {"adf_level": mma_d["sa_adf_level"], "ac1": mma_d["sa_ac1"]}

    # quality flags
    flags = {}
    if len(values) >= 12 and values.nunique() <= 3:
        flags["const_like"] = True
    last = s.index.max()
    if (last.year if hasattr(last, "year") else int(str(last)[:4])) < 2024:
        flags["dead"] = True
    if len(values) < 12:
        flags["short"] = True

    return {
        "metric_id": mid,
        "flow_stock": flow_stock,
        "value_kind": value_kind,
        "frequency_native": fid,
        "hierarchy_parent": parent,
        "hierarchy_depth": depth,
        "econ_group": None,  # шаг 2 (LLM)
        "econ_tags": None,
        "stat_profile": psycopg2.extras.Json(_clean({
            "cv": stat.get("cv"), "ac1": stat.get("ac1"), "n": stat.get("n"),
        })),
        "transforms": psycopg2.extras.Json(_clean(tr)),
        "stationarity": psycopg2.extras.Json(_clean({
            "adf_level": stat.get("adf_level"), "adf_diff": stat.get("adf_diff"),
            "kpss_level": stat.get("kpss_level"),
        })),
        "sa_method": "STL" if sar else None,
        "seasonal_amplitude": sar.get("amplitude") if sar else None,
        "sma_signal_ratio": (tr.get("ma3") or {}).get("corr_raw"),
        "smoothed_available": [k for k in ("ma3", "ma6", "ma12", "sar", "mma", "saar") if tr.get(k)],
        "quality_flags": psycopg2.extras.Json(flags),
        "ai_model": "stat_only",
        "ai_confidence": 0.5,
    }


def upsert_rows(conn, rows):
    with conn.cursor() as cur:
        psycopg2.extras.execute_batch(cur, """
            INSERT INTO derived.metric_enrichment
              (metric_id, flow_stock, value_kind, frequency_native, hierarchy_parent,
               hierarchy_depth, econ_group, econ_tags, stat_profile, transforms,
               stationarity, sa_method, seasonal_amplitude, sma_signal_ratio,
               smoothed_available, quality_flags, ai_model, ai_confidence)
            VALUES (%(metric_id)s,%(flow_stock)s,%(value_kind)s,%(frequency_native)s,
                    %(hierarchy_parent)s,%(hierarchy_depth)s,%(econ_group)s,%(econ_tags)s,
                    %(stat_profile)s,%(transforms)s,%(stationarity)s,%(sa_method)s,
                    %(seasonal_amplitude)s,%(sma_signal_ratio)s,%(smoothed_available)s,
                    %(quality_flags)s,%(ai_model)s,%(ai_confidence)s)
            ON CONFLICT (metric_id) DO UPDATE SET
              flow_stock=EXCLUDED.flow_stock, value_kind=EXCLUDED.value_kind,
              frequency_native=EXCLUDED.frequency_native,
              hierarchy_parent=EXCLUDED.hierarchy_parent,
              hierarchy_depth=EXCLUDED.hierarchy_depth,
              stat_profile=EXCLUDED.stat_profile, transforms=EXCLUDED.transforms,
              stationarity=EXCLUDED.stationarity, sa_method=EXCLUDED.sa_method,
              seasonal_amplitude=EXCLUDED.seasonal_amplitude,
              sma_signal_ratio=EXCLUDED.sma_signal_ratio,
              smoothed_available=EXCLUDED.smoothed_available,
              quality_flags=EXCLUDED.quality_flags,
              ai_model=EXCLUDED.ai_model, ai_confidence=EXCLUDED.ai_confidence,
              enriched_at=now()
        """, rows, page_size=200)
    conn.commit()


def main():
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    conn = psycopg2.connect(
        host=os.environ.get("PGHOST", "127.0.0.1"),
        port=int(os.environ.get("PGPORT", "5432")),
        user=os.environ.get("PGUSER", "wiki"),
        dbname=os.environ.get("PGDATABASE", "research_wiki"),
    )
    by_metric = load_series(conn, limit=limit)
    done = 0
    errors = 0
    batch = []
    for (mid, code, name, tags, fid), obs in by_metric.items():
        try:
            row = enrich_one(mid, code, name, tags, fid, obs, conn)
            if row:
                batch.append(row)
                done += 1
            if len(batch) >= 500:
                upsert_rows(conn, batch)
                batch = []
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"ERR {code}: {e}", file=sys.stderr)
    if batch:
        upsert_rows(conn, batch)
    print(f"enriched={done} errors={errors}")


if __name__ == "__main__":
    main()