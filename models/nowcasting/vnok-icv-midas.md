---
title: MIDAS ВНОК/ИКВ — nowcasting инвестиций в основной капитал
created: 2026-09-08
updated: 2026-09-08
type: model
model_class: MIDAS
status: draft
hypotheses: [H-007, H-008]
tags: [nowcasting, mixed-frequency, investment, ВНОК, ИКВ]
sources: [rosreestr_deals.db, cbr_lending.db, wordstat]
confidence: medium
---

# Nowcasting ИКВ/ВНОК: эскроу + материалы + фирменный блок

## Назначение
Квартальный nowcast yoy ИКВ/ВНОК до публикации Росстата. Гипотезы: [[hypotheses.yaml|H-007]] (эскроу lag2 ≥ 0.7) и [[hypotheses.yaml|H-008]] (firm-level блок +10% RMSE). Дизайн: [[queries/vnok-nowcasting-design|vnok-nowcasting-design]].

## Спецификация
- Целевая: yoy ВНОК IFO (SA, 56 кв. 2012+, основной), yoy ИКВ (25 кв., валидация/регионы)
- Блоки: эскроу-притоки (мес., lag2), цемент (мес.), зарплата стройки (мес.), Wordstat S6-B2B (нед., planned), РСБУ/IFRS-панель девелоперов (кв., planned)
- Спецификации: bridge (бенчмарк), MIDAS-Almon (основной), U-MIDAS (робаст), MF-VAR, DFM, structured ML (фирменный блок)
- Комбинация: Bates-Granger ансамбль; DM-тесты vs AR(1)

## Код и данные
- Код: planned — `scripts/nowcast_vnok_midas.py`; пилотные расчёты в queries/ikv-nowcasting-pilot
- Данные: rosreestr_deals.db (gdp_use_ifo_quarterly 479 строк, ikv_*, ВДС F), cbr_lending.db (escrow_monthly 118К/55 мес), wordstat_weekly_construction.csv
- Воспроизводимость: после написания кода

## Результаты (пилот, 2026-08-29)
- corr эскроу↔ИКВ: +0.75 lag2 (13 кв.), цемент +0.50 синхр., зарплата +0.34 l1
- OLS (эскроу l1 + зарплата l1 + wordstat l1): R2=0.75, n=12
- Wordstat для ИКВ слаб (+0.17); GDELT-тоны исключены (ложный сигнал 2026Q1)
- Nowcast 2026Q2 ≈ 96% к 2025Q2 (диапазон 95–99) — по nowcast_investments_housing_sep2026.pdf

## Обновление
- next_check: этап 1 дизайна — удлинение ИКВ до 2005 (ЕАЭС/ЕМИСС), скоринг B2B-фраз, backtest бенчмарков
- Владелец: @lnr

^[queries/vnok-nowcasting-design.md; queries/ikv-nowcasting-pilot.md; nowcast_investments_housing_sep2026.pdf]