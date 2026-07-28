---
title: "Balcilar-Gupta-Miller 2012 — Нелинейные модели для прогнозирования цен на жильё"
type: annotation
created: 2026-07-28
updated: 2026-07-28
tags: [annotation, non-linear, STAR, forecasting, US-regions]
source: "[[papers/Balcilar-The-Out-of-Sample-Forecasting-Performance-of-Non-Linear-Models-of-Regonal-Housing-Prices-in]]"
authors: "Mehmet Balcilar, Rangan Gupta, Stephen M. Miller"
journal: "International Journal of Forecasting (электронная версия SSRN)"
---

# Balcilar-Gupta-Miller 2012 — Нелинейные модели для прогнозирования цен на жильё

## Суть в одном абзаце

Сравнивает линейные AR и нелинейные STAR (smooth-transition autoregressive) модели для прогнозирования цен на жильё по 4 регионам США. **Нелинейность есть, но помогает только на длинных горизонтах**. На коротких горизонтах линейная AR доминирует. На длинных (8+ кварталов) STAR превосходит AR в point forecasts, но differences в interval и density forecasts незначительны. В dynamic 25-step ex-ante тесте (2010–2012, пост-кризисный период) разница линейных/нелинейных моделей невелика.

## Цель

Проверить, улучшают ли нелинейные модели прогнозы цен на жильё по сравнению с линейными бенчмарками — point, interval и density forecasts.

## Метод

- **Данные**: месячные индексы цен на жильё (S&P/Case-Shiller) для 4 Census regions (Northeast, South, Midwest, West), 1968:1–2012:6
- **Модели**: AR (линейный) vs STAR (нелинейный smooth-transition)
  - STAR: regimes определяются smooth transition variable (lagged house price growth)
  - Transition function: logistic (LSTAR) или exponential (ESTAR)
- **Оценка**: In-sample 1968–2000, out-of-sample 2001:1–2010:5
- **Тесты**: Point forecasts (MSFE), interval forecasts (coverage rates), density forecasts (log predictive density)

## Ключевые результаты

1. **Нелинейность подтверждена in-sample**: STAR significantly better than AR in-sample для 3 из 4 регионов (Midwest — линейный)
2. **Out-of-sample: long horizons only** — STAR превосходит AR на 8+ квартальных горизонтах, но на 1-4 кварталов AR dominates
3. **Interval/density forecasts**: no major differences между линейными и нелинейными моделями — нелинейность помогает только point-прогнозам на длинных горизонтах
4. **Dynamic 25-step ex-ante test** (2010–2012): разница линейных/нелинейных незначительна — нелинейность нестабильна во времени

## Практический вывод

- **Нелинейность — nice-to-have, не must-have**: на коротких горизонтах AR достаточно, STAR даёт marginal gains
- **Необходимость проверки out-of-sample**: in-sample нелинейность ≠ out-of-sample преимущество (типичная проблема)
- Для **российского рынка**: можно проверить STAR на региональных данных, но не ожидать больших выигрышей на коротких горизонтах

## Почему это предупреждение для ML-энтузиастов

- Базовая нелинейность (STAR) не бьёт простой AR на большинстве горизонтов
- Это мотивация для более сложных нелинейностей: EEMD decomposition + SVR (Plakandaras), deep learning (Ye 2024), но их тоже нужно проверять out-of-sample

## Связанные страницы

- [[reviews/ml-ne-linearnye-modeli-dlya-prognozirovaniya]] — кластер ML
- [[papers/Plakandaras-Forecasting-the-U.S.-Real-House-Price-Index]] — EEMD + SVR
- [[papers/Qiongwei-Ye-House-price-prediction-using-machine-learning-for-Ames-Iowa-2024]] — ML для Ames Iowa