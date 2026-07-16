---
title: Канал кредитных ограничений (collateral constraint)
created: 2026-07-16
updated: 2026-07-16
type: concept
tags: [collateral-constraint, mortgage, monetary-policy]
sources: [raw/papers/workpapers-monetary-policy/iacoviello-2005-house-prices.md]
confidence: high
---

# Канал кредитных ограничений (collateral constraint channel)

## Определение

Кредитное ограничение, обеспеченное стоимостью жилья — механизм, при котором
заёмная способность домохозяйств определяется стоимостью их недвижимого
имущества: чем выше цена жилья, тем больше можно занять под залог, тем выше
потребление.

## Модель Iacoviello (2005)

Matteo Iacoviello в статье "House Prices, Borrowing Constraints, and Monetary
Policy in the Business Cycle" (AER, 2005, ~3 940 цитирований) формализовал этот
канал в DSGE-модели с двумя типами домохозяйств:

1. **Заёмщики (borrowers)** — face collateral constraints, имеют высокую
   предельную склонность к потреблению (MPC). Занимают под залог жилья.

2. **Кредиторы (lenders)** — не face constraints, сберегают, имеют низкий MPC.

Ключевой механизм:

$$q_t \uparrow \Rightarrow \text{borrowing capacity} \uparrow \Rightarrow C_t \uparrow \Rightarrow Y_t \uparrow$$

где $q_t$ — real house prices.

### Амплификация и передача

- **Шок спроса**: рост цен на жильё увеличивает borrowing capacity заёмщиков →
  потребление растёт ещё сильнее → положительная обратная связь. Модель
  описывает **усилитель** (accelerator) demand shocks.

- **Шок предложения**: в модели с номинальным долгом, рост издержек производства
  → снижение цен на товары → увеличение реальной стоимости долга заёмщиков →
  снижение borrowing capacity. Это "decelerator" — номинальный долг
  **стабилизирует** экономику при supply shocks.

### Оценка параметров

Iacoviello оценивает модель через минимизацию расстояния между импульсными
функциями модели и VAR (GDP, inflation, house prices, Fed Funds rate, 1974Q1–2003Q2).
Результаты:
- Collateral constraints dramatically improve response of aggregate demand to
  housing price shocks
- Nominal debt improves sluggish response of output to inflation surprises

## Политические выводы Iacoviello

1. **Монетарной политике НЕ выгодно напрямую реагировать на цены жилья** —
   включение house prices в Taylor rule даёт незначительные gains в стабилизации
   output и inflation.

2. **Номинальный (vs индексированный) долг улучшает trade-off output-inflation** —
   потому что источники trade-off в модели не усиливаются: shocks transfer
   resources from lenders to borrowers during downturn.

## Связь с российским контекстом

В России канал кредитных ограничений проявляется через:
- [[lgotnaya-ipoteka|Льготную ипотеку]] — субсидированная ставка снижает
  платёж, но не relaxing collateral constraint (домохозяйство уже имеет жильё
  в залоге)
- Оценку стоимости жилья банками — при падающих ценах banks tighten LTV
  ratios, что усиливает спад

См. также: [[bank-rossii|ЦБ РФ]], [[effekt-zamesheniya|эффект замещения]],
[[transmisionnyi-mehanizm-dkp-zhile|трансмиссионный механизм]]

^[raw/papers/workpapers-monetary-policy/iacoviello-2005-house-prices.md]
