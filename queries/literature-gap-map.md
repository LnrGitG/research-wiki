---
title: Literature Gap Map — карта пробелов литературы для РФ-кейса
created: 2026-09-08
updated: 2026-09-08
type: query
tags: [gap-analysis, research-design, housing-supply, monetary-policy, developer-finance, nowcasting]
sources: [wiki-concepts, papers/catalog.md]
confidence: medium
---

# Literature Gap Map: что закрыто литературой, что открыто для России

Матрица «вопрос × рынок × данные»: где существующая литература даёт ответ,
где ответ не переносим на РФ, и где РФ-данные позволяют проверить то,
что не проверено нигде. Синтез поверх [[concepts/research-ideas-russia-housing|idea bank]]
и [[queries/sintez-monetarnaya-politika-i-rynok-zhilya|комплексного синтеза ДКП-жильё]].

## Матрица пробелов

| Вопрос | Международная литература | Российская литература | Статус для РФ | Источники |
|--------|--------------------------|----------------------|---------------|-----------|
| Эластичность предложения жилья | Saiz 2010 (2.6→1.3 US), Baum-Snow & Han 2024 (0.5–0.74 tract) | CMWP: 0.62–0.91 SR регионально | **Открыто**: firm-level эластичность conditional на финансовые ограничения — нет аналога в литературе | [[Saiz 2010]], [[Baum-Snow & Han 2024]] |
| Трансмиссия ДКП → цены жилья | Mishkin 2007, Iacoviello 2005, Wang 2024 (асимметрия) | Sinyakov 2025 (1.5–2.3% на 1 п.п.), Demidova 2025 (dual system 8% vs 20%+) | **Частично открыто**: асимметрия ужесточение/смягчение в РФ не оценена; Wang (2024) показывает, что сдерживающая политика сильнее — тест на данных РФ невозможен из-за одного эпизода ужесточения | [[Mishkin 2007]], [[Wang 2024]], [[Sinyakov 2025]] |
| Финансовое здоровье девелоперов → предложение | MACON 2023-2025 (descriptive), China: VeB 2026 (структурный бенчмарк) | **Пусто**: нет peer-reviewed работ по РФ | **Ключевой пробел** — панель SPARK+ЕИСЖС уникальна (2000+ дев, escrow-балансы) | [[MACON]], [[Bernanke-Gertler-Gilchrist 1996]] |
| Эффект замещения льготной ипотеки | Международный аналог — оценка субсидий (мета: 60-80% substitution) | Оценено (wiki): 60–80% | **Закрыто в статике, открыто в динамике**: контрциклическая гипотеза (эффект↓ при высоких ставках) не проверена панельно | [[effekt-zamescheniya]] |
| Макропруденциальные инструменты | Kuttner & Shim 2013 (DSTI эффективнее), ЦБ 2025 (МПЛ: 46%→3% высокорисковых) | Лаптева 2025 (лаг 2 квартала, ~6 мес длительность) | **Частично открыто**: интеракция МПЛ × эластичность предложения не исследована (Andaloussi et al. 2024 — только рамочно) | [[Kuttner & Shim 2013]], [[Лаптева 2025]] |
| Nowcasting СМР/ввод | MIDAS, FAVAR (Bernanke 2003, Bork 2012, Koop 2019) | Wordstat-композит (corr 0.63 lead-1m) | **Открыто**: смешанные данные (Wordstat + GDELT + ЕИСЖС + опендата) в одной MIDAS-модели — литературного аналога нет | [[Koop 2019]], H-001 |
| Ожидания цен жилья | Case-Shiller tradition, "irrational exuberance" | Smirnova 2025 (двойная функция жилья), hedge-мотив | **Открыто**: РФ-обследования ожиданий (ЦБ inFOM) не связаны с ценовой динамикой в одном фреймворке | [[ozhidaniya-ceny-zhilya]] |
| Cost pass-through стройматериалы → цены | Лит. разрозненна (контрактная структура) | MAX ЖБИ 2026: труд +35-38%/3гр | **Открыто**: асимметрия pass-through по типу контракта (fixed vs cost-plus) не тестировалась нигде | [[concepts/construction-productivity-regulation]] |
| Shelter inflation и optimal policy | Chodorow-Reich 2025 (ignore shelter) | Ласкин/Пупенцова 1.37%, Ко-Инвест 1.1% vs Росстат 4.1% | **Противоречие данных** (см. X-записи): расхождение индексов в 3-4 раза само по себе research question | [[shelter-inflation-optimal-monetary-policy]] |

## Приоритизированные пробелы (по ценности × доступности данных)

1. **Firm-level supply elasticity под финансовыми ограничениями** — SPARK+ЕИСЖС+ФНС опендата есть в wiki; литературы нет вообще (для любого рынка — MACON только descriptive). Публикационный потенциал: JUE/RED.
2. **Escrow-механика как exogenous cash flow shock** — уникальный институт РФ (214-ФЗ); международный аналог отсутствует → вклад в литературу о financial constraints (Hadlock-Pierce, Crouzet).
3. **Mixed-frequency nowcasting с поисковыми и GDELT-данными** — H-001 показывает сигнал (0.63 lead-1m); литература по search-data для строительства (не цен жилья) почти пуста.
4. **Двойная система ставок (льготная vs рыночная) и pass-through** — Demidova 2025 фиксирует dual system, но нет оценки, как это меняет эффективность макропруденциальных лимитов.
5. **Асимметрия ДКП на жильё РФ** — идентификация ограничена (один эпизод ужесточения 2023–2025); возможен proxy-подход через региональную вариацию (Zvereva 2025 spillovers).

## Выводы для research-wiki

- Наибольший дефицит — не в трансмиссии ДКП (закрыта синтезом), а в **предложении**: финансовое здоровье девелоперов как heterogeneity-источник эластичности.
- Два «фирменных» РФ-вклада в международную литературу: escrow-канал и firm-level эластичность — оба уже обеспечены данными из панели.
- Из gap-map напрямую извлекаются гипотезы H-002…H-006 и противоречия (см. hypotheses.yaml).

## Связи

- [[concepts/research-ideas-russia-housing]] — исходный idea bank (п. 10.4: литературный gap-map)
- [[queries/supply-elasticity-estimation-design]] — дизайн эмпирики по пробелу №1
- [[queries/sintez-monetarnaya-politika-i-rynok-zhilya]] — закрытая часть карты (ДКП)
- [[hypotheses.yaml]] — реестр, порождённый этой картой

^[Синтез концептов wiki: transmisionnyi-mehanizm-dkp-zhile, macroprudentialnaya-politika-rynok-zhilya, effekt-zamescheniya, regionalnaya-differenciaciya, research-ideas-russia-housing; queries/sintez-monetarnaya-politika-i-rynok-zhilya, supply-elasticity-estimation-design]