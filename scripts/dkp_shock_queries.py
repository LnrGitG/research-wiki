# -*- coding: utf-8 -*-
"""Вариант A: шоки ДКП в цепочках графового слоя — семантика запросов.

Три метода идентификации поверх существующих рёбер (без DDL):
1. path_deviation — фактический шаг против объявленной траектории
   среднегодовой ключевой ставки последнего опорного прогноза
   (BRW-семантика, Bu et al. 2021).
2. jk_mix — информационная против чистой компоненты по распределению
   block×direction аргументов (Jarociński–Karadi 2020, AER).
3. sentiment_residual — остаток регрессии rate_delta на тональный
   профиль заседания (Aruoba–Drechsel 2024, AEJ:Macro).

Выход: таблица meeting-аннотаций + JSON для dkp_context.
"""
import json
import sys

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

# ---------------------------------------------------------------- метод 1
# path_deviation: для каждого решения сравниваем фактическую ставку
# со среднегодовой траекторией последнего ОПОРНОГО прогноза (is_pillar
# пуст в БД — используем графовый факт: forecast есть только у meeting
# 103; до появления прогнозов по прошлым раундам метод даёт аннотацию
# только для решений после 24.07.2026).
SQL_PATHDEV = """
WITH last_fc AS (
    SELECT f.meeting_id AS fc_meeting, f.horizon_year,
           COALESCE(f.value_point, (f.value_low + f.value_high) / 2) AS rate_mid,
           m2.meeting_date AS fc_date,
           ROW_NUMBER() OVER (PARTITION BY f.horizon_year ORDER BY m2.meeting_date DESC) AS rn
    FROM dkp.forecast f
    JOIN dkp.meeting m2 ON m2.meeting_id = f.meeting_id
    WHERE f.series_code = 'key_rate_avg' AND f.scenario = 'base'
),
dec AS (
    SELECT d.decision_id, d.meeting_id, m.meeting_date, d.rate_prev, d.rate_new,
           d.delta_bp, d.action
    FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
)
SELECT dec.decision_id, dec.meeting_date, dec.rate_prev, dec.rate_new, dec.delta_bp,
       fc.horizon_year, fc.rate_mid, fc.fc_date,
       ROUND((dec.rate_new - fc.rate_mid) * 100, 1) AS deviation_bp
FROM dec
JOIN last_fc fc ON fc.horizon_year = EXTRACT(YEAR FROM dec.meeting_date) AND fc.rn = 1
WHERE fc.fc_date < dec.meeting_date
ORDER BY dec.meeting_date
"""

# ---------------------------------------------------------------- метод 2
# jk_mix: чистый шок = аргументы о спросе/кредите при hawkish-перевесе;
# информационный = risk_infl/expectations при нейтрально-мягких фактах.
# Доля информационной компоненты = (risk_infl+inflation_expect+signal)
# против фактического блока (demand+credit+labour+output).
SQL_JK = """
SELECT d.decision_id, m.meeting_date, d.delta_bp, d.action,
    COUNT(*) FILTER (WHERE a.block IN ('demand','credit','labour','output','inflation_now')) AS fact_args,
    COUNT(*) FILTER (WHERE a.block IN ('risk_infl','inflation_expect','signal','transmission')) AS info_args,
    COUNT(*) FILTER (WHERE a.direction = 'hawkish') AS hawk,
    COUNT(*) FILTER (WHERE a.direction = 'dovish') AS dov,
    COUNT(*) FILTER (WHERE a.direction = 'neutral') AS neu,
    COUNT(*) AS total
FROM dkp.argument a
JOIN dkp.decision d USING (decision_id)
JOIN dkp.meeting m USING (meeting_id)
GROUP BY 1, 2, 3, 4
ORDER BY m.meeting_date
"""

# ---------------------------------------------------------------- метод 3
# sentiment_residual: OLS rate_delta ~ hawk_share; остаток = шок,
# не объяснённый коммуникацией. Без numpy (только stdlib) — формулы
# простой регрессии.
rows = query(SQL_JK)
xs, ys = [], []
for r in rows:
    total = r[9] or 0
    if total == 0:
        continue
    hawk_share = (r[6] or 0) / total
    xs.append(hawk_share)
    ys.append(float(r[2] or 0))

n = len(xs)
if n >= 3:
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    beta = sxy / sxx if sxx else 0.0
    alpha = my - beta * mx
    ss_res = sum((y - (alpha + beta * x)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys)
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
else:
    beta = alpha = r2 = 0.0

residuals = {r[1].isoformat(): round(float(r[2] or 0) - (alpha + beta * (r[6] or 0) / (r[9] or 1)), 1)
             for r in rows if (r[9] or 0) > 0}

# ---------------------------------------------------------------- отчёт
print("=" * 100)
print("МЕТОД 1: path_deviation (факт против траектории последнего прогноза)")
print("=" * 100)
for r in query(SQL_PATHDEV):
    did, md, prev, new, delta, hy, mid, fcdate, dev = r
    print(f"  {md} решение {did}: ставка {new} (шаг {delta:+d}) против траектории-{hy} "
          f"{mid} от {fcdate} → отклонение {dev:+.1f} б.п." if mid is not None else
          f"  {md} решение {did}: траектория-{hy} не задана (range)")

print()
print("=" * 100)
print("МЕТОД 2: jk_mix (информационная vs чистая компонента)")
print("=" * 100)
print(f"{'дата':<12}{'шаг':>6}{'факт':>6}{'инфо':>6}{'доля инфо':>10}{'hawk':>6}{'dov':>5}  интерпретация")
for r in query(SQL_JK):
    did, md, delta, action, fact, info, hawk, dov, neu, total = r
    info_share = info / (info + fact) if (info + fact) else 0
    if info_share >= 0.40:
        interp = "информационно-насыщенное (вес прогнозов/рисков)"
    elif hawk >= 2 * dov and delta > 0:
        interp = "чистый ужесточающий (факты при hawkish)"
    elif dov >= hawk and delta < 0:
        interp = "чистый смягчающий (факты при dovish)"
    elif hawk >= 2 * dov and delta == 0:
        interp = "ястребиная пауза (facts hawkish, шаг 0)"
    else:
        interp = "смешанный"
    print(f"{md}  {delta:+5d}  {fact:>5}  {info:>5}  {info_share:>9.2f}  {hawk:>5}  {dov:>4}  {interp}")

print()
print("=" * 100)
print(f"МЕТОД 3: sentiment_residual (OLS: delta_bp = {alpha:.1f} + {beta:.1f} × hawk_share; R² = {r2:.2f}, n = {n})")
print("=" * 100)
top = sorted(residuals.items(), key=lambda kv: abs(kv[1]), reverse=True)[:8]
for md, res in top:
    print(f"  {md}: остаток {res:+.1f} б.п.")

# JSON для dkp_context (в будущем шаг — интеграция)
out = {
    "path_deviation": [
        {"decision_id": r[0], "meeting_date": str(r[1]), "deviation_bp": float(r[8]),
         "horizon_year": int(r[5]), "forecast_date": str(r[7])}
        for r in query(SQL_PATHDEV)
    ],
    "jk_mix": [
        {"decision_id": r[0], "meeting_date": str(r[1]), "delta_bp": int(r[2]),
         "info_share": round(r[4] / r[9], 2) if r[9] else None}
        for r in query(SQL_JK)
    ],
    "sentiment_residual": residuals,
    "ols": {"alpha": round(alpha, 2), "beta": round(beta, 2)},
}
with open("/tmp/dkp_shock_annotations.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("\nJSON аннотаций: /tmp/dkp_shock_annotations.json")