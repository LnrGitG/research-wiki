CREATE SCHEMA IF NOT EXISTS core;

CREATE SCHEMA IF NOT EXISTS meta;

CREATE SCHEMA IF NOT EXISTS derived;

CREATE SCHEMA IF NOT EXISTS marts;

CREATE SCHEMA IF NOT EXISTS pipeline;

CREATE TABLE core.unit (
    unit_id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    unit_code    text NOT NULL UNIQUE,          -- 'RUB', 'MLN_RUB', 'SQM', 'PCT', 'COUNT'
    name_ru      text NOT NULL,
    description  text,
    created_at   timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE core.frequency (
    frequency_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    frequency_code text NOT NULL UNIQUE,         -- 'D','M','Q','A','CUM_M','CUM_Y'
    name_ru        text NOT NULL,
    period_type    text NOT NULL
                   CHECK (period_type IN ('date','month','quarter','year','cumulative')),
    months_per_period int CHECK (months_per_period BETWEEN 1 AND 12)
);

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

CREATE INDEX idx_region_parent ON core.region(parent_id);

CREATE INDEX idx_region_level  ON core.region(level);

CREATE INDEX idx_region_name_trgm ON core.region USING gin (name_ru gin_trgm_ops);

CREATE INDEX idx_file_release ON core.file_registry(release_id);

CREATE INDEX idx_smm_raw_metric ON meta.source_metric_mapping USING gin (raw_metric gin_trgm_ops);

CREATE INDEX idx_obs_lookup ON core.observation
    (metric_id, region_id, period_start DESC, assessment_type, release_id DESC);

CREATE INDEX idx_obs_release   ON core.observation(release_id);

CREATE INDEX idx_obs_flags     ON core.observation USING gin (quality_flags);

CREATE INDEX idx_dm_output ON derived.derived_metric(output_metric_id, computed_at DESC);

CREATE TABLE meta.region_alias (
       alias       text NOT NULL,
       region_id   bigint NOT NULL REFERENCES core.region(region_id),
       source_id   bigint REFERENCES core.source(source_id),   -- в каком источнике встречается
       confidence  text NOT NULL DEFAULT 'manual'
                   CHECK (confidence IN ('exact','manual','inferred','needs_review')),
       created_at  timestamptz NOT NULL DEFAULT now(),
       PRIMARY KEY (alias, source_id)
   );