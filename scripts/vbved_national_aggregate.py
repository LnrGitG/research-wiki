#!/usr/bin/env python3
"""H-VB-2, шаг 2: связь ВБВЭД с ипотекой на НАЦИОНАЛЬНОМ агрегате.

Строит два агрегата ВБВЭД по регионам (простой средний и взвешенный по ВРП-2024)
и сопоставляет их с общероссийскими выдачами ИЖК (регион 1) на месячных данных
2022-01..2026-08.

Проверки, которые различают реальный лаг и ложную связь на трендах:
  R1  уровни г/г: vb ~ izhk(k), HAC;
  R2  профиль лагов 0..9 по отдельности;
  R3  ADL (лаги зависимой + лаги ипотеки 0..6), HAC(12);
  R4  подпериоды 2022-2024 / 2023-2026;
  R5  регрессия с линейным трендом (M4-аналог);
  R6  CCF на ускорениях (первые разности г/г);
  R7  CCF после детренда обоих рядов;
  R8  ADF уровней и разностей;
  R9  стационарная зависимая: d(vb) ~ izhk(k) + d(vb)(-1).

Печатает числа, использованные в записке
queries/vbved-national-aggregate-20261025.md.

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 scripts/vbved_national_aggregate.py
"""
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from db_tunnel import available, query  # noqa: E402

VBVED = "vbved_reg_m"
IZHK = "cbr_izhk_volume_m"
GRP = "grp_level"


def hac(y, X, maxlags=6):
    df = pd.concat([y.rename("y"), X], axis=1).dropna()
    res = sm.OLS(df["y"], sm.add_constant(df[X.columns])).fit(
        cov_type="HAC", cov_kwds={"maxlags": maxlags})
    return res, len(df)


def ccf(a, b, maxk=9):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    n = len(a)
    out = []
    for k in range(-maxk, maxk + 1):
        if k >= 0:
            x, y = (a[: n - k], b[k:]) if k > 0 else (a, b)
        else:
            x, y = a[-k:], b[: n + k]
        ok = ~(np.isnan(x) | np.isnan(y))
        out.append((k, int(ok.sum()),
                    float(np.corrcoef(x[ok], y[ok])[0, 1]) if ok.sum() > 3 else np.nan))
    return pd.DataFrame(out, columns=["k", "n", "corr"])


def load():
    reg = query(f"""
        SELECT o.region_id, o.period_start, o.value, o.sub_dimension
        FROM data.observation o JOIN catalog.metric m ON m.metric_id = o.metric_id
        WHERE m.metric_code = '{VBVED}'
          AND o.observation_status IS DISTINCT FROM 'rejected'""")
    d = pd.DataFrame(reg, columns=["region_id", "period", "value", "sub"])
    d["period"] = pd.to_datetime(d["period"])
    d["value"] = d["value"].astype(float)
    # под метрикой лежат и месячные строки (sub IS NULL), и накопительные
    # ("накопительно: январь-август") — берём только месячный слой
    d = d[d["sub"].isna()]

    grp = query(f"""
        SELECT o.region_id, o.value FROM data.observation o
        JOIN catalog.metric m ON m.metric_id = o.metric_id
        JOIN catalog.region r ON r.region_id = o.region_id
        WHERE m.metric_code = '{GRP}' AND o.period_start = '2024-01-01'
          AND o.observation_status IS DISTINCT FROM 'rejected'
          AND r.name_ru NOT ILIKE '%федеральный округ%'
          AND r.name_ru NOT ILIKE '%Российская Федерация%'""")
    w = pd.DataFrame(grp, columns=["region_id", "grp"])
    w["grp"] = w["grp"].astype(float)

    iz = query(f"""
        SELECT o.period_start, o.value FROM data.observation o
        JOIN catalog.metric m ON m.metric_id = o.metric_id
        WHERE m.metric_code = '{IZHK}' AND o.region_id = 1
          AND o.observation_status IS DISTINCT FROM 'rejected'
        ORDER BY o.period_start""")
    dz = pd.DataFrame(iz, columns=["period", "vol"])
    dz["period"] = pd.to_datetime(dz["period"])
    dz["vol"] = dz["vol"].astype(float)

    return d, w, dz


def main():
    if not available():
        raise SystemExit("нет доступа к research_wiki (тоннель 15432)")

    d, w, dz = load()
    print(f"ВБВЭД: {len(d)} строк, {d.region_id.nunique()} регионов, "
          f"{d.period.nunique()} месяцев {d.period.min():%Y-%m}..{d.period.max():%Y-%m}")
    print(f"веса ВРП-2024: {len(w)} субъектов, сумма {w.grp.sum()/1e6:.1f} трлн руб.")

    ww = d.merge(w, on="region_id", how="left")
    agg = (ww.dropna(subset=["grp"]).groupby("period").apply(
        lambda x: pd.Series({"vb_simple": x["value"].mean(),
                             "vb_w": np.average(x["value"], weights=x["grp"])}),
        include_groups=False).reset_index())

    dz = dz.drop_duplicates("period", keep="last").set_index("period").asfreq("MS")
    dz["vol_yoy"] = 100 * dz["vol"] / dz["vol"].shift(12)

    m = agg.merge(dz[["vol_yoy"]].reset_index(), on="period", how="inner")
    m = m.dropna(subset=["vol_yoy"]).sort_values("period").reset_index(drop=True)
    m["vb_s"] = m["vb_simple"] - 100
    m["vb_w"] = m["vb_w"] - 100
    m["iz"] = m["vol_yoy"] - 100
    m["t"] = np.arange(len(m))
    print(f"выборка: n={len(m)}, {m.period.min():%Y-%m}..{m.period.max():%Y-%m}")

    print("\n=== R8: ADF ===")
    for c in ["vb_s", "vb_w", "iz"]:
        a, ad = adfuller(m[c].dropna(), autolag="AIC"), adfuller(m[c].diff().dropna(), autolag="AIC")
        print(f"  {c}: уровень {a[0]:+.2f} (p={a[1]:.3f}); разность {ad[0]:+.2f} (p={ad[1]:.3f})")

    print("\n=== R1: уровни, лаг 6, HAC(6) ===")
    for c in ["vb_s", "vb_w"]:
        r, n = hac(m[c], pd.DataFrame({"iz_l6": m["iz"].shift(6)}), 6)
        print(f"  {c}: b={r.params['iz_l6']:+.5f} (t={r.tvalues['iz_l6']:.2f}), "
              f"R2={r.rsquared:.3f}, n={n}")

    print("\n=== R2: профиль лагов 0..9 (HAC 6) ===")
    for c in ["vb_s", "vb_w"]:
        row = []
        for k in range(10):
            r, n = hac(m[c], pd.DataFrame({"x": m["iz"].shift(k)}), 6)
            row.append(f"k{k}:{r.params['x']:+.4f}(t{r.tvalues['x']:.1f})")
        print(f"  {c}: " + " ".join(row))

    print("\n=== R3: ADL лаги зависимой 1-2 + ипотека 0..6, HAC(12) ===")
    for c in ["vb_s", "vb_w"]:
        X = pd.DataFrame({"y_l1": m[c].shift(1), "y_l2": m[c].shift(2)})
        for k in range(7):
            X[f"iz_l{k}"] = m["iz"].shift(k)
        r, n = hac(m[c], X, 12)
        sig = {k: (round(r.params[f'iz_l{k}'], 5), round(r.tvalues[f'iz_l{k}'], 2))
               for k in range(7) if abs(r.tvalues[f'iz_l{k}']) > 1.96}
        print(f"  {c}: n={n}, R2={r.rsquared:.3f}, значимые лаги ипотеки: {sig}")

    print("\n=== R4: подпериоды, отдельные регрессии, HAC(6) ===")
    for lab, sub in [("2022-2024", m[m.period <= "2024-12-01"]),
                     ("2023-2026", m[m.period >= "2023-01-01"])]:
        cells = []
        for k in [0, 3, 5, 6, 9]:
            for c in ["vb_s", "vb_w"]:
                r, _ = hac(sub[c], pd.DataFrame({"x": sub["iz"].shift(k)}), 6)
                cells.append(f"{c[3:]}.k{k}:{r.params['x']:+.4f}(t{r.tvalues['x']:.1f})")
        print(f"  {lab} (n={len(sub)}): " + " ".join(cells))

    print("\n=== R5: с линейным трендом, HAC(6) ===")
    for c in ["vb_s", "vb_w"]:
        for k in [0, 3, 5, 6, 9]:
            X = pd.DataFrame({"x": m["iz"].shift(k), "trend": m["t"]})
            r, _ = hac(m[c], X, 6)
            print(f"  {c} k={k}: iz={r.params['x']:+.5f}(t={r.tvalues['x']:.2f}) "
                  f"тренд={r.params['trend']:+.4f}(t={r.tvalues['trend']:.2f})")

    print("\n=== R6: CCF на ускорениях d(yoy) ===")
    for c in ["vb_s", "vb_w"]:
        cc = ccf(m[c].diff(), m["iz"].diff())
        print(f"  {c}: " + " ".join(f"{r.k}:{r.corr:+.2f}" for r in cc.itertuples()))

    print("\n=== R7: детренд обоих, CCF остатков ===")
    def detr(s):
        b = np.polyfit(m["t"], s, 1)
        return s - np.polyval(b, m["t"])
    for c in ["vb_s", "vb_w"]:
        a, b = detr(m[c]), detr(m["iz"])
        cc = ccf(a, b)
        print(f"  {c}: " + " ".join(f"{r.k}:{r.corr:+.2f}" for r in cc.itertuples()))

    print("\n=== R9: стационарная зависимая d(vb) на izhk(k) + d(vb)(-1), HAC(6) ===")
    for c in ["vb_s", "vb_w"]:
        m["d_" + c] = m[c].diff()
        for k in [0, 3, 5, 6, 9]:
            X = pd.DataFrame({"iz": m["iz"].shift(k), "dy_l1": m["d_" + c].shift(1)})
            r, _ = hac(m["d_" + c], X, 6)
            print(f"  d_{c} k={k}: iz={r.params['iz']:+.5f}(t={r.tvalues['iz']:.2f}) "
                  f"dy_l1={r.params['dy_l1']:+.3f}(t={r.tvalues['dy_l1']:.1f})")

    print("\n=== контроль артефакта перекрытия yoy-окон ===")
    print(f"  corr(izhk_yoy_t, izhk_yoy_(t+12)) = "
          f"{np.corrcoef(m['iz'][:-12], m['iz'][12:])[0,1]:+.3f} (механический знаменатель)")
    print("\nсредние по годам (simple, iz):")
    print(m.assign(yr=m.period.dt.year).groupby("yr")[["vb_s", "iz"]].mean().round(2).to_string())


if __name__ == "__main__":
    main()
