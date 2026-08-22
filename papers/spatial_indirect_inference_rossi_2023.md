---
title: "Continuously Updated Indirect Inference in Heteroskedastic Spatial Models"
authors: [Francesca Rossi]
year: 2023
journal: "Econometric Theory"
volume: 39
issue: 1
pages: "107–145"
doi: "10.1017/S0266466621000384"
publisher: "Cambridge University Press"
published_online: "2021-09-22"
publication_date: "2023-02"
issn: "1469-4360"
url: "https://www.cambridge.org/core/journals/econometric-theory/article/continuously-updated-indirect-inference-in-heteroskedastic-spatial-models/11CABB59EA7FAA3CD8F3981ED8CD39BE"
keywords: [spatial econometrics, indirect inference, heteroskedasticity, continuous updating, house prices]
tags: [spatial-econometrics, indirect-inference, heteroskedasticity, continuous-updating, OLS, QMLE, spatial-autoregression, house-prices, Boston, Moran-I, spatial-lag, spatial-error]
source: cambridge-core
type: original-article
open_access: true
refs_count: 30
---

# Continuously Updated Indirect Inference in Heteroskedastic Spatial Models

**Francesca Rossi**

*Econometric Theory*, Vol. 39, Issue 1, pp. 107–145 (February 2023)
DOI: [10.1017/S0266466621000384](https://doi.org/10.1017/S0266466621000384)

## Abstract

Spatial units typically vary over many of their characteristics, introducing potential unobserved heterogeneity which invalidates commonly used homoskedasticity conditions. In the presence of unobserved heteroskedasticity, methods based on the quasi-likelihood function generally produce inconsistent estimates of both the spatial parameter and the coefficients of the exogenous regressors. A robust generalized method of moments estimator as well as a modified likelihood method have been proposed in the literature to address this issue. The present paper constructs an alternative indirect inference (II) approach which relies on a simple ordinary least squares procedure as its starting point. Heteroskedasticity is accommodated by utilizing a new version of continuous updating that is applied within the II procedure to take account of the parameterization of the variance–covariance matrix of the disturbances. Finite-sample performance of the new estimator is assessed in a Monte Carlo study. The approach is implemented in an empirical application to house price data in the Boston area, where it is found that spatial effects in house price determination are much more significant under robustification to heterogeneity in the equation errors.

## Методология

- **Модель:** Spatial autoregressive (SAR) с heteroskedastic errors
- **Проблема:** QMLE несостоятелен при heteroskedasticity (spatial units vary)
- **Метод:** Indirect Inference (II) с continuously updating
  - Binding function: OLS → spatial parameter
  - Continuous updating: параметризация variance-covariance матрицы
- **Стартовая точка:** OLS (простая, не требует знания структуры heteroskedasticity)
- **Monte Carlo:** оценка finite-sample performance
- **Приложение:** цены на жильё в Boston area — Harrison-Rubinfeld data

## Ключевые выводы

1. **QMLE несостоятелен** при unobserved heteroskedasticity в spatial моделях
2. **Indirect Inference с continuous updating** — альтернатива GMM и modified likelihood
3. **OLS как binding function** — простота, не требует спецификации heteroskedasticity
4. **Boston house prices:** spatial effects **значительно более значимы** при робастификации к heterogeneity
5. **Moran's I** тест на spatial autocorrelation — ключевая диагностика

## References (30 works) — ключевые

| # | Автор | Статья | DOI |
|---|-------|--------|-----|
| 1 | Yang | Indirect inference estimation of spatial autoregressions | 10.3390/econometrics8030034 |
| 3 | Case | Spatial patterns in household demand | 10.2307/2938168 |
| 4 | Pace | On the Harrison and Rubinfeld data | 10.1006/jeem.1996.0052 |
| 5 | Scheinkman | Crime and social interactions | 10.2307/2946686 |
| 7 | Prucha | Specification and estimation of SAR with AR disturbances | 10.1016/j.jeconom.2009.10.025 |
| 8 | Rossi | Indirect inference in spatial autoregression | 10.1111/ectj.12084 |
| 11 | Prucha | Asymptotic distribution of Moran I test | 10.1016/S0304-4076(01)00064-1 |
| 12 | Lee | Consistency of LS for mixed regressive SAR | 10.1017/S0266466602182028 |
| 13 | Lee | Asymptotic distributions of QMLE for SAR | 10.1111/j.1468-0262.2004.00558.x |
| 14 | Lee | GMM and 2SLS for mixed regressive SAR | 10.1016/j.jeconom.2005.10.004 |
| 20 | Rubinfeld | Hedonic housing prices and demand for clean air | 10.1016/0095-0696(78)90006-2 |
| 22 | LeSage | Theory and Practice of Spatial Econometrics | — |
| 23 | Lee | GMM estimation of SAR with unknown heteroskedasticity | 10.1016/j.jeconom.2009.10.035 |
| 24 | Simlai | Estimation of variance of housing prices (spatial cond. heterosk.) | 10.1016/j.qref.2013.07.001 |
| 25 | Prucha | Cliff-Ord model with heteroskedastic innovations | 10.1111/j.1467-9787.2009.00618.x |

## Связь с нашим исследованием

- **Spatial econometrics для регионов РФ:** 96 регионов = spatial units с heteroskedasticity
- **Hedonic price models:** Harrison-Rubinfeld (Boston) — классика, применима к оценке цен на жильё по регионам
- **SAR с heteroskedasticity:** регионы РФ различаются по размеру, плотности, экономике → heteroskedasticity
- **Indirect Inference:** альтернатива QMLE для spatial lag/error моделей — устойчивость к misspecification
- **Moran's I:** тест spatial autocorrelation для региональных цен на жильё
- **R пакеты:** `spdep` (Moran's I, SAR), `spatialreg` (SAR, SEM, SDM), `splm` (spatial panel)
- **LeSage & Pace (2009):** *Introduction to Spatial Econometrics* — ключевая ссылка
- **30 ссылок** — Lee, Prucha, LeSage — основа spatial econometrics
