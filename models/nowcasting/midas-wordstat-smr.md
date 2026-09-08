---
title: "MIDAS Wordstat+GDELT+ЕИСЖС → СМР"
created: 2026-09-08
updated: 2026-09-08
type: model
model_class: MIDAS
status: draft
hypotheses: [H-006]
tags: [nowcasting, mixed-frequency, search-data, leading-indicators]
sources: [data/wordstat_weekly_construction.csv, gdelt, eiszhc]
confidence: medium
---

# MIDAS: Wordstat + GDELT + ЕИСЖС → yoy СМР

## Назначение
Nowcasting yoy СМР на горизонте 1 месяц из высокочастотных источников. Целевая гипотеза: [[hypotheses.yaml|H-006]] — RMSE ниже квартального AR; базовый сигнал — wordstat-композит S2–S5 (corr 0.63 lead-1m, H-001).

## Спецификация
- Целевая: yoy СМР (Росстат, месячная)
- Блоки:
  1. Wordstat-композит S2+S3+S4+S5 (недельно, lead-1m)
  2. GDELT-упоминания строительства/девелоперов (дневно → недельная агрегация)
  3. ЕИСЖС: выдача разрешений / эскроу (мес.)
- Almon-lag для высокочастотных блоков (U-MIDAS как робаст-спецификация при малой выборке)
- Идентификация: без ограничений, forecasting-only

## Код и данные
- Код: planned — `scripts/nowcast_midas.py` (не написан, status: draft)
- Данные: `data/wordstat_weekly_construction.csv` (есть), GDELT-агрегаты (скрипт gdelt_sentiment_weekly.py), ЕИСЖС (ingest_eiszhk.py)
- Воспроизводимость: после написания кода

## Результаты
- Прогон от 2026-09-08 (поиск, не модель): corr композита 0.63 lead-1m; S1 (ИЖС) слабый
- Валидация: backtest 2022–2026 vs AR — planned

## Обновление
- next_check: собрать блоки GDELT и ЕИСЖС в одну частотную панель → написать scripts/nowcast_midas.py → backtest vs AR
- Владелец: @lnr

^[hypotheses.yaml H-001/H-006; data/wordstat_weekly_construction.csv]