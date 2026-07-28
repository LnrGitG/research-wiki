---
title: "Taylor 2007 — Жильё и монетарная политика: от Great Moderation к subprime-краху"
type: annotation
created: 2026-07-27
updated: 2026-07-27
tags: [annotation, taylor-rule, housing-cycle, subprime, monetary-policy, классика]
source: "[[papers/taylor-2007-housing-monetary-policy]]"
authors: "John B. Taylor (Stanford / NBER)"
journal: "NBER WP 13682 (2007); Symposium KC Fed Jackson Hole"
citations: "~700 (Taylor rule + housing cycle)"
---

# Taylor 2007 — Жильё и монетарная политика

## Суть в одном абзаце

**Контрфактуальный анализ**: если бы ФРС следовала Taylor rule (1.5 × инфляция + 0.5 × выпуск) 2002–2006 вместо реального курса ставок, housing starts были бы в 2 раза ниже, а цены на жильё не выросли бы на 10% в год. Экстремально низкие ставки 2002–2005 → бум строительства → рост цен на 20%+ (Case-Shiller) → всплеск субпрайм-ипотеки → дефолты → крах. **Главный вывод**: правила ДКП (Taylor rule) предотвращают жилищные пузыри; отклонение от правила = причина GFC.

## Цель

Проверить гипотезу, что отклонение ФРС от Taylor rule в 2002–2006 стало причиной жилищного бума и последующего краха субпрайм.

## Метод

- **Модель**: простое уравнение housing starts (квартильные данные США, 1959Q2–2007Q2)
  - Зависимая: housing starts (логарифм)
  - Независимая: federal funds rate (опережащий лаг)
  - **Эластичность**: semi-elasticity ≈ −8.3 (статистически значима)
- **Контрфакт**: моделирование двух сценариев (фактические ставки vs Taylor rule, smoothed с шагом 25 bp)
- **Корреляция**: корреляция между инфляцией цен на жильё и rates delinquency на субпрайм (r ≈ 0.8+)

## Ключевые результаты

1. **Great Moderation жилья**: волатильность residential investment упала с 13% (до 1980-х) до 5% (после) — связано с улучшением ДКП
2. **Отклонение 2002–2005**: фактический FFR был значительно ниже Taylor rule (аналогично турбулентным 1970-м)
3. **Бум и крах в модели**: при Taylor rule housing starts были бы ~50% от фактических, цены не выросли бы на 10%/год
4. **Субпрайм**: низкие ставки → дешёвая ипотека → demand surge → price inflation 20%+ → delinquency/foreclosure rates падали → кредитные рейтинги завышены → при возврате к норме = крах
5. **Эластичность стабильна**: −8.3 в 1959–2007; не изменилась в пост-1984 период → секьюритизация не ослабила канал

## Контрфактуальное уравнение

```
Housing Starts_t = α + β × FFR_{t-2} + ε
β ≈ −8.3 (стандартная ошибка значима)
```

При Taylor rule (smoothed) FFR на 2002–2006:
- Реальный: 1% → 2.2% (ниже правила)
- Counterfactual: 2% → 5.25% (следовал бы правилу)
- Результат: housing starts в модели — на 50% ниже при Taylor rule

## Почему это классика

- **Прямое доказательство** связи между правилами ДКП и жилищными циклами
- Основа для всех последующих работ о **«leaning against the wind»** (реакции ЦБ на цены активов)
- Цитируется в: **Bernanke 2003** (monetary housing cycle), **Iacoviello 2005** (collateral channel), **Glaeser-Gyourko 2008** (supply bubbles)
- Связь с **кластером [[reviews/dkp-transmissiya-na-rynok-zhilya]]** (канал user cost) и **[[reviews/rossiyskie-issledovaniya-rynka-zhilya]]** (аналог: льготная ипотека = субсидированный FFR)

## Ограничения

- Простая модель housing starts — нет структуры предложения (Saiz 2010), нет кредитных ограничений (Iacoviello 2005)
- Фиксированный Taylor rule без учёта supply-side шоков
- Не включает международную трансмиссию (Corsetti 2020)
- Контрфакт — one-variable модель, без динамического general equilibrium

## Прямое значение для РФ

- **Льготная ипотека 2020–2024** = функциональный аналог экстремально низкого FFR в Тейлоре
- Жирнов 2025: льготная ипотека подняла ввод на 29% и цены на 2× — аналогично Taylor's boom
- Сворачивание льгот в середине 2024 = аналог возврата FFR к правилу — коррекция уже началась
- Вопрос для РФ: следует ли использовать Taylor-подобное «правило» для ипотечных субсидий?

## Связанные страницы

- [[concepts/econometric-models-housing-market]] — раздел ДКП и housing
- [[papers/mishkin-2007-housing-monetary-transmission]] — 6 каналов трансмиссии
- [[reviews/dkp-transmissiya-na-rynok-zhilya]] — полный обзор трансмиссии
- [[reviews/rossiyskie-issledovaniya-rynka-zhilya]] — российские субсидии