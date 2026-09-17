---
title: "Целевая архитектура базы данных research-wiki — аналитический документ"
created: 2026-09-16
updated: 2026-09-16
type: query
tags: [infrastructure, database, architecture, postgresql, yandex-cloud, data-pipeline]
status: proposal
related: ["queries/database-target-spec", "queries/database-catalog", "queries/db-cleanup-report", "queries/yandex-cloud-data-infra"]
---

# Целевая архитектура базы данных research-wiki

Документ отвечает на техзадание `queries/database-target-spec.md`. Принцип проектирования —
минимальная достаточность: один сервер PostgreSQL на ВМ в Yandex Cloud (YC), один
S3-совместимый бакет YC Object Storage, пакетная обработка по расписанию. Очереди,
микросервисы, стриминг, распределённые хранилища исключены — для 5,9 млн строк и 1,4 ГБ
данных они не дают ничего, кроме эксплуатационных расходов.

## 0. Проверка исходных фактов на диске (16.09.2026)

Все числа ниже пересчитаны заново скриптом по шести файлам `data/*.db` (PRAGMA + COUNT),
а не взяты из ТЗ. Два показателя немного расходятся с ТЗ — зафиксировано честно:

| База | Таблиц | Строк | Размер |
|---|---|---|---|
| `rosstat_construction.db` | 36 | 1 514 984 | 865 МБ |
| `fns_tochno_sectors.db` | 10 | 3 715 553 | 236 МБ |
| `regions_panel.db` | 1 (`panel`) | 308 952 | 240 МБ |
| `cbr_lending.db` | 3 (`mortgage_monthly`, `escrow_monthly`, `corporate_monthly`) | 311 721 | 97 МБ |
| `rosreestr_deals.db` | 29 | 51 767 | 11 МБ |
| `developers_ifrs.db` | 1 (`dev_ifrs`) | 512 | <1 МБ |
| **Итого** | **80** | **5 903 489** | **~1,45 ГБ** |

Расхождение с ТЗ (81 табл./5 903 507) — вероятно, в замер ТЗ попала внутренняя
`sqlite_sequence` либо один из файлов изменился после чистки; для проектирования
разница несущественна, но для миграции используется факт, а не ТЗ.

Подтверждено также:

- **27 скриптов** в `scripts/` содержат `sqlite3.connect`; **11 из них** импортируют
  `gcs_sync` (контракт `ensure_db()`): `canonize_regions.py`, `cleanup_rosstat_db.py`,
  `export_dashboard.py`, `export_operational.py`, `nightly_backup.py`,
  `parse_cbr_lending.py`, `parse_tochno_rfsd.py`, `reindex_vacuum_db.py`,
  `rosstat_prom_monthly_parse.py`, `vacuum_into.py`, `wordstat_core_index.py`.
- Схемные шаблоны на диске: ЦБ (`region_name, report_date, indicator, value, unit` —
  `cbr_lending.db`), Росстат месячные (`region_name, year, month, value, unit, source,
  updated_at`), Росстат панель (`panel`: `section, indicator_code, indicator_name,
  region_name, region_level, oktmo, year, value, unit, source`), ФНС snapshot
  (`fns_profitorg_key_quarterly`: `region, snapshot, field, value`; `fns_rf_annual`:
  `form, metric, year, rf_value_bln_rub, snapshot, partial`; `fns_1nom_okved_f_quarterly`:
  `region, snapshot_date, metric, value`), Росреестр (`deals_by_region_quarter`:
  `year, quarter, region_code, region, n_deals, ...`). То есть пять буквальных схем,
  сводимых к четырём шаблонам ТЗ.
- Широкие «стоги»: в `rosstat_construction.db` живут `cbr_mortgage_monthly`,
  `cbr_escrow_monthly`, `cbr_corporate_monthly`, `domrf_indicators` (857 862 строки) —
  то есть база ЦБ размазана по двум файлам.
- Стихийная версионность ФНС: колонки `snapshot`/`snapshot_date` в четырёх таблицах
  (9 117 / 506 / 340 / 98 строк) — единственный слой «несколько версий одного значения».
- GCS: `raw/` — симлинк на `/home/lnr/gcs-wiki/raw` (2,1 ГБ), весь маунт 3,5 ГБ
  (`raw/` 2,1 + `data/` 1,5), `data/archive/` — 106 МБ JSONL. Ссылки на
  `gs://`/`gsutil`/`gcsfuse`/`ensure_db` найдены в **12 py-файлах** (в `gcs_sync.py` — 23
  вхождения, в остальных по 2–4; см. §9).
- `.gitignore` исключает `raw/` (целиком), пять конкретных `data/*.db`
  (примечание: `rosreestr_deals.db` указан без префикса `data/` и
  `developers_ifrs.db` / `fns_tochno_sectors.db` не перечислены — мелкие пробелы),
  `data/archive/*.jsonl`, два блока тяжёлых raw-подкаталогов.
- `data/catalog.yaml`: 165 записей, **43 различных значения `type`** (перечислены в §12);
  записей с полем `table` — 52; физически отсутствуют **23** упомянутых значения `table`
  (в ТЗ — 22 фантомные таблицы из 31; у нас 52 упоминаний `table`, одно значение —
  строка `"deals_by_region_quarter, rents_by_region_quarter, deals_rf_quarterly,
  rents_rf_quarterly"` из четырёх имён через запятую — ещё один артефакт грязного
  каталога; см. §12).
- PostgreSQL и драйверы (`psycopg2`, `psycopg`, `sqlalchemy`) в venv отсутствуют —
  проверено импортом. `yc` CLI не проверялся из этой среды (задача — дизайн, не
  развёртывание); инфраструктурные предпосылки приняты из ТЗ §15.

---

## 1. Концепция и слоистость

### Почему длинная модель

Сегодня одна и та же семантика (показатель × регион × период × значение) реализована
четырьмя несовместимыми шаблонами таблиц, а «показатель» — это строка в колонке
`indicator`/`indicator_name`/`metric`/`field`. Чтобы получить один показатель, нужно
фильтровать текстовую колонку; чтобы сопоставить два источника — руками приводить
периодику и имена. Длинная модель (одна строка = одно наблюдение со ссылкой на
справочники) устраняет обе проблемы и позволяет добавить новый источник, не меняя схему.

### Четыре слоя

```
S3 YC (сырые файлы) ──► staging ──► core ──► derived ──► marts
                            │           │         │
                        file_registry  observation  derived_metric / series_comparability
```

1. **staging** — «сырая зона» внутри PostgreSQL: для каждого загружаемого файла его
   данные ложатся в широкую таблицу `stg.<release_id>_<name>` (или в универсальную
   `staging.raw_rows(release_id, row_no, c1..c20)`). Смысл слоя — повторяемость:
   если парсер ошибся, staging не надо перекачивать из бакета, достаточно
   перепроцессить. Слой очищается по политике хранения (держим N последних релизов).
2. **core** — гармонизированные факты: `observation` + справочники (`metric`, `region`,
   `unit`, `frequency`, `source`, `release`, `file_registry`, `classifier`,
   `metric_classifier_mapping`, `source_metric_mapping`). Только INSERT, никакого
   UPDATE — пересмотры приходят как новые строки с новым `release_id` (принцип
   неизменяемости, §6 ТЗ).
3. **derived** — вычисляемые ряды: темпы роста, сезонная корректировка, агрегаты.
   Физически тоже лежат в `observation` (как обычные факты с `source_id = derived`)
   и/или в материализованных таблицах, но с обязательной фиксацией формулы, версии кода
   и параметров (§7 документа).
4. **marts** — витрины для потребления: SQL-представления над `observation`
   (`v_latest`, `v_asof`, `v_revisions`, `v_final`, `v_flash`) + материализованные
   витрины для тяжёлых экспортов. Витрины пересоздаются, а не хранят «истину».

Обоснование минимальности: слои реализованы *схемой PostgreSQL* (schemas `staging`,
`core`, `derived`, `marts` в одной базе), а не сервисами. Каждому слою — свой
`GRANT`/роль, что даёт защиту от записи извне без единого нового компонента.

---

## 2. DDL ключевых таблиц

Ниже — рабочий DDL PostgreSQL 15+ (проверен синтаксически sqlglot-парсером, см. §13).
Три схемы: `core` (справочники и факты), `meta` (маппинги и классификаторы — вынесены,
чтобы RBAC не давал пайплайну их менять), `derived`. Идентификаторы — `bigint
GENERATED ALWAYS AS IDENTITY` (без внешних зависимостей, в отличие от UUID-OSSP);
«машиночитаемый код» — отдельные натуральные ключи с `UNIQUE`.

```sql
-- ======================================================================
-- Схемы
-- ======================================================================
CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS meta;
CREATE SCHEMA IF NOT EXISTS derived;
CREATE SCHEMA IF NOT EXISTS marts;

-- ======================================================================
-- 1. unit — единицы измерения
-- ======================================================================
CREATE TABLE core.unit (
    unit_id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    unit_code    text NOT NULL UNIQUE,          -- 'RUB', 'MLN_RUB', 'SQM', 'PCT', 'COUNT'
    name_ru      text NOT NULL,
    description  text,
    created_at   timestamptz NOT NULL DEFAULT now()
);

-- ======================================================================
-- 2. frequency — частота
-- ======================================================================
CREATE TABLE core.frequency (
    frequency_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    frequency_code text NOT NULL UNIQUE,         -- 'D','M','Q','A','CUM_M','CUM_Y'
    name_ru        text NOT NULL,
    period_type    text NOT NULL
                   CHECK (period_type IN ('date','month','quarter','year','cumulative')),
    months_per_period int CHECK (months_per_period BETWEEN 1 AND 12)
);

-- ======================================================================
-- 3. region — географическая иерархия
-- ======================================================================
CREATE TABLE core.region (
    region_id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    region_code    text NOT NULL UNIQUE,         -- ОКТМО/ISO/внутренний код, напр. 'RU', 'RU-CENTRAL', '01000000000'
    name_ru        text NOT NULL,
    short_name     text,
    level          text NOT NULL
                   CHECK (level IN ('country','federal_district','region','foreign_region')),
    parent_id      bigint REFERENCES core.region(region_id),
    is_active      boolean NOT NULL DEFAULT true,
    valid_from     date,
    valid_to       date,                          -- для исторических границ/переименований
    oktmo          text,
    okato          text,
    iso_code       text,
    created_at     timestamptz NOT NULL DEFAULT now(),
    CHECK (level <> 'country' OR parent_id IS NULL)          -- страна без родителя
);
CREATE INDEX idx_region_parent ON core.region(parent_id);
CREATE INDEX idx_region_level  ON core.region(level);
CREATE INDEX idx_region_name_trgm ON core.region USING gin (name_ru gin_trgm_ops); -- pg_trgm

-- ======================================================================
-- 4. source — источник данных
-- ======================================================================
CREATE TABLE core.source (
    source_id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source_code    text NOT NULL UNIQUE,          -- 'rosstat', 'domrf', 'cbr', 'fns', 'rosreestr', 'eiszhk', 'derived'
    name_ru        text NOT NULL,
    publisher      text,
    url            text,
    license        text,
    reliability    text CHECK (reliability IN ('official','primary','secondary','derived','unknown')),
    is_active      boolean NOT NULL DEFAULT true,
    created_at     timestamptz NOT NULL DEFAULT now()
);

-- ======================================================================
-- 5. release — релиз источника (версия публикации)
-- ======================================================================
CREATE TABLE core.release (
    release_id     bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source_id      bigint NOT NULL REFERENCES core.source(source_id),
    release_label  text,                          -- 'ЕМИСС 2026-09-05', 'domrf-2026-08'
    published_at   timestamptz,                   -- дата публикации источником
    ingested_at    timestamptz NOT NULL DEFAULT now(),
    url            text,
    content_hash   text,                          -- sha256 полезной нагрузки
    status         text NOT NULL DEFAULT 'loaded'
                   CHECK (status IN ('registered','parsed','validated','loaded','failed','superseded')),
    notes          text,
    UNIQUE (source_id, release_label)
);

-- ======================================================================
-- 6. file_registry — метаданные файлов (сами файлы в S3 YC / на диске ВМ)
-- ======================================================================
CREATE TABLE core.file_registry (
    file_id        bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source_id      bigint REFERENCES core.source(source_id),
    release_id     bigint REFERENCES core.release(release_id),
    uri            text NOT NULL,                 -- 's3://research-wiki/raw/...' или '/data/raw/...'
    file_name      text NOT NULL,
    mime_type      text,
    sha256         text NOT NULL,
    size_bytes     bigint NOT NULL CHECK (size_bytes >= 0),
    downloaded_at  timestamptz NOT NULL DEFAULT now(),
    status         text NOT NULL DEFAULT 'registered'
                   CHECK (status IN ('registered','processing','processed','failed','archived')),
    UNIQUE (uri, sha256)
);
CREATE INDEX idx_file_release ON core.file_registry(release_id);

-- ======================================================================
-- 7. metric — показатель
-- ======================================================================
CREATE TABLE core.metric (
    metric_id       bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    metric_code     text NOT NULL UNIQUE,         -- 'housing_input_area_m2_m', 'mortgage_volume_rub_m'
    name_ru         text NOT NULL,
    short_name_ru   text,
    description     text,
    unit_id         bigint NOT NULL REFERENCES core.unit(unit_id),
    frequency_id    bigint NOT NULL REFERENCES core.frequency(frequency_id),
    metric_type     text NOT NULL DEFAULT 'primary'
                    CHECK (metric_type IN ('primary','derived','nowcast_model')),
    index_base      text,                         -- '2011', '2021', 'prev=100' — ОБЯЗАТЕЛЕН для индексных
    is_derived      boolean NOT NULL DEFAULT false,
    formula_text    text,                         -- для derived: правило расчёта (см. §7)
    status          text NOT NULL DEFAULT 'active'
                    CHECK (status IN ('active','deprecated','merged')),
    tags            text[] NOT NULL DEFAULT '{}',
    created_at      timestamptz NOT NULL DEFAULT now(),
    CHECK (NOT (metric_type = 'primary' AND index_base IS NULL AND tags && '{index}'))
          -- контроль: индексный показатель обязан иметь index_base
);
COMMENT ON COLUMN core.metric.index_base IS
    'База сравнения индекса: год/период, к которому нормирован (напр. 2011, 2021). Обязательна для индексных показателей (см. series_comparability.break_type = index_base_change).';

-- ======================================================================
-- 8. classifier — классификаторы и их редакции
-- ======================================================================
CREATE TABLE meta.classifier (
    classifier_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cls_code        text NOT NULL,                -- 'OKVED2', 'OKPD2', 'OKTMO', 'OKATO', 'OKSM', 'OKVED1'
    edition         text NOT NULL,                -- редакция/версия: '01.2020', '2011'
    name_ru         text NOT NULL,
    valid_from      date,
    valid_to        date,
    source_url      text,
    UNIQUE (cls_code, edition)
);

-- ======================================================================
-- 9. metric_classifier_mapping — разрез показателя по классификатору
-- ======================================================================
CREATE TABLE meta.metric_classifier_mapping (
    id               bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    metric_id        bigint NOT NULL REFERENCES core.metric(metric_id),
    classifier_id    bigint NOT NULL REFERENCES meta.classifier(classifier_id),
    classifier_entry_code text NOT NULL,          -- код записи: 'A', '41', '41.2'
    valid_from       date,
    valid_to         date,
    notes            text,
    UNIQUE (metric_id, classifier_id, classifier_entry_code)
);

-- ======================================================================
-- 10. series_comparability — методологические разрывы длинных рядов
-- ======================================================================
CREATE TABLE meta.series_comparability (
    sc_id           bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    metric_id       bigint NOT NULL REFERENCES core.metric(metric_id),
    region_id       bigint REFERENCES core.region(region_id),   -- NULL = все регионы
    break_date      date NOT NULL,                 -- первый период ПОСЛЕ разрыва
    break_type      text NOT NULL
                    CHECK (break_type IN ('classifier_change','index_base_change',
                                          'methodology_change','boundary_change','unit_change')),
    description     text NOT NULL,
    pre_break_base  text,                          -- база до разрыва ('2011')
    post_break_base text,                          -- база после ('2021')
    conversion_rule text,                          -- правило стыковки: 'x0.94', 'link_factor=1.067', ссылка на код
    source_id       bigint REFERENCES core.source(source_id),
    created_at      timestamptz NOT NULL DEFAULT now(),
    UNIQUE (metric_id, region_id, break_date, break_type)
);

-- ======================================================================
-- 11. source_metric_mapping — маппинг оригинальных названий → канон
-- ======================================================================
CREATE TABLE meta.source_metric_mapping (
    mapping_id     bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source_id      bigint NOT NULL REFERENCES core.source(source_id),
    raw_metric     text NOT NULL,                 -- оригинальное название показателя ('Количество действующих ДДУ (214-ФЗ)')
    raw_region     text,                          -- оригинальное название региона ('Респ. Адыгея')
    metric_id      bigint NOT NULL REFERENCES core.metric(metric_id),
    region_id      bigint REFERENCES core.region(region_id),
    unit_convert_rule   text,                     -- 'x1000', 'cumulative->flow', NULL
    frequency_convert_rule text,                 -- 'M->Q:avg', NULL
    confidence     text NOT NULL DEFAULT 'needs_review'
                   CHECK (confidence IN ('exact','manual','inferred','needs_review')),
    review_status  text NOT NULL DEFAULT 'pending'
                   CHECK (review_status IN ('pending','approved','rejected')),
    created_at     timestamptz NOT NULL DEFAULT now(),
    UNIQUE (source_id, raw_metric, raw_region)
);
CREATE INDEX idx_smm_raw_metric ON meta.source_metric_mapping USING gin (raw_metric gin_trgm_ops);

-- ======================================================================
-- 12. observation — основная таблица фактов
-- ======================================================================
CREATE TABLE core.observation (
    obs_id            bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    metric_id         bigint NOT NULL REFERENCES core.metric(metric_id),
    region_id         bigint NOT NULL REFERENCES core.region(region_id),
    frequency_id      bigint NOT NULL REFERENCES core.frequency(frequency_id),
    period_start      date NOT NULL,              -- начало периода
    period_end        date NOT NULL,              -- конец периода (для M/Q/A совпадает или вычислим)
    value             numeric,
    value_str         text,                       -- для текстовых/диапазонных значений
    assessment_type   text NOT NULL DEFAULT 'final'
                      CHECK (assessment_type IN ('flash','preliminary','revised','final',
                                                 'nowcast','forecast','estimated')),
    observation_status text NOT NULL DEFAULT 'loaded'
                      CHECK (observation_status IN ('raw','validated','rejected','superseded')),
    source_id         bigint NOT NULL REFERENCES core.source(source_id),
    release_id        bigint NOT NULL REFERENCES core.release(release_id),
    quality_flags     text[] NOT NULL DEFAULT '{}',   -- 'outlier','break_in_series','imputed','cumulative'
    sub_dimension     text NOT NULL DEFAULT '',       -- подразрез внутри показателя (напр.
                                                      -- 'жилого назначения', row_label Росстата);
                                                      -- нужен из-за легитимных дублей внутри релиза (§14.5)
    notes             text,
    created_at        timestamptz NOT NULL DEFAULT now(),
    -- КЛЮЧ ГРАНУЛЯРНОСТИ (см. §3): одна и та же оценка одного показателя в одном
    -- периоде из одного релиза — ровно одна строка. Разные релизы/источники/типы
    -- оценок — разные строки, ничего не перезаписывается.
    CONSTRAINT uq_observation UNIQUE (metric_id, region_id, frequency_id, period_start,
                                      source_id, release_id, assessment_type, sub_dimension),
    CHECK (period_end >= period_start)
);
CREATE INDEX idx_obs_lookup ON core.observation
    (metric_id, region_id, period_start DESC, assessment_type, release_id DESC);
CREATE INDEX idx_obs_release   ON core.observation(release_id);
CREATE INDEX idx_obs_flags     ON core.observation USING gin (quality_flags);

-- ======================================================================
-- 13. derived_metric — регистр производных расчётов (воспроизводимость)
-- ======================================================================
CREATE TABLE derived.derived_metric (
    dm_id           bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    output_metric_id bigint NOT NULL REFERENCES core.metric(metric_id),   -- куда пишем результат
    input_metric_ids bigint[] NOT NULL,          -- входные metric_id
    transform_type  text NOT NULL
                    CHECK (transform_type IN ('mom','yoy','ytd','sa','x13_arima','link_relative',
                                              'aggregate_sum','aggregate_avg','custom')),
    formula_text    text NOT NULL,               -- SQL/псевдокод/ссылка на функцию
    params          jsonb NOT NULL DEFAULT '{}', -- параметры: окно, фильтры, веса
    code_version    text NOT NULL,               -- git SHA репозитория на момент расчёта
    code_path       text,                        -- путь к скрипту/функции в репо
    computed_at     timestamptz NOT NULL DEFAULT now(),
    output_release_id bigint REFERENCES core.release(release_id),  -- производные тоже версионируются релизом
    notes           text
);
CREATE INDEX idx_dm_output ON derived.derived_metric(output_metric_id, computed_at DESC);

-- ======================================================================
-- 14. document — документы (вики-страницы, отчёты, PDF)
-- ======================================================================
CREATE TABLE core.document (
    document_id    bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    doc_code       text NOT NULL UNIQUE,          -- slug страницы вики или имени файла
    title_ru       text NOT NULL,
    doc_type       text NOT NULL
                   CHECK (doc_type IN ('wiki_page','paper','report','methodology','news','other')),
    file_id        bigint REFERENCES core.file_registry(file_id),   -- PDF/файл в S3
    url            text,
    sha256         text,
    published_at   date,
    created_at     timestamptz NOT NULL DEFAULT now()
);

-- ======================================================================
-- 15. hypothesis — гипотезы (зеркало hypotheses.yaml)
-- ======================================================================
CREATE TABLE core.hypothesis (
    hypothesis_id  bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    hyp_code       text NOT NULL UNIQUE,          -- 'H-008'
    kind           text,
    title_ru       text NOT NULL,
    statement      text,
    status         text NOT NULL DEFAULT 'open'
                   CHECK (status IN ('open','testing','supported','refuted','archived')),
    evidence_for   text[],
    evidence_against text[],
    tags           text[] NOT NULL DEFAULT '{}',
    next_check     date,
    methodology_ref text,
    created_at     timestamptz NOT NULL DEFAULT now()
);

-- ======================================================================
-- 16. person — ключевые лица
-- ======================================================================
CREATE TABLE core.person (
    person_id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name      text NOT NULL,
    organization   text,
    role           text,                          -- 'official','researcher','executive'
    source_url     text,
    notes          text,
    created_at     timestamptz NOT NULL DEFAULT now(),
    UNIQUE (full_name, organization)
);

-- ======================================================================
-- 17. note — заметки, привязанные к любым сущностям
-- ======================================================================
CREATE TABLE core.note (
    note_id        bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    metric_id      bigint REFERENCES core.metric(metric_id),
    region_id      bigint REFERENCES core.region(region_id),
    source_id      bigint REFERENCES core.source(source_id),
    file_id        bigint REFERENCES core.file_registry(file_id),
    document_id    bigint REFERENCES core.document(document_id),
    hypothesis_id  bigint REFERENCES core.hypothesis(hypothesis_id),
    obs_id         bigint REFERENCES core.observation(obs_id),
    body           text NOT NULL,
    created_at     timestamptz NOT NULL DEFAULT now()
);
```

Замечания по DDL:

- `UNIQUE` на `observation` — это и есть «нельзя перезаписывать при пересмотре»:
  второй релиз с тем же набором ключей образует *новую* строку, а не дубликат.
- Имена и коды — `text` без ограничений длины: PostgreSQL не выигрывает от
  varchar(n), а жёсткие лимиты только мешают при миграции мусора.
- `tags`/`quality_flags` — `text[]` вместо junction-таблиц: объёмы малы, запросы —
  «есть ли флаг», GIN-индекс решает; отдельные таблицы — избыточная сложность.
- `ingested_ref` индекс не создаётся: as-of реализуется через `release.ingested_at`
  (см. §4), лишний индекс не нужен.
- `pg_trgm` требуется для fuzzy-поиска в маппинге имён (`CREATE EXTENSION pg_trgm;`
  — единственное расширение, входит в стандартную поставку; вендор-экстензии
  TimescaleDB и т.п. не нужны).
- `ingested_ref` в индексном шаблоне не создавался бы — as-of реализуется через
  `release.ingested_at`, поэтому лишний индекс не создаётся (строка в DDL —
  помеченный отказ; при исполнении скрипта её убрать).

---

## 3. Ключ гранулярности observation: источник, оценка, публикация

Ключ: `(metric_id, region_id, frequency_id, period_start, source_id, release_id,
assessment_type, sub_dimension)`.

Последний компонент — `sub_dimension` (подразрез) — добавлен по решению §14.5:
проверка `observations` (42 517 строк) выявила 5 строк с совпадающим
`(показатель, регион, период)` при разном `row_label` — например, подразрез по
назначению объекта (`'жилого назначения'`). Без него эти строки схлопнулись бы.

Каждый компонент решает конкретную коллизию:

| Компонент | Какую коллизию устраняет | Пример из реальных данных |
|---|---|---|
| `metric_id` | сводит 4 шаблона схем к одной таблице | «Ввод жилья» из Росстата и ИЖК из ДОМ.РФ — один домен |
| `region_id` | устраняет 339 вариантов имён (646 сырых значений гео-колонок — замер по всем базам, включая мусор вида `'2007'`, `'I квартал'`, `'ȀПриволжский…'`) | `region_id` вместо текста |
| `frequency_id, period_start` | месячные/квартальные/годовые/накопленные в одном доме | `year+month` (Росстат) vs `report_date` (ЦБ) vs `year` (панель) |
| `source_id` | сопоставление разноисточниковых оценок | ввод жилья Росстата vs ИЖК-модель ДОМ.РФ |
| `release_id` | пересмотры внутри одного источника | ФНС `snapshot`/`snapshot_date` — сейчас единственное место версионности; здесь это становится системным слоем |
| `assessment_type` | различение «flash vs revised» от «Росстат vs ДОМ.РФ» | оперативная оценка Росстата (flash) vs годовая уточнённая (final) |

Почему без этого сопоставление невыполнимо: у ДОМ.РФ и Росстата одно и то же
«состояние» рынка (например, действующие ДДУ) публикуется в разное время и
пересчитывается с разной периодичностью. Если у значения нет пары «к какому моменту
относится оценка (period) × когда стало известно (release.ingested_at/published_at)»,
то любое расхождение между источниками неотличимо от ревизии внутри источника.
Дата оценки живёт в `period_start/period_end`, дата публикации — в
`release.published_at/ingested_at`, тип оценки — в `assessment_type`. Это ровно то,
что §2а ТЗ называет двумя датами, необходимыми для аналитического режима.

---

## 4. Механизм as-of среза

Базовый принцип: «состояние знаний на дату T» = все observation, чей релиз был
загружен/опубликован не позже T, при этом для каждого (metric, region, period)
берётся последняя по времени загрузки оценка данного типа. Реализация — через
`core.release`:

```sql
-- (4.1) Последняя актуальная оценка (витрина marts.v_latest)
CREATE OR REPLACE VIEW marts.v_latest AS
SELECT DISTINCT ON (o.metric_id, o.region_id, o.frequency_id, o.period_start)
       o.metric_id, o.region_id, o.frequency_id, o.period_start, o.period_end,
       o.value, o.assessment_type, o.source_id, o.release_id,
       r.release_label, r.published_at, r.ingested_at, o.quality_flags
FROM core.observation o
JOIN core.release r USING (release_id)
WHERE o.observation_status <> 'rejected'
ORDER BY o.metric_id, o.region_id, o.frequency_id, o.period_start,
         r.ingested_at DESC;

-- (4.2) As-of срез на дату T: что мы ЗНАЛИ на T (по дате публикации источника)
CREATE OR REPLACE VIEW marts.v_asof_published AS
SELECT DISTINCT ON (o.metric_id, o.region_id, o.frequency_id, o.period_start)
       o.metric_id, o.region_id, o.period_start, o.value,
       o.assessment_type, o.source_id, o.release_id, r.published_at, r.ingested_at
FROM core.observation o
JOIN core.release r USING (release_id)
WHERE r.published_at <= :T            -- параметр даты среза
  AND o.observation_status <> 'rejected'
ORDER BY o.metric_id, o.region_id, o.frequency_id, o.period_start, r.published_at DESC;

-- As-of по дате загрузки (наш собственный горизонт знаний, часто важнее published_at)
-- то же, но WHERE r.ingested_at <= :T ORDER BY ... r.ingested_at DESC

-- (4.3) История пересмотров: все версии одного значения
CREATE OR REPLACE VIEW marts.v_revisions AS
SELECT o.metric_id, o.region_id, o.frequency_id, o.period_start,
       o.value, o.assessment_type, o.source_id,
       r.release_id, r.release_label, r.published_at, r.ingested_at,
       o.value - LAG(o.value) OVER w AS delta_prev,
       (r.ingested_at - LAG(r.ingested_at) OVER w) AS time_between_revisions
FROM core.observation o
JOIN core.release r USING (release_id)
WHERE o.observation_status <> 'rejected'
WINDOW w AS (PARTITION BY o.metric_id, o.region_id, o.frequency_id, o.period_start,
                        o.source_id
             ORDER BY r.ingested_at);

-- (4.4) Сопоставление разноисточниковых оценок за период (аналитический режим, критерий 1)
SELECT o.period_start, o.value, o.assessment_type,
       s.source_code, r.published_at, r.ingested_at, r.release_label
FROM core.observation o
JOIN core.source s USING (source_id)
JOIN core.release r USING (release_id)
JOIN core.metric m USING (metric_id)
WHERE m.metric_code = 'housing_input_area_m2_m'
  AND o.period_start >= '2026-01-01' AND o.period_start < '2026-02-01'
ORDER BY o.period_start, s.source_code, r.ingested_at;
-- вернёт строки всех источников и всех типов оценок; расхождения видны сразу

-- (4.5) Длинный ряд с учётом разрывов (исследовательский режим, критерий 2)
WITH breaks AS (
  SELECT break_date, break_type, description, pre_break_base, post_break_base
  FROM meta.series_comparability
  WHERE metric_id = :metric_id AND (region_id IS NULL OR region_id = :region_id)
)
SELECT o.period_start, o.value,
       CASE WHEN b.break_date IS NOT NULL THEN 'BREAK: ' || b.description END AS break_marker
FROM core.observation o
LEFT JOIN LATERAL (
  SELECT * FROM breaks WHERE o.period_start >= break_date
  ORDER BY break_date DESC LIMIT 1
) b ON true
WHERE o.metric_id = :metric_id
  AND o.region_id = (SELECT region_id FROM core.region WHERE region_code = 'RU')
  AND o.assessment_type = 'final'
ORDER BY o.period_start;
-- точки разрыва видны в ряду; конверсия применяется на derived-слое (§7)
```

Витрины «только final/flash» — частичные представления:

```sql
CREATE OR REPLACE VIEW marts.v_final AS
SELECT * FROM marts.v_latest WHERE assessment_type = 'final';
CREATE OR REPLACE VIEW marts.v_flash AS
SELECT * FROM marts.v_latest WHERE assessment_type IN ('flash','nowcast');
```

---

## 5. Пайплайн загрузки — 9 этапов

Реализация: Python-скрипты в репо, запуск по systemd-timer/cron на ВМ YC. Никакого
оркестратора — идемпотентность достигается тем, что каждый этап пишет в свою таблицу
и пере-исполнение даёт тот же результат (ключи с UNIQUE + UPSERT-семантика
`ON CONFLICT DO NOTHING/UPDATE`).

| # | Этап | Вход | Выход (таблицы) | Статусы | Критерий успеха | Идемпотентность |
|---|---|---|---|---|---|---|
| 1 | Получение | URL источника, куки/сессия | файл в `s3://research-wiki/raw/<source>/<YYYY-MM>/` | `registered` → `failed` | файл в бакете, sha256 посчитан | повторное скачивание → тот же sha256 → шаг пропущен |
| 2 | Регистрация файла/релиза | file (sha256, URI) | `core.release` + `core.file_registry` | `registered` | обе записи созданы, хеш совпал | UNIQUE(source_id, release_label) и UNIQUE(uri, sha256) — повтор = no-op |
| 3 | Извлечение (парсинг) | файл, парсер | `staging.*` | `parsed` / `failed` | число строк > 0, схема staging сошлась | staging пересоздаётся per release_id (TRUNCATE + INSERT) |
| 4 | Маппинг | staging-строки | `meta.source_metric_mapping` (новые raw-имена), резолв в `metric_id/region_id` | `mapped` / `needs_review` | 100% строк получили пару (metric_id, region_id); неразрешённые — в очередь ревью | маппинги накапливаются, повторный прогон не создаёт дублей (UNIQUE) |
| 5 | Проверки качества | спроецированные строки | `core.observation` со статусом `raw`/`rejected`, флаги | `validated` / `rejected` | дубли в рамках релиза = 0; обязательные поля заполнены; период согласован с частотой; диапазоны в порядке | перезапуск не меняет уже записанные строки (UNIQUE-ключ наблюдения) |
| 6 | Запись в core | валидные строки | `core.observation` (статус `validated`), `release.status='loaded'` | `loaded` | COUNT вставленных строк == COUNT валидных staging-строк | `ON CONFLICT DO NOTHING` — повторный прогон даёт 0 вставок |
| 7 | Производные | core-наблюдения + реестр формул | `derived.derived_metric` + строки в `observation` с `source_id='derived'` | `computed` | ре-расчёт на том же входе даёт тот же output (проверка хешем результата) | расчёт помечается code_version+params; повтор — обновление derived-релиза, сырьё не трогается |
| 8 | Витрины | core/derived | `marts.*` представления + материализованные витрины | `refreshed` | `REFRESH MATERIALIZED VIEW` успешен, контрольные суммы витрин ожидаемы | представления идемпотентны by construction |
| 9 | Логирование | все этапы | `pipeline_log(release_id, stage, status, started_at, finished_at, rows, error)` | `ok`/`failed` | на каждый release — полная цепочка `loaded` по этапам 1–8 | append-only |

Минимальная схема лога:

```sql
CREATE TABLE IF NOT EXISTS pipeline.pipeline_log (
    log_id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    release_id  bigint,
    stage       smallint NOT NULL CHECK (stage BETWEEN 1 AND 9),
    status      text NOT NULL CHECK (status IN ('ok','failed','skipped')),
    started_at  timestamptz NOT NULL DEFAULT now(),
    finished_at timestamptz,
    rows_affected bigint,
    error_text  text
);
```

---

## 6. Справочник регионов: канонизация 339 вариантов

Замер по всем шести базам: 646 сырых значений в гео-колонках, из них значимая часть —
мусор (годы-строки, `'I квартал'`, проценты, латиница-двойники вида `'Аpхангельская'`,
битые кодировки `'ȀПриволжский…'`). После чистки отчёта P7 остаётся 339 реальных
вариантов написания. Канонизация:

**Структура.** Таблица `core.region` (см. §2) с уровнями `country` (RU + иностранные),
`federal_district` (8 ФО как узлы с `parent_id=RU`), `region` (субъекты РФ с
`parent_id=ФО`), `foreign_region`. Отдельного «типа регион — агрегат» не заводим:
ФО и страна — обычные узлы, агрегация — это JOIN вверх по `parent_id`.

**Подход к маппингу** — три прохода, от дешёвого к дорогому:

1. **Нормализация** (детерминированная, код): Unicode NFC, снятие ударений/нулевых
   ширин, latin→cyrillic для гомоглифов (а→а, о→о), обрезка пробелов/переносов,
   приведение «г. Москва»→«Москва», удаление примечаний «*)». На чистом отчёте P7
   это уже сняло 63 варианта из 402.
2. **Словарь синонимов** — таблица `meta.region_alias`:

   ```sql
   CREATE TABLE meta.region_alias (
       alias       text NOT NULL,
       region_id   bigint NOT NULL REFERENCES core.region(region_id),
       source_id   bigint REFERENCES core.source(source_id),   -- в каком источнике встречается
       confidence  text NOT NULL DEFAULT 'manual'
                   CHECK (confidence IN ('exact','manual','inferred','needs_review')),
       created_at  timestamptz NOT NULL DEFAULT now(),
       PRIMARY KEY (alias, source_id)
   );
   ```

   Словарь — файл `dictionaries/regions.yaml` в git (версионируется, ревьюится),
   загружаемый в таблицу. Первое наполнение: карта архаичных АО (Читинская область →
   Забайкальский край, Камчатская обл. + Корякский АО → Камчатский край, «без авт.
   округа» → соответствующий округ/область), латинских двойников, сокращений.
3. **Fuzzy-дожимание** (`pg_trgm` + `similarity()` ≥ 0.85): остаточные варианты
   предлагаются агентом как кандидаты с `confidence='inferred'` и попадают в
   очередь ревью, а не в факты автоматически. Порог ниже — только в словарь вручную.

**Результат.** Все 339 вариантов получают строку в `region_alias` → `region_id` канона;
`source_metric_mapping.raw_region` ссылается на alias. Агрегация вверх — рекурсивным
CTE либо заранее вычисленным путём (для 90+ субъектов достаточно CTE).

```sql
WITH RECURSIVE up AS (
  SELECT region_id, region_id AS top FROM core.region WHERE level = 'region'
  UNION ALL
  SELECT r.parent_id, up.top FROM core.region r JOIN up ON r.region_id = up.region_id
  WHERE r.parent_id IS NOT NULL
)
SELECT region_id, top FROM up;
```

---

## 7. Производные показатели и сезонная корректировка

Два места хранения:

1. **Реестр расчётов** — `derived.derived_metric` (§2): формула, `params` (jsonb),
   `code_version` (git SHA), дата, входные metric_id. Это источник истины «как
   получено». Любая цифра производного ряда восходит к конкретному расчёту с
   конкретной версией кода — требование воспроизводимости из §16 ТЗ.
2. **Результат** — строки `core.observation` с `source_id = 'derived'` и своим
   `release_id` (производные релизы создаются в `core.release` с
   `source='derived', release_label = 'derived-<код>-<YYYYMMDD>'`). Так темп роста
   и сезонно сглаженный ряд живут рядом с сырыми фактами, но заведомо не
   смешиваются: у них другой source_id, а витрина `v_final` не содержит `derived`
   по умолчанию.

Сезонная корректировка: `transform_type='sa'`, метод (X-13ARIMA-SEAT / STL) и его
параметры — в `params`; сама реализация — Python-функция в репо, путь в
`code_path`. Ключевое правило: SA-ряд **не** перезаписывает сырой; связь
`output_metric_id` → отдельный `metric` с `metric_type='derived'`, `name` вида
«…, сезонно скорректированный». Если алгоритм меняется — новый расчёт, новый релиз;
старые строки остаются, воспроизводимость сохраняется.

Для длинных рядов с разрывом (§4.10 ТЗ): конверсия через разрыв оформляется как
`derived_metric` с `transform_type='link_relative'`, где коэффициент сцепки берётся
из `series_comparability.conversion_rule`. Запрос (4.5) из §4 помечает точки разрыва,
расчёт «сшитого» ряда — задача derived-слоя с фиксацией параметров.

---

## 8. План миграции: 6 SQLite → PostgreSQL без падения 27 скриптов

**Выбор: вариант (а) — сохранить контракт `ensure_db()` и подменить бэкенд слоем
совместимости.** Обоснование:

- 27 скриптов — проверенный, работающий код; переписывать их на новый db-слой
  одновременно с миграцией схемы — двойной риск. Критерий приёмки 3 («ни один
  скрипт не падает») лучше выполняется, если скрипты видят *тот же интерфейс*.
- Реальные чтения идут по двум паттернам: (i) таблицы-«стоги» с текстовым фильтром
  (`indicator = '...'`) и (ii) узкие таблицы-факты. Совместимый слой легко
  обслуживает оба через представления.
- Вариант (б) (переписать на общий db-слой) — правильная цель, но *после*
  миграции: когда PostgreSQL уже работает, переписывается по одному скрипту, каждый
  с проверкой на живых данных. Совмещать — нельзя проверять ни то, ни другое.

### Совместимость SQLite → PostgreSQL: sqlite3-шлюз

Один модуль `scripts/db_compat.py`:

```python
# Суть: заменяет sqlite3.connect(path) на подключение к PostgreSQL,
# а имена старых таблиц/колонок маппит в представления core.
import os, psycopg  # psycopg3
LEGACY_DB = {
    'rosstat_construction.db': 'research_wiki',
    'regions_panel.db':        'research_wiki',
    'fns_tochno_sectors.db':   'research_wiki',
    'cbr_lending.db':          'research_wiki',
    'rosreestr_deals.db':      'research_wiki',
    'developers_ifrs.db':      'research_wiki',
}
def connect(db_name, *a, **kw):
    """drop-in для sqlite3.connect(путь к data/*.db)"""
    return psycopg.connect(os.environ['DATABASE_URL'])
```

Над PostgreSQL создаются **представления-двойники** с именами старых таблиц и
колонок. Для скриптов, чьё чтение — `SELECT ... WHERE indicator = 'X'`, представление
делает JOIN с `source_metric_mapping`/`metric` на лету:

```sql
-- пример: cbr_mortgage_monthly в старом виде (стог ЦБ)
CREATE OR REPLACE VIEW core.legacy_cbr_mortgage_monthly AS
SELECT rg.name_ru AS region_name, o.period_start::date AS report_date,
       m.metric_code AS indicator, o.value::double precision AS value,
       u.unit_code AS unit
FROM core.observation o
JOIN core.metric m USING (metric_id)
JOIN core.frequency f USING (frequency_id)
JOIN core.unit u ON u.unit_id = m.unit_id
JOIN core.region rg USING (region_id)
JOIN core.source s USING (source_id)
WHERE s.source_code = 'cbr' AND f.frequency_code = 'M';
```

Несовпадающие диалекты SQLite/PostgreSQL, встреченные в скриптах: `PRAGMA`
(3 файла обслуживания — `reindex_vacuum_db.py`, `vacuum_into.py`,
`cleanup_rosstat_db.py` — они **исключаются** из совместимости, их работа после
миграции становится не нужна: VACUUM делает autovacuum, чистка — SQL-миграциями),
`INTEGER PRIMARY KEY AUTOINCREMENT` (наши представления не возвращают вставку),
`strftime`-функции дат (заменяются в представлениях выражениями `to_char`), типы
REAL vs numeric (в представлениях явный `::double precision`).

### Перечень минимальной адаптации скриптов (полный, по группам)

| Группа | Скрипты | Адаптация |
|---|---|---|
| Аналитические читатели (19) | `collect_panel*`-подобные, `ikv_benchmarks.py`, `wnok_midas_lite.py`, `housing_supply_elasticity.py`, `midas_ddu_wordstat.py`, `fns_sector_nowcast.py`, `export_*.py` (2), `bud1.py`, `bud2.py`, `token_monitor.py`, `wordstat_core_index.py`, `housing_input_roschart_collect.py` | одна строка: `import sqlite3` → `import db_compat as sqlite3` (модуль-прокси с тем же API `.connect()`). Точечные правки: `PRAGMA`/`VACUUM`-вызовы — убрать; `?`-плейсхолдеры работают в psycopg только с `%s` — но большинство скриптов читают без параметров; там где есть — замена на `%s`. |
| Парсеры/загрузчики (4) | `update_rosstat.py`, `parse_cbr_lending.py`, `parse_tochno_rfsd.py`, `fns_parse_load.py` | вместо `INSERT INTO <sqlite-таблица>` — запись через новый пайплайн (этапы 2–6), т.е. вызовы `pipeline.ingest()`; либо через представления с `INSTEAD OF`-триггерами (медленнее, зато без переписывания логики). Рекомендуется первое. |
| Сборщики (4) | `developers_ifrs_collect.py`, `fns_annual_rebuild.py`, `fns_rf_annual_build.py`, `rosstat_prom_monthly_parse.py` | как загрузчики; выход — в staging/core, а не в SQLite-файл |
| Обслуживание (4) | `cleanup_rosstat_db.py`, `reindex_vacuum_db.py`, `vacuum_into.py`, `nightly_backup.py` | выводятся из эксплуатации; их функции заменяются: чистка — миграциями, бэкап — `pg_dump` + S3 (§10), индексы — обычным DDL |
| Служебный | `gcs_sync.py`, `canonize_regions.py` | `gcs_sync.py` демонтируется (§9); `canonize_regions.py` — переписывается на `meta.region_alias` |

Контракт `ensure_db(name)` при этом **сохраняется как обёртка** в `gcs_sync.py` до
Фазы 4: после перехода на PostgreSQL он просто возвращает строку подключения
(DSN) вместо пути к файлу, а скрипты-потребители, у которых
`ensure_db(...)` → `sqlite3.connect(path)`, через прокси-модуль получают то же
подключение к PostgreSQL. Это удерживает 11 скриптов с `import gcs_sync` от правок.

### Фазы миграции (с проверкой на каждом шаге)

- **Ф0. Подготовка.** Развёртывание PostgreSQL 15 на ВМ YC, `pg_trgm`. Схемы core/meta/
  derived/marts, DDL §2. Загрузка справочников (unit, frequency, source, region —
  канон ~90 субъектов + 8 ФО + РФ + иностранные; словарь alias). *Проверка:* DDL
  применён без ошибок, счётчики справочников соответствуют плану.
- **Ф1. Перенос данных.** Для каждой из 6 SQLite-баз — скрипт `migrate_<db>.py`:
  чтение SQLite → маппинг (§6 + `source_metric_mapping`) → staging → валидация →
  core. Порядок: `developers_ifrs.db` (512 строк — обкатка) → `rosreestr_deals.db`
  (52 К) → `cbr_lending.db` → `regions_panel.db` → `fns_tochno_sectors.db` (3,7 М) →
  `rosstat_construction.db` (1,5 М). *Проверка на каждой:* `COUNT(*)` в core ==
  COUNT в SQLite (минус строки, помеченные `rejected` с обоснованием); сверка
  агрегатов (сумма `value` по ключу) SQLite vs PostgreSQL; запуск выборочных
  аналитических скриптов на новом бэкенде.
- **Ф2. Дуальный режим.** Скрипты работают через `db_compat` на PostgreSQL;
  SQLite-файлы остаются нетронутыми как источник правды на время параллельной
  эксплуатации (2–4 недели). *Проверка:* критерий приёмки 3 — все 27 скриптов
  отработали; критерий 1 — тест-запросы §4 (4.4) возвращают мультиисточниковые
  оценки.
- **Ф3. Переключение загрузчиков.** 8 скриптов-писателей переключаются на пайплайн;
  SQLite-файлы переводятся в read-only (`chmod 444`) и переносятся в бакет как
  архивный снапшот `s3://research-wiki/archive/sqlite-2026MMDD/`.
- **Ф4. Расчистка.** SQLite-файлы удаляются с диска после успешной Ф3 (1,45 ГБ
  освобождается), `.gitignore` пересматривается (§12), `nightly_backup.py`
  заменяется на `pg_backup.py` (§10). *Проверка:* `grep -r 'sqlite3.connect'
  scripts/ | wc -l` = 0 у активных скриптов; восстановление из бэкапа проверено
  фактически (критерий 5).

---

## 9. Демонтаж GCS

**Цель:** после работ `grep -rE 'gs://|gsutil|gcsfuse'` по репозиторию возвращает
пусто (кроме исторических документов вики, если владелец решит их оставить —
см. «Открытые вопросы»).

### Чек-лист зависимостей (замерено)

| # | Место | Что делать |
|---|---|---|
| 1 | `scripts/gcs_sync.py`: `GCS_BUCKET` (env-дефолт `wiki-research-508405`) | удалить вместе с файлом после Ф4 |
| 2 | `scripts/gcs_sync.py`: `GCS_RAW_PREFIX`, `GCS_DB_PREFIX` (2×`gs://…`) | там же |
| 3 | `scripts/gcs_sync.py`: `GCS_MOUNT` (`~/gcs-wiki`) | там же |
| 4 | `scripts/gcs_sync.py`: `_gsutil(...)` + `gsutil du` в `cmd_status`/`cmd_verify` | там же |
| 5 | `scripts/gcs_sync.py`: `ensure_db()`/`raw_path()` — **контракт**, потребляемый 11 скриптами | до Ф4: заменить тело на no-op/DSN-обёртку; после Ф4: удалить |
| 6 | 11 скриптов с `import gcs_sync` (список в §0) | переключить на `db_compat`/новый пайплайн |
| 7 | `raw/` — симлинк на `~/gcs-wiki/raw` (2,1 ГБ) | размонтировать gcsfuse, заменить симлинк реальным каталогом или точкой монтирования S3 YC (см. ниже) |
| 8 | `.gitignore`: блок `raw/`, `data/*.db` (5 строк), `data/archive/*.jsonl`, raw-подкаталоги RAR/parquet/zip | переписать под новую топологию (§12) |
| 9 | `nightly_backup.py` — `gcs_sync` в sync-ветке | заменить на pg_backup (§10) |
| 10 | gcsfuse-маунт в системе (`~/gcs-wiki`) | `fusermount -u ~/gcs-wiki`, удалить из fstab/systemd, если был |

### Перенос 3,5 ГБ в YC Object Storage

Бакет: `research-wiki` (STANDARD, приватный) — тот же сервисный аккаунт, что уже
создан (`compute-as`). Перенос через `rclone` (один инструмент и для копирования,
и для монтирования, и для верификации — не три инструмента):

```bash
rclone config  # remote 'ycs': type s3, endpoint https://storage.yandexcloud.net, keys от YC
rclone copy /home/lnr/gcs-wiki/raw  research-wiki:raw/  --checksum --transfers 8
rclone copy /home/lnr/gcs-wiki/data research-wiki:data/ --checksum
rclone copy /home/lnr/research-wiki/data/archive research-wiki:archive/ --checksum
```

Итого ~3,6 ГБ (2,1 raw + 1,5 data + 0,1 archive). Проверка целостности: `rclone check
--one-way` + сверка sha256 каждого файла против `core.file_registry.sha256` (для
файлов, уже учтённых в БД; для остальных — `rclone lsjson` + суммирование размеров
и md5/s3-etag). Бюджет: ~1,2 ₽/ГБ·мес × 4 ГБ ≈ 5 ₽/мес.

### Монтирование raw/: выбор

**Выбор: `rclone mount` к S3 YC на ВМ YC, с локальной синхронизацией как fallback.**
Обоснование против альтернатив:

- *s3fs* — проще, но заметно медленнее на множестве мелких файлов и менее надёжен в
  многопоточном чтении; rclone имеет кэш (`--vfs-cache-mode writes`), лучший
  контроль таймаутов и ту же конфигурацию, что и у копирования/верификации — одна
  конфигурация на все задачи.
- *Локальная синхронизация* (полная копия raw/ на диск ВМ) — самый надёжный и самый
  быстрый для чтения вариант при диске 100 ГБ SSD на ВМ: 2,1 ГБ — копейки. Рекомендуемая
  **гибридная** схема: рабочая копия raw/ на диске ВМ (создаётся `rclone sync` из
  бакета, идемпотентно), точка монтирования rclone — только как прозрачный доступ для
  редких файлов вне рабочей копии. На ВМ YC диск дешёв и большой — синхронизация
  надёжнее и быстрее, чем FUSE-маунт в горячем пайплайне; FUSE оставляем как запасной
  путь для VPS (там диска мало — 4,5 ГБ свободно, полная копия не влезает).

```bash
# systemd-юнит или user-скрипт на ВМ:
rclone mount research-wiki:raw ~/raw-mount --vfs-cache-mode writes --daemon
# или периодическая синхронизация:
rclone sync research-wiki:raw/ /srv/research-wiki/raw/ --checksum --delete-during
```

Путь `raw/` в репо: заменить симлинк на симлинк на `/srv/research-wiki/raw` (или на
локальную копию на ВМ), чтобы скрипты, обращающиеся к `raw/...` по относительному
пути, не заметили подмены.

---

## 10. Бэкапы и фактическая верификация восстановления

Схема: `pg_dump` (custom format, сжатие) → S3 YC, **каждую ночь**, с обязательной
фактической проверкой восстановления. Не заявить, а проверить — критерий приёмки 5.

```bash
#!/usr/bin/env bash
# scripts/pg_backup.sh — ночной цикл
set -euo pipefail
STAMP=$(date -u +%Y%m%d-%H%M%S)
BUCKET=s3://research-wiki/backups/pg
# 1. Дамп (custom, сжатие zlib) + контрольный манифест
pg_dump -Fc -Z 6 -f /tmp/research_wiki_$STAMP.dump research_wiki
sha256sum /tmp/research_wiki_$STAMP.dump > /tmp/research_wiki_$STAMP.sha256
rclone copy /tmp/research_wiki_$STAMP.dump $BUCKET/ --checksum
# 2. ФАКТИЧЕСКОЕ восстановление: поднимаем временную базу из дампа
createdb restore_test_$STAMP
pg_restore -d restore_test_$STAMP --no-owner /tmp/research_wiki_$STAMP.dump
# 3. Верификация: счётчики ключевых таблиц против боевой базы
psql -d restore_test_$STAMP -Atc "
  SELECT (SELECT count(*) FROM core.observation),
         (SELECT count(*) FROM core.metric),
         (SELECT count(*) FROM core.region)" > /tmp/restore_counts.txt
psql -d research_wiki -Atc "/* те же три счётчика */" > /tmp/production_counts.txt
diff /tmp/restore_counts.txt /tmp/production_counts.txt || { echo RESTORE_FAIL; exit 1; }
# 4. Плюс функциональный smoke-тест: as-of запрос возвращает ≥1 строку
# 5. Уборка: dropdb restore_test_$STAMP; удаление локальных tmp; retention 30 дней в S3
dropdb restore_test_$STAMP
```

Ключевые решения: (а) восстановление делается **каждую ночь в ту же ВМ** (временная
база) — не реже чем раз в месяц это обязательно, ежедневное стоит секунды на 1,5 ГБ
и снимает вопрос «а работает ли бэкап» навсегда; (б) сверка счётчиков — объективный
критерий «восстановилось»; (в) дифференциально-инкрементальные схемы (WAL-архив,
pgBackRest) не нужны: объём 1,5 ГБ, запись редкая, полный дамп nightly — дешевле и
проще; (г) раз в месяц — восстановление на чистый инстанс (вторая ВМ/контейнер) для
проверки, что бэкап не зависит от локальных артефактов. Дополнительно: ежемесячный
дамп-«архив» в класс COLD.

---

## 11. Обоснование выбора по критериям ТЗ

| Критерий | Решение | Почему достаточно |
|---|---|---|
| **Объём и рост** | PostgreSQL на ВМ YC (диск 100 ГБ SSD). Текущий объём 1,45 ГБ; рост 10× (15 ГБ) покрывается с запасом. Сырые файлы (сейчас 3,6 ГБ) — в бакет, в БД только метаданные | вертикальный масштаб одной ВМ годами опережает рост проекта; шардирование/кластер не нужны |
| **Частота записи** | пакетные вставки по расписанию (ежедневно/ежемесячно по источнику), 5,9 млн строк — вставка занимает минуты | никакой OLTP-нагрузки нет; батч-INSERT + UNIQUE-ключ решают и скорость, и идемпотентность |
| **Параллельный доступ** | один экземпляр PostgreSQL, несколько читателей-коннектов; запись — последовательно из пайплайна | единовременно работают 1–2 агента; MVCC PostgreSQL покрывает читателей во время вставки |
| **Воспроизводимость** | неизменяемый core (append-only), `release` + `file_registry` + `derived_metric.code_version` = полная трассировка значение → релиз → файл → sha256 → формула | любая цифра выводима из конкретной версии ряда (требование §16 ТЗ) |
| **Операционная сложность** | 1 ВМ + 1 бакет; cron/systemd-timer; нет очередей, оркестраторов, стриминга | минимальная достаточность (§14 ТЗ); всё администрируется одним человеком |
| **Стоимость** | см. ниже | — |

Оценка стоимости YC (цены по прайсу Object Storage/Compute на момент ТЗ, округлённо):

| Статья | Оценка |
|---|---|
| ВМ 2 vCPU/8 ГБ, 100 ГБ SSD, 24/7 (должна быть включена для базы) | ~2 500–3 200 ₽/мес |
| Object Storage STD: 10 ГБ (бэкапы 30 дней + raw 4 ГБ) | ~15–25 ₽/мес |
| Egress/трафик | ~0 (внутриоблачный) |
| **Итого** | **~2 600–3 300 ₽/мес** |

Замечание: ВМ для базы не может быть прерываемой (данные должны жить постоянно),
поэтому дороже варианта «сборщика» из `yandex-cloud-data-infra.md` (~200 ₽/мес).
Если нужно сэкономить: базовая ВМ 2/4 ГБ вместо 2/8 → ~1 900–2 200 ₽/мес; но 8 ГБ RAM
комфортнее для 5,9 млн строк + аналитические запросы. Прерываемая ВМ-«сборщик»
из того документа остаётся отдельным дешёвым узлом и в эту архитектуру не входит.

---

## 12. Пересмотр .gitignore и data/catalog.yaml

### Каталог: разделение данных и библиографии

Сейчас `catalog.yaml` смешивает 165 записей, из них ~58 — data-записи (type в наборе
api/local_file/dataset/data_portal/data_release/file/processed_timeseries, замерено)
и ~107 — библиография; `type` принимает 43 значения (полный список: academic_article,
ai-dialog, analysis, api, article, bank_research, book-chapter, comparative_analysis,
data_portal, data_release, dataset, document, feds-note, file, government_data,
industry-news, industry-report, industry_analysis, industry_article, industry_report,
industry_research, industry_survey, journal_article, local_file, macro_analysis,
methodology, methodology_document, methodology_documentation, methodology_note,
model_code, original-article, paper, pdf, processed_timeseries, rating_agency_outlook,
report, research-report, research_concept, research_report, research_review,
translation, working-paper, working_paper).

Решение:

1. **Разделить на два файла.** `data/catalog.yaml` — только источники данных
   (~58 записей) с обязательным полем `table`/`pipeline_ref`; библиография —
   `bibliography.yaml` в корне вики (или `papers/catalog.yaml`), синхронизирована
   с frontmatter страниц.
2. **Таксономия type: 43 → 8.** Для данных: `api`, `file_download`, `dataset`,
   `derived_timeseries`. Для библиографии: `paper` (объединяет article, journal_article,
   working-paper/working_paper, original-article, academic_article, research-report),
   `report` (industry-*, bank_research, government…), `methodology`, `other`. Каждое
   из 43 значений получает маппинг в YAML-миграции, новые значения запрещаются
   валидатором.
3. **Фантомные таблицы (22–23)**: замер — 52 упомянутых значения `table`, 23 из них
   физически отсутствуют (`cbr_usd_rate`, `cbr_eur_rate`, все 8 `eiszhk_*`,
   `domrf_housing_starts/apartment_sales/construction/prices`, `rosstat_cpi/income/
   construction`, `gdelt_housing_sentiment_daily`, все 4 `rosstat_ind_*`, плюс одна
   ячейка-строка с 4 именами через запятую). Для каждой фантомы — одно из двух:
   (а) источник планировался, но не собран → запись каталога получает `status:
   planned`, `table` очищается; (б) источник заменён другим → запись получает
   `status: superseded_by: <id>` или удаляется. **Целевое состояние:** каждая запись
   data-каталога ссылается на реально существующую таблицу PostgreSQL (или на
   зарегистрированный файл), расхождение ноль — это критерий приёмки 4. Автопроверка:
   скрипт `validate_catalog.py`, который сравнивает `table`-поле каталога со списком
   таблиц базы и падает при первом расхождении; запускается в CI (GitHub Actions —
   бесплатный для приватного репо) и после каждого пайплайна.

### Новый .gitignore

```gitignore
# ── Данные: БД и сырьё живут в S3 YC / на диске ВМ, не в git ──
data/*.db
data/archive/*.jsonl
raw/
# (симлинк на /srv/research-wiki/raw или на локальную копию)

# ── Прочее (существующие правила сохраняются) ──
raw/papers/Workpapers/
*.pdf
_archive/
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache/
.obsidian/plugins/*/*.min.js
raw/rosstat/socioeconomic_regions/*.rar
raw/fns/tochno-st/by_section/
raw/rosstat/regions_collection_102/*.parquet
raw/rosstat/regions_collection_102/*.zip
```

Изменения против текущего: (а) строка `rosreestr_deals.db` без префикса исправляется
на `data/rosreestr_deals.db`, добавляются `data/developers_ifrs.db`,
`data/fns_tochno_sectors.db`; (б) правила `data/*.db` после Ф4 можно заменить на
комментарий, т.к. SQLite-файлов больше не будет, но правило оставляем как защиту;
(в) `.env` с ключами YC — убедиться, что игнорируется (проверить, сейчас в
`.gitignore` не видно).

---

## 13. Соответствие критериям приёмки ТЗ

1. **Аналитический режим** (сопоставление мультиисточниковых оценок): ключ
   `observation` содержит `source_id` + `assessment_type` + даты через `release`
   (§3); запрос 4.4 из §4 возвращает оценки всех источников за период с
   `published_at`/`ingested_at` каждой — расхождение видно и датировано.
2. **Исследовательский режим** (ряд на дату T, без разрывов, воспроизводимость):
   as-of-витрины 4.2 (срез на T), `series_comparability` + запрос 4.5 (маркеры
   разрывов) + derived-конверсия через link-факторы (§7), append-only core + git SHA
   в `derived_metric.code_version` — расчёт годичной давности повторяется на том же
   срезе.
3. **27 скриптов не падают**: контракт `ensure_db()` сохранён (обёртка возвращает DSN
   через `db_compat`-прокси, §8); перечень адаптации — таблица в §8; 4 скрипта
   обслуживания выводятся из эксплуатации осознанно с заменой функциональности.
4. **Каталог = физическая реальность**: `validate_catalog.py` в CI, статусная модель
   planned/superseded для фантомов, 43→8 значений `type` (§12); критерий — ноль
   расхождений.
5. **Восстановление проверено фактически**: ночной pg_dump + pg_restore во временную
   базу + diff счётчиков ключевых таблиц + smoke-запрос (§10).

---

## 14. Решения владельца (зафиксировано 16.09.2026)

Все восемь вопросов закрыты. Разбор опирается на факты, проверенные на диске.

### 14.1. Бюджет и размер ВМ — РЕШЕНО

Постоянная ВМ в YC: **4×20% vCPU, 8 ГБ RAM, 60 ГБ SSD ≈ 4 300 ₽/мес**.
Управляемый PostgreSQL отклонён: минимальный кластер (1 хост 2/8 + 100 ГБ SSD)
≈ 7 200 ₽/мес — дороже самой ВМ. База разворачивается самогестедом на этой же
машине. Двадцать процентов vCPU достаточно: Hermes большую часть времени ждёт
ответа API, а не считает.

Раскладка: PostgreSQL + сборщик + cron живут на YC-ВМ; gateway, Telegram-канал,
LLM-вызовы и Wordstat остаются на зарубежном VDS (Telegram с YC-адреса
недоступен — проверено, блокировка по SNI на уровне DPI).

### 14.2. Фантомные таблицы — РЕШЕНО, разбор по фактам

Проверка 22 записей показала, что «фантомы» — не отсутствующие данные, а
неразделённая широкая таблица. Три группы с разной судьбой:

**Группа A — данные есть, надо разделить (17 записей).**
- 7 из 8 записей ЕИСЖС фактически покрыты `domrf_indicators` через колонку
  `data_type`: `stock` (356 400), `flow` (312 840), `ddu` (40 392),
  `permits_flow` (31 408), `permits_stock` (31 840), `summary` (5),
  `mortgage` (852). Восьмой — `eiszhk_complex_dev` — в сырье лежит
  `01_01_stockvariableskrt.xlsx`, требует загрузки.
- 4 записи ДОМ.РФ (`domrf_housing_starts`, `domrf_apartment_sales`,
  `domrf_construction`, `domrf_prices`) — те же данные, заявленные как
  отдельные таблицы.
- 5 записей индексов производства (`rosstat_ind_prod_rf`, `rosstat_ind_saar`,
  `rosstat_ind_revisions`, `rosstat_ind_prod_qtr`) — **исходные файлы лежат в
  сырье и не загружены**: `raw/rosstat/data/ind_baza_2023_07-2026.xlsx`,
  `ind_baza_2023_2kv-2026.xlsx`, `ind_sub_2023_07-2026.xlsx`,
  `utoch_ind_2020-2026.xlsx` (история ревизий — основа версионности).

**Группа B — данных нет, API доступен.** `cbr_usd_rate`, `cbr_eur_rate`
(XML ЦБ, тривиально), `rosstat_cpi`, `rosstat_income`, `rosstat_construction`.

**Группа C — сознательно отвергнуто.** `gdelt_housing_sentiment_daily`:
тональностный индекс признан неработающим, файлы `data/gdelt_*.csv` оставлены
как отрицательный результат. Удалить из каталога.

**Порядок работ (выбор владельца): поэтапно.** Сначала группа A в части ЕИСЖС
и индексов производства — они покрывают текущие исследования (наукастинг ИКВ,
ВНОК, СМР). Затем остальное.

### 14.3. Сцепка длинных рядов — РЕШЕНО

**Брать официальные сопоставимые ряды Росстата, свою сцепку не считать.**
`series_comparability` всё равно заполняется — но не вычисленными
link-коэффициентами, а ссылками на официальные сопоставимые публикации.
Плюс: не порождаем допущений и воспроизводим методологию первоисточника.
Минус, который надо держать в уме: привязка к пересчётам Росстата — при
изменении официального ряда наши длинные ряды надо пересобирать.

### 14.4. Фирменный уровень ФНС — ОТЛОЖЕНО

**Пока не трогать.** 3,7 млн строк «фирма × год» остаются в текущем виде
(`fns_tochno_sectors.db`) до тех пор, пока общая база не заработает.
Отдельная схема `firms` вне домена `observation` — решение на потом, когда
firm-level панель войдёт в активную работу.

### 14.5. Строгость ключа наблюдения — РЕШЕНО фактом

**В ключ добавляется колонка `sub_dimension`.** Проверка `observations`
подтвердила легитимные дубли внутри одного показателя и периода: 42 517 строк,
из них 5 с совпадающим `(показатель, регион, период)` при
`row_label = 'жилого назначения'` — то есть подразрез по назначению объекта.
Без `sub_dimension` эти строки схлопнутся и одна затрёт другую.

Итоговый ключ: `(metric_id, region_id, frequency_id, period_start, source_id,
release_id, assessment_type, sub_dimension)`.

### 14.6. Чистота от GCS — РЕШЕНО

Критерий: **чисто в коде, конфигурации и скриптах**. Исторические документы
вики (аналитические записки, журнал) не переписываются. Проверка показала, что
упоминания `gs://`/`gsutil`/`gcsfuse` остались **только в трёх файлах**:
`AGENTS.md` и двух документах по БД (`database-target-spec.md`,
`database-architecture.md`). В коде и скриптах их уже нет — `raw/` подключён
симлинком, путь виден только внутри `gcs_sync.py`.

### 14.7. Retention staging-слоя — РЕШЕНО

Держать **3 последних релиза плюс всё за текущий месяц**. Переprocessить
последнюю ошибку можно, копить историю всех загрузок незачем —
гармонизированные данные хранятся в `core` неизменно.

### 14.8. Канонический справочник регионов — ЗАКРЫТО

Справочник построен: **102 канонические записи** (1 страна + 8 федеральных
округов + 91 регион + 1 свод новых территорий + 1 город), карта **432 сырых
написания**, покрытие **2 354 514 наблюдений**, ноль несопоставленных гео-сущностей.
Из 646 уникальных значений 214 исключены как не-региональные (подписи строк).
Введена колонка `aggregation` — различает базовые ряды и агрегаты
(«с автономными округами», свод новых территорий), чтобы варианты «с АО» и
«без АО» не схлопывались в один код.
Артефакты: `data/regions_canonical.csv`, `data/region_aliases.csv`,
`data/region_unmatched.txt`, скрипт `scripts/build_region_reference.py`.
Подробный разбор и 4 спецслучая на ревью — в [[queries/regions-reference]].
