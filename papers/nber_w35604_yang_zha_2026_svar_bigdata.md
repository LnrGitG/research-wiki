---
title: "Algorithm-Driven SVARs: Navigating the Wilderness of Big Data"
authors: "Yucheng Yang, Tao Zha"
year: 2026
publisher: "NBER"
type: working-paper
nber_id: w35604
doi: "10.3386/w35604"
url: "https://www.nber.org/papers/w35604"
pdf: null  # gated
pages: null  # PDF недоступен
jel: [C32, E44, E52]
programs: [Money and Interest Rates, Economic Fluctuations and Growth, International Finance and Macroeconomics]
tags: [SVAR, Bayesian, monetary-policy, credit-spread, housing, transmission, big-data, variable-selection, proxy-SVAR, methodology]
created: 2026-08-14
updated: 2026-08-14
status: stub  # PDF gated by NBER
---

# Algorithm-Driven SVARs: Navigating the Wilderness of Big Data

**NBER Working Paper No. 35604, August 2026**

**Authors:** Yucheng Yang, Tao Zha

**DOI:** [10.3386/w35604](https://doi.org/10.3386/w35604)

**NBER Programs:** Money and Interest Rates; Economic Fluctuations and Growth; International Finance and Macroeconomics

> ⚠️ PDF недоступен (NBER gated access). Файл не сохранён в `raw/papers/`.

## Аннотация (англ.)

Every SVAR result is conditional on two choices: the restrictions that identify the shock and the variables on which they operate. The literature disciplines the first; the second is chosen by hand. We develop a Bayesian methodology that constructs information sets, uses an out-of-sample criterion, and retains the largest system it admits. Under recursive identification, output rises with housing production rather than household credit alone. For monetary policy, an anchor-free joint Bayesian proxy SVAR with multiple instruments strengthens the credit spread channel. A core system augmented with the selected corporate spread identifies expected default risk as a potent transmission margin.

## Перевод аннотации (RU)

Каждый результат SVAR обусловлен двумя выборами: ограничениями, идентифицирующими шок, и переменными, на которые они действуют. Литература дисциплинирует первый; второй выбирается вручную. Мы разрабатываем байесовскую методологию, которая конструирует информационные множества, использует внеконтрольный критерий (out-of-sample) и сохраняет наибольшую систему, которую она допускает. При рекурсивной идентификации выпуск растёт вместе с жилищным строительством, а не только с кредитованием домохозяйств. Для денежно-кредитной политики связанная байесовская proxy-SVAR без якоря с множественными инструментами усиливает канал кредитного спреда. Базовая система, дополненная выбранным корпоративным спредом, идентифицирует ожидаемый риск дефолта как мощный маржинальный канал трансмиссии.

## Ключевые тезисы

1. **Проблема выбора переменных в SVAR:** литература контролирует ограничения (идентификация), но выбор переменных для системы остаётся субъективным («by hand»). Это потенциальный источник необоснованных результатов.

2. **Байесовская методология отбора:** алгоритм конструирует информационные множества, использует out-of-sample критерий и сохраняет максимально большую систему — автоматизирует то, что обычно делает исследователь вручную.

3. **Жильё и выпуск:** при рекурсивной идентификации **выпуск растёт с жилищным производством**, а не только с кредитованием домохозяйств — это разделяет реальный (строительство) и финансовый (кредит) каналы.

4. **ДКП и кредитный спред:** anchor-free joint Bayesian proxy SVAR с множественными инструментами усиливает канал кредитного спреда. Корпоративный спред идентифицирует ожидаемый риск дефолта как канал трансмиссии.

## Релевантность для исследования

| Аспект | Связь |
|--------|-------|
| **Жильё и рост** | Прямая: «output rises with housing production rather than household credit alone» — разделяет вклад строительства vs кредитования |
| **ДКП трансмиссия** | Кредитный спред и риск дефолта как канал — связан с исследованием ценовой загадки ЦБ РФ |
| **Методология SVAR** | Автоматизация выбора переменных — применима к оценке вклада строительства в рост через SVAR |
| **Bayesian proxy SVAR** | Множественные инструменты — релевантно для идентификации шоков жилищного строительства |

## Связи

- `papers/nber_w35588_galiani_2026_ai_econometric_coding.md` — AI в эконометрике (методология)
- `concepts/econometric-models-housing-market.md` — эконометрические модели жилья
- `papers/cbr_2026_economic_growth_factors.md` — факторы роста (ЦБ РФ)
- Тема: SVAR, переменный отбор, жилищное строительство и выпуск, трансмиссия ДКП

## Acknowledgements

We thank Lukas Hack, Tom Sargent, and participants at various seminars and conferences for helpful discussions, as well as Tong Xu for his initial involvement in this project. Hongyi Fu provided outstanding research assistance.