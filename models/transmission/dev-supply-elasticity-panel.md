---
title: "IV-FE панель: эластичность предложения × финансовые ограничения девелоперов"
created: 2026-09-08
updated: 2026-09-08
type: model
model_class: RF/ML
status: draft
hypotheses: [H-002, H-003]
tags: [supply-elasticity, developer-finance, financial-constraints, econometrics]
sources: [spark, eiszhc, fnn-opendata]
confidence: medium
---

# Эластичность предложения, обусловленная финансовым здоровьем девелоперов

## Назначение
Оценка firm-level эластичности предложения (старты/ввод на рост цен) с интеракцией финансовых ограничений. Целевые гипотезы: [[hypotheses.yaml|H-002]] (эластичность ниже при Net Debt/EBITDA > 4x) и [[hypotheses.yaml|H-003]] (escrow-release как экзогенный cash-flow шок). База — [[queries/supply-elasticity-estimation-design|дизайн исследования]].

## Спецификация
- Уровень: девелопер × год × регион (SPARK + ЕИСЖС + ФНС опендата)
- Зависимая: лог стартов (ЕИСЖС); альтернативно ввод
- Ключевая регрессия: $\ln Starts_{i,t} = \beta_1 \Delta p_{r,t} + \beta_2 \Delta p_{r,t} \times FC_{i,t-1} + \gamma X + \mu_i + \lambda_t + \varepsilon$
- FC-меры: Net Debt/EBITDA > 4x dummy, Interest Coverage < 2 dummy
- Идентификация: Bartik (bank-lending shocks × связи девелопер-банк); escrow-release timing как IV (H-003)
- Ожидания: β1 > 0, β2 < 0

## Код и данные
- Код: planned — частично `scripts/housing_supply_elasticity.py` (существует, макро-уровень); firm-level — не написан
- Данные: SPARK-выгрузка (собрать 2015–2025), ЕИСЖС (ingest_eiszhk.py), ФНС опендата (fns_opendata_collect.py)
- Воспроизводимость: после сборки панели

## Результаты
- Макро-референс: региональная SR-эластичность 0.62–0.91 (CMWP, IV-FE)
- Firm-level: нет оценок ни в литературе, ни здесь — ключевой вклад (gap №1 в [[queries/literature-gap-map|gap-map]])

## Обновление
- next_check: SPARK-панель → дескриптив по тирам (large/medium/small) → IV-FE с интеракциями
- Владелец: @lnr

^[queries/supply-elasticity-estimation-design; queries/literature-gap-map; hypotheses.yaml]