---
title: Данные и источники для эконометрического моделирования рынка жилья
type: concept
created: 2026-07-31
updated: 2026-07-31
tags:
  - data
  - sources
  - econometrics
  - housing
  - mortgage
  - construction
sources:
  - concepts/econometric-models-housing-market
  - papers/glaeser-gyourko-2018-housing-supply-jep
confidence: high
---

# Данные и источники для эконометрического моделирования рынка жилья

Справочник источников данных, переменных и особенностей сбора, используемых в эконометрических моделях рынка жилья. Основан на анализе ~180+ статей коллекции.

---

## 1. Основные категории показателей

### 1.1. Зависимые переменные (целевые)

| Показатель | Обозначение в моделях | Источники | Частота | Примечания |
|-----------|----------------------|-----------|---------|------------|
| **Индекс цен на жильё (номинальный/реальный)** | HPI, RHPI, log(HPI) | FHFA, S&P/Case-Shiller, OECD, BIS, Eurostat, Rосстат | Monthly/Quarterly | Дефлирование: CPI (HPI/CPI) |
| **Арендные ставки** | Rent, ZRI, asking rent | Zillow, RealPage, BLS (OER), Census | Monthly/Quarterly | OER — Owner's Equivalent Rent, CPI компонента |
| **Цена сделки** | SalePrice, median price | NAR, CoreLogic, ZTRAX | Monthly | Медианные vs повторные продажи |
| **Объёмы продаж** | Sales, transactions | NAR, Census (new homes), CoreLogic | Monthly | Existing vs new home sales |
| **Жилищное строительство** | Starts, permits, completions | Census (Building Permits Survey), HUD | Monthly | Разрешения — ведущий индикатор для starts |
| **Инвестиции в жильё** | Residential Investment | BEA (NIPA), Росстат | Quarterly | Компонента ВВП |
| **Доля собственного жилья** | Homeownership rate | Census (CPS/HVS) | Quarterly | Вариация по регионам |
| **Доступность жилья** | P/MPPC, P/Rent, P/Income, NAR Affordability Index | Собственные расчёты (Glaeser-Gyourko 2018), NAR, OECD | Annual/Quarterly | P/MPPC = Tobin's q для жилья |

### 1.2. Объясняющие переменные

#### Макроэкономические

| Показатель | Роль в моделях | Источники | Частота |
|-----------|---------------|-----------|---------|
| **ВВП / GDP** | Экономическая активность, спрос | BEA, Eurostat, Росстат, Росстат | Quarterly |
| **Промышленное производство** | Альтернатива GDP для высокочастотных моделей | FRB, Eurostat | Monthly |
| **Доходы населения** | Доступность, спрос | BLS (CPS), BEA (PI), Росстат | Quarterly/Annual |
| **Занятость / безработица** | Макроконтроль, риск-фактор | BLS, Eurostat, Росстат | Monthly |
| **Инфляция (CPI)** | Дефлятор, user cost | BLS, Eurostat, Росстат | Monthly |
| **Инфляционные ожидания** | Формирование цен, монетарная трансмиссия | SPF, Michigan Survey, ЦБ РФ | Quarterly |
| **Численность населения** | Долгосрочный спрос | Census, Eurostat, Росстат | Annual |

#### Монетарные и финансовые

| Показатель | Роль в моделях | Источники | Частота |
|-----------|---------------|-----------|---------|
| **Ключевая ставка ЦБ** | Канал ДКП | ФРС, ЕЦБ, ЦБ РФ | Monthly (даты заседаний) |
| **Денежная масса (M2)** | Канал ликвидности | ФРС, ЕЦБ, ЦБ РФ | Monthly |
| **Кредитные агрегаты** | Кредитный канал | ФРС (H.8), ЕЦБ (MFI), ЦБ РФ | Monthly |
| **Ипотечные ставки** | User cost, доступность | Freddie Mac (PMMS), MBA, ЦБ РФ | Weekly/Monthly |
| **Ипотечный кредит** | Объёмы выдачи | MBA (weekly), ЦБ РФ (monthly), FHA | Weekly/Monthly |
| **CDS-спред (суверенный/банковский)** | Риск, финансовый стресс | Datastream, Markit | Daily |
| **Долгосрочные ставки (10Y)** | User cost, альтернативная доходность | FRB, ECB, Bloomberg | Daily |
| **Финансовый стресс / uncertainty** | Контроль риска | MNB FISS, CISS/ECB, EPU, SFSI | Monthly/Weekly |

#### Жилищно-строительные

| Показатель | Роль в моделях | Источники | Частота |
|-----------|---------------|-----------|---------|
| **Запасы жилья (housing stock)** | Stock-flow balance | Census (decennial), ACS | Annual |
| **Строительство (starts/permits)** | Предложение (supply), эластичность | Census, HUD | Monthly |
| **Ввод жилья (completions)** | Фактическое предложение | Census, Росстат | Monthly |
| **Объём незавершённого строительства** | Циклический индикатор | Census, Росстат | Monthly |
| **Доля ипотечных сделок** | Структура финансирования | MBA, ЦБ РФ, ДОМ.РФ | Monthly |
| **LTV, DSTI** | Кредитные ограничения | Survey of Consumer Finances, ЦБ РФ | Annual/Quarterly |
| **Просрочки / foreclosures** | Риск финансовой стабильности | MBA (delinquency survey), CoreLogic, ЦБ РФ | Monthly/Quarterly |
| **Предложение земли (land supply)** | Географические ограничения | Saiz 2010 (геоданные), WRLURI | Static (cross-section) |

---

## 2. Основные источники данных

### 2.1. Международные организации

| Источник | Ссылка | Данные | Покрытие | Частота | Доступ |
|----------|--------|--------|----------|---------|--------|
| **BIS** | `bis.org/statistics/pp.htm` | Property price statistics, credit aggregates | 60+ стран | Quarterly | Бесплатно |
| **OECD** | `oecd.org/housing` | Housing prices, affordability ratios | 40 стран | Quarterly | Бесплатно |
| **IMF IFS** | `data.imf.org` | Макро-финансовые ряды | 190+ стран | Monthly/Quarterly | Бесплатно |
| **IMF Global Housing Watch** | `imf.org/en/Topics/housing` | HPI, affordability, policy | 50+ стран | Quarterly | Бесплатно |
| **World Bank** | `databank.worldbank.org` | Доходы, население, Gini | 200+ стран | Annual | Бесплатно |
| **Eurostat** | `ec.europa.eu/eurostat` | HPI, CPI, GDP, population | EU + EA | Monthly/Quarterly | Бесплатно |
| **ECB Statistical Data Warehouse** | `sdw.ecb.europa.eu` | MFI rates, credit, HPI | EA | Monthly | Бесплатно |
| **BIS Residential Property Price** | `bis.org/statistics/pp.htm` | Long-run HPI (с 1970) | 60+ стран | Quarterly | Бесплатно |

### 2.2. США

| Источник | Ссылка | Данные | Частота | Доступ |
|----------|--------|--------|---------|--------|
| **FRED (St. Louis Fed)** | `fred.stlouisfed.org` | ~850 000 рядов: GDP, CPI, interest rates, credit, HPI | Daily/Monthly | **Бесплатно, API** |
| **FHFA HPI** | `fhfa.gov/Data` | Повторные продажи, state/MSA-уровень | Quarterly | Бесплатно |
| **S&P/CoreLogic Case-Shiller** | `spglobal.com/spdji` | 20 MSA, национальный (с 1890) | Monthly | Подписка (частично FRED) |
| **Census Bureau** | `census.gov` | Housing starts, permits, CPS | Monthly | Бесплатно |
| **BLS** | `bls.gov` | CPI (shelter), employment, wages | Monthly | Бесплатно |
| **HUD SOCDS** | `huduser.gov/portal/datasets/socda.html` | Building permits by MSA | Up to 2020 | Бесплатно, discontinued |
| **NAR** | `nar.realtor` | Existing home sales, prices | Monthly | Бесплатно |
| **MBA** | `mba.org` | Mortgage applications, delinquency | Weekly/Quarterly | Подписка (частично FRED) |
| **Freddie Mac PMMS** | `freddiemac.com/pmms` | Primary Mortgage Market Survey (30Y, 15Y, 5/1 ARM) | Weekly | Бесплатно |
| **Zillow Research** | `zillow.com/research` | Zillow Home Value Index (ZHVI), ZRI, ZORI | Monthly | Бесплатно (API неофиц.) |
| **CoreLogic** | `corelogic.com` | HPI, delinquencies, foreclosure | Monthly | Подписка |
| **ATTOM Data Solutions** | — | Ипотечные сделки, CTM | Monthly | Подписка |
| **American Housing Survey** | `census.gov/programs-surveys/ahs` | Микроданные по жилью (sqft, age, cost) | Biannual | Бесплатно |
| **Survey of Consumer Finances** | `federalreserve.gov/econres/scfindex.htm` | Net worth, home equity, LTV | Triennial (с 1983) | Бесплатно |
| **Panel Study of Income Dynamics** | `psidonline.isr.umich.edu` | Панельная динамика богатства, жилья | Biennial | Бесплатно (регистрация) |
| **SCE (NY Fed)** | `newyorkfed.org/microeconomics/hhdc` | Ожидания цен на жильё, инфляционные ожидания | Monthly | Бесплатно |
| **University of Michigan Survey** | `data.sca.isr.umich.edu` | Инфляционные ожидания, ожидания цен | Monthly | Бесплатно (регистрация) |

### 2.3. Великобритания / Европа

| Источник | Ссылка | Данные | Частота | Доступ |
|----------|--------|--------|---------|--------|
| **Nationwide HPI** | `nationwidehousepriceindex.co.uk` | UK HPI, regional | Monthly | Бесплатно |
| **Halifax HPI** | `lloydsbankinggroup.com` | UK HPI, regional | Monthly | Бесплатно |
| **UK HPI (gov.uk)** | `gov.uk/government/collections/uk-house-price-index` | Land Registry, official | Monthly | Бесплатно |
| **Bank of England** | `bankofengland.co.uk/statistics` | Mortgage approvals, rates | Monthly | Бесплатно |
| **Office for National Statistics** | `ons.gov.uk` | CPI, GDP, population, housing | Monthly/Quarterly | Бесплатно |
| **Banque de France** | `banque-france.fr` | Credit, housing, financial stability | Monthly | Бесплатно |
| **Deutsche Bundesbank** | `bundesbank.de` | Macro, credit, property | Monthly | Бесплатно |
| **Banca d'Italia** | `bancaditalia.it` | Housing market data | Quarterly | Бесплатно |

### 2.4. Россия

| Источник | Ссылка | Данные | Частота | Доступ |
|----------|--------|--------|---------|--------|
| **Росстат** | `rosstat.gov.ru` | Цены на жильё (первичка/вторичка), строительство (starts/completions), доходы, CPI | Monthly/Quarterly | Бесплатно |
| **Банк России (ЦБ РФ)** | `cbr.ru/statistics` | Ипотека (ставки, объёмы выдачи, задолженность), ключевая ставка, кредитные агрегаты | Monthly | Бесплатно |
| **ДОМ.РФ / наш.дом.рф** | `xn--80az8a.xn--d1aqf.xn--p1ai/аналитика/статистические_ряды`, `наш.дом.рф` | Ипотечный калькулятор, статистические ряды (цены на жильё, ввод, ипотека), аналитика, счета эскроу, реестр новостроек | Monthly/Quarterly | Бесплатно (сайт защищён WAF, для автоматизации — ручной экспорт) |
| **ЕИСЖС (наш.дом.рф)** | `наш.дом.рф` | Реестр новостроек, счета эскроу | Monthly | Бесплатно (API) |
| **ЦИАН / Авито** | `cian.ru`, `avito.ru` | Цены предложения, объявления | Daily | API (частично платный) |
| **РАСК (рейтинговое агентство строительства)** | — | Качество данных по строительной отрасли | Quarterly | Бесплатно |
| **АКРА / НРА** | `acra-ratings.ru` | Обзоры рынка жилья и девелоперов | Quarterly | Бесплатно |
| **Strategy Partners** | — | Исследования рынка стротельства | Annual | Бесплатно |
| **Sherpa Group** | — | Региональная аналитика строительства | Quarterly | Бесплатно |
| **РЭБ (RLMS-HSE)** | `rlms-hse.cpc.unc.edu` | Домохозяйства, жилищные условия | Biennial | Бесплатно (регистрация) |

### 2.5. Альтернативные / Big Data

| Источник | Данные | Покрытие | Частота | Доступ |
|----------|--------|----------|---------|--------|
| **Google Trends** | Поисковые запросы (ипотека, цены жилья) | Страны, регионы | Daily/Weekly | Бесплатно (gtrendsR) |
| **Zillow Transaction Data (ZTRAX)** | Сделки, оценки, mortgages | США, ~180M+ сделок | Point-in-time | Академическая подписка |
| **Redfin / Data Centre** | Listing data, 표준 | США, Canada | Daily | API |
| **RealPage** | Apartment rent, occupancy | США, 150+ MSA | Monthly | Подписка |
| **Yelp / Social Media** | Локальная экономическая активность | США | Monthly | API |
| **Satellite imagery** | Строительство, землепользование | Глобальное | Monthly/Annual | Ограниченный |
| **Geospatial (SLR, DEM)** | Рельеф, водные объекты, эластичность предл. | Глобальное | Static | Бесплатно (USGS SRTM) |

---

## 3. Классификация по частоте

| Частота | Типовые показатели | Источники |
|---------|-------------------|-----------|
| **Daily** | CDS spreads, stock indices, exchange rates, interest rate futures | Bloomberg, Datastream, FRED |
| **Weekly** | Mortgage rates (Freddie Mac PMMS), mortgage applications (MBA) | FRED, MBA |
| **Monthly** | HPI (Case-Shiller, FHFA), CPI, starts/permits, unemployment, money supply, credit | FRED, Census, BLS, BIS |
| **Quarterly** | GDP, disposable income, homeownership rate, regional HPI | BEA, Census, BIS, OECD |
| **Annual** | Population, changes in housing stock, demographics, regulatory indices | Census, ACS, Gyourko et al. |
| **Static/Cross-section** | Geographic variables (elevation, slope, water proximity, Saiz elasticity), WRLURI | Saiz 2010, Gyourko-Saiz-Summers 2008 |

---

## 4. Ключевые особенности данных

### 4.1. Проблемы качества

| Проблема | Описание | Решение |
|----------|----------|---------|
| **Публикационный лаг** | GDP, HPI публикуются с задержкой 1-3 мес. | Nowcasting / DFM / mixed-frequency |
| **Ревизии данных** | GDP неоднократно пересматривается | Real-time data vintages (ALFRED), усреднение |
| **Mixed frequency** | HPI — monthly, GDP — quarterly | MIDAS, MF-VAR, MF-BVAR |
| **Несбалансированная панель** | Разная длина рядов по странам/регионам | DFM, factor models, entropic tilting |
| **Конструктивные разрывы** | COVID (2020), GFC (2008), смена методологии | Dummy, subsamples, TVP |
| **Цензурирование / отсутствие** | Региональные цены не везде доступны | Spatial interpolation, factor models |
| **Прокси-переменные** | Цены предложения vs. цены сделок | Hedonic correction, repeat sales |
| **Эндогенность** | Цены ↔ строительство; ставки ↔ цены | IV, sign restrictions, external instruments |

### 4.2. Индексы цен на жильё: сравнение подходов

| Метод | Примеры | Плюсы | Минусы |
|-------|---------|-------|--------|
| **Repeat Sales** | S&P/Case-Shiller, FHFA | Контроль качества; только по объектам с ≥2 продажами | Смещение выборки (молодые объекты); нет новых домов |
| **Hedonic** | Census, Eurostat, Zillow ZHVI | Контроль состава жилья; можно для новой застройки | Зависимость от спецификации; требует микроданных |
| **Stratified Median** | NAR, Nationwide | Простота | Не контролирует состав |
| **Sales Price Appraisal Ratio (SPAR)** | FHFA | Комбинирует appraisal + sale | Appraisal bias |
| **Прокси: цена предложения** | ЦИАН, Авито | Высокая частота (daily); полный охват | Bias (завышение vs сделки), неликвидные объекты |

### 4.3. Доступ бесплатных vs. платных данных

```
Бесплатно: FRED, BIS, OECD, Eurostat, Census, BLS, FHFA, Freddie Mac, Zillow, Nationwide
Платно/частично: S&P/Case-Shiller (FRED → бесплатно, CoreLogic → подписка)
                 CoreLogic ZTRAX → академическая лицензия
                 Bloomberg / Datastream → подписка, но CDS можно через FRED
                 RealPage → подписка
```

---

## 5. Сбор данных для типовых исследовательских задач

### 5.1. Региональная панель цен (Россия)

```
Росстат → цены на первичном/вторичном рынке жилья по регионам (85 субъектов)
ЦБ РФ  → ипотечные ставки, объёмы выдачи по регионам
Росстат → строительство (ввод жилья), доходы, население
ДОМ.РФ → счета эскроу, льготная ипотека
```

### 5.2. Межстрановая панель (BIS/OECD)

```
BIS → property price statistics (60+ стран, quarterly, с 1970)
OECD → affordability ratios, housing prices
IMF IFS → GDP, CPI, interest rates, credit
World Bank → population, Gini
```

### 5.3. США — MSA-уровень

```
FRED → HPI (FHFA by MSA), unemployment, GDP by metro, mortgage rates
Census → starts/permits by MSA
Zillow → ZHVI, ZRI (by MSA, zip-code)
AHS → microdata (sqft, age, cost, 98 CBSAs, 1985-2013)
SCF → home equity, wealth distribution
```

### 5.4. Nowcasting / High-frequency

```
Freddie Mac PMMS → weekly mortgage rates
MBA → weekly mortgage applications
Google Trends → daily search volume
Zillow → daily/updated monthly ZHVI
FRED ALFRED → real-time vintages
```

---

## 6. API и автоматизация

| Источник | API | Пакет | Примечание |
|----------|-----|-------|------------|
| **FRED** | `api.stlouisfed.org` | `pandas-datareader`, `fredapi` | API key, бесплатный |
| **BIS** | `stats.bis.org/api` | — | REST, без ключа |
| **OECD** | `stats.oecd.org/SDMX-JSON` | `pandas-datareader` | Без ключа |
| **Eurostat** | `ec.europa.eu/eurostat/api/` | `pandas-datareader`, `eurostat` | Без ключа |
| **World Bank** | `api.worldbank.org/v2` | `pandas-datareader` | Без ключа |
| **Zillow** | RapidAPI (неоф.) | — | Ограничения |
| **ИМФ** | `data.imf.org/api` | — | JSON, без ключа |
| **Google Trends** | `trends.google.com` | `pytrends` | Без ключа, rate limits |
| **ЦБ РФ** | `cbr.ru/development/v3/opendata` | — | XML/JSON, без ключа |
| **Росстат** | `fedstat.ru`/`statdata.gks.ru` | — | XML, нестабильный |
| **ДОМ.РФ** | `xn--80az8a.xn--d1aqf.xn--p1ai/api/` | — | REST, за WAF (503/403 от автоматизации); ручной экспорт через браузер |
| **Eikon/Datastream** | — | `pandas-datareader` | Подписка |

---

## Связанные страницы

- [[concepts/econometric-models-housing-market]]
- [[concepts/regionalnaya-differenciaciya]]
- [[reviews/nowcasting-i-mixed-frequency-modeli]]
- [[reviews/favar-faktornye-modeli]]
- [[reviews/predlozhenie-i-regulirovanie-zhilya]]
- [[reviews/rossiyskie-issledovaniya-rynka-zhilya]]
- [[entities/россия-рынок]]