# Гайд: база research_wiki → семантический слой и дашборды в Metabase

Дата проверки: 28.10.2026. Все числа в тексте получены запросами к живой базе
и приводятся как снимок на дату; при чтении гайда их надо перечитывать
запросом, а не принимать на веру. Целевая аудитория — владелец и агенты,
собирающие семантический слой и пользовательские дашборды.

Документ состоит из трёх частей: (1) карта базы и справочник полей, (2) перенос
семантики в Metabase, (3) оценка реализуемости и известные препятствия.

---

## 0. Как читать гайд

Три маршрута:

- **«Мне нужен показатель»** — раздел 2 (каталог) → раздел 9 (рецепт «последнее
  значение»). Метрика ищется по `metric_code`, не по памяти и не по `metric_id`
  из чужой схемы.
- **«Строю семантический слой»** — разделы 4–7: что уже размечено, какие поля
  становятся Measures/Metrics/Segments в Metabase.
- **«Дашборд врёт или тормозит»** — разделы 8–10: свежесть, дефекты данных,
  почему шаблон агрегации нельзя ставить по умолчанию.

Правило документа: любое утверждение о свежести и объёме — запросом.

---

## 1. Карта схем: что доступно BI-роли, что нет

Подключение BI выполнено ролью `metabase_ro` (создана 27.10.2026). Фактические
права проверены 28.10.2026:

| Схема | Роль | Доступ `metabase_ro` | Что там лежит |
|---|---|---|---|
| `data` | факты | SELECT (242 объекта) | `observation` + 240 партиций по годам и месяцам, `observation_intraday` |
| `catalog` | справочники | SELECT (12 таблиц) | `metric`, `region`, `source`, `release`, `unit`, `frequency`, `topic`, `metric_alias`, `metric_region_scope`, `metric_topic`, `event`, `source_endpoint` |
| `derived` | компат-слой | SELECT (17 объектов) | `v_metric_context`, `v_catalog_active`, `v_observation_recent`, `catalog_facets`, `metric_card`, `metric_semantic`, `v_metric_semantic`, `catalog_relations`, `metric_crosswalk`, `metric_provenance`, `v_publication_lag`/`_trusted` |
| `ops` | журналы и качество | SELECT (11 объектов) | `freshness_snapshot`, `quality_rule`/`quality_result`, `alert`, `ingest_run`/`ingest_queue`, `v_freshness_board`, `v_quality_board` |
| `core` | совместимость | **НЕТ** (`permission denied for schema core`) | `v_datalens_observations` — широкая витрина DataLens, `metric`/`region`/`source` как представления |
| `meta` | политики | **НЕТ** | `catalog_policy`, `classifier`, `metric_classifier_mapping`, `series_comparability`, `source_metric_mapping` |
| `dkp` | ДКП | **НЕТ** | заседания, решения, аргументы, прогнозы |
| `v2`, `v2_stage` | заморожено | нет грантов | не использовать |
| `attic` | карантин | нет | не использовать |

Практический вывод: **витрина `core.v_datalens_observations` для Metabase
недоступна**. Семантический слой строится на `data` + `catalog` + `derived` +
`ops`. Это не потеря: перечисленные представления дают то же покрытие, кроме
предразложенных `year/month/quarter` (их считаем в модели).

Технические ограничения сессии, проверенные на живом подключении:
`default_transaction_read_only = on`, `statement_timeout = 2 min`,
`idle_in_transaction_session_timeout = 3 min`, `lock_timeout = 10 s`, TLS
включён (`pg_stat_ssl.ssl = true`). Следствие для дизайна: тяжёлые
денормализованные запросы на 6,9 млн строк надо ограничивать фильтром по
метрике до JOIN'ов, иначе дашборд упрётся в двухминутный таймаут.

---

## 2. Ядро фактов: `data.observation`

17 колонок, 6 893 105 строк (снимок 28.10.2026), партиции по `period_start`.

| Поле | Тип | Назначение |
|---|---|---|
| `observation_id` | bigint | PK |
| `metric_id` | int | → `catalog.metric`; в BI не показывать пользователю |
| `region_id` | int | → `catalog.region`; региона `region_code` здесь нет |
| `period_start` / `period_end` | date | начало и конец периода; `date`, поэтому внутридневные метки — в `observation_intraday` |
| `value` | numeric | числовое значение |
| `value_str` | text | текстовый результат (когда значение не число) |
| `frequency_id` | int | → `catalog.frequency` |
| `release_id` | int | → `catalog.release`; входит в уникальный ключ |
| `source_id` | int | → `catalog.source` (в ключ не входит) |
| `assessment_type` | text | `final` 6 584 422, `preliminary` 279 499, `flash` 27 501, `revised` 812, `forecast` 6 |
| `observation_status` | text | `validated` 4 894 442, `raw` 1 963 603, `rejected` 35 819, `superseded` 1 264, `preliminary` 352 |
| `sub_dimension` | text | подразрез; заполнен лишь в 54 150 строках (0,8 %) |
| `quality_flags` | text[] | массив признаков качества |
| `event_id` | int | для событийных рядов (частота `E`) |
| `notes`, `created_at` | | служебные |

Правила для BI:

- фильтр по умолчанию: `observation_status <> 'rejected'`; для «официальных»
  карточек — `assessment_type IN ('final','revised')`, `preliminary`/`flash`
  показывать отдельной серией или меткой;
- `sub_dimension IS NOT NULL` означает, что под одним периодом лежит несколько
  строк-разрезов: суммировать их без оговорки нельзя (например, два продукта с
  разными единицами);
- уникальный ключ `ux_observation` объявлен `ON ONLY` на родителе и в партициях
  не работает, поэтому дубли месяцев физически возможны — витрина должна
  дедуплицировать (`DISTINCT ON (metric_id, region_id, period_start, frequency_id,
  sub_dimension)` с приоритетом свежего `release_id`), иначе динамика «двоится».

---

## 3. Каталог: `catalog.*`

### 3.1 `catalog.metric` (17 352 строки, активных 12 681; уникальных `metric_code` — 12 682, дублей кода 0)

| Поле | Назначение |
|---|---|
| `metric_code` | **ключ резолва**; стабильный технический код (`vztgr`, `kep1_14`, `emiss_43062_unemp_q`) |
| `name_ru`, `short_name_ru` | отображаемое имя; для подписей чартов брать `short_name_ru`, если есть |
| `unit_id`, `frequency_id`, `source_id` | FK в `catalog.unit` / `frequency` / `source` |
| `metric_type`, `index_base` | тип ряда и база индекса (для индексов — от чего 100) |
| `is_derived`, `formula_text` | расчётные ряды и их формула |
| `tags` | массив меток (`stage5` и др.) |
| `is_active` | признак актуальности; неактивные в справочники BI не тянуть |
| `version`, `released_at`, `status` | служебные |

### 3.2 `catalog.region` (102 строки)

`region_code` (мнемоника, `vologda`), `name_ru`, `short_name`, `level`
(91 `region`, 8 `federal_district`, по одному `country`/`city`/`aggregate`),
`parent_id` (округ субъекта), `oktmo`, `okato`, `iso_code`, `aggregation`,
`valid_from`/`valid_to` (исторические территории).

Обязательно в BI: фильтр по `level = 'region'` для региональных карт и
`level = 'country'` для национальных рядов. Складывать уровни в одну сумму —
грубая ошибка (округ + субъекты + РФ дадут двойной счёт).

### 3.3 Остальные справочники

| Таблица | Строк | Ключевые поля |
|---|---|---|
| `catalog.source` | 18 | `source_code`, `name_ru`, `publisher`, `reliability` |
| `catalog.release` | 277 | `label`, `published_at`, `content_hash`, `status` |
| `catalog.unit` | — | `unit_code`, `name_ru` |
| `catalog.frequency` | — | `freq_code`, `name_ru`, `period_type`, `months_per_period` |
| `catalog.topic` | 12 | `topic_code`, `name_ru`, `parent_id`; привязок мало — максимум 11 метрик у «Долговой нагрузки населения», у тем «Жильё и ипотека», «Региональный разрез» — ноль |
| `catalog.metric_alias` | 77 | `alias`, `lang`, `alias_type` — источник для поиска по синониму |
| `catalog.metric_region_scope` | — | `scope` ∈ `country`/`region`/`all`: если `country`, регионального разреза у ряда НЕТ |
| `catalog.event` | — | событийные ряды ДКП/аукционов |

Словарь частот по активным метрикам: `M` 10 847, `Q` 1 103, `A` 707, `D` 13,
`W` 11, `H`/`I`/`E` — 0.

---

## 4. Готовый читаемый слой `derived`

Это то, на чём строится семантический слой; всё доступно роли BI.

| Объект | Объём | Содержание |
|---|---|---|
| `v_metric_context` | 12 682 строки | строка на метрику: `name_ru`, `unit`, `source`, `frequency`, `topic`, `aliases`, `last_observation`, `observations`, `expected_next`, `freshness`, `region_scope` |
| `v_catalog_active` | 2 890 строк | `measure`, `unit_canonical`, `domain`, `freshness`, `last_obs_at`, `depth_obs`, `is_aggregate` |
| `v_observation_recent` | — | последние значения: `metric_code`, `region_name`, `period_start`, `value`, `unit` |
| `catalog_facets` | 16 814 | `measure`, `unit_canonical`, `seasonally_adjusted`, `domain`, `depth_obs`, `is_aggregate`; частичный кэш, но заполненность 100 % |
| `metric_semantic` | 1 821 | `temporal_type`, `accumulation`, `comparison_base`, `econ_group`, `control_status` |
| `v_metric_semantic` | — | то же с `metric_code` и `name_ru` — основной источник для Measures |
| `metric_card` | 3 169 | карточки с эмбеддингом (поиск по смыслу) |
| `catalog_relations` | 169 | связи `is_part_of` (иерархия показателей) |
| `metric_crosswalk`, `metric_provenance` | — | склейка дублей в канонический ряд |

Пересечение «активна + есть фасеты + есть семантика» = **1 796 метрик**; из них
с глубиной ≥10 наблюдений — **1 138**. Это реалистичный размер первого
семантического слоя: не 12 тысяч, а ~1,1–1,8 тысячи показателей.

---

## 5. Что уже размечено в семантике и чего не хватает

`derived.metric_semantic` (1 821 строка):

- `temporal_type`: `flow` 926, `index` 380, `stock` 256, `ratio` 172,
  `average` 51, `price` 36;
- `accumulation`: `single_period` 613, `year_to_date` 331, **`NULL` 877**;
- `comparison_base`: `level` 1 232, `same_period_last_year` 193,
  `previous_period` 183, **`NULL` 213**;
- `econ_group` (12 групп): строительство 476, «другое» 406, промпроизводство 170,
  инвестиции 155, ипотека 150, доходы 118, цены 110, ввод жилья 64, бюджет 53,
  кредитование 44, демография 30, эскроу 23;
- `control_status`: `verified` 1 482, `partial` 339.

Не хватает трёх вещей, каждая видна в дашборде:

1. **У 877 метрик не указан характер накопления.** Если ряд накопленный с начала
   года, а в чарте стоит «квартальный поток», подпись врёт (касается ФНС 1-НОМ,
   ИКВ и подобных).
2. **У 213 нет базы сравнения.** Тогда непонятно, процент это «к предыдущему
   месяцу» или «к тому же месяцу прошлого года» — а ИПЦ `kep1_14` как раз
   индекс к предыдущему месяцу (100,5 = +0,5 %), тогда как реальная зарплата
   `kep4_25` — к тому же месяцу прошлого года.
3. **`measure` и `temporal_type` расходятся по охвату**: `measure` есть у 2 890
   метрик, семантика у 1 821, пересечение 1 796. Правило агрегации в Metabase
   берётся по `measure` (он шире), а `temporal_type` уточняет вид графика.

Все три разрыва закрываются не изменением схемы, а настройкой в Metabase
(раздел 6.3) плюс блоком «требует подтверждения» в конце гайда.

---

## 6. Семантический слой в Metabase: соответствие объектов

### 6.1 Двухуровневая модель Metabase

Metabase различает **Measures** (сохранённые агрегаты, привязанные к таблице) и
**Metrics** (именованные показатели поверх Measures с фильтрами и разрезом),
плюс **Segments** (сохранённые фильтры) и **Models** (сохранённые вопросы,
которые ведут себя как таблицы). Именно эта четвёрка и есть «семантический
слой» в терминах Metabase.

| Наш объект | Объект Metabase | Как настраивать |
|---|---|---|
| `data.observation` + `catalog.*` | Database + Table | подключение ролью `metabase_ro`, видимость только нужных таблиц |
| `derived.v_metric_context` | Model «Метрика (справочник)» | одна строка на метрику; поле для пикеров и подписей |
| `derived.v_catalog_active` | Model «Метрика: домен и мера» | источник `domain`, `measure`, `unit_canonical` |
| `derived.v_metric_semantic` | Model «Семантика ряда» | источник `temporal_type`, `accumulation`, `comparison_base` |
| `catalog.region` | Table + FK | `level`, `parent_id`; FK на регион из модели фактов |
| `measure = level` | Measure `SUM(value)` | 2 711 метрик; сумма допустима |
| `measure = growth_rate` / `index` | Measure `AVG(value)`, «Do not sum» | 114 + 49 метрик; суммирование запрещено |
| `domain` (`construction`, `housing`, `credit`, …) | Segment | сохранённый фильтр по домену |
| `freshness` | Segment + поле-индикатор | `свежие`/`отстают`/`устарели` |
| `topic` (12 тем) | Segment | привязок мало, домен надёжнее |
| `level = 'region'` | Segment «Субъекты РФ» | отдельно от округов и РФ |
| `observation_status <> 'rejected'` | Segment «Годные наблюдения» | фильтр по умолчанию в модели |

### 6.2 Настройки Data Model (Admin → Table metadata)

- `metric_code`, `region_code`, `frequency_code`, `source_code` — тип **Category**,
  «Filterable», без агрегаций;
- `value` — **Number**, display: `Decimal`, точность по единице (для процентов 1–2
  знака, для тыс. м² — 1);
- `period_start` — **Date**, «Binning» выключить (гранулярность задаётся
  `frequency_code`), иначе Metabase самовольно сгруппирует месяц в квартал;
- `unit_code`/`unit_name` — поля подписи, не меры;
- `sub_dimension` — Category, «Filterable», но **не** default breakout: это
  разрез, а не измерение времени;
- `assessment_type`, `observation_status` — Category, порядок значений задать
  вручную (`final` → `revised` → `preliminary` → `flash`);
- скрыть (`visibility: hidden`) — `observation_id`, `metric_id`, `region_id`,
  `release_id`, `source_id`, `quality_flags`, `notes`, `created_at`.

### 6.3 Агрегации: единственное место, где легко испортить всю витрину

| `measure` | Метрики | Агрегация по умолчанию | Запрещено |
|---|---|---|---|
| `level` | 2 711 | Sum (для территорий) / Average (для душевых и % ) | — |
| `growth_rate` | 114 | Average, «Do not sum» | Sum, Cumsum |
| `index` | 49 | Average (или Last для «индекс на дату») | Sum |
| `ratio`, `average`, `price` | из семантики | Average / Last | Sum |
| `NULL` | 15 | требует ручной разметки | любая агрегация без проверки |

Дополнительно: `accumulation = year_to_date` (331 метрика) — в графике ставить
«Cumulative» **нельзя** (ряд уже накоплен), а квартальные потоки считать
разностью соседних YTD-точек, причём по правилу ФНС «апрель = I квартал,
июль = II, октябрь = III, январь = IV прошлого года» (иначе сдвиг на квартал
переворачивает знак лаговой связи).

### 6.4 Что придётся делать вручную, а не «само»

- Дедупликацию месяцев: `GROUP BY period_start` с `max(release_id)`.
- Признак «ряд накопленный»: брать из `accumulation`, в чарте — подпись
  «накопительно с начала года».
- Разрывы сопоставимости (`meta.series_comparability`) ролью BI **не читаются**
  — либо грант, либо перенос полей в представление `derived` (см. раздел 11).
- Свежесть: `v_metric_context.freshness` (допуски пер-частотой: D 10, W 5, M 75,
  Q 160, A 550 дней) плюс снимок `ops.freshness_snapshot`; дату «данные
  актуальны на» брать из снимка, не из памяти.

---

## 7. Источники свежести и качества

| Объект | Что отвечает | Как использовать |
|---|---|---|
| `derived.v_metric_context.freshness` | статус по метрике | карточка KPI с цветом |
| `derived.v_metric_context.expected_next` | ожидаемая дата следующей точки | подпись «следующее обновление» |
| `ops.freshness_snapshot` | 487 436 строк истории снимков | график деградации, фильтр по последнему `taken_at` |
| `ops.v_freshness_board` | сводка по частотам и статусам | вкладка «Здоровье данных» |
| `ops.v_quality_board` | нарушения по правилам | вкладка «Качество» |
| `ops.alert` | активные алерты | баннер дашборда |
| `derived.v_publication_lag_trusted` | лаг публикации, только правдоподобные | подпись «источник публикует с задержкой N дней»; полное `v_publication_lag` не использовать — у части релизов `published_at` подменён датой загрузки |

---

## 8. Дефекты данных, которые обязан учитывать каждый дашборд

1. **Сентинелы вместо пропусков.** `-99999999` и `-77777777` в `value` — это
   «в источнике прочерк». 35 819 строк уже помечены `rejected`; фильтр по
   статусу обязателен, иначе средняя и карта по региону считаются неверно.
2. **Свежесть не судится по `region_id = 1`.** У части рядов строка РФ лежит под
   другим идентификатором или `NULL`; вывод «ряд кончился в 2022» — типичная
   ошибка такого фильтра.
3. **ИПЦ `kep1_14` — индекс к предыдущему месяцу (100,5 = +0,5 %), не проценты.**
   Региональный `emiss_31074_cpi_prevm_m` у строки РФ имеет разрыв 2023–2025 —
   для национальной дефляции брать только `kep1_14`.
4. **ФНС 1-НОМ (`drpotr`, `rusdrpotr`) — накопленный итог с начала года**, квартал
   помечен датой публикации: апрель = I кв., июль = II, октябрь = III, январь =
   IV прошлого года. Плюс дубли в 2020Q4–2022Q4 (до 2 630 строк вместо 2 207).
5. **`vvp` — ВВП в постоянных ценах, сезонно не сглажен**: сравнивать только г/г.
6. **Дубли месяцев** сдвигают окна `cumprod`/`shift-12` на годы.
7. **Исторические территории**: `valid_from`/`valid_to` у региона; доля Крыма до
   2014 — это сентинелы, а не нули.
8. **Единица живёт в `unit_canonical`, а у многопродуктовых рядов — в
   `sub_dimension`**: два продукта могут иметь одно имя и разные единицы.
9. **Единица в каталоге не всегда осмысленна.** У 1 427 активных метрик
   `unit_code = 'unknown'` (368 402 наблюдения), ещё у 1 537 — обобщённое
   `units`, у 1 248 — `ratio`. Подпись «unknown» в чарте — не косметика:
   читатель не знает, рубли это или тыс. м². Правило: перед выводом метрики в
   витрину проверять `catalog.unit`, а при `unknown` — подписывать единицу
   вручную в описании Measures и заносить дефект в очередь каталога.

---

## 9. Рецепты для Metabase (проверены ролью `metabase_ro`)

### 9.1 Модель фактов: `derived.v_bi_observation` (уже создана)

С 28.10.2026 денормализованная витрина существует: `derived.v_bi_observation`,
6 856 188 строк (срез без `observation_status = 'rejected'`), 29 колонок —
`metric_code`/`metric_name`/`metric_short_name`, `freq_code`/`freq_name`,
`period_start`/`period_end`/`year`/`month`/`quarter`, `region_code`/
`region_name`/`region_level`/`region_id`, `unit_code`/`unit_name`,
`source_code`/`source_name`, `release_label`/`published_at`, `value`/`value_str`,
`sub_dimension`, `assessment_type`, `observation_status`, `quality_flags`,
`release_id`, `observation_id`. В Metabase это готовая таблица — Model строить
не нужно, достаточно ограничить видимость колонок.

Замеры под ролью BI: `count(*)` — 2,54 с; выборка по `metric_code` + уровень
региона — 0,14 с; агрегат по метрике — 0,08 с.

Эквивалентный SQL (оставлен для случая, когда нужна своя модель с
дополнительными полями, например `months_per_period`):

```sql
SELECT o.metric_id, m.metric_code, m.name_ru, mu.unit_code, mu.name_ru AS unit_name,
       o.region_id, r.region_code, r.name_ru AS region_name, r.level AS region_level,
       o.period_start, o.period_end, f.freq_code,
       CASE f.freq_code WHEN 'M' THEN 1 WHEN 'Q' THEN 3 WHEN 'A' THEN 12 ELSE NULL END AS months_per_period,
       o.value, o.sub_dimension, o.assessment_type, o.observation_status,
       s.source_code, rel.label AS release_label, rel.published_at
FROM data.observation o
JOIN catalog.metric  m  ON m.metric_id = o.metric_id AND m.is_active
JOIN catalog.frequency f ON f.frequency_id = o.frequency_id
LEFT JOIN catalog.unit    mu ON mu.unit_id = m.unit_id
LEFT JOIN catalog.region  r  ON r.region_id = o.region_id
LEFT JOIN catalog.source  s  ON s.source_id = o.source_id
LEFT JOIN catalog.release rel ON rel.release_id = o.release_id
WHERE o.observation_status <> 'rejected'
```

В Metabase сохранить как **Model** с обязательным фильтром-параметром по
`metric_code` (Field Filter) — иначе каждый чарт будет сканировать 6,9 млн строк
и упрётся в `statement_timeout = 2 min`.

### 9.2 Последнее значение по метрике

```sql
SELECT DISTINCT ON (m.metric_code, r.region_code)
       m.metric_code, m.name_ru, r.name_ru AS region, o.period_start, o.value
FROM data.observation o
JOIN catalog.metric m USING (metric_id)
JOIN catalog.region r USING (region_id)
WHERE o.observation_status <> 'rejected' AND r.level = 'region'
ORDER BY m.metric_code, r.region_code, o.period_start DESC, o.release_id DESC
```

### 9.3 «Паспорт региона» (12 KPI одной таблицей)

База — модель 9.1, фильтры: `region_level = 'region'`, `region_code = <параметр>`,
`freq_code` из справочника метрики; агрегация `max(period_start)` на метрику,
затем join значений по этой дате. В Metabase: один вопрос на KPI + Dashboard с
параметром `region_code`.

### 9.4 Свежесть и «когда обновится»

```sql
SELECT metric_code, name_ru, frequency, last_observation, expected_next,
       observations, freshness, region_scope
FROM derived.v_metric_context
WHERE freshness <> 'свежие'
ORDER BY last_observation DESC
```

### 9.5 Сравнение регионов с нормировкой

Индекс к базовому периоду считать в SQL, а не «суммой»:

```sql
WITH base AS (
  SELECT o.region_id, o.value AS v0
  FROM data.observation o JOIN catalog.metric m USING (metric_id)
  WHERE m.metric_code = 'vztgr' AND o.period_start = DATE '2020-01-01'
)
SELECT r.name_ru, o.period_start, round(100 * o.value / NULLIF(b.v0,0), 1) AS idx
FROM data.observation o
JOIN catalog.metric m USING (metric_id)
JOIN catalog.region r USING (region_id)
JOIN base b ON b.region_id = o.region_id
WHERE m.metric_code = 'vztgr' AND o.observation_status <> 'rejected'
ORDER BY 1, 2
```

### 9.6 Проверка «пустой ответ ≠ нет данных»

```sql
SELECT count(*) FROM data.observation o JOIN catalog.metric m USING (metric_id)
WHERE m.metric_code = '<код>';
```

Ноль строк при ненулевом `count(*)` по метрике означает неверный регион или
`region_scope = 'country'`, а не отсутствие ряда.

---

## 10. Чек-лист приёмки дашборда

- [ ] Все числа идут из модели 9.1, прямых `SELECT` по `data.observation` в
      чартах нет.
- [ ] Стоит фильтр `observation_status <> 'rejected'`, сентинелы не видны.
- [ ] Для `growth_rate`/`index`/`ratio` сумма запрещена (проверить настройку поля,
      а не только чарта).
- [ ] У каждой карточки подписана единица из `unit_canonical`.
- [ ] Указан период и дата последнего наблюдения (из `v_metric_context`).
- [ ] Накопленные ряды (`accumulation = year_to_date`) подписаны «накопительно».
- [ ] Территориальные уровни не смешаны (`level` — отдельный фильтр).
- [ ] Есть вкладка «Здоровье данных» на `ops.v_freshness_board` / `v_quality_board`.
- [ ] Известные разрывы сопоставимости выведены примечанием (сейчас — вручную,
      см. раздел 11).

---

## 11. Оценка реализуемости: что можно сделать сразу, а что требует решения

### 11.1 Работает уже сейчас (проверено 28.10.2026)

| Проверка | Результат |
|---|---|
| Подключение ролью `metabase_ro` по TLS | удачно, `ssl = true` |
| Режим сессии | `default_transaction_read_only = on` — записать в ядро из BI невозможно |
| SELECT на `data.observation` | 6 893 105 строк читаются |
| SELECT на `derived.v_metric_context` | 12 682 строки |
| SELECT на `catalog.metric` | 17 352 строки |
| SELECT на `ops.freshness_snapshot` | 487 436 строк |
| `v2` в грантах | отсутствует — замороженный слой недоступен по ошибке |
| Хост/порт/SSL из README `infra/mcp-db-research-wiki` | совпадают с фактическими |

То есть **семантический слой и дашборды реализуемы на текущих правах
полностью**, без единого изменения схемы: 12 справочников, факты, 17 объектов
`derived` и журналы `ops` закрывают и карточки, и динамику, и свежесть, и
качество.

### 11.2 Три препятствия (каждое — одна строка, но это права/схема)

| # | Препятствие | Следствие сейчас | Статус на 28.10.2026 |
|---|---|---|---|
| B1 | нет `USAGE` на схему `core` → `v_datalens_observations` недоступна | витрина DataLens не переиспользуется; `year/month/quarter` считаем в модели | **оставлено как есть** по рекомендации: BI живёт на `derived`, витрина DataLens — снимок под другую задачу |
| B2 | нет `USAGE` на схему `meta` | разрывы сопоставимости, классификаторы и политики в дашборд не попадали | **снято**: `GRANT USAGE ON SCHEMA meta` + `GRANT SELECT ON ALL TABLES IN SCHEMA meta` роли `metabase_ro`. Важно: `meta.series_comparability` и `meta.classifier` сейчас **пусты** (0 строк) — грант открывает путь, но наполнять их надо отдельной задачей |
| B3 | нет тонкой денормализованной витрины под BI | модель 9.1 — 7 JOIN'ов на 6,9 млн строк, риск упереться в `statement_timeout = 2 min` | **снято**: создано представление `derived.v_bi_observation` (6 856 188 строк, срез без `rejected`), грант `SELECT` роли выдан; скрипт `scripts/build_bi_observation_view.py` идемпотентен |

Замеры под ролью `metabase_ro` после снятия B2/B3: `count(*)` по витрине — 2,54 с,
выборка по метрике и региону — 0,14 с, агрегат по метрике — 0,08 с. То есть
двухминутный таймаут перестаёт быть ограничением: фильтр по `metric_code`
отрабатывает за десятые доли секунды.

Откат (одной транзакцией, если понадобится): `DROP VIEW derived.v_bi_observation;`
`REVOKE ALL ON ALL TABLES IN SCHEMA meta FROM metabase_ro;`
`REVOKE USAGE ON SCHEMA meta FROM metabase_ro;`

### 11.3 Чего не хватает в самих данных (не в правах)

- 877 метрик без `accumulation`, 213 без `comparison_base` — до 48 % семантики
  неполно; в дашбордах это лечится подписями и ручной разметкой Measures, а не
  новой схемой.
- Пересечение «фасеты + семантика + наблюдения ≥10» = 1 138 метрик: это ядро
  первой витрины. Остальные 11,5 тысячи активных метрик в пикеры не выводить —
  справочник превратится в свалку.
- Темы `catalog.topic` почти не заполнены (0 привязок у «Жильё и ипотека»),
  поэтому группировка в дашборде — по `domain` из фасетов, где `other`
  (618 метрик) означает «не размечено», а не «нет домена».
- Приложение Metabase с этого хоста недостижимо: порт 3000 на ВМ `research-db`
  закрыт, контейнеров Metabase на ВМ нет, узлы tailnet на 3000 не отвечают.
  Инстанс живёт вне периметра VPS (рабочий ноутбук или облако) — это не мешает
  ничему, но версию и доступ к Admin API надо уточнить у владельца: от версии
  зависит, доступны ли **Measures/Metrics** (новый семантический слой) или
  только Models + Segments.

---

## 12. Требует подтверждения владельца

1. **B1** — переиспользовать ли витрину `core.v_datalens_observations` (грант) или
   строить модель только на `derived`. Решение по умолчанию уже действует:
   живём на `derived`, `core` не открываем.
2. **B2, B3** — закрыты 28.10.2026 (грант на `meta` выдан, `derived.v_bi_observation`
   создана и доступна роли). Подтверждения не требуют, откат описан в 11.2.
3. **Наполнение `meta.series_comparability` и `meta.classifier`** — таблицы пусты;
   без наполнения примечания о разрывах сопоставимости в дашборде появятся
   только после отдельной задачи.
4. **Спорная агрегация**: для `index` по умолчанию Average или Last — влияет на
   все индексные чарты; предлагаю Average с подписью «среднее по периоду».
5. **Порог ядра витрины**: 1 138 метрик (≥10 наблюдений) или расширить до 1 796
   (весь пересечение). От этого зависит наполнение пикеров.
6. **Версия Metabase** и наличие Admin API-доступа: без него слои настраиваются
   руками, с ним — воспроизводимо скриптом.

## 13. Сопровождение

Гайд живёт в репозитории (`queries/`), обновляется при изменении схемы или прав
роли. Числа в тексте — снимок; проверочные запросы приведены в разделах 9 и 11.
После любого `GRANT`/`REVOKE` и после пересборки `derived` обязателен прогон
чек-листа раздела 10.
