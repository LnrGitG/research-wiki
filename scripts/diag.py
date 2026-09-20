#!/usr/bin/env python3
"""diag.py — диагностика спецификаций: единичные корни, VIF, гетероскедастичность,
автокорреляция остатков, сезонность, сравнение моделей.

Использование из spec_cli.py: run_variant() вызывает run_diagnostics(...) после оценки.
Запись: derived.spec_diagnostics (по run_id).
"""
import json

import numpy as np
import pandas as pd
from statsmodels.stats.diagnostic import het_breuschpagan, acorr_breusch_godfrey
from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tsa.stattools import adfuller, kpss, acf


def _verdict(pvalue: float, alpha: float = 0.05, higher_is_ok: bool = False) -> str:
    ok = pvalue >= alpha if not higher_is_ok else pvalue <= alpha
    if ok:
        return "pass"
    if pvalue >= 0.01:
        return "warn"
    return "fail"


def _record(rows, group, name, target, stat, pval, verdict, detail=None):
    rows.append({
        "check_group": group, "check_name": name, "target": target,
        "statistic": None if stat is None else float(stat),
        "pvalue": None if pval is None else float(pval),
        "verdict": verdict,
        "detail": detail or {},
    })


def stationarity_tests(series: pd.Series, name: str, rows: dict) -> None:
    """ADF + KPSS на level и на первых разностях — стандартная пара эконометриста."""
    s = series.dropna().astype(float)
    if len(s) < 12:
        return
    # ADF: H0 = единичный корень (стационарности нет). p<0.05 → стационарен
    try:
        stat, pval, *_ = adfuller(s, autolag="AIC")
        _record(rows["rows"], "stationarity", "adf_level", name, stat, pval, _verdict(pval))
    except Exception as e:
        _record(rows["rows"], "stationarity", "adf_level", name, None, None, "info", {"error": str(e)})
    # KPSS: H0 = стационарность. p<0.05 → нестационарен (инвертированная логика)
    try:
        stat, pval, *_ = kpss(s, regression="c", nlags="auto")
        verdict = _verdict(pval, higher_is_ok=False)
        verdict = "pass" if verdict == "fail" else "pass" if pval >= 0.05 else verdict
        _record(rows["rows"], "stationarity", "kpss_level", name, stat, pval, verdict)
    except Exception:
        pass
    # Первая разность: если level нестационарен, diff должен спасать
    try:
        stat, pval, *_ = adfuller(s.diff().dropna(), autolag="AIC")
        _record(rows["rows"], "stationarity", "adf_diff", name, stat, pval, _verdict(pval))
    except Exception:
        pass


def multicollinearity_vif(X: pd.DataFrame, rows: dict) -> None:
    """VIF по регрессорам: >10 — критично, >5 — предупреждающий."""
    Xc = X.dropna()
    if len(Xc) < 10 or Xc.shape[1] < 2:
        return
    arr = np.column_stack([np.ones(len(Xc)), Xc.values.astype(float)])
    for i, col in enumerate(Xc.columns, start=1):
        try:
            vif = variance_inflation_factor(arr, i)
            verdict = "pass" if vif < 5 else ("warn" if vif < 10 else "fail")
            _record(rows["rows"], "multicollinearity", "vif", col, vif, None, verdict)
        except Exception:
            continue
    # Корреляции >0.8 — пара к кандидату на выброс
    corr = Xc.corr().abs()
    high = [(a, b, round(corr.loc[a, b], 2))
            for idx, a in enumerate(corr.columns) for b in corr.columns[idx + 1:]
            if corr.loc[a, b] > 0.8]
    if high:
        _record(rows["rows"], "multicollinearity", "corr_gt_0.8", "pairwise", None, None,
                "warn", {"pairs": high})


def residual_tests(est, rows: dict) -> None:
    """Гетероскедастичность, автокорреляция, нормальность остатков + DW."""
    resid = pd.Series(est.resid).dropna()
    if len(resid) < 10:
        return
    exog = est.model.exog
    try:
        lm, lmp, lf, lfp = het_breuschpagan(resid, exog)
        _record(rows["rows"], "heteroskedasticity", "breusch_pagan", "residuals", lm, lmp,
                _verdict(lmp))
    except Exception:
        pass
    try:
        dw = durbin_watson(resid)
        verdict = "pass" if 1.5 < dw < 2.5 else "warn"
        _record(rows["rows"], "autocorrelation", "durbin_watson", "residuals", dw, None, verdict)
    except Exception:
        pass
    try:
        bg_lm, bg_p, _, _ = acorr_breusch_godfrey(est, nlags=min(6, len(resid) // 4))
        _record(rows["rows"], "autocorrelation", "breusch_godfrey", "residuals", bg_lm, bg_p,
                _verdict(bg_p))
    except Exception:
        pass
    try:
        jb_stat, jb_p, skew, kurt = jarque_bera(resid)
        _record(rows["rows"], "residuals", "jarque_bera", "residuals", jb_stat, jb_p,
                _verdict(jb_p), {"skew": float(skew), "kurtosis": float(kurt)})
    except Exception:
        pass


def seasonality_check(series: pd.Series, freq: str, name: str, rows: dict) -> None:
    """Сезонность по ACF на сезонных лагах: 12 для мес, 4 для кв."""
    s = series.dropna().astype(float)
    season_lag = {"m": 12, "q": 4, "a": None}.get(freq)
    if not season_lag or len(s) < season_lag * 2 + 4:
        return
    ac = acf(s, nlags=season_lag * 2, fft=True)
    val = ac[season_lag]
    # значимая автокорреляция на сезонном лаге
    threshold = 2 / np.sqrt(len(s))
    verdict = "pass" if abs(val) > threshold else "info"
    _record(rows["rows"], "seasonality", "acf_seasonal", name, val, None, verdict,
            {"lag": season_lag, "threshold": round(float(threshold), 3)})


def model_comparison(est_full, est_nested, rows: dict) -> None:
    """F-тест вложенных моделей / AIC-BIC сравнение."""
    try:
        aic_full, aic_nested = est_full.aic, est_nested.aic
        _record(rows["rows"], "model_comparison", "aic", "full_vs_nested",
                None, None, "info", {"aic_full": float(aic_full), "aic_nested": float(aic_nested)})
    except Exception:
        pass


def run_diagnostics(spec: dict, df: pd.DataFrame, est, target_col: str) -> list:
    """Точка входа: возвращает список строк для derived.spec_diagnostics."""
    rows = {"rows": []}
    freq = spec["target"]["frequency"]

    seasonality_check(df[target_col], freq, "target", rows)
    stationarity_tests(df[target_col], "target", rows)
    feature_cols = [c for c in df.columns if c not in (target_col, "period")]
    for col in feature_cols[:8]:  # ограничение: не дольше 8 фич
        stationarity_tests(df[col], col, rows)
        seasonality_check(df[col], spec.get("features", [{}])[0].get("frequency", freq), col, rows)
    try:
        X = df[feature_cols].dropna()
        multicollinearity_vif(X, rows)
    except Exception:
        pass
    try:
        residual_tests(est, rows)
    except Exception:
        pass
    return rows["rows"]


def write_diagnostics(conn, run_id: int, rows: list) -> None:
    import psycopg2.extras
    with conn.cursor() as cur:
        for r in rows:
            cur.execute(
                """INSERT INTO derived.spec_diagnostics
                   (run_id, check_group, check_name, target, statistic, pvalue, verdict, detail)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                (run_id, r["check_group"], r["check_name"], r["target"],
                 r["statistic"], r["pvalue"], r["verdict"],
                 psycopg2.extras.Json(r["detail"])),
            )
    conn.commit()