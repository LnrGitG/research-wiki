#!/usr/bin/env python3
"""H-001: наивный бенчмарк для nowcasting-а г SMR по композиту Wordstat.

Зачем: H-001 заявляет r=+0.618 (lead-1m, n=19) между композитом S2-S5 и yoy ИФО
СМР. Корреляция в уровнях не является мерой качества прогноза: yoy-ряд сильно
персистентен, поэтому перенос последнего наблюдения может объяснять большую
часть этой корреляции. Скрипт считает OOS-ошибки (MAE, RMSE) и направленную
точность для набора тривиальных и простых моделей на том же окне оценки.

Дизайн:
  * композит месяца t известен в момент t, цель — yoy СМР месяца t+1;
  * окно оценки: цели 2025-02..2026-08 (n=19), то же, что в перекате 01.10.2026;
  * все параметрические модели оцениваются расширяющимся окном (expanding),
    только на данных до t включительно — без заглядывания вперёд;
  * ряд yoy СМР: metric_id 56209 (kep1_7_y2, КЭП 1.7, канонический по
    scripts/metric_registry.py), месячный, % к соответствующему месяцу
    прошлого года (100 = прошлый год).

Модели:
  naive        y_hat = y_t                       (случайное блуждание в уровне)
  seasonal     y_hat = y_{t-11}                  (сезонно-наивная, лаг 12 мес)
  mean3        y_hat = среднее y за t-2..t
  ar1          y_{t+1} = a + b*y_t
  ar2          y_{t+1} = a + b1*y_t + b2*y_{t-1}
  comp         y_{t+1} = a + b*comp_t            (спецификация корреляции H-001)
  comp_ar      y_{t+1} = a + b*y_t + c*comp_t    (композит поверх персистентности)
  delta        dy_{t+1} = a + b*comp_t           (прогноз изменения, не уровня)

Метрики: MAE, RMSE, Theil U (RMSE модели / RMSE naive), направленная точность
(DA — доля верно угаданных знаков изменения y), корреляция прогноза с фактом.

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 scripts/h001_naive_benchmark.py
"""
import csv
import json
import os
import statistics
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as dbt

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(REPO, "data", "wordstat_weekly_construction.csv")
OUT = os.path.join(REPO, "data", "h001_naive_benchmark.json")
S25 = {"S2_mat", "S3_mach", "S4_b2b", "S4_procure", "S5_permits"}
SMR_METRIC = 56209
EVAL_LO, EVAL_HI = "2025-02", "2026-08"
MIN_TRAIN = 24


def load_composite_monthly(path):
    byweek = defaultdict(lambda: defaultdict(float))
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            byweek[r["date"].strip()][r["group"].strip()] += float(r["share"])
    bm = defaultdict(list)
    for d, g in byweek.items():
        bm[d[:7]].append(sum(g.get(k, 0.0) for k in S25))
    return {k: statistics.fmean(v) for k, v in bm.items()}


def load_smr():
    rows = dbt.query(
        "SELECT period_start, value FROM data.observation "
        "WHERE metric_id=%s ORDER BY period_start", (SMR_METRIC,))
    out = {}
    for p, v in rows:
        out[str(p)[:7]] = float(v)          # дубли релизов: последний побеждает
    return out


def month_shift(ym, k):
    y, m = int(ym[:4]), int(ym[5:7])
    m += k
    while m > 12:
        m -= 12
        y += 1
    while m < 1:
        m += 12
        y -= 1
    return f"{y:04d}-{m:02d}"


def ols(features, target, x):
    """МНК через нормальные уравнения; features — список списков."""
    k = len(features[0])
    XtX = [[sum(f[i] * f[j] for f in features) for j in range(k)] for i in range(k)]
    Xty = [sum(f[i] * t for f, t in zip(features, target)) for i in range(k)]
    # Гаусс с выбором ведущего элемента
    A = [row[:] + [Xty[i]] for i, row in enumerate(XtX)]
    for col in range(k):
        piv = max(range(col, k), key=lambda r: abs(A[r][col]))
        if abs(A[piv][col]) < 1e-12:
            return None
        A[col], A[piv] = A[piv], A[col]
        for r in range(k):
            if r != col:
                f = A[r][col] / A[col][col]
                for c in range(col, k + 1):
                    A[r][c] -= f * A[col][c]
    beta = [A[i][k] / A[i][i] for i in range(k)]
    return sum(b * xi for b, xi in zip(beta, x))


def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return float("nan")
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den = (sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys)) ** 0.5
    return num / den if den else float("nan")


def metrics(fc, act, base):
    err = [f - a for f, a in zip(fc, act)]
    mae = statistics.fmean(abs(e) for e in err)
    rmse = (statistics.fmean(e * e for e in err)) ** 0.5
    base_rmse = (statistics.fmean((b - a) ** 2 for b, a in zip(base, act))) ** 0.5
    da = statistics.fmean(
        1.0 if (f - b) * (a - b) > 0 else (0.0 if (f - b) * (a - b) < 0 else 0.5)
        for f, a, b in zip(fc, act, base))
    return {"mae": round(mae, 4), "rmse": round(rmse, 4),
            "theil_u": round(rmse / base_rmse, 3) if base_rmse else None,
            "da": round(da, 3), "corr": round(pearson(fc, act), 3)}


def main():
    comp = load_composite_monthly(CSV)
    smr = load_smr()
    months = sorted(m for m in comp if m in smr)          # месяцы с композитом и фактом
    pairs = [(m, month_shift(m, 1)) for m in months if month_shift(m, 1) in smr]
    print(f"композит: {len(comp)} мес ({min(comp)}..{max(comp)}); "
          f"СМР: {len(smr)} мес ({min(smr)}..{max(smr)}); пар lead-1: {len(pairs)}")

    r_all = pearson([comp[t] for t, _ in pairs], [smr[t1] for _, t1 in pairs])
    print(f"корреляция композит/СМР на всём пересечении: r={r_all:+.4f}, n={len(pairs)}")

    results, detail = {}, []
    for t, t1 in pairs:
        if not (EVAL_LO <= t1 <= EVAL_HI):
            continue
        y_t, y_act = smr[t], smr[t1]
        hist = [smr[m] for m in months if m < t]          # строго до t
        if len(hist) < MIN_TRAIN:
            continue
        f = {"naive": y_t}
        prev12 = month_shift(t, -11)
        f["seasonal"] = smr.get(prev12)
        f["mean3"] = statistics.fmean(hist[-3:])
        # expanding OLS на парах (предиктор s -> y_{s+1}), s < t
        tr = [(m, month_shift(m, 1)) for m in months
              if m < t and month_shift(m, 1) in smr and month_shift(m, 1) <= t]
        tr = tr[-(len(tr)):]
        if len(tr) >= MIN_TRAIN:
            y_tr = [smr[b] for _, b in tr]
            f["ar1"] = ols([[smr[a]] for a, _ in tr], y_tr, [y_t])
            f["ar2"] = ols([[smr[a], smr.get(month_shift(a, -1), 0.0)] for a, _ in tr],
                           y_tr, [y_t, smr.get(month_shift(t, -1), 0.0)])
            f["comp"] = ols([[comp[a]] for a, _ in tr], y_tr, [comp[t]])
            f["comp_ar"] = ols([[smr[a], comp[a]] for a, _ in tr], y_tr, [y_t, comp[t]])
            dy = [smr[b] - smr[a] for a, b in tr]
            f["delta"] = y_t + (ols([[comp[a]] for a, _ in tr], dy, [comp[t]]) or 0.0)
        detail.append({"from": t, "target": t1, "actual": y_act, **f})

    act = [d["actual"] for d in detail]
    base = [d["naive"] for d in detail]
    for name in ["naive", "seasonal", "mean3", "ar1", "ar2", "comp", "comp_ar", "delta"]:
        vals = [d[name] for d in detail if d.get(name) is not None]
        if len(vals) == len(detail) and len(detail) >= 6:
            results[name] = metrics(vals, act, base)

    print(f"\nокно оценки: цели {EVAL_LO}..{EVAL_HI}, n={len(detail)}")
    print(f"{'модель':<10}{'MAE':>7}{'RMSE':>8}{'TheilU':>8}{'DA':>7}{'corr':>7}")
    for k, v in sorted(results.items(), key=lambda kv: kv[1]["mae"]):
        print(f"{k:<10}{v['mae']:>7.3f}{v['rmse']:>8.3f}"
              f"{(v['theil_u'] if v['theil_u'] is not None else float('nan')):>8.2f}"
              f"{v['da']:>7.3f}{v['corr']:>7.3f}")

    # диагностика персистентности: сколько уровня объясняет перенос последнего значения
    lev = pearson([smr[t] for t, _ in pairs], [smr[t1] for _, t1 in pairs])
    d_comp = [comp[t1] - comp[t] for t, t1 in pairs]
    d_smr = [smr[t1] - smr[t] for t, t1 in pairs]
    print(f"\nперсистентность yoy СМР (y_t vs y_t+1): r={lev:+.4f}, n={len(pairs)}")
    print(f"корреляция Δкомпозит vs ΔСМР: r={pearson(d_comp, d_smr):+.4f}")

    # устойчивость корреляции: подпериоды и скользящее окно длины окна оценки
    print("\n-- корреляция по подпериодам --")
    sub = {}
    for lo, hi in [("2018-01", "2021-12"), ("2022-01", "2024-12"),
                   ("2025-01", "2025-12"), ("2026-01", "2026-07")]:
        xs = [comp[t] for t, _ in pairs if lo <= t <= hi]
        ys = [smr[t1] for t, t1 in pairs if lo <= t <= hi]
        if len(xs) >= 4:
            key = f"{lo}..{hi}"
            sub[key] = {"r": round(pearson(xs, ys), 3), "n": len(xs)}
            print(f"  {key}: r={sub[key]['r']:+.3f} n={len(xs)}")

    W = len(detail)
    roll = []
    for i in range(len(pairs) - W + 1):
        win = pairs[i:i + W]
        roll.append(pearson([comp[t] for t, _ in win], [smr[t1] for _, t1 in win]))
    roll_sorted = sorted(roll)
    share_above = sum(1 for r in roll if r >= 0.6) / len(roll)
    print(f"\n-- скользящее окно {W} мес ({len(roll)} окон) --")
    print(f"  медиана r={statistics.median(roll):+.3f}; "
          f"мин={roll_sorted[0]:+.3f}; макс={roll_sorted[-1]:+.3f}")
    print(f"  доля окон с r>=0.60: {share_above:.1%}; "
          f"с r<=0: {sum(1 for r in roll if r <= 0) / len(roll):.1%}")

    payload = {"eval_window": [EVAL_LO, EVAL_HI], "n_eval": len(detail),
               "subperiods": sub,
               "rolling": {"window": W, "n_windows": len(roll),
                           "median": round(statistics.median(roll), 3),
                           "min": round(roll_sorted[0], 3),
                           "max": round(roll_sorted[-1], 3),
                           "share_ge_060": round(share_above, 3)},
               "corr_full_overlap": round(r_all, 4), "n_full": len(pairs),
               "persistence_r": round(lev, 4),
               "corr_deltas": round(pearson(d_comp, d_smr), 4),
               "metrics": results, "detail": detail}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
    print(f"\nсохранено: {OUT}")


if __name__ == "__main__":
    main()
