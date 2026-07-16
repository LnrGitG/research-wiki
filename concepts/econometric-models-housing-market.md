---
title: эконометрические модели жилищного рынка
created: 2026-07-16
updated: 2026-07-16
type: concept
tags:
  - models
  - econometrics
  - time-series
sources:
  - raw/papers/dipasquale-wheaton-1994-housing-market-dynamics.pdf
  - raw/articles/ecb-2025-monetary-policy-housing-consumption.md
  - raw/papers/wheaton-2014-ecm-housing-supply-elasticities.md
  - raw/articles/yunus-2012-securitized-re-macro-vecm-ssrn.md
  - raw/papers/madsen-2011-q-model-house-prices.md
  - raw/papers/topel-rosen-1988-housing-investment.md
  - raw/papers/baum-snow-duranton-2025-housing-supply-affordability.md
  - raw/articles/bhattacharjee-jensen-butler-2024-regional-housing-emerald.md
confidence: medium
---

# Эконометрические модели жилищного рынка

## Сводная таблица методов

| Модель | Тип | Уравнения | Данные | Ключевые работы |
|---|---|---|---|---|
| **Stock-flow** | Structural | 2-3 | Quarterly, national/metro | DiPasquale-Wheaton 1992-1994, Capozza et al. 2002 |
| **Asset-market (User cost)** | Structural | 1-2 | Quarterly, national | Poterba 1984 |
| **Tobin's Q** | Structural | 2-3 | Quarterly, national | Topel-Rosen 1988, Madsen 2011 |
| **Error correction (ECM)** | Time-series | 1-2 | Quarterly, MSA/metro | Wheaton 2014, DiPasquale-Wheaton 1994 (VECM) |
| **VAR / SVAR / BVAR** | Time-series | 5-7 | Quarterly, national/metro | ECB 2025 (SBVAR), Yunus 2012 (VECM, 10 стран), **Лысенко 2025** (BVAR со знаковыми ограничениями, 7 шоков, РФ) |
| **DSGE + VECM** | Structural hybrid | 5-10 | Quarterly, national | Brookes et al. 2011 (DSGE housing in VECM) |
| **Panel FE/RE** | Panel | 1-2 | Annual/metro | Green-Malpezzi-Mayo 2005 (45 MSA) |
| **Diffusion/Spatial** | Spatial econometrics | 1-3 | Quarterly, metro | Hilber-Vermeulen 2016 (England+Wales) |
| **Dynamic factor (DFM)** | Time-series | 50+ series | Monthly, national | RBNZ 2025 (nowcasting) |
| **Cross-section (hedonic)** | Structural | 1 | Annual/metro | Saiz 2010 (26 metro IV) |
| **Sentiment (LLM)** | ML-based | 1-2 | Text + monthly | Rogoff-Yang 2026 (China-Japan) |
| **Agent-Based Model (ABM)** | Computational | Много агентов | Quarterly, national | Bardoscia et al. 2025 (Bank of Spain WP 2502: UK housing + prudential) |

## Классификация по горизонтам прогноза

| Горизонт | Модель | Пример |
|---|---|---|
| **Short-run (1-4 quarters)** | ECM, VAR/SVAR, DFM | Wheaton 2014 (ECM), ECB 2025 (SBVAR), RBNZ 2025 (DFM) |
| **Medium-run (1-3 years)** | Stock-flow, Tobin's Q, Panel FE | DiPasquale-Wheaton 1994, Madsen 2011 |
| **Long-run (5+ years)** | Asset-market, DSGE, Cross-section | Poterba 1984, Brookes 2011, Saiz 2010 |

## Связи методов с исследовательскими задачами

### Ценовая динамика housing:
- **Short-run**: Shock propagation → VAR/SVAR (ECB 2025), ECM (Wheaton 2014)
- **Medium-run**: Stock-flow equilibrium → DiPasquale-Wheaton 1994, Capozza 2002
- **Long-run**: Fundamental valuation → Asset-market (Poterba 1984), Cross-section (Saiz 2010)

### Инвестиции в строительство:
- **Tobin's Q → Housing starts**: Topel-Rosen 1988 (Q = PV(marginal product) / cost)
- **Q = 1 long-run equilibrium**: If Q > 1, construction expands; if Q < 1, depreciates
- **Madsen 2011**: Q model extended to include land prices, taxes, construction costs

### Macro-linkages:
- **Monetary policy transmission**: ECB 2025 (household consumption via housing + furniture)
- **Global RE cycles**: Yunus 2012 (VECM, 10 countries, EPRA/NAREIT)
- **Sentiment channel**: Rogoff-Yang 2026 (LLM-based sentiment amplifies wealth effect)

### Regional analysis:
- **Spatial diffusion**: Hilber-Vermeulen 2016 (England+Wales, spatial econometrics)
- **MSA heterogeneity**: Wheaton 2014 (ECM per MSA, supply elasticity heterogeneity)
- **Russia**: Regional FE models — see existing wiki: [[концепты/региональная эластичность]]

## Методологические тренды

1. **1980s-1990s**: Structural models (stock-flow, asset-market, Tobin's Q)
2. **2000s**: Time-series (ECM, VAR) + Panel (FE/RE, hedonic)
3. **2010s**: Spatial econometrics, DSGE, cross-country comparisons
4. **2020s**: ML (LLM sentiment), Dynamic factor models, SBVAR, **BVAR со знаковыми ограничениями** (Лысенко 2025), Agent-Based Models (Bardoscia et al. 2025)

## Проблемы идентификации

- **Endogeneity**: Price affects construction, construction affects price → IV/SVAR needed
- **Non-stationarity**: I(1) series (prices, stock) → cointegration (ECM) or differencing
- **Heterogeneity**: Regional differences require panel FE or separate ECMs
- **Data limitations**: Short samples (MSA/metro), measurement error, publication lag → DFM (RBNZ 2025)

## Применения к российскому рынку

- **ECM/VECM**: Wheaton 2014, Yunus 2012 → apply to Rosstat regional data
- **Stock-flow**: DiPasquale-Wheaton 1994 → Moscow/St Petersburg metro
- **Panel FE**: Green-Malpezzi-Mayo 2005 → 45+ Russian cities (if data exists)
- **SVAR**: ECB 2025 → CBR key rate → housing → consumption transmission
- **DFM**: RBNZ 2025 → nowcasting Russian GDP from high-frequency RE indicators
- **Sentiment**: Rogoff-Yang 2026 → Russian RE media analysis (ЦИАН, Авито, РБК)

## Связанные страницы

- [[концепты/ценообразование-субсидии-mortgage]]
- [[концепты/жилищный-цикл-инвестиции]]
- [[концепты/региональная дифференциация]]
- [[entities/россия-рынок]]