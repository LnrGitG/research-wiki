#!/usr/bin/env python3
"""Проверка гипотезы блокировки (lock-in) на российских данных research_wiki.

Гипотеза: при сжатии объёма сделок с жильём прирост цен ускоряется, то есть
коэффициент при приросте объёма в уравнении прироста цен отрицателен.

Данные:
  * 1099 — Росстат, цена 1 кв. м жилья, квартальная, РФ (region_id=1),
    рынки primary/secondary, 2016Q1–2026Q2;
  * 71937 — ЦБ, жилищные кредиты, шт., месячный региональный разрез
    (80 регионов), сумма по регионам как национальный прокси объёма,
    2019-01–2026-08;
  * 74626/74627 — ЦБ, средняя цена 1 кв. м, первичный/вторичный рынок по
    регионам, 2025Q1–2026Q2 (только для вспомогательного среза).

Все выборки дедуплицируются по (metric_id, region_id, period_start) —
в data.observation встречаются дубли релизов.

Запуск:
  /home/lnr/.hermes/hermes-agent/venv/bin/python3 \
      ~/research-wiki-private/scripts/lockin_check_ru.py

Вывод: JSON в stdout и в queries/lockin-effect-ru-2026-10.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_tunnel import query_dict  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT_JSON = REPO / "queries" / "lockin-effect-ru-2026-10.json"

PRICE_METRIC = 1099
LOANS_METRIC = 71937
PRICE_PRIMARY_REG = 74626
PRICE_SECONDARY_REG = 74627
MIN_REGIONS = 80


def fetch(sql: str) -> pd.DataFrame:
    rows = query_dict(sql)
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    for col in ("value", "observation_id", "region_id", "metric_id"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in ("period_start",):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])
    return df


def national_prices() -> pd.DataFrame:
    df = fetch(
        f"""
        SELECT observation_id, metric_id, region_id, period_start, sub_dimension, value
        FROM data.observation
        WHERE metric_id = {PRICE_METRIC} AND region_id = 1
          AND sub_dimension LIKE 'market: %'
        """
    )
    if df.empty:
        raise SystemExit("нет данных по метрике 1099")
    df = (
        df.sort_values("observation_id", ascending=False)
        .drop_duplicates(["metric_id", "region_id", "sub_dimension", "period_start"])
        .sort_values("period_start")
    )
    df["market"] = np.where(
        df["sub_dimension"].str.contains("primary"), "primary", "secondary"
    )
    wide = df.pivot_table(index="period_start", columns="market", values="value", aggfunc="first")
    wide = wide.asfreq("QS") if isinstance(wide.index, pd.DatetimeIndex) else wide
    return wide


def quarterly_loans() -> tuple[pd.Series, pd.Series]:
    df = fetch(
        f"""
        SELECT observation_id, metric_id, region_id, period_start, value
        FROM data.observation
        WHERE metric_id = {LOANS_METRIC}
        """
    )
    if df.empty:
        raise SystemExit("нет данных по метрике 71937")
    df = (
        df.sort_values("observation_id", ascending=False)
        .drop_duplicates(["metric_id", "region_id", "period_start"])
    )
    df["quarter"] = df["period_start"].dt.to_period("Q").dt.start_time
    per_region = df.groupby(["region_id", "quarter"])["value"].sum().reset_index()
    coverage = per_region.groupby("quarter")["region_id"].nunique()
    total = per_region.groupby("quarter")["value"].sum()
    return total, coverage


def yoy(series: pd.Series, periods: int = 4) -> pd.Series:
    return (series / series.shift(periods) - 1.0) * 100.0


def ols_hac(y: pd.Series, X: pd.DataFrame, maxlag: int = 4):
    X = sm.add_constant(X.astype(float))
    model = sm.OLS(y.astype(float), X).fit(cov_type="HAC", cov_kwds={"maxlags": maxlag})
    return model


def spec_lagged(name: str, price_yoy: pd.Series, vol_yoy: pd.Series,
                start: str, end: str) -> dict:
    """Прирост цен против объёма с лагом 1 и 2 квартала: проверка направления."""
    df = pd.concat({"price": price_yoy, "volume": vol_yoy}, axis=1, join="inner").dropna()
    df = df.loc[start:end].copy()
    df["vol_l1"] = df["volume"].shift(1)
    df["vol_l2"] = df["volume"].shift(2)
    df = df.dropna()
    if len(df) < 12:
        return {"spec": name, "error": "слишком короткая выборка", "n": int(len(df))}
    model = ols_hac(df["price"], df[["vol_l1", "vol_l2"]])
    return {
        "spec": name,
        "n": int(len(df)),
        "period": [str(df.index.min().date()), str(df.index.max().date())],
        "coef_vol_l1": round(float(model.params["vol_l1"]), 4),
        "p_vol_l1": round(float(model.pvalues["vol_l1"]), 4),
        "coef_vol_l2": round(float(model.params["vol_l2"]), 4),
        "p_vol_l2": round(float(model.pvalues["vol_l2"]), 4),
        "r2": round(float(model.rsquared), 4),
    }


def spec_national(name: str, price_yoy: pd.Series, vol_yoy: pd.Series,
                  start: str, end: str) -> dict:
    df = pd.concat({"price": price_yoy, "volume": vol_yoy}, axis=1, join="inner").dropna()
    df = df.loc[start:end].copy()
    if len(df) < 12:
        return {"spec": name, "error": "слишком короткая выборка", "n": int(len(df))}
    df["trend"] = np.arange(len(df), dtype=float) / 4.0
    for q in range(2, 5):
        df[f"q{q}"] = (df.index.quarter == q).astype(float)
    model = ols_hac(df["price"], df[["volume", "trend", "q2", "q3", "q4"]])
    return {
        "spec": name,
        "n": int(len(df)),
        "period": [str(df.index.min().date()), str(df.index.max().date())],
        "coef_volume": round(float(model.params["volume"]), 4),
        "se_volume": round(float(model.bse["volume"]), 4),
        "p_volume": round(float(model.pvalues["volume"]), 4),
        "ci95_volume": [round(float(v), 4) for v in model.conf_int().loc["volume"]],
        "coef_trend": round(float(model.params["trend"]), 4),
        "p_trend": round(float(model.pvalues["trend"]), 4),
        "r2": round(float(model.rsquared), 4),
        "se_type": "HAC (Newey-West), maxlag=4",
    }


def spec_simple(name: str, price_yoy: pd.Series, vol_yoy: pd.Series,
                start: str, end: str) -> dict:
    df = pd.concat({"price": price_yoy, "volume": vol_yoy}, axis=1, join="inner").dropna()
    df = df.loc[start:end]
    if len(df) < 6:
        return {"spec": name, "error": "слишком короткая выборка", "n": int(len(df))}
    model = ols_hac(df["price"], df[["volume"]], maxlag=4)
    r = float(np.corrcoef(df["price"], df["volume"])[0, 1])
    return {
        "spec": name,
        "n": int(len(df)),
        "period": [str(df.index.min().date()), str(df.index.max().date())],
        "corr": round(r, 4),
        "coef_volume": round(float(model.params["volume"]), 4),
        "se_volume": round(float(model.bse["volume"]), 4),
        "p_volume": round(float(model.pvalues["volume"]), 4),
        "r2": round(float(model.rsquared), 4),
    }


def regional_crosscheck() -> dict:
    price = fetch(
        f"""
        SELECT observation_id, metric_id, region_id, period_start, value
        FROM data.observation
        WHERE metric_id IN ({PRICE_PRIMARY_REG}, {PRICE_SECONDARY_REG})
        """
    )
    loans = fetch(
        f"""
        SELECT observation_id, metric_id, region_id, period_start, value
        FROM data.observation
        WHERE metric_id = {LOANS_METRIC} AND period_start >= '2025-01-01'
        """
    )
    if price.empty or loans.empty:
        return {"error": "нет данных для регионального среза"}
    price = (
        price.sort_values("observation_id", ascending=False)
        .drop_duplicates(["metric_id", "region_id", "period_start"])
    )
    price["quarter"] = price["period_start"].dt.to_period("Q").dt.start_time
    loans = (
        loans.sort_values("observation_id", ascending=False)
        .drop_duplicates(["metric_id", "region_id", "period_start"])
    )
    loans["quarter"] = loans["period_start"].dt.to_period("Q").dt.start_time
    vol = loans.groupby(["region_id", "quarter"])["value"].sum().rename("volume")
    out = {}
    for mid, label in ((PRICE_PRIMARY_REG, "primary"), (PRICE_SECONDARY_REG, "secondary")):
        sub = price[price["metric_id"] == mid].set_index(["region_id", "quarter"])["value"]
        df = pd.concat([sub.rename("price"), vol], axis=1, join="inner").reset_index()
        df = df.sort_values(["region_id", "quarter"])
        df["price_yoy"] = df.groupby("region_id")["price"].pct_change(4) * 100
        df["vol_yoy"] = df.groupby("region_id")["volume"].pct_change(4) * 100
        d = df.dropna(subset=["price_yoy", "vol_yoy"])
        out[label] = {
            "n": int(len(d)),
            "regions": int(d["region_id"].nunique()),
            "quarters": [str(q.date()) for q in sorted(d["quarter"].unique())],
            "corr": round(float(d["price_yoy"].corr(d["vol_yoy"])), 4) if len(d) > 2 else None,
        }
    return out


def main() -> None:
    prices = national_prices()
    loans, coverage = quarterly_loans()

    price_primary_yoy = yoy(prices["primary"]).dropna()
    price_secondary_yoy = yoy(prices["secondary"]).dropna()
    vol_yoy = yoy(loans).dropna()

    valid_quarters = coverage[coverage >= MIN_REGIONS].index
    vol_yoy = vol_yoy[vol_yoy.index.isin(valid_quarters)]

    result = {
        "hypothesis": "сжатие объёма сделок ускоряет прирост цен (коэффициент при объёме < 0)",
        "data": {
            "price_metric": PRICE_METRIC,
            "volume_metric": LOANS_METRIC,
            "volume_proxy_note": "число жилищных кредитов включает рефинансирование и не равно числу сделок",
            "coverage_regions_min": int(coverage.min()),
            "coverage_regions_max": int(coverage.max()),
            "quarters_with_full_coverage": int(len(valid_quarters)),
        },
        "series_tail": {
            "price_primary_yoy": {str(k.date()): round(float(v), 2) for k, v in price_primary_yoy.tail(10).items()},
            "volume_yoy": {str(k.date()): round(float(v), 2) for k, v in vol_yoy.tail(10).items()},
        },
        "specs": [
            spec_national("primary ~ volume + trend + quarter dummies", price_primary_yoy, vol_yoy,
                          "2019-01-01", "2026-06-30"),
            spec_national("secondary ~ volume + trend + quarter dummies", price_secondary_yoy, vol_yoy,
                          "2019-01-01", "2026-06-30"),
            spec_simple("primary ~ volume (простая, 2023Q1–2026Q2)", price_primary_yoy, vol_yoy,
                        "2023-01-01", "2026-06-30"),
            spec_national("primary ~ volume + trend + сезонность, 2020Q1–2022Q4 (до шока ставки)",
                          price_primary_yoy, vol_yoy, "2020-01-01", "2022-12-31"),
            spec_national("primary ~ volume + trend + сезонность, 2024Q3–2026Q2 (после массовой льготной)",
                          price_primary_yoy, vol_yoy, "2024-07-01", "2026-06-30"),
            spec_lagged("primary ~ volume с лагами 1 и 2 квартала, 2020Q1–2026Q2",
                        price_primary_yoy, vol_yoy, "2020-01-01", "2026-06-30"),
        ],
        "regional_crosscheck": regional_crosscheck(),
        "limitations": [
            "число кредитов включает рефинансирование и не равно числу сделок",
            "ряд объёма до 2023 года неполон по покрытию регионов",
            "эффект субсидированных программ не отделён",
            "метрика ДДУ ДОМ.РФ (73072) непригодна без переинжеста",
        ],
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
