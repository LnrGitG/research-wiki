---
title: "Estimation and Inference with Near Unit Roots"
authors: [Peter C.B. Phillips]
year: 2023
journal: "Econometric Theory"
volume: 39
issue: 2
pages: "221–263"
doi: "10.1017/S0266466622000342"
publisher: "Cambridge University Press"
published_online: "2022-07-27"
publication_date: "2023-04"
issn: "1469-4360"
url: "https://www.cambridge.org/core/journals/econometric-theory/article/estimation-and-inference-with-near-unit-roots/961D55BA08CFFEAAE9772CE271D64A3C"
keywords: [near unit roots, nonstationary time series, mildly integrated, mildly explosive, housing market]
tags: [unit-roots, near-unit-roots, nonstationary, mildly-integrated, mildly-explosive, local-unit-root, autoregressive-roots, housing-market, house-prices, Australia, inference, time-series]
source: cambridge-core
type: original-article
open_access: true
refs_count: 41
---

# Estimation and Inference with Near Unit Roots

**Peter C.B. Phillips**

*Econometric Theory*, Vol. 39, Issue 2, pp. 221–263 (April 2023)
DOI: [10.1017/S0266466622000342](https://doi.org/10.1017/S0266466622000342)

## Abstract

New methods are developed for identifying, estimating, and performing inference with nonstationary time series that have autoregressive roots near unity. The approach subsumes unit-root (UR), local unit-root (LUR), mildly integrated (MI), and mildly explosive (ME) specifications in the new model formulation. It is shown how a new parameterization involving a localizing rate sequence that characterizes departures from unity can be consistently estimated in all cases. Simple pivotal limit distributions that enable valid inference about the form and degree of nonstationarity apply for MI and ME specifications and new limit theory holds in UR and LUR cases. Normalizing and variance stabilizing properties of the new parameterization are explored. Simulations are reported that reveal some of the advantages of this alternative formulation of nonstationary time series. **A housing market application of the methods is conducted that distinguishes the differing forms of house price behavior in Australian state capital cities over the past decade.**

## Методология

- **Модель:** Near-unit-root framework — обобщение UR, LUR, MI, ME
- **Параметризация:** localizing rate sequence, характеризующая отклонения от единичного корня
- **Идентификация:** consistly estimated across all cases (UR/LUR/MI/ME)
- **Inference:** pivotal limit distributions для MI/ME; новая limit theory для UR/LUR
- **Свойства:** normalizing и variance-stabilizing transformations
- **Приложение:** цены на жильё в столицах штатов Австралии — различение форм поведения цен

## Ключевые выводы

1. **Единая параметризация** для всех типов near-unit-root процессов (UR, LUR, MI, ME)
2. **Consistent estimation** локализующей rate sequence во всех случаях
3. **Pivotal limit distributions** для inference о форме и степени nonstationarity (MI/ME)
4. **Housing market application:** различение форм поведения цен на жильё между городами Австралии
5. **Bubble detection:** ME (mildly explosive) — формализация тестирования пузырей (Phillips-Yu)

## References (41 works) — ключевые

| # | Автор | Статья | DOI |
|---|-------|--------|-----|
| 4 | Wei | Asymptotic inference for nearly nonstationary AR(1) | 10.1214/aos/1176350492 |
| 6 | Phillips | Uniform limit theory for stationary autoregression | 10.1111/j.1467-9892.2005.00452.x |
| 8 | Shin | Testing null of stationarity vs unit root (KPSS) | 10.1016/0304-4076(92)90104-Y |
| 9 | Phillips | Time series regression with a unit root | 10.2307/1913237 |
| 10 | Phillips | Towards a unified asymptotic theory for autoregression | 10.1093/biomet/74.3.535 |
| 11 | Phillips | Regression theory for near-integrated time series | 10.2307/1911357 |
| 14 | Yu | Explosive behavior in 1990s NASDAQ (bubble dating) | 10.1111/j.1468-2354.2010.00625.x |
| 16 | Hansen | Grid bootstrap and the autoregressive model | 10.1162/003465399558463 |
| 17 | Mikusheva | One-dimensional inference in AR models | — |
| 20 | Giraitis | Smoothing local-to-moderate unit root theory | 10.1016/j.jeconom.2010.01.009 |
| 23 | Elliott | Robustness of cointegration methods | 10.2307/2998544 |
| 27 | Mikusheva | Uniform inference in autoregressive models | 10.1111/j.1468-0262.2007.00798.x |
| 32 | Yu | Testing for multiple bubbles: exuberance and collapse | 10.1111/iere.12132 |
| 33 | Yu | Testing for multiple bubbles: real-time detectors | 10.1111/iere.12131 |
| 38 | Magdalinos | Limit theory for moderate deviations from unit root | 10.1016/j.jeconom.2005.08.002 |
| 40 | Stock | Confidence intervals for largest AR root in US macro | 10.1016/0304-3932(91)90034-L |

## Связь с нашим исследованием

- **Near-unit-root тестирование:** цены на жильё в регионах РФ — UR vs LUR vs MI vs ME
- **Bubble detection (ME):** mildly explosive roots = формализация тестирования жилищных пузырей — применимо к российским ценам 2020–2024 (льготная ипотека)
- **Phillips-Yu bubble tests:** PSY (Phillips-Shi-Yu) — уже в пакете `MultipleBubbles` (CRAN Task View, раздел 7)
- **Hedonic price models:** цены на жильё — различение nonstationarity между регионами
- **Австралийский пример:** столицы штатов = аналогия с региональными столицами РФ
- **R пакеты:** `tseries::adf()`, `urca` (ADF, KPSS, Zivot-Andrews), `MultipleBubbles` (PSY test) — из CRAN Task View
- **41 ссылка** — Phillips, Yu, Mikusheva, Hansen, Stock — ключевая эконометрическая литература по unit roots
