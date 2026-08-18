---
title: "Algorithm-Driven SVARs: Navigating the Wilderness of Big Data"
authors: "Yucheng Yang, Tao Zha"
year: 2026
publisher: "NBER"
type: working-paper
nber_id: w35604
doi: "10.3386/w35604"
url: "https://www.nber.org/papers/w35604"
pdf: "raw/papers/nber_w35604_yang_zha_2026_svar_bigdata.pdf"
pages: 91
jel: [C11, C32, C52, C55, E44, E52]
programs: [Money and Interest Rates, Economic Fluctuations and Growth, International Finance and Macroeconomics]
tags: [SVAR, Bayesian, monetary-policy, credit-spread, housing, housing-production, transmission, big-data, variable-selection, proxy-SVAR, out-of-sample, identification, Leamer, default-risk, methodology]
created: 2026-08-14
updated: 2026-08-14
---

# Algorithm-Driven SVARs: Navigating the Wilderness of Big Data

**NBER Working Paper No. 35604, August 2026**

**Authors:** Yucheng Yang (University of Zurich), Tao Zha (Emory University, FRB Atlanta, NBER)

**DOI:** [10.3386/w35604](https://doi.org/10.3386/w35604)

**Code:** https://tzha.net/code/

**JEL:** C11, C32, C52, C55, E44, E52

## Аннотация (англ.)

Every SVAR result is conditional on two choices: the restrictions that identify the shock and the variables on which they operate. The literature disciplines the first; the second is chosen by hand. We develop a Bayesian methodology that constructs information sets, uses an out-of-sample criterion, and retains the largest system it admits. Under recursive identification, output rises with housing production rather than household credit alone. For monetary policy, an anchor-free joint Bayesian proxy SVAR with multiple instruments strengthens the credit spread channel. A core system augmented with the selected corporate spread identifies expected default risk as a potent transmission margin.

## Перевод аннотации (RU)

Каждый результат SVAR обусловлен двумя выборами: ограничениями, идентифицирующими шок, и переменными, на которые они действуют. Литература дисциплинирует первый; второй выбирается вручную. Мы разрабатываем байесовскую методологию, которая конструирует информационные множества, использует out-of-sample критерий и сохраняет наибольшую систему, которую она допускает. При рекурсивной идентификации выпуск растёт вместе с жилищным строительством, а не только с кредитованием домохозяйств. Для денежно-кредитной политики связанная байесовская proxy-SVAR без якоря с множественными инструментами усиливает канал кредитного спреда. Базовая система, дополненная выбранным корпоративным спредом, идентифицирует ожидаемый риск дефолта как мощный канал трансмиссии.

## Методология

### Компонент 1: Конструирование информационного множества

- Исследователь задаёт: экономический вопрос, core-переменные, идентифицирующие ограничения
- Алгоритм конструирует surrounding information set
- Итеративная процедура: на каждой итерации оценивается текущий SVAR → вычисляются composite disturbances → auxiliary optimization определяет, содержат ли переменные вне системы предсказательную информацию для этих disturbances
- Отобранные переменные входят в систему, SVAR переоценивается, disturbances обновляются
- Процедура останавливается, когда ни одна переменная не входит → terminal information set
- Различные значения параметра сложности модели → terminal systems разной размерности

### Компонент 2: Bayesian OOS (out-of-sample) критерий

- Validation sample (не участвует в конструировании) оценивает прогнозы core-переменных
- Для каждой loss function правило сохраняет системы, достоверно лучшие reference
- Финальное правило: выбирает наибольшую систему в объединении сохранённых множеств (under squared and absolute loss)

### Теоретические гарантии

- Finite termination
- Uniqueness of construction path and terminal system
- Exact stopping characterization
- Invariance to measurement units of remaining candidates
- Stability under small numerical perturbations
- Existence and uniqueness of OOS-selected system

## Приложение 1: Кредитование домохозяйств и жильё

### Исходная система: MSV (Mian, Sufi, Verner 2020)
- Core: household credit, output, tradables/non-tradables
- Результат MSV: шок кредитования домохозяйств → рост выпуска

### Результат алгоритма

**Алгоритм отбирает 13-переменную систему** (включая 4 показателя жилищного строительства):
- Industrial production (IP)
- Commercial & industrial loans (BC)
- Consumer & real estate loans (HHC)
- Hours in goods-producing industries (HRS-G)
- **Housing starts in the South (HS-S)**
- **New housing permits, Northeast (PER-NE)**
- **New housing permits (PER)**
- **New housing permits, West (PER-W)**
- 1-year Treasury minus fed funds rate (T1Y-FF)
- Excess bond premium (EBP)
- GZ corporate bond spread (GZS)
- Hours in manufacturing (HRS-M)
- Initial claims for unemployment insurance (UI)

### Ключевой результат

> **A household credit shock raises household credit, but the posterior median of output shows no meaningful initial boom and all four measures of housing production decline.**

> **A separate housing production shock raises permits, starts, industrial production, and household credit together. Within the selected system, output rises when housing production expands and does not rise when household credit expands while housing production contracts.**

Этот результат:
1. Устойчив под обеими идентификациями: recursive (MSV) и heteroskedasticity (BPSS)
2. Разделяет жилищное строительство от кредитования домохозяйств без приписывания примитивной причины
3. **Модели жилищного кредита и делового цикла должны позволять жилищному строительству двигаться отдельно от кредитования домохозяйств**

## Приложение 2: Денежно-кредитная политика

### Исходная система: GK (Gertler & Karadi 2015)
- Core: 6 переменных GK, один внешний инструмент
- Anchor: innovation в 1-летней Treasury ставке

### Метод: Anchor-free joint Bayesian proxy SVAR
- Три инструмента Swanson (2021): federal funds rate, forward guidance, large-scale asset purchases
- Идентификационная теорема: вектор внешних инструментов идентифицирует один шок ⟺ хотя бы один инструмент коррелирован с этим шоком
- Не требует reduced-form innovation anchor

### Результат

- Алгоритм отбирает **19-переменную систему** (не плотную лестницу Treasury rates, а различные margins: labour market, housing, external, commodity, equity valuation, volatility, credit, liquidity)
- В системе с GZ spread: tightening ДКП повышает **и** excess bond premium **и** expected default risk
- Joint estimation с 3 инструментами и без anchor **усиливает** центральный кредитный канал GK
- Selected corporate spread идентифицирует expected default risk как канал трансмиссии

## Ключевые тезисы для исследования

1. **Жильё → рост, а не кредит → рост:** «output rises with housing production rather than household credit alone» — разделяет реальный (строительство) и финансовый (кредит) каналы

2. **Информационное множество = часть evidence:** выбор переменных в SVAR не предварительная «домашняя работа», а часть результата. Hand-selection в эпоху big data «no longer defensible»

3. **Дисциплина для information set:** «Identification has long been disciplined. In the age of big data, the information set deserves the same discipline»

4. **Модульность:** framework допускает alternative optimization criteria, loss functions, proper scoring rules, latent factors

5. **Кредитный спред как канал ДКП:** corporate spread = expected default risk + excess bond premium; tightening повышает оба компонента

## Релевантность для исследования

| Аспект | Связь |
|--------|-------|
| **Жильё и рост** | **Прямая:** «output rises with housing production, not household credit alone» — центральный тезис для исследования вклада строительства в рост |
| **SVAR методология** | Автоматизация выбора переменных применима к оценке вклада строительства через SVAR на российских данных |
| **ДКП трансмиссия** | Кредитный спред и риск дефолта как канал — связан с исследованием ценовой загадки ЦБ РФ |
| **Bayesian proxy SVAR** | Множественные инструменты без anchor — применимо к идентификации шоков ДКП в России |
| **Housing production vs credit** | Разделение реального и финансового каналов — основа для декомпозиции вклада строительства |

## Связи

- `papers/nber_w35588_galiani_2026_ai_econometric_coding.md` — AI в эконометрике (методология)
- `concepts/econometric-models-housing-market.md` — эконометрические модели жилья
- `papers/cbr_2026_economic_growth_factors.md` — факторы роста (ЦБ РФ)
- `concepts/research-ideas-russia-housing.md` — план исследования
- Leamer (1978) — концептуальная основа: model selection как часть inference

## Acknowledgements

We thank Lukas Hack, Tom Sargent, and participants at various seminars and conferences for helpful discussions, as well as Tong Xu for his initial involvement in this project. Hongyi Fu provided outstanding research assistance. The views expressed herein are those of the authors and do not necessarily reflect those of the Federal Reserve Bank of Atlanta, the Federal Reserve System, or the National Bureau of Economic Research.