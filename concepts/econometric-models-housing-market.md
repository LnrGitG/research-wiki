---
title: эконометрические модели жилищного рынка
created: 2026-07-16
updated: 2026-07-26
type: concept
tags:
  - models
  - econometrics
  - time-series
  - data
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
| **VAR / SVAR / BVAR** | Time-series | 5-7 | Quarterly, national/metro | ECB 2025 (SBVAR), Yunus 2012, Лысенко 2025 (РФ), **Yildirim 2025 (BSVAR, Турция)**, **Suh 2023 (Корея)**, **Drift 2024 (Bayesian, credit conditions)**, **Velasco (Bayesian, асимметрии ДКП)** |
| **FAVAR** | Time-series factor | 50-100+ series | Quarterly/monthly | **Bernanke 2003 (классика)**, **Eickmeier 2011 (TV-FAVAR)**, **Mumtaz 2011 (UK)**, **Gupta 2009 (house price inflation)**, **Gao 2022 (региональные цены)**, **Paccagnini 2017**, **Soares 2011 (ЕА)**, **Lin (high-dimensional)** |
| **Dynamic factor (DFM)** | Time-series | 50+ series | Monthly, national | RBNZ 2025, **Das 2010 (DFM vs VAM)**, **Ng (иерархический факторный анализ США)**, **Smith 2025 (NZ)**, **Yarui 2011 (DFM vs LBVAR)** |
| **DSGE + VECM** | Structural hybrid | 5-10 | Quarterly, national | Brookes et al. 2011, **Paries (DSGE, ДКП и жильё США/ЕА)** |
| **Panel FE/RE** | Panel | 1-2 | Annual/metro | Green-Malpezzi-Mayo 2005 (45 MSA), **Glindro 2008 (9 стран АТР)** |
| **Diffusion/Spatial** | Spatial econometrics | 1-3 | Quarterly, metro | Hilber-Vermeulen 2016, **Bailey 2014 (spatio-temporal, strong/weak dependence)**, **Kaas 2024 (housing boom)**, **Mattera 2025 (spatio-temporal clustering)** |
| **Cross-section (hedonic)** | Structural | 1 | Annual/metro | Saiz 2010 (26 metro IV) |
|| **Sentiment (LLM)** | ML-based | 1-2 | Text + monthly | Rogoff-Yang 2026 (China-Japan) ||
|| **Sentiment (Boolean/Keyword)** | Rule-based | 1-2 | Text + daily/weekly/monthly | **Horvath et al. 2026 (MNB WP 2026/3, Hungary SFSI)** ||
|| **Machine Learning** | ML-based | 1 | Cross-section/panel | **Qiongwei-Ye 2024 (Ames, Iowa)**, **Hao (prediction model)** ||
| **Nowcasting** | Mixed-frequency | 10-100 series | Daily/monthly | **Koop et al. 2019 (MF-VAR, UK regional)**, **Zubarev (MFBVAR, ВВП РФ)**, **Tallman-Zaman 2020 (BVAR + surveys)**, **Entropic Tilting (BVAR + nowcasts)** |
| **Agent-Based Model (ABM)** | Computational | Много агентов | Quarterly, national | Bardoscia et al. 2025 (Bank of Spain WP 2502) |
| **Growth-at-Risk (GaR)** | Quantile regressions | 1-3 | Quarterly | **Adrian 2020 (IMF, downside risks house prices)** |

## Классификация по горизонтам прогноза

| Горизонт | Модель | Пример |
|---|---|---|
| **Short-run (1-4 quarters)** | ECM, VAR/SVAR, DFM, nowcasting | Wheaton 2014, ECB 2025, RBNZ 2025, **Zubarev (MFBVAR РФ)**, **Koop 2019 (MF-VAR)** |
| **Medium-run (1-3 years)** | Stock-flow, Tobin's Q, Panel FE, FAVAR | DiPasquale-Wheaton 1994, Madsen 2011, **Gupta 2009 (FAVAR)** |
| **Long-run (5+ years)** | Asset-market, DSGE, Cross-section | Poterba 1984, Brookes 2011, Saiz 2010, **Paries (DSGE)** |

---

## 📊 Используемые показатели (анализ 105 статей коллекции)

### Частота упоминания показателей

| Показатель | Статей | Роль в моделях |
|---|---|---|
| **rent (аренда)** | 101 | User cost, imputed rent, доходность |
| **interest rate (ставка)** | 89 | Канал трансмиссии ДКП, user cost |
| **housing stock** | 88 | Stock-flow, предложение |
| **inflation** | 85 | Реальные vs номинальные цены, дефлятор |
| **demand** | 83 | Уравнение спроса |
| **GDP** | 80 | Макроконтекст, доход |
| **credit (кредит)** | 75 | Кредитный канал, LTV, ипотека |
| **construction** | 71 | Инвестиции, предложение |
| **income** | 66 | Доступность жилья, спрос |
| **supply** | 66 | Уравнение предложения |
| **house price (HPI/RHPI)** | 64+37 | Зависимая переменная |
| **unemployment** | 56 | Макроконтроль |
| **sales/transactions** | 50 | Ликвидность рынка |
| **CPI** | 49 | Дефлирование |
| **mortgage** | 48 | Ипотечный канал |
| **exchange rate** | 45 | Открытая экономика (Турция, Канада) |
| **LTV/debt** | 37+37 | Финансовые ограничения |

### Типовой набор переменных по классам моделей

**FAVAR/DFM (50-150 рядов):**
- Целевая: real house price index (национальный или региональный)
- Блоки факторов: (1) реальный сектор (GDP, industrial production, employment), (2) цены (CPI, PPI, inflation expectations), (3) монетарные (policy rate, money supply, credit aggregates), (4) финансовые (bond yields, stock indices, term spread), (5) жилищные (starts, permits, sales, mortgage rates)

**VAR/SVAR (5-7 переменных):**
- Типовой набор: house price growth, GDP growth, inflation, policy rate, credit growth (+ mortgage rate, exchange rate для открытых экономик)

**ECM/VECM:**
- Длинное уравнение: log(real HPI) ~ log(income), log(user cost), log(stock/population)
- Короткое: ΔHPI ~ EC-term + Δставки + Δкредита

---

## 🗄️ Источники данных

| Источник | Статей | Что даёт |
|---|---|---|
| **Federal Reserve / FRED** | 66/30 | US macro, ставки, кредит — де-факто стандарт |
| **Census Bureau** | 30 | Housing starts, permits, vacancies (США) |
| **ECB** | 29 | Макро ЕА, MFI loans, ставки |
| **IMF** | 28 | IFS, Global Housing Watch, макро по странам |
| **OECD** | 24 | HPI по странам, affordability ratios |
| **Bank of England** | 23 | UK macro, mortgage approvals |
| **BIS** | 20 | **BIS property price statistics** — главный источник для межстрановых сравнений цен на жильё |
| **S&P (Case-Shiller)** | 16 | S&P/CoreLogic/Case-Shiller HPI (США) |
| **Eurostat** | 14 | HPI ЕС, жилищная статистика |
| **NAR*** | — | Existing home sales (США) |
| **Нацстатистики** | ~20 | TurkStat (Турция), KOSTAT (Корея), GSO (Вьетнам), Статкомитет (Узбекистан), Росстат |

\* — автоматический подсчёт по тексту; NAR/CIAN содержат ложные срабатывания на подстроки.

### Страновое покрытие коллекции

| Регион | Статей | Специфика данных |
|---|---|---|
| **US** | 84 | Длиннейшие ряды (Case-Shiller с 1890, FHFA с 1975), MSA-уровень |
| **UK** | 68 | Nationwide/Halifax HPI, региональные панели |
| **EU/Euro Area** | 64/45 | ECB HPI, короткие ряды (с ~1995) |
| **OECD-кросс-кантри** | 24 | BIS/OECD HPI, единая методология |
| **Канада, Австралия, NZ** | 27/21/20 | CMHC, ABS, RBNZ |
| **Развивающиеся** | TR 15, ZA 19, IR 17, CN 18, VN, MA, UZ | Короткие ряды (с ~2003-2010), проблемы качества |
| **Россия** | 12 | Росстат, ЦБ; ряды с ~2000, разрывы |

---

## ⏱️ Характеристики временных рядов

### Частота наблюдений

| Частота | Статей | Типовое применение |
|---|---|---|
| **Quarterly** | 89 | Стандарт для VAR/FAVAR/структурных моделей (макроданные квартальные) |
| **Monthly** | 73 | DFM, nowcasting, HPI, ставки, Google Trends |
| **Annual** | 65 | Кросс-кантри панели, долгосрочные структурные модели |
| **Daily/Weekly** | 22/19 | Финансовые переменные, наукастинг, поисковые тренды |

### Длина выборок

- **Длинные (50+ лет)**: США (Case-Shiller 1890–, FHFA 1975–), UK (Nationwide 1952–)
- **Средние (25-50 лет)**: OECD-страны, ЕА (с 1970-80-х)
- **Короткие (15-25 лет)**: Турция (с 2003/2010), Вьетнам, ЮАР, Казахстан
- **Очень короткие (<15 лет)**: Россия (региональные HPI с ~2008), Узбекистан

### Свойства рядов и следствия для моделей

| Свойство | Диагностика | Решение |
|---|---|---|
| **Нестационарность I(1)** | ADF/KPSS: уровни цен нестационарны | Коинтеграция → VECM/ECM; или первые разности → Δlog HPI |
| **Коинтеграция** | Johansen: HPI ~ income + user cost + stock | ECM (Wheaton 2014), VECM (Yunus 2012) |
| **Структурные сдвиги** | GFC 2008, COVID 2020, режимы ДКП | TVP-FAVAR (Mumtaz 2011), sign-restriction BVAR (Лысенко 2025), TVP модели (Velasco) |
| **Асимметрия** | Реакция на шоки ≠ в бум/рецессию | Quantile regressions (Adrian 2020 GaR), нелинейные модели (Balcilar 2012) |
| **Пространственная зависимость** | Региональные цены коррелированы | Spatio-temporal (Bailey 2014), GVAR, иерархические факторные (Ng) |
| **Mixed frequency** | HPI месячный, GDP квартальный | MIDAS (12 статей), MF-VAR (Koop 2019), MFBVAR (Zubarev) |
| **Публикационный лаг** | Макроданные выходят с задержкой | Nowcasting (DFM), Entropic tilting |
| **Гетерогенность регионов** | Разные эластичности предложения | Panel FE, отдельные ECM по MSA (Wheaton 2014), Rapach 2009 (state-level forecastability) |

---

## Связи методов с исследовательскими задачами

### Ценовая динамика housing:
- **Short-run**: Shock propagation → VAR/SVAR (ECB 2025), ECM (Wheaton 2014), **BSVAR (Yildirim 2025)**
- **Medium-run**: Stock-flow equilibrium → DiPasquale-Wheaton 1994, Capozza 2002
- **Long-run**: Fundamental valuation → Asset-market (Poterba 1984), Cross-section (Saiz 2010), **Gattini 2010 (EA fundamentals)**

### Инвестиции в строительство:
- **Tobin's Q → Housing starts**: Topel-Rosen 1988 (Q = PV(marginal product) / cost)
- **Q = 1 long-run equilibrium**: If Q > 1, construction expands; if Q < 1, depreciates
- **Madsen 2011**: Q model extended to include land prices, taxes, construction costs
- **Albuquerque 2024**: housing supply channel of monetary policy

### Macro-linkages (трансмиссия ДКП → жильё):
- **Классика**: Iacoviello (Europe), Elbourne (UK), Nocera (EA), Eickmeier 2010 (housing booms)
- **Региональная гетерогенность**: Negro 2006 (US states), Fischer 2019 (US regional), Corsetti 2020 (One Money Many Markets)
- **Нестандартная ДКП**: Nsafoah (Canada, conventional vs unconventional)
- **Открытая экономика**: Bandt (international transmission), Hirata 2013 (global synchronization), Vigfusson 2017 (international MP FAVAR)
- **Развивающиеся**: Chen (China), Tabaghi 2013 (Iran), Daoui 2021 (Morocco), Lekhuleni (South Africa), Yildirim (Turkey × 2)

### Regional analysis:
- **Spatial diffusion**: Hilber-Vermeulen 2016, **Cepni (uncertainty shocks comovement)**, **Suh 2023 (Korea regional cycles)**
- **MSA heterogeneity**: Wheaton 2014, Rapach 2009 (US states), Rapach 2007 (8th District)
- **Russia**: Regional FE models — see [[концепты/региональная дифференциация]]

### Прогнозирование (forecasting literature):
- **Factor models**: Gupta (large data), Bork 2012, Das 2010/2011, Ng (hierarchical)
- **Нелинейные**: Balcilar 2012 (US regional non-linear)
- **ML**: Qiongwei-Ye 2024, Hao
- **Nowcasting**: Koop 2019, Zubarev, Tallman-Zaman 2020
- **Оценка точности**: Margaritella 2025 (equal forecast accuracy tests), Rapach (forecastability heterogeneity)

## Методологические тренды

1. **1980s-1990s**: Structural models (stock-flow, asset-market, Tobin's Q)
2. **2000s**: Time-series (ECM, VAR) + Panel (FE/RE, hedonic) + FAVAR (Bernanke 2003)
3. **2010s**: Spatial econometrics, DSGE, TV-FAVAR (Eickmeier 2011, Mumtaz 2011), Bayesian methods
4. **2020s**: ML (LLM sentiment, RF), Nowcasting (MFBVAR), SBVAR, знаковые ограничения (Лысенко 2025), GaR (Adrian 2020), ABM (Bardoscia 2025), spatio-temporal clustering (Mattera 2025)

## Проблемы идентификации

- **Endogeneity**: Price affects construction, construction affects price → IV/SVAR needed
- **Non-stationarity**: I(1) series → cointegration (ECM) or differencing
- **Heterogeneity**: Regional differences require panel FE or separate ECMs
- **Data limitations**: Short samples (особенно РФ и развивающиеся рынки), measurement error, publication lag → DFM/nowcasting
- **Structural breaks**: GFC, COVID, режимы ДКП → TVP models, subsample analysis

## Применения к российскому рынку

- **ECM/VECM**: Wheaton 2014, Yunus 2012 → Rosstat regional data
- **Stock-flow**: DiPasquale-Wheaton 1994 → Moscow/St Petersburg metro
- **FAVAR**: **Garmider (FAVAR для РФ)** → расширить на жилищный блок
- **Nowcasting**: **Zubarev (MFBVAR, наукастинг ВВП РФ)** → добавить HPI Росстата/Домклик
- **SVAR**: ECB 2025 → CBR key rate → housing → consumption transmission; Лысенко 2025 (7 шоков, знаковые ограничения)
- **Строительная тематика**: **Sternik 2018 (методика прогнозирования объёмов)**
- **Sentiment**: Rogoff-Yang 2026 → Russian RE media analysis (ЦИАН, Авито, РБК)

## Связанные страницы

- [[концепты/ценообразование-субсидии-mortgage]]
- [[концепты/жилищный-цикл-инвестиции]]
- [[концепты/региональная дифференциация]]
- [[entities/россия-рынок]]
