---
title: Монетарная политика и рынок жилья: комплексная библиография
created: 2026-07-16
updated: 2026-07-16
type: summary
tags: [monetary-policy, mortgage, housing-prices, literature-review]
sources:
  - raw/papers/workpapers-monetary-policy/*
  - raw/papers/russian-monetary-policy-housing/*
---

# Монетарная политика и рынок жилья: комплексная библиография

## Обзор

Документ собрал **13 ключевых исследований** (2007–2025) по взаимосвязи денежно-кредитной политики и рынка жилья. Работы охватывают три измерения:

1. **Международные теории и эмпирика** — фундаментальные модели трансмиссии ДКП к жилью
2. **Российские исследования** — оценка трансмиссионного механизма ДКП в РФ, региональная гетерогенность
3. **Макропруденциальная политика** — таргетированные инструменты для сдерживания жилищных имбалансов

Все статьи добавлены в wiki как `raw/papers/` и проанализированы в концептуальных страницах.

---

## Часть 1: Международные теории и эмпирика

### 1.1. Каналы трансмиссии и структурные модели

**Iacoviello M. (2005)** — "House Prices, Borrowing Constraints, and Monetary Policy in the Business Cycle"
- **Журнал:** American Economic Review, Vol. 95, No. 3, pp. 739-764
- **Цитирований:** ~3,940
- **Ключевой вклад:** DSGE-модель с кредитными ограничениями, обеспеченными стоимостью жилья (collateral constraints). Два типа домохозяйств: borrowers и lenders. Демонстрирует amplification demand shocks через housing wealth.
- **Выводы для политики:** 
  - Монетарной политике невыгодно напрямую реагировать на цены жилья (включение в Taylor rule даёт negligible gains)
  - Номинальный долг улучшает output-inflation trade-off для центробанка
- **Методология:** VAR (GDP, inflation, house prices, Fed Funds rate), structural estimation

**Mishkin F.S. (2007)** — "Housing and the Monetary Transmission Mechanism"
- **Источник:** Federal Reserve Bank of Kansas City (Jackson Hole Symposium)
- **Ключевой вклад:** Систематизация шести каналов трансмиссии ДКП к рынку жилья:
  1. Interest rate channel (user cost of capital)
  2. Expectations channel
  3. Housing supply channel
  4. Wealth effect channel
  5. Balance sheet / credit channel
  6. Risk-taking channel
- **Выводы:** Жилищный рынок — amplifier monetary shocks. Структура ипотечных рынков определяет скорость передачи.

**Taylor J.B. (2007)** — "Housing and Monetary Policy"
- **Источник:** NBER Working Paper No. 13682
- **Цитирований:** ~1,324
- **Ключевой вклад:** Counterfactual analysis показывает, что отклонение Fed Funds rate от правила 2002-2005 стало причиной housing boom-bust cycle
- **Эмпирика:** semi-elasticity housing starts to Fed Funds rate ≈ -8.3 (stable across periods)
- **Выводы:** Rule-based policy stabilizes housing cycle. Deviations от Taylor rule могут быть причиной имбалансов.

### 1.2. Жилищная инфляция и оптимальная ДКП (пост-пандемийные)

**Chodorow-Reich G., Mehrotra N. (2026)** — "Housing Policy, Inflation, and Monetary Policy: An Unorthodox View"
- **Источник:** Brookings Institution (February 2026)
- **Ключевой вклад:** "Unorthodox view": оптимальная монетарная политика должна игнорировать shelter inflation из-за interplay rent stickiness, inelastic housing supply, и search frictions как механизма rationing demand
- **Оспаривает три ортодоксальных тезиса:**
  1. CPI/PCE дают substantial weight rent → ЦБ должен реагировать
  2. House prices и mortgage rates НЕ входят в consumer price index
  3. Housing supply policy не влияет на conduct of monetary policy
- **Методология:** теоретический анализ + эмпирические данные 2022-2024 (mortgage rates утроились, но shelter inflation не отразил этот рост)
- **Связь с Россией:** shelter inflation в РФ (ЖКХ + rent) устойчив, не реагирует на monetary tightening — поддерживает "unorthodox view"

---

## Часть 2: Российские исследования

### 2.1. Трансмиссия ДКП к рынку жилья

**Sinyakov A., Shelovanova T. (2023/2025)** — "Demand for consumer loans in Russia: How strong is the interest rate channel of monetary policy?"
- **Источник:** Bank of Russia Working Paper No. 120 (December 2023); опубликовано как Russian Journal of Economics 11(1), pp. 47-75 (March 2025)
- **DOI:** 10.32609/j.ruje.11.145314
- **Ключевой вклад:** Первое в России исследование эластичности спроса домохозяйств по процентной ставке на микроданных (Всероссийское обследование домохозяйств по потребительским финансам, 6000+ households)
- **Основные результаты:**
  - +1 п.п. к ставке снижает вероятность обращения за кредитом на 1.5-2.3% (слабая эластичность)
  - +10 п.п. к ставке снижает вероятность вдвое (strong effect at large changes)
  - Инфляционные ожидания домохозяйств позитивно коррелируют с кредитным спросом
- **Policy implication:** Для охлаждения потребительского (и жилищного) спроса ЦБ приходится повышать ставку существенно выше, чем в странах с более эластичным спросом
- **Связь с жильём:** Слабый interest rate channel означает, что ДКП менее эффективна на рынке жилья, чем в других секторах

**Demidova O.A., Shchankina A.A. (2025)** — "Impact of key interest rate changes on mortgage rates in Russian regions"
- **Журнал:** Экономика и математические методы (РАН), Vol. 61, No. 2, pp. 75-89
- **DOI:** 10.31857/S0424738825020061
- **Данные:** 85 регионов РФ, monthly data, January 2016 – August 2023
- **Методология:** Error Correction Model (ECM); две зависимые переменные:
  - Weighted average mortgage rate (published by CBR)
  - Commercial mortgage rate (excluding subsidized programmes)
- **Ключевые результаты:**
  - До COVID (Jan 2016 – Feb 2020): долгосрочная связь между ключевой ставкой (MIACR) и ипотечными ставками в **76 регионах** (weighted average) и **61 регионе** (commercial)
  - COVID (до Feb 2022): связь распалась — только **4 региона** (weighted) и **14 регионов** (commercial)
  - SVO (до Aug 2023): **5 регионов** (weighted) и **30 регионов** (commercial)
- **Regional timing:** Европейская часть реагирует в первый месяц, Сибирь/Дальний Восток — со второго (multiple intermediaries)
- **Вывод:** Льготные программы (Льготная ипотека, семейная, дальневосточная, IT) **ослабляют передачу** ключевой ставки в ипотечные ставки. Transmission mechanism **broken** в большинстве регионов.

**Zvereva V. (2025)** — "Monetary Policy Transmission Mechanism: The Role of Household Heterogeneity and Spatial Effects"
- **Журнал:** Russian Journal of Macroeconomics and Financial Economics, Vol. 17, No. 3
- **Данные:** 81 регион РФ, January 2017 – January 2025
- **Методология:** Panel data spatial models
- **Ключевые результаты:**
  - Трансмиссия ДКП эффективнее в регионах с:
    - Высокой долей трудовых доходов (vs трансфертов)
    - Низкой долей бедности
    - Высокой долей домохозяйств, способных покупать durable goods и накапливать финансовые активы
  - **Spatial spillovers:** эффект income inequality в одном регионе переносится на соседей (миграция, секторальная специализация)
  - Несмотря на структурные шоки 2022+, transmission остаётся effective
- **Связь с жильём:** Региональная асимметрия transmission влияет на housing markets неодинаково. Единая ключевая ставка работает по-разному в 81 регионе.

**Smirnova Z. (2025)** — "Real Estate Market and Monetary Policy: Searching for Balance"
- **Источник:** Econs.online Opinions (July 18, 2025)
- **Примечание:** Opinions не отражают позицию Банка России
- **Ключевые аргументы:**
  1. **Macro-criticality:** рынок жилья макро-критичен — кризисы в housing market вызывают более глубокие падения ВВП и длятся дольше (IMF-данные)
  2. **Двойственная функция жилья:** базовая потребность + инвестиционный актив. При низких ставках стимулируются **обе функции** → transmission работает с **двойной силой**
  3. **5 каналов трансмиссии к жилью:**
     - Interest rate channel
     - Balance sheet channel
     - Wealth channel
     - Risk-taking channel
     - Expectations channel
  4. **Irrational exuberance:** channel ожиданий доминирует над risk-taking → заёмщики берут обязательства без учёта платёжеспособности; банки simplify audit standards → bubble
- **Policy implication:** Monetary policy + macroprudential policy **комплементарны**, не заменители

### 2.2. Синтез российских исследований

Концептуальная страница: [[rossiyskie-issledovaniya-transmissii-dkp]]

**Главные выводы:**
1. ДКП в России **менее эффективна** на рынке жилья, чем в странах с рыночным ипотечным кредитованием:
   - Эластичность спроса слабая (Sinyakov & Shelovanova 2023/2025)
   - Pass-through нарушен льготными программами (Demidova & Shchankina 2025)
   - Региональная асимметрия (Zvereva 2025)
2. **Двойственная функция жилья** усиливает эффект низких ставок (Smirnova 2025): investment demand + consumption demand → amplification
3. **Irrational exuberance** в России особенно силён: покупка жилья = "защита от инфляции" в массовом сознании
4. **Policy implication:** ЦБ РФ вынужден:
   - Использовать макропруденциальные инструменты (см. Часть 3)
   - Повышать ставку выше, чем требовалось бы без льготных программ
   - Учитывать региональную гетерогенность при calibration

---

## Часть 3: Макропруденциальная политика

### 3.1. Международный опыт

**Kuttner K.N., Shim I. (2013)** — "Can non-interest rate policies stabilise housing markets? Evidence from a panel of 57 economies"
- **Источник:** BIS Working Papers No. 433 (November 2013)
- **Данные:** 57 стран, 1980–2012
- **Методология:** Panel regressions, mean group estimator, panel event study
- **Обследованы 9 инструментов:** DSTI limits, LTV limits, housing supply exposure limits, housing-related taxes, reserve requirements, liquidity requirements, credit growth limits, foreign currency lending limits, dynamic provisioning
- **Ключевые результаты:**
  1. **DSTI limits** — наиболее consistent tool для снижения роста ипотечного кредитования (+4-7 п.п. за 4 квартала)
  2. **Housing-related taxes** — единственный инструмент с значимым влиянием на **цены** жилья
  3. **LTV limits** — работают в panel regressions, но неустойчивы в mean group/event study (возможно из-за эндогенности или обхода)
  4. Reserve requirements, credit growth limits — менее специфичны для жилья
  5. Foreign currency limits — effective в emerging markets
- **Policy implication:** Monetary policy = blunt tool for housing; macroprudential tools = targeted. Compelmentary use most effective.

### 3.2. Российский опыт

**Центральный банк РФ (April 2025)** — Press release: "Банк России принял ряд решений по макропруденциальной политике"
- **Источник:** http://www.cbr.ru/press/pr/?file=638811071460772255finstab.htm
- **Дата:** 24 апреля 2025
- **Ключевые решения:**
  1. **Макропруденциальные лимиты (МПЛ) по ипотеке на Q3 2025:**
     - Ограничение доли высокорискованных кредитов с ПДН>50%, ПДН>80%, первоначальным взносом <20%
     - Снижены с 1 июля 2025 г. макропруденциальные надбавки (после улучшения структуры выдач)
  2. **Результаты политики:**
     - Доля кредитов с ПДН>80% в ДДУ: с 46% (Q3 2023) → **3%** (Q1 2025)
     - На вторичном рынке: с 47% → **12%**
     - Первоначальный взнос <20%: с 51% → **5%** (ДДУ: с 59% → 2%)
     - Макропруденциальный буфер: 834 млрд руб (7.1% портфеля потребкредитов)
  3. **Проблемы:**
     - Доля просроченных >90 дней в ипотеке: с 0.5% (Q1 2024) → 0.9% (Q1 2025) — ухудшение (за счёт кредитов, выданных в ажиотажный период H2 2023 – H1 2024)
     - Качество потребительских кредитов: доля просрочки >30 дней >2.7% (+1.2 п.п.)

**Лаптева Е.В. (2025)** — "Оценка влияния макропруденциальной политики на сдерживание потребительского кредитования в России"
- **Журнал:** Экономический журнал Высшей школы экономики, Vol. 29, No. 4, pp. 609-642
- **DOI:** 10.17323/1813-8691-2025-29-4-609-642
- **Данные:** 591 банк, quarterly data, 2015–2021
- **Методология:** Dynamic panel data model (GMM); aggregate MPP index based on Kozlovtseva et al. (2020), extended post-2019
- **Ключевые результаты:**
  1. Макропруденциальные меры оказывают **статистически значимое сдерживающее влияние** на потребительское кредитование
  2. Эффект проявляется через **~2 квартала** после введения и сохраняется **~6 месяцев**
  3. **Асимметрия:** ужесточение более эффективно, чем смягчение
  4. **Гетерогенность:** сильнее эффект на:
     - Банках с низким депозитным фондированием
     - Меньших банках
     - Банках с низкой долей потребительских кредитов в активах
  5. Несмотря на шоки 2022-2025, transmission остаётся effective
- **Ограничения:**
  - Период не включает 2022-2025 (санкции, структурные изменения)
  - Не отделяет полностью эффекты МПП и ДКП

### 3.3. Сравнение: Россия vs международный опыт

| Измерение | International (Kuttner & Shim) | Россия |
|---|---|---|
| Наиболее эффективный инструмент | **DSTI limits** (→кредиты) и housing taxes (→цены) | **МПЛ + надбавки** (→структура выдачи) |
| Влияние на цены жилья | Только налоги | Не обследовано эмпирически |
| Скорость эффекта | 4 квартала | **2 квартала** (Lapteva 2025) |
| Роль ДКП | Комплементарна МПП | **Слабо передаётся** в ипотеку (Sinyakov 2025) |
| Роль льготной ипотеки | Не рассматривается | **Обходит** ДКП и МПП |
| Асимметрия | Не обследована | Ужесточение > смягчение (Lapteva 2025) |

**Ключевое различие:** В России МПП используется не только для ограничения рисков, но и для **компенсации слабого трансмиссионного механизма ДКП**. Поскольку [[rossiyskie-issledovaniya-transmissii-dkp|трансмиссия ДКП к рынку жилья нарушена]] (эффект замещения 60–80%, льготная ипотека), МПП становится основным инструментом сдерживания рисков.

---

## Концептуальные страницы wiki

Все работы проанализированы в следующих концептуальных страницах:

1. [[transmisionnyi-mehanizm-dkp-zhile|Трансмиссионный механизм ДКП через рынок жилья]] — Mishkin (2007): 6 каналов
2. [[collateral-constraint-channel|Канал кредитных ограничений]] — Iacoviello (2005): DSGE-модель, amplification
3. [[zhilishchnye-cikly-i-monetarnaya-politika|Жилищные циклы и монетарная политика]] — Taylor (2007): counterfactual analysis
4. [[shelter-inflation-optimal-monetary-policy|Shelter inflation и оптимальная монетарная политика]] — Chodorow-Reich & Mehrotra (2026): "unorthodox view"
5. [[rossiyskie-issledovaniya-transmissii-dkp|Российские исследования трансмиссии ДКП к рынку жилья]] — Sinyakov, Demidova, Zvereva, Smirnova (2023-2025)
6. [[macroprudentialnaya-politika-rynok-zhilya|Макропруденциальная политика на рынке жилья]] — Kuttner & Shim, ЦБ РФ, Лаптева (2013-2025)

---

## Исходные материалы (raw papers)

Все PDF/ markdown файлы сохранены в ~/research-wiki/raw/papers/:

### International (Step 1)
- `workpapers-monetary-policy/iacoviello-2005-house-prices.md` (82K chars)
- `workpapers-monetary-policy/taylor-2007-housing-monetary-policy.md` (21K chars)
- `workpapers-monetary-policy/mishkin-2007-housing-monetary-transmission.md` (123K chars)
- `workpapers-monetary-policy/chodorow-reich-mehrotra-2026-housing-policy-inflation.md` (59K chars)

### Russian (Step 2)
- `russian-monetary-policy-housing/sinyakov-cbr-wp120-2023.md` (240K chars)
- `russian-monetary-policy-housing/demidova-shchankina-2025-key-rate-mortgage.md`
- `russian-monetary-policy-housing/zvereva-2025-monetary-transmission-heterogeneity.md`
- `russian-monetary-policy-housing/smirnova-2025-real-estate-monetary-policy.md`

### Macroprudential (Step 3)
- `workpapers-monetary-policy/kuttner-shim-2013-bis-wp433.md`
- `workpapers-monetary-policy/cbr-macroprudential-2025-april.md`
- `workpapers-monetary-policy/lapteva-2025-macropudential-russia.md`

---

## Policy implications (summary)

Общий вывод из всех 13 работ:

1. **ДКП в России менее эффективна** на рынке жилья, чем в странах с рыночным ипотечным кредитованием:
   - Слабая эластичность спроса (1.5-2.3% на 1 п.п.)
   - Pass-through нарушен льготными программами (60-80% эффект замещения)
   - Региональная асимметрия (81 регион)

2. **Макропруденциальная политика** становится основным инструментом сдерживания рисков:
   - МПЛ + надбавки улучшили структуру ипотеки (ПДН>80%: с 46% → 3%)
   - Эффект проявляется через 2 квартала и сохраняется ~6 месяцев
   - Асимметрия: ужесточение > смягчение

3. **Shelter inflation** может не требовать монетарной реакции:
   - Rents sticky + inelastic supply + search frictions → optimal policy can ignore
   - В России: shelter inflation (ЖКХ + rent) устойчив, не реагирует на ДКП

4. **Двойственная функция жилья** усиливает эффект низких ставок:
   - Investment demand + consumption demand → amplification
   - "Irrational exuberance" в России особенно силён

5. **Необходимость таргетированных мер:**
   - ДКП = blunt tool для жилья (может вызвать рецессию)
   - МПП = targeted instruments (DSTI/LTV limits, housing taxes)
   - Комплементарное использование наиболее эффективно
