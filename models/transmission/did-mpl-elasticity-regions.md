---
title: "DiD-панель регионов: МПЛ × эластичность предложения"
created: 2026-09-08
updated: 2026-09-08
type: model
model_class: RF/ML
status: draft
hypotheses: [H-005, H-004]
tags: [macroprudential, supply-elasticity, regional-differentiation, econometrics]
sources: [cbr, rosstat-regions, domrf]
confidence: medium
---

# DiD: макропруденциальные лимиты по эластичности регионов

## Назначение
Оценка эффекта МПЛ-эпизодов (ЦБ РФ, 2023–2025) на цены и транзакции в разрезе эластичности предложения регионов. Целевые гипотезы: [[hypotheses.yaml|H-005]] (лимиты действуют на цены только в эластичных регионах) и [[hypotheses.yaml|H-004]] (эффект замещения как функция спреда — контрол-переменная).

## Спецификация
- Уровень: регион × месяц (цены, транзакции, кредиты)
- Обработка: эпизоды ужесточения МПЛ (даты ЦБ); treatment-интенсивность = доля высокорисковых кредитов до эпизода
- Спецификация: $y_{r,t} = \beta (MP L_t \times Elasticity_r) + \mu_r + \lambda_t + \varepsilon_{r,t}$
- Elasticity_r: из макро-оценок (housing_supply_elasticity.py, 0.3–2.5) или Saiz-proxy (рельеф из data-sources-housing-econometrics)
- Ожидание: β < 0 в эластичных регионах; в неэластичных (СПб, Москва) — сжатие транзакций без эффекта на цены
- Референс: Лаптева 2025 (лаг 2 квартала, длительность ~6 мес), ЦБ 2025 (высокорисковые 46%→3%)

## Код и данные
- Код: planned; базовые региональные ряды — collect_panel.py (1429 зап, 7 источников)
- Данные: panel из data/ (cbr_mortgage_monthly: 96 регионов × 90 мес уже в catalog), Росстат региональный (rosstat-socioeconomic-regions)
- Воспроизводимость: после определения эпизодов МПЛ

## Результаты
- Нет прогонов; предварительный контур — в [[concepts/macroprudentialnaya-politika-rynok-zhilya|концепте макропруденциальной политики]]

## Обновление
- next_check: каталогизировать эпизоды МПЛ 2023–2025 → pre-trends → DiD
- Владелец: @lnr

^[concepts/macroprudentialnaya-politika-rynok-zhilya; hypotheses.yaml H-005]