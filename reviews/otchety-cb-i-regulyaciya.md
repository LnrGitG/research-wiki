---
title: "Отчёты ЦБ, регуляторика и макрофинансовая стабильность — обзор кластера"
type: review
created: 2026-07-27
updated: 2026-07-27
tags: [review, central-bank, macro-financial, housing-risk, expectations, regulation]
cluster_size: 5
---

# Отчёты ЦБ, регуляторика и макрофинансовая стабильность

## О кластере

Кластер объединяет работы, которые выходят за рамки чистой эконометрики и фокусируются на **практике принятия решений ЦБ, макропруденциальной регуляторике и оценке рисков** на рынке жилья. Ядро — две статьи: [[papers/Adrian-Predicting-Downside-Risks-to-House-Prices-and-Macro-Financial-Stability-2020]] (Adrian et al., IMF 2020) и [[papers/boe-2026-house-price-expectations]] (Dhamija, Nunes, Tara, Банк Англии 2026). Первая предлагает **novel non-parametric approach** для прогнозирования downside risks к ценам на жильё (house-prices-at-risk) в 32 странах; вторая — доказывает, что домохозяйства **overweight** (придают избыточный вес) ожиданиям роста цен на жильё при формировании ожиданий по инфляции.

Между ними — два отчёта, которые добавляют контекст: [[papers/Harvard-JCHS-Americas-Rental-Housing-2024]] (ежегодный отчёт JCHS о рынках аренды) и [[papers/Effects-of-a-Mortgage-Interest-Rate-Subsidy-Evidence-from-Colombia]] (оценка влияния субсидирования ипотечных ставок в Колумбии — кейс, релевантный для понимания последствий ипотечных субсидий).

## Сводная таблица

| Статья | Тип | Метод | Данные/период | Ключевой результат |
|---|---|---|---|---|
| [[papers/Adrian-Predicting-Downside-Risks-to-House-Prices-and-Macro-Financial-Stability-2020]] | IMF WP (Adrian, Deghi, Katagiri, Shahid, Valckx) | Макро-модель + предсказательные квантильные регрессии, panel quantile regression; house-prices-at-risk | 32 развитые и развивающиеся экономики; overvaluation + excessive credit growth | Текущая переоценка жилья + избыточный рост кредита + ужесточение фин. условий совместно прогнозируют higher downside risks к росту цен через 3 года; macroprudential policy — наиболее эффективный инструмент снижения рисков на всех горизонтах |
| [[papers/boe-2026-house-price-expectations]] | SWP Банка Англии (Dhamija, Nunes, Tara, 2026) | SCE + Michigan Survey; IV (Saiz 2010 supply elasticity); двухсекторная NK модель | Опросы домохозяйств США | Домохозяйства overweight ожидания цен на жильё при формировании ожиданий по инфляции (коэффициент 25–45%, значительно выше доли жилья в CPI); эффект сильнее у домохозяйств с низкой numeracy и недавних переездов; влияет на IS-кривую и loss function ЦБ |
| [[papers/Harvard-JCHS-Americas-Rental-Housing-2024]] | Ежегодный отчёт JCHS (Harvard University) | Статистический анализ рынков аренды + сценарии | США, 2024 | Рынок аренды США находится под давлением: рекордная доля арендаторов с высокой нагрузкой (50%+ дохода на жильё); дефицит доступного жилья; влияние политики на арендные ставки растёт |
| [[papers/Effects-of-a-Mortgage-Interest-Rate-Subsidy-Evidence-from-Colombia]] | Научная статья | Различные эмпирические методы оценки субсидий | Колумбия, ипотечные программы | Субсидирование ипотечных ставок влияет на доступность и объём выдачи, но эффект частично поглощается ростом цен; оценка net benefit для целевых групп |
| [[papers/rapach-2009-forecastability]] | (дополнительно из поиска) | Prognose-тесты, комбинация прогнозов | US states | Различия в прогнозируемости цен на жильё между штатами: прибрежные штаты наименее прогнозируемы из фундаменталов |

## Основные выводы по темам

### Ожидания и инфляционный канал

[[papers/boe-2026-house-price-expectations]] — ключевая находка: **ожидания по жилью непропорционально важны для инфляционных ожиданий домохозяйств**. Домохозяйства не разделяют «потребительскую» (найм) и «активную» (собственность) компоненты цен на жильё в CPI. Это означает, что монетарная политика, нацеленная на инфляцию, должна учитывать жилищный канал: рост цен на жильё → рост инфляционных ожиданий → реакция ЦБ. В модели Банка Англии это модифицирует IS-уравнение, но не Phillips curve.

Этот механизм имеет прямое отношение к **российскому контексту**: в условиях высоких цен на жильё (рост ×2 с 2020 г. благодаря льготной ипотеке) инфляционные ожидания могут быть завышены, что влияет на реальную ставку и решения ЦБ.

### Macropруденциальная регуляция и финансовые риски

[[papers/Adrian-Predicting-Downside-Risks-to-House-Prices-and-Macro-Financial-Stability-2020]] — первый в систематическом масштабе анализ **house-prices-at-risk** (HaR). Ключевой результат:
- **Overvaluation жилья + быстрый рост кредита** = предиктор будущих кризисов
- **Macroprudential policy** (LTQ caps, stress testing) эффективнее монетарной как инструмент снижения рисков
- Монетарное смягчение снижает downside risks ТОЛЬКО в развитых экономиках

Это прямое обоснование **двойного мандата ЦБ**: инфляция + финансовая стабильность через макропруденциальные инструменты, а не через ставку.

### Субсидии и доступность жилья

[[papers/Effects-of-a-Mortgage-Interest-Rate-Subsidy-Evidence-from-Colombia]] — полезный кейс для понимания механизмов ипотечных субсидий:
- Субсидии повышают доступность, но **частично капитализируются в цены**
- Net benefit для целевых групп ниже, чем номинальная экономия по ставке
- Дизайн программы (targeting) критичен для эффективности

Аналогично российскому опыту: [[reviews/rossiyskie-issledovaniya-rynka-zhilya]] Жирнов 2025 показывает схожие механизмы.

## Противоречия и пробелы

1. **Overweight vs rational expectations**: Dhamija et al. показывают, что домохозяйства систематически overweight housing in inflation expectations. Это противоречит рациональным ожиданиям, но подтверждается эмпирически — вопрос, как интегрировать в макро-модели ЦБ.
2. **Монетарная vs макропруденциальная политика**: Adrian et al. показывают, что macroprudential эффективнее монетарной для снижения рисков — но в России макропруденциальные инструменты развиты слабо (нет стресс-тестирования LTV, нет countdown для DTI).
3. **Отсутствие российских macro-financial studies**: в кластере нет ни одной работы по РФ по теме macro-financial stability. Российские ЦБ-отчёты (Банк России — обзоры финстабильности) не включены.
4. **JCHS 2024** — описательный обзор, без новых эконометрических результатов.

## Что читать первым

1. [[papers/Adrian-Predicting-Downside-Risks-to-House-Prices-and-Macro-Financial-Stability-2020]] — наиболее методологически оригинальная: first non-parametric approach к HaR + кросс-страновая панель
2. [[papers/boe-2026-house-price-expectations]] — новая находка (overweight) с сильным дизайн-идентификацией (IV + IV heterogeneity)
3. [[papers/Effects-of-a-Mortgage-Interest-Rate-Subsidy-Evidence-from-Colombia]] — релевантный кейс субсидий для РФ
4. [[papers/Harvard-JCHS-Americas-Rental-Housing-2024]] — актуальный обзор арендного рынка

## Связанные страницы

- [[concepts/econometric-models-housing-market]]
- [[reviews/rossiyskie-issledovaniya-rynka-zhilya]]
- [[reviews/dkp-transmissiya-na-rynok-zhilya]]
- [[concepts/transmisionnyi-mehanizm-dkp-zhile]]