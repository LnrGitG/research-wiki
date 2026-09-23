-- ============================================================================
-- Схема dkp: решения Банка России по ключевой ставке (предложение архитектуры)
-- БД research_wiki (PostgreSQL 16.15, ВМ YC research-db).
-- Автор: профиль macroeconomist, 2026-09-23. СТАТУС: предложение, не применено.
--
-- Цели (из постановки):
--  1) хранить решения по ключевой ставке: значение, изменение, решение СД,
--     заявление Председателя, резюме (пресс-релиз), среднесрочный прогноз
--     (4 раза в год, к опорным заседаниям);
--  2) поддерживать анализ эффективности ДКП (прогноз vs факт, трансмиссия,
--     предсказуемость траектории);
--  3) сохранять весь исторический ряд предпосылок и аргументов Банка России
--     для учёта при принятии очередного решения.
--
-- Принципы: не дублировать конвенции v2 — документы регистрируются в
-- core.document + core.file_registry (sha256), происхождение загрузки — в
-- v2.load_run/load_check, источник v2.source id=2 (cbr). Ключевой новый
-- объект — dkp.argument: разбор каждого вербального источника на атомарные
-- аргументы с рубрикатором и вектором (pgvector, Yandex 256-dim, как в
-- build_yandex_embeddings.py) — это и есть «ряд предпосылок».
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS dkp;
COMMENT ON SCHEMA dkp IS
  'Решения Банка России по ключевой ставке: заседания, решения, решётка операционных ставок, аргументы, резюме обсуждения, среднесрочные прогнозы.';

-- ---------------------------------------------------------------------------
-- 1. Заседания Совета директоров по ключевой ставке
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dkp.meeting (
    meeting_id        bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    meeting_date      date NOT NULL,
    decision_kind     text NOT NULL DEFAULT 'scheduled'
                      CHECK (decision_kind IN ('scheduled', 'unscheduled')),
    is_pillar         boolean NOT NULL DEFAULT false,   -- опорное: со среднесрочным прогнозом
    press_release_url text,
    published_at      timestamptz,
    created_at        timestamptz NOT NULL DEFAULT now(),
    UNIQUE (meeting_date, decision_kind)
);
COMMENT ON TABLE dkp.meeting IS
  'Календарь заседаний СД: 8 плановых в год (пятницы), из них 4 опорных. Источник: cbr.ru/dkp/mp_dec/ (лента) + cbr.ru/dkp/how_dec/.';

-- ---------------------------------------------------------------------------
-- 2. Решение СД (значение ключевой ставки + формулировка)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dkp.decision (
    decision_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    meeting_id    bigint NOT NULL REFERENCES dkp.meeting(meeting_id),
    rate_prev     numeric(6,2) NOT NULL,   -- ключевая ставка до решения
    rate_new      numeric(6,2) NOT NULL,   -- ключевая ставка после решения
    delta_bp      integer GENERATED ALWAYS AS
                  (round((rate_new - rate_prev) * 100)) STORED,
    action        text NOT NULL CHECK (action IN ('cut', 'hold', 'hike')),
    headline_ru   text,                    -- формулировка пресс-релиза одной строкой
    signal_note   text,                    -- сопроводительный сигнал (каким текстом)
    document_id   bigint REFERENCES core.document(document_id),  -- пресс-релиз
    source_id     bigint REFERENCES v2.source(source_id) DEFAULT 2,
    sha256        text,                    -- дублируется из file_registry для скорости
    UNIQUE (meeting_id)
);
COMMENT ON TABLE dkp.decision IS
  'Решение по ключевой ставке. Политика единого голоса: одно решение на заседание.';

-- ---------------------------------------------------------------------------
-- 3. Решётка операционных ставок, действующая с даты решения
--    (ступенчатое хранение: строка = уровень ставки с effective_from;
--     вьюха v_daily_rates разворачивает в дневной ряд)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dkp.rate_level (
    level_id       bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    decision_id    bigint REFERENCES dkp.decision(decision_id),  -- решение, вводящее уровень
    rate_code      text NOT NULL,        -- открытый словарь, см. COMMENT
    rate_group     text NOT NULL,        -- 'key'|'constant'|'auction'|'deposit'|'irr'|'nkr'
    value          numeric(9,4) NOT NULL,
    annualized     boolean NOT NULL DEFAULT true,
    effective_from date NOT NULL,
    effective_to   date,                 -- NULL = действует; поддерживается при загрузке
    source_id      bigint REFERENCES v2.source(source_id) DEFAULT 2,
    UNIQUE (rate_code, effective_from)
);
CREATE INDEX IF NOT EXISTS ix_rate_level_code_from ON dkp.rate_level (rate_code, effective_from);
COMMENT ON TABLE dkp.rate_level IS
  'Операционная решётка: ключевая, ПВР/СПВР, РЕПО (аукцион/фикс), ИКР, НКР, ломбардные, депозитные, СКС/СКС-о.
   Точные коды операций сверять с cbr.ru/hd_base и комментариями операционной процедуры — словарь открытый.';

-- ---------------------------------------------------------------------------
-- 4. Атомарные аргументы (ПРЕДПОСЫЛКИ — ядро исторического ряда)
--    Каждый вербальный источник (пресс-релиз, пресс-конференция, резюме
--    обсуждения, доклады) разбирается на аргументы: блок + направление + текст.
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dkp.argument (
    argument_id  bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    decision_id  bigint REFERENCES dkp.decision(decision_id),   -- если привязан к решению
    statement_id bigint,   -- FK на dkp.statement (см. ниже); заполнить после
    block        text NOT NULL,        -- рубрикатор ниже
    direction    text NOT NULL DEFAULT 'neutral'
                 CHECK (direction IN ('hawkish', 'neutral', 'dovish')),
    text_raw     text NOT NULL,        -- исходный абзац/тезис
    text_short   text,                 -- сжатая формулировка
    source_doc_code text,              -- doc_code в core.document
    source_span  text,                 -- 'пресс-релиз §2', 'пресс-конф. 12:05'
    embedding    vector(256),          -- Yandex text-search-doc, как в вики-стеке
    classifier_version text NOT NULL,  -- кто размечал: 'manual' | 'llm:<model>:<prompt_v>'
    created_at   timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_argument_block ON dkp.argument (block, decision_id);
-- HNSW (pgvector 0.6): поиск прецедентов по смыслу; объёмы ~10^3 строк.
CREATE INDEX IF NOT EXISTS ix_argument_emb
    ON dkp.argument USING hnsw (embedding vector_cosine_ops);
COMMENT ON TABLE dkp.argument IS
  'Рубрикатор block (v1, открытый): inflation_now, inflation_expect, inflation_forecast,
   demand, output, labour, wages, fx, credit, budget_rule, fiscal, external, oil,
   import_prices, risk_infl, risk_disinfl, transmission, signal, rationale, dissent, other.
   Пополнять по фактической структуре пресс-релизов; изменение рубрикатора — версионировать.';

-- ---------------------------------------------------------------------------
-- 5. Заявления Председателя (и другие вербальные интервенции)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dkp.statement (
    statement_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    kind         text NOT NULL,        -- 'press_conf' | 'speech' | 'testimony' | 'interview'
    speaker      text NOT NULL DEFAULT 'Председатель Банка России',
    event_date   date NOT NULL,
    meeting_id   bigint REFERENCES dkp.meeting(meeting_id),  -- пресс-конф. привязана к заседанию
    url          text NOT NULL UNIQUE,
    body         text NOT NULL,
    embedding    vector(256),
    document_id  bigint REFERENCES core.document(document_id),
    created_at   timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_statement_emb
    ON dkp.statement USING hnsw (embedding vector_cosine_ops);

-- ---------------------------------------------------------------------------
-- 6. Резюме обсуждения ключевой ставки (с 02.2024) — разброс мнений СД
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dkp.minutes (
    minutes_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    meeting_id   bigint NOT NULL REFERENCES dkp.meeting(meeting_id),
    published_at timestamptz,
    url          text NOT NULL UNIQUE,
    body         text NOT NULL,
    embedding    vector(256),
    document_id  bigint REFERENCES core.document(document_id),
    created_at   timestamptz NOT NULL DEFAULT now()
);
COMMENT ON TABLE dkp.minutes IS
  'Резюме обсуждения: аргументы сторон без атрибуции; аналитический материал для direction в dkp.argument (block=board_view).';

-- ---------------------------------------------------------------------------
-- 7. Среднесрочный прогноз Банка России (к опорным заседаниям, 4 раза в год)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dkp.forecast (
    forecast_id  bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    meeting_id   bigint NOT NULL REFERENCES dkp.meeting(meeting_id),
    scenario     text NOT NULL DEFAULT 'base',     -- 'base' | 'proinfl' | 'disinfl'
    series_code  text NOT NULL,                    -- словарь ниже
    horizon_year smallint NOT NULL,                -- 2026..2029
    value_low    numeric,
    value_high   numeric,
    value_point  numeric,                          -- точка, если диапазона нет
    unit_code    text NOT NULL,                    -- 'pct_yoy' | 'pct_avg' | 'pp' | 'usd_bn' | 'usd_barrel'
    run_id       integer REFERENCES v2.load_run(run_id),   -- происхождение загрузки
    UNIQUE (meeting_id, scenario, series_code, horizon_year)
);
CREATE INDEX IF NOT EXISTS ix_forecast_series ON dkp.forecast (series_code, horizon_year);
COMMENT ON TABLE dkp.forecast IS
  'series_code (v1): inflation_dec, inflation_avg, key_rate_avg, gdp_yoy, gdp_q4q4,
   cons_total, cons_hh, gross_saving, gross_capital, export_goods, import_goods,
   m2n, claims_total, claims_firms, claims_hh, claims_mortgage,
   ca_balance, trade_balance, export_bp, import_bp, services_balance, income_balance,
   oil_price_tax. Расширяется по фактическим таблицам ЦБ. Диапазон «6,0–7,0» -> low/high;
   точка «4,0» -> value_point.';

-- ---------------------------------------------------------------------------
-- 8. Фактическая реализация прогнозных рядов (ревизионно-осведомлённая)
--    Даёт ошибку прогноза ex post; совместима с v2 (source, run_id).
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dkp.forecast_realized (
    realized_id  bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    series_code  text NOT NULL,
    period_year  smallint NOT NULL,
    value_point  numeric NOT NULL,
    unit_code    text NOT NULL,
    as_of        date NOT NULL,        -- дата среза факта (для ревизий Росстата/ЦБ)
    source_id    bigint REFERENCES v2.source(source_id),
    run_id       integer REFERENCES v2.load_run(run_id),
    UNIQUE (series_code, period_year, as_of)
);
COMMENT ON TABLE dkp.forecast_realized IS
  'Факт по годам того же словаря series_code. Ревизии Росстата/ЦБ хранятся всеми срезами as_of (сравнение v2.series_revision).';

-- ---------------------------------------------------------------------------
-- Вьюхи анализа
-- ---------------------------------------------------------------------------

-- Полная хронология решений с режимами
CREATE OR REPLACE VIEW dkp.v_decisions AS
SELECT d.decision_id, m.meeting_date, m.decision_kind, m.is_pillar,
       d.rate_prev, d.rate_new, d.delta_bp, d.action, d.headline_ru
FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id);

-- Ошибка прогноза: диапазон/точка vs факт (база для RMSFE, как в NBP №87)
CREATE OR REPLACE VIEW dkp.v_forecast_error AS
SELECT f.meeting_id, m.meeting_date, f.scenario, f.series_code, f.horizon_year,
       f.value_low, f.value_high, f.value_point AS forecast_point,
       r.value_point AS actual, r.as_of,
       (r.value_point - f.value_point) AS err_point,
       CASE WHEN f.value_low IS NOT NULL
            THEN (r.value_point BETWEEN f.value_low AND f.value_high)
            ELSE NULL END AS hit_range
FROM dkp.forecast f
JOIN dkp.meeting m USING (meeting_id)
JOIN dkp.forecast_realized r
  ON r.series_code = f.series_code AND r.period_year = f.horizon_year
 AND r.as_of = (SELECT max(r2.as_of) FROM dkp.forecast_realized r2
                WHERE r2.series_code = f.series_code AND r2.period_year = f.horizon_year);

-- Эволюция аргументации: частоты блоков и тональности по решениям
CREATE OR REPLACE VIEW dkp.v_argument_blocks AS
SELECT a.decision_id, m.meeting_date, a.block, a.direction,
       count(*) AS n_arguments
FROM dkp.argument a
JOIN dkp.decision d USING (decision_id)
JOIN dkp.meeting m USING (meeting_id)
GROUP BY a.decision_id, m.meeting_date, a.block, a.direction;

-- Контекст очередного решения: последняя решётка ставок + последний прогноз
-- + аргументы последних раундов (SQL-шаблон для агента, см. queries-заметку)
CREATE OR REPLACE VIEW dkp.v_decision_context AS
WITH last_meeting AS (
    SELECT max(meeting_date) AS d FROM dkp.meeting
),
last_forecast AS (
    SELECT f.* FROM dkp.forecast f
    JOIN dkp.meeting m USING (meeting_id)
    WHERE m.is_pillar
      AND m.meeting_date = (SELECT max(meeting_date) FROM dkp.meeting WHERE is_pillar)
)
SELECT l.rate_code, l.value, l.effective_from,
       lf.series_code, lf.horizon_year, lf.value_low, lf.value_high, lf.value_point
FROM dkp.rate_level l CROSS JOIN last_meeting, last_forecast lf
WHERE l.effective_to IS NULL;