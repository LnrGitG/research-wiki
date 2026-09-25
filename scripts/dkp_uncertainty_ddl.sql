-- =====================================================================
-- dkp.uncertainty_item — мнение регулятора о неопределённости
-- Дизайн: queries/dkp-uncertainty-layer-design.md (002f78b, вариант B)
-- Универсальные рёбра: has_uncertainty, resolved_by, conditions,
-- outweighs + переиспользование uses_metric (item → v2.metric).
-- =====================================================================

CREATE TABLE IF NOT EXISTS dkp.uncertainty_item (
    item_id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    meeting_id   bigint NOT NULL REFERENCES dkp.meeting(meeting_id),
    statement_id bigint REFERENCES dkp.statement(statement_id),  -- provenance-FK
    minutes_id   bigint REFERENCES dkp.minutes(minutes_id),      -- если из Резюме
    kind         text NOT NULL CHECK (kind IN
                 ('risk_balance', 'open_question', 'conditionality', 'calibration')),
    variable     text NOT NULL,          -- fuel, power_capacity, budget, demand,
                                         -- credit, labour, fx, external,
                                         -- inflation_expect, transmission, other
    direction    text NOT NULL DEFAULT 'two_sided' CHECK (direction IN
                 ('proinflation', 'disinflation', 'two_sided')),
    horizon      text DEFAULT 'medium' CHECK (horizon IN
                 ('short', 'medium', 'long')),
    premise      text,                   -- для conditionality: условие
    consequence  text,                   -- для conditionality: следствие
    text_raw     text NOT NULL,          -- цитата из документа
    text_short   text,                   -- сжатая формулировка ≤140
    source_span  text,                   -- 'пресс-релиз §риски', 'Резюме §3'
    confidence_note text,                -- «потребуется больше данных» и т.п.
    status       text NOT NULL DEFAULT 'open' CHECK (status IN
                 ('open', 'updated', 'resolved')),
    resolved_by  bigint REFERENCES dkp.uncertainty_item(item_id),
    resolution_note text,
    embedding    vector(256),            -- Yandex text-search-doc, как у argument
    classifier_version text NOT NULL,    -- 'llm:gpt-oss-120b:uncertainty_v1' | 'manual_v1'
    created_at   timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS ix_unc_item_meeting ON dkp.uncertainty_item (meeting_id, kind);
CREATE INDEX IF NOT EXISTS ix_unc_item_variable ON dkp.uncertainty_item (variable, status);
CREATE INDEX IF NOT EXISTS ix_unc_item_emb
    ON dkp.uncertainty_item USING hnsw (embedding vector_cosine_ops);

COMMENT ON TABLE dkp.uncertainty_item IS
  'Мнение регулятора о неопределённости (IMF WP/26/133): risk_balance — баланс
   про/дезинфляционных рисков; open_question — открытый вопрос; conditionality —
   развилка «условие => следствие»; calibration — ordinal-оценка степени.
   Жизненный цикл: open → updated → resolved (resolved_by на item следующего
   заседания). Предметная таксономия в variable и узлах concept:<имя>, не в рёбрах.';

-- Уникальность цитаты внутри заседания (защита от дублей перепрогонов)
CREATE UNIQUE INDEX IF NOT EXISTS ix_unc_item_dedup
    ON dkp.uncertainty_item (meeting_id, md5(text_raw));