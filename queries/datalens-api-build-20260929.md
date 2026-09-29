# DataLens-коллекция: сборка через Public API (29.09.2026)

**Метка: «Независимый расчет, не связанный с Банком России».**

## Собрано

Датасеты (4, в воркбуке Wiki `wxaisbjylfeif`, connection `research-wiki-pg`):

| Имя | ID | Поля |
|---|---|---|
| ds_region_monthly | mq9joqmxxxnu5 | 8 (value = MEASURE) |
| ds_region_rating | 48r16b0n8djqn | 8 (value/rank_in_fo/fo_median = MEASURE) |
| ds_rf_trend | swfpu2izqtsab | 5 (value = MEASURE, period = DIMENSION) |
| db_health | im5fktvy1uqm1 | 4 (age_days/n_obs = MEASURE) |

Чарты (8, editor d3_node / GravityCharts): Д1. ИПЦ по округам `15ozyyztk43sk`;
Д3.1 ИПЦ по ФО `9dw77wjo84tcs`; Д1.2 Зарплата `rvepqjrq5xt8a`; Д1.3 ИЖК долг
`lp8jke07xn0k4`; Д1.4 Ввод жилья `fj2deb9v7zh4y`; Д2.1 Топ-10 регионов
`ptcnom5z4l148`; Д2.2 Рейтинг в ФО `fj2dee441d0cy`; Д4. Свежесть источников
`ptcnplbf5gvk8`.

Дашборд «Паспорт региона (Д1-Д3)» `dh0blcujorc4w` (8 виджетов, сетка 2×4):
https://datalens.yandex.ru/dh0blcujorc4w

## Рабочий цикл Public API (важно для повторного использования)

1. IAM: `yc iam create-token > /tmp/dl_token.txt`; заголовки:
   Bearer + `x-dl-org-id: bpfd2ponvctukuknls2i` + **`x-dl-api-version: 2`**.
2. BASE `https://api.datalens.tech`, все методы под `/rpc/<method>`.
3. Создание датасета: `createDataset` c `workbookId` (рядом с entry), датасет
   `rls: {}`, `rls2: {}` (объекты, не null/массивы), `raw_schema: []`.
4. Схема: `getDataset` → `validateDataset` c `data.updates =
   [{action:'refresh_source', source: <полный источник>}]` (обновления — внутри
   data) → из ответа берём `result_schema` → кастуем меры →
   `updateDataset {datasetId, data: {mode:'publish', dataset: full}}`.
5. Чарт: `createEditorChart` c `workbookId` ВНЕ entry; `type: 'd3_node'`
   (Gravity Charts), `data` — все поля строками (`meta/params/controls/config`
   — строковые JSON), `sources` — строка JSON c SQL-источниками.
6. Дашборд: `createDashboard` c `workbookId` вне entry; `data.schemeVersion: 8`,
   `settings` с полным набором полей (в т.ч. `autoupdateInterval: null`),
   `salt` непустой, `counter ≥ 1`; widget-item: `data.tabs[0].chartId`,
   layout отдельным массивом.

## Что осталось в UI

- Визуальность чартов (оси, легенды, форматирование, карты-choropleth);
- селекторы (регион/ФО) — через control_node;
- Д1/Д2/Д3 как отдельные дашборды (сейчас один общий на 8 виджетов).