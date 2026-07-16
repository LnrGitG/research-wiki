# Wiki Schema

## Domain
Экономика жилья, ипотечного кредитования и рынка недвижимости — академические исследования, рабочие доклады (working papers), аналитические отчёты по доступности жилья, жилищной инфляции, государственным программам субсидирования и строительной индустрии.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `lgotnaya-ipoteka.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/papers/source-file.pdf]`
  at the end of paragraphs whose claims come from a specific source.
- **Язык:** страницы вики — на русском. Названия файлов — на английском или транслите.

## Frontmatter
```yaml
---
title: Название страницы
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/papers/source-name.pdf]
confidence: high | medium | low
contested: true                        # when unresolved contradictions
contradictions: [other-page-slug]
---
```

### raw/ Frontmatter

```yaml
---
source_url: https://example.com/paper   # original URL, if applicable
ingested: YYYY-MM-DD
sha256: <hex digest of the raw content below the frontmatter>
---
```

## Tag Taxonomy

### Рынок жилья и цены
- `housing-prices` — динамика цен на жильё, индексы, affordability
- `housing-inflation` — жилищная инфляция, факторы роста цен
- `housing-supply` — предложение жилья, строительство, ввод в эксплуатацию
- `housing-demand` — спрос на жильё, демографические факторы
- `regional-analysis` — региональные различия, конвергенция цен

### Ипотека и кредитование
- `mortgage` — ипотечное кредитование, ставки, доступность
- `subsidized-mortgage` — льготная ипотека, госпрограммы субсидирования
- `mortgage-subsidy` — субсидирование процентных ставок, налоговые вычеты
- `mortgage-default` — дефолты по ипотеке, риски

### Государственная политика
- `housing-policy` — жилищная политика, регулирование рынка
- `government-intervention` — государственное вмешательство, меры поддержки
- `tax-policy` — налоговые вычеты, фискальные меры

### Экономика и кризисы
- `economic-crisis` — экономические кризисы, шоки, влияние на рынок жилья
- `macroeconomic-factors` — макроэкономические факторы, ВВП, безработица
- `construction-industry` — строительная индустрия, инвестиции

### Методология
- `econometrics` — эконометрические методы, модели
- `cross-country` — международные сравнения, межстрановой анализ

### Денежно-кредитная политика
- `monetary-policy` — монетарная политика, ключевая ставка, трансмиссионный механизм
- `mortgage-pass-through` — передача изменений ставки ЦБ в ипотечные ставки
- `collateral-constraint` — кредитные ограничения, обеспеченные стоимостью жилья
- `housing-cycle` — циклы рынка жилья, boom-bust

### Мета
- `comparison` — сравнительный анализ
- `literature-review` — обзор литературы
- `policy-recommendation` — рекомендации для политики

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed,
add it here first, then use it. This prevents tag sprawl.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when its content is fully superseded

## Entity Pages
- Страны и регионы (Россия, Швейцария, Колумбия — если есть межстрановые сравнения)
- Госпрограммы (Льготная ипотека, Семейная ипотека, etc.)
- Организации (ЦБ РФ, ДОМ.РФ, BIS, etc.)

## Concept Pages
- Экономические концепции (жилищная инфляция, конвергенция цен, affordability)
- Механизмы политики (субсидирование ставок, налоговые вычеты, ипотечные каникулы)
- Методологические подходы (гедонические индексы, difference-in-differences, etc.)

## Comparison Pages
- Межстрановые сравнения жилищной политики
- Сравнение эффектов разных мер поддержки
- Сопоставление эконометрических подходов

## Update Policy
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
