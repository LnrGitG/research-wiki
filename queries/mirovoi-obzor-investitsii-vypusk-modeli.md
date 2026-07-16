---
title: Обзор мировой литературы — инвестиции, выпуск и модели жилищного рынка
created: 2026-07-16
updated: 2026-07-16
type: query
tags: [construction-industry, housing-prices, housing-supply, investment, literature-review, econometrics]
confidence: high
---

# Обзор мировой академической литературы: инвестиции, выпуск в строительстве, модели жилищного рынка

## Оглавление

1. [Модели жилищного рынка](#1-модели-жилищного-рынка)
2. [Оценка инвестиций в строительстве](#2-оценка-инвестиций-в-строительстве)
3. [Выпуск и предложение в строительстве](#3-выпуск-и-предложение-в-строительстве)
4. [Рекомендации по загрузке в wiki](#4-рекомендации-по-загрузке)

---

## 1. Модели жилищного рынка

### 1.1 Семинальные работы

| # | Авторы | Год | Название | Журнал | Вклад |
|---|--------|-----|----------|--------|-------|
| 1 | **DiPasquale D., Wheaton W.C.** | 1992 | The Markets for Real Estate Assets and Space: A Conceptual Framework | _Real Estate Economics_ | Четырёхквадрантная модель (4QD): связь рынка пространства (аренда) и рынка активов (цены) через строительство и stock-adjustment |
| 2 | **DiPasquale D., Wheaton W.C.** | 1994 | Housing Market Dynamics and the Future of Housing Prices | _Journal of Urban Economics_ | Эмпирическая модель: housing starts = f(цены, издержки, ставки); stock-flow adjustment |
| 3 | **Poterba J.M.** | 1984 | Tax Subsidies to Owner-Occupied Housing: An Asset-Market Approach | _Quarterly Journal of Economics_ | Модель asset-market equilibrium: цена жилья = PV будущих rents за вычетом налогов; инфляция + налоги → user cost |
| 4 | **Capozza D.R., Hendershott P.H., Mack C., Mayer C.J.** | 2002 | Determinants of Real House Price Dynamics | _NBER Working Paper_ | Эмпирическая модель динамики цен: серийная корреляция, mean reversion, реакция на шоки; различие по metro areas |
| 5 | **Glaeser E.L., Gyourko J.** | 2005 | Urban Decline and Durable Housing | _Journal of Political Economy_ | Модель с долговечным жильём: почему цены не падают ниже издержек строительства; асимметрия реакции |

### 1.2 Современные обзоры и расширения

| # | Авторы | Год | Название | Фокус |
|---|--------|-----|----------|-------|
| 6 | **Baum-Snow N., Duranton G.** | 2025 | Housing Supply and Housing Affordability | Обзор литературы: связь предложения и доступности; NBER/Handbook chapter |
| 7 | **Been V., Ellen I.G., O'Regan K.** | 2025 | Supply Skepticism Revisited | Обзор строгих недавних исследований: рост предложения ↓ рост арендной платы в регионе |
| 8 | **Zhao C. et al.** | 2023 | Impact of Housing Policies on the Real Estate Market | Систематический количественный обзор литературы по жилищной политике |
| 9 | **Damm A.P. et al.** | 2025 | Medium-Run Impacts of Immigration on the Housing Market | Применение augmented 4-Quadrant Model к миграции |
| 10 | **Chauhan R.S.** | 2024 | Applying System Dynamics to Housing Supply | Современное расширение 4QD: системная динамика |

### 1.3 Ключевые модели — суть

**Четырёхквадрантная модель (DiPasquale-Wheaton, 1992):**
```
         Рынок активов               Рынок пространства
    P = R/i  ←──┐                  R = f(D, S)  ←──┐
         │       │                       │          │
         ↓       │                       ↓          │
    P → Construction  ──→  Stock  ──→  S → R       │
         Строительство             Предложение      │
```
Равновесие: аренда (R) определяет цены (P), цены определяют строительство, строительство определяет stock, stock определяет аренду.

**Asset-market approach (Poterba, 1984):**
P = R / [(1−τ)·i + δ + τ_p − π_e]
где user cost = процент + износ + налоги − ожидаемый прирост капитала.

**Stock-flow model (DiPasquale-Wheaton, 1994):**
Housing starts = f(P, construction costs, interest rates)
ΔStock = Starts − δ·Stock

---

## 2. Оценка инвестиций в строительстве

### 2.1 Семинальные работы

| # | Авторы | Год | Название | Журнал | Метод |
|---|--------|-----|----------|--------|-------|
| 11 | **Topel R., Rosen S.** | 1988 | Housing Investment in the United States | _Journal of Political Economy_ | Supply-determined model: investment = f(Tobin's Q, adjustment costs). Эмпирика: quarterly 1963–1983, marginal cost curve |
| 12 | **Rosen S., Topel R.** | 1986 | A Time-Series Model of Housing Investment in the U.S. | _NBER Working Paper 1818_ | Более ранняя версия: time-series model |
| 13 | **Somerville C.T.** | 1996 | Residential Construction Costs and the Supply of New Housing | _NBER Summer Institute_ | Издержки строительства как ключевой фактор предложения |
| 14 | **Kenny G.** | 1999 | Asymmetric Adjustment Costs and the Dynamics of Housing Supply | _Central Bank of Ireland_ | Асимметричные adjustment costs: строительство реагирует по-разному на рост и падение спроса |

### 2.2 Tobin's Q в жилищном строительстве

| # | Авторы | Год | Название | Ключевой результат |
|---|--------|-----|----------|-------------------|
| 15 | **Madsen J.B.** | 2011 | A q Model of House Prices | _Monash University_ | Q-модель цен: изменения ставок, демографии и дохода определяют Q → инвестиции |
| 16 | **Barth N. et al.** | 2023 | Linking Housing Tobin's Q to Land Prices | _OsloMet Housing Lab_ | Связь Tobin's Q с ценами на землю |
| 17 | **Freimark J.D.** | 2020 | Tobin's Q Theory of Investment Applied to Housing | _Washington State University_ | Эмпирический тест Q-теории для жилищных инвестиций |

Q = (Рыночная цена жилья) / (Издержки строительства)
Если Q > 1 → выгодно строить → рост инвестиций.

### 2.3 Мультипликатор и акселератор в строительстве

| # | Авторы | Год | Название | Вклад |
|---|--------|-----|----------|-------|
| 18 | **Ive G.J., Gruneberg S.L.** | 2000 | Construction Investment, the Multiplier and the Accelerator | _The Economics of the Modern Construction Sector_ | Строительные инвестиции, мультипликатор и акселератор в макроэкономическом контексте |
| 19 | **Erol I., Unal U.** | 2015 | Role of Construction Sector in Economic Growth | _MPRA Paper_ | Эконометрические методы: Granger causality, коэффициенты корреляции; роль стройки в экономическом росте |

### 2.4 Современные исследования инвестиций

| # | Авторы | Год | Название | Метод |
|---|--------|-----|----------|-------|
| 20 | **Garcia D., Tüzemen D.** | 2025 | Reexamining Lackluster Productivity Growth in Construction | _Fed FEDS_ | Падение производительности в строительстве (−0.3 п.п./год в 2019–2023) |
| 21 | **Gurmu A.T. et al.** | 2026 | Econometric Analysis of Macroeconomic Factors Influencing Construction | _Construction Management & Economics_ | VAR-модель: макроэкономические факторы → строительный труд |
| 22 | **Ma L. et al.** | 2021 | Housing Price Dynamics on Residential Construction | _Structural Change & Econ Dynamics_ | Panel ECM: связь цен и строительства в Австралии |

---

## 3. Выпуск и предложение в строительстве

### 3.1 Эластичность предложения жилья — ключевая литература

Это центральная тема, связывающая цены, регулирование и строительство.

| # | Авторы | Год | Название | Журнал | Эластичность / Метод |
|---|--------|-----|----------|--------|---------------------|
| 23 | **Saiz A.** | 2010 | The Geographic Determinants of Housing Supply | _Quarterly Journal of Economics_ | Эластичность 1.25–2.45; geography (slope, water) как инструмент для regulation |
| 24 | **Glaeser E.L., Gyourko J., Saiz A.** | 2008 | Housing Supply and Housing Bubbles | _Journal of Urban Economics_ | Эластичное предложение → меньшие пузыри |
| 25 | **Gyourko J., Molloy R.** | 2014 | Regulation and Housing Supply | _NBER Working Paper_ / _Handbook of Urban Economics_ | Обзор: как регулирование ограничивает предложение |
| 26 | **Hilber C.A.L., Vermeulen W.** | 2016 | The Impact of Supply Constraints on House Prices in England | _Economic Journal_ | Regulatory constraints → рост цен; causal evidence, TSLS |
| 27 | **Ihlanfeldt K.** | 2005 | The Effect of Land Use Regulation on Housing and Land Prices | _Journal of Urban Economics_ | Регулирование ↑ цены земли и жилья |
| 28 | **Green R.K., Malpezzi S., Mayo S.K.** | 2005 | Metropolitan-Specific Estimates of the Price Elasticity of Supply of Housing | _Journal of Urban Economics_ | Оценки эластичности для 45 MSA |
| 29 | **Chapelle G. et al.** | 2023 | Land-Use Regulation and Housing Supply Elasticity | _Working Paper_ | Французский кейс по аналогии с Saiz (2010) |
| 30 | **Banerjee R. et al.** | 2024 | A Novel Measure of Housing Supply Elasticity | _BIS Quarterly Review_ | Эластичность = Δpermits / Δprices (BIS methodology) |

### 3.2 Эмпирические модели выпуска

| # | Авторы | Год | Название | Метод |
|---|--------|-----|----------|-------|
| 31 | **Mayer C.J., Somerville C.T.** | 2000 | Land Use Regulation and New Construction | _Regional Science & Urban Economics_ | Квартальная модель: housing starts = f(regulation, prices, costs); 44 MSA, 1985–1996 |
| 32 | **Mayer C.J., Somerville C.T.** | 2000 | Using the Urban Growth Model to Estimate Housing Supply | _Journal of Urban Economics_ | Эмпирическая модель из urban growth theory; более низкие эластичности |
| 33 | **Wheaton W.C.** | 2014 | Error Correction Models of MSA Housing 'Supply' Elasticities | _MIT Working Paper_ | ECM для оценки эластичности предложения на уровне MSA |
| 34 | **Grimes A., Aitken A.** | 2010 | Housing Supply, Land Costs and Price Adjustment | _Real Estate Economics_ | Предложение, издержки земли и adjustment цен |

### 3.3 Производительность в строительстве

| # | Авторы | Год | Название | Фокус |
|---|--------|-----|----------|-------|
| 35 | **Sveikauskas L. et al.** | 2018 | Measuring Productivity Growth in Construction | _BLS Monthly Labor Review_ | Новые меры производительности для 4 типов строительства |
| 36 | **McKinsey Global Institute** | 2017 | Reinventing Construction: A Route to Higher Productivity | Отчёт MGI | Производительность стройки отстаёт от экономики в целом |
| 37 | **NIST** | 2012 | Metrics and Tools for Measuring Construction Productivity | _NIST SP 1101_ | Методология измерения производительности на уровне задач, проектов, отрасли |

---

## 4. Рекомендации по загрузке в wiki

Ниже — приоритизированный список для первоочередной загрузки. Отобраны по критериям: (a) методологическая значимость для эконометрических методов, (b) применимость к российскому контексту, (c) цитируемость.

### 🔴 Tier 1 — Must-have (семь работ — фундамент)

| # | Скачать | Почему важно |
|---|---------|-------------|
| 1 | **DiPasquale, Wheaton (1992)** — 4-Quadrant Model | Теоретический фундамент: как связаны рынок аренды, цены, строительство и stock |
| 2 | **DiPasquale, Wheaton (1994)** — Housing Market Dynamics | Эмпирическая stock-flow модель: starts = f(цены, издержки, ставки) |
| 3 | **Poterba (1984)** — Tax Subsidies, Asset-Market Approach | User cost model — основа для analyses субсидий и налогов |
| 4 | **Topel, Rosen (1988)** — Housing Investment in the U.S. | Supply-determined investment model: Tobin's Q, adjustment costs |
| 5 | **Mayer, Somerville (2000)** — Land Use Regulation and New Construction | Эмпирическая модель starts = f(regulation, prices, costs) для 44 MSA |
| 6 | **Gyourko, Molloy (2014)** — Regulation and Housing Supply (Handbook chapter) | Исчерпывающий обзор литературы по регулированию |
| 7 | **Saiz (2010)** — Geographic Determinants of Housing Supply | Инструментальные переменные: geography → regulation → эластичность |

### 🟡 Tier 2 — Значимые расширения

| # | Скачать | Почему важно |
|---|---------|-------------|
| 8 | **Hilber, Vermeulen (2016)** — Supply Constraints in England | Causal evidence (TSLS): регулирование → цены |
| 9 | **Capozza et al. (2002)** — Determinants of Real House Price Dynamics | Эмпирика: серийная корреляция, mean reversion, metro-level heterogeneity |
| 10 | **Madsen (2011)** — A q Model of House Prices | Tobin's Q для жилья: ставки + демография + доход → Q → цены |
| 11 | **Baum-Snow, Duranton (2025)** — Housing Supply and Affordability | Свежий handbook-обзор всей литературы |
| 12 | **Green, Malpezzi, Mayo (2005)** — Supply Elasticity Estimates | Оценки эластичности для 45 MSA |
| 13 | **Kenny (1999)** — Asymmetric Adjustment Costs | Асимметрия: строительство реагирует по-разному на подъём и спад |
| 14 | **Glaeser, Gyourko, Saiz (2008)** — Housing Supply and Bubbles | Эластичное предложение → меньше пузыри |

### 🟢 Tier 3 — Методологические и контекстные

| # | Скачать | Почему важно |
|---|---------|-------------|
| 15 | **Garcia, Tüzemen (2025)** — Productivity Growth in Construction | Свежие данные: падение производительности в стройке |
| 16 | **Been et al. (2025)** — Supply Skepticism Revisited | Новый обзор: рост предложения реально снижает аренду |
| 17 | **Wheaton (2014)** — Error Correction Models of Supply Elasticities | ECM для эластичности на уровне MSA |
| 18 | **Gurmu et al. (2026)** — VAR Model for Construction | Современное применение VAR к строительной отрасли |

### 📊 Карта методов

```
                       ┌─────────────────────────┐
                       │   Модели жил. рынка     │
                       │  (DiPasquale-Wheaton)   │
                       └───────────┬─────────────┘
                                   │
            ┌──────────────────────┼──────────────────────┐
            ▼                      ▼                      ▼
   ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────┐
   │  Инвестиции     │  │  Выпуск / Starts  │  │  Эластичность    │
   │  (Topel-Rosen)  │  │  (Mayer-Somerville│  │  предложения     │
   │  Tobin's Q      │  │   DiPasquale-     │  │  (Saiz, Green-   │
   │  Adjustment     │  │   Wheaton 1994)   │  │   Malpezzi-Mayo) │
   │  costs          │  │  Stock-flow       │  │  Geography IV    │
   └─────────────────┘  └──────────────────┘  └──────────────────┘
                                   │
                        ┌──────────┴──────────┐
                        ▼                     ▼
               ┌──────────────┐    ┌──────────────────┐
               │ Регулирование│    │  Производительность│
               │ (Gyourko-    │    │  (Garcia-Tüzemen, │
               │  Molloy,     │    │   Sveikauskas)    │
               │  Hilber-     │    │  BLS, NIST        │
               │  Vermeulen)  │    └──────────────────┘
               └──────────────┘
```

---

## Связанные страницы вики

- [[ekonometricheskie-issledovaniya-rynka-nedvizhimosti-2020-2026|Обзор эконометрических исследований рынка недвижимости 2020–2026]]
- [[zhilischnaya-inflyaciya|Жилищная инфляция]]
- [[dostupnost-zhilya|Доступность жилья]]
- [[lgotnaya-ipoteka|Льготная ипотека]]

---

## Следующий шаг

Готов загрузить любую из этих работ. Пришли ссылки на PDF (arXiv, NBER, SSRN, journal sites) или укажи приоритет — начну с Tier 1.
