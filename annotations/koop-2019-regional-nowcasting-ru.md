---
title: "Koop-McIntyre-Mitchell 2019 — Nowcasting региональной экономики Великобритании"
type: annotation
created: 2026-07-28
updated: 2026-07-28
tags: [annotation, nowcasting, mixed-frequency, stacked-VAR, entropic-tilting, UK-regions]
source: "[[papers/Koop-etal-JRSSA2019-UK-regional-nowcasting-using-a-mixed-frequency-Vector-Autoregressive]]"
authors: "Gary Koop, Stuart McIntyre, James Mitchell"
journal: "Journal of the Royal Statistical Society: Series A, 2019"
---

# Koop-McIntyre-Mitchell 2019 — Nowcasting региональной экономики

## Суть в одном абзаце

Разработали **stacked mixed-frequency VAR + entropic tilting** для nowcasting регионального ВВП (GVA) Великобритании. Проблема: региональный GVA доступен только ежегодно с лагом 11+ месяцев, а нац. GVA публикуется ежеквартально. Решение: использовать quarterly UK GVA для обновления quarterly nowcasts annual regional GVA growth. Entropic tilting позволяет оптимально наложить аггрегационное ограничение (нац. GVA = взвешенная сумма региональных) без latent variables.

## Цель

Предоставить timely quarterly nowcasts annual regional GVA growth для 9 регионов Великобритании, используя quarterly UK GVA data.

## Метод

- **Модель**: stacked mixed-frequency VAR (low-frequency regional GVA + high-frequency UK GVA)
  - Regional GVA: annual, 9 регионов, 1966–2016
  - UK GVA: quarterly, 1997–2016
  - Bayesian priors для shrinkage (Carriero-Clark-Marcellino 2015)
  - Multivariate stochastic volatility
- **Entropic tilting**: обновляет density nowcasts при каждом quarterly UK GVA release
  - Aggregation constraint: UK GVA = weighted average of regional GVA
- **Real-time nowcasting**: unconditional forecast в начале года → обновляется quarterly через entropic tilting

## Ключевые результаты

1. **Entropic tilting значительно улучшает nowcasts**: точность ↑ по сравнению с unconditional forecasts на 30–50%
2. **Aggregation constraint critical**: onaltilting без constraint на aggregation → прогнозы по регионам не сходятся к нац. GVA
3. **Computational advantages stacked VAR**: no latent variables, no MCMC data augmentation → simpler и faster
4. **Регулярные quarterly nowcasts**: можно производить «flash» estimates за 6+ месяцев до официального релиза ONS
5. **Применимо к другим странам**: та же проблема с regional data lag существует в US (BEP publishes quarterly state data 3 months after national GDP)

## Почему это важно

- **First application stacked VAR + entropic tilting for regional nowcasting**: метод можно применить к регионам РФ
- **Aggregation constraint** — ключевая инновация: regional nowcasts должны суммироваться к national figure
- **Real-time applicability**: метод работает с first-release data, а не с revised data → no look-ahead bias
- **Bridge к housing**: regional GVA growth → proxy для regional housing demand

## Для российского применения

- В РФ региональный ВВП также публикуется с лагом (Росстат)
- Monthly indicators (индекс промпроизводства, розничные продажи) могут заменить UK quarterly GVA
- Regional VAMP (валовая добавленная по макросекторам) + national VAMP → stacked VAR с aggregation constraint
- Entropic tilting позволяет on-the-fly update regional forecasts при каждом quarterly release

## Связанные страницы
- [[reviews/nowcasting-i-mixed-frequency-modeli]] — полный обзор nowcasting
- [[papers/Tallman-Zaman-IJF-2020-Combining-survey-long-run-forecasts-and-nowcasts-with-BVAR]] — combining + entropic tilting
- [[papers/rbnz-2025-gdp-nowcasting-dfm]] — DFM nowcasting from RBNZ