-- ============================================================================
-- graph_ddl.sql — графовый слой знаний в research_wiki (PG-нативный, RCTE)
-- Дизайн: ~/macroeconomist/queries/kg-graph-layer-design.md, dkp-communication-stack-design.md §4
-- Дата: 2026-09-25. Плоские таблицы + рекурсивные CTE; без AGE/Neo4j.
-- Каждая грань обязана иметь provenance (файл/строка, DOI, FK).
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS graph;

-- -------------------------------------------------------------------- node --
CREATE TABLE IF NOT EXISTS graph.node (
    node_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    node_type text NOT NULL,
              -- paper | concept | query_note | metric | hypothesis
              -- cbr_meeting | cbr_decision | cbr_statement | cbr_minutes
              -- cbr_forecast_series | cbr_argument | author | source
    ref_key   text NOT NULL,   -- естественный ключ: paper_code, meeting_id, series_code...
    title     text NOT NULL,
    props     jsonb NOT NULL DEFAULT '{}'::jsonb,
    created_at timestamptz NOT NULL DEFAULT now(),
    UNIQUE (node_type, ref_key)
);
CREATE INDEX IF NOT EXISTS ix_node_type ON graph.node (node_type);
CREATE INDEX IF NOT EXISTS ix_node_ref  ON graph.node (ref_key);

-- -------------------------------------------------------------------- edge --
CREATE TABLE IF NOT EXISTS graph.edge (
    edge_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    src_id    bigint NOT NULL REFERENCES graph.node(node_id) ON DELETE CASCADE,
    dst_id    bigint NOT NULL REFERENCES graph.node(node_id) ON DELETE CASCADE,
    edge_type text NOT NULL,
              -- cites | wikilinks | belongs_to | extends | uses_metric
              -- supports_hypothesis | same_topic
              -- dkp: has_decision | has_statement | has_minutes
              --      has_forecast | follows | with_signal | in_mode
              --      has_argument | validates
    weight    real NOT NULL DEFAULT 1.0,
    provenance jsonb NOT NULL DEFAULT '{}'::jsonb,  -- {file,line|doi|fk|url}
    created_at timestamptz NOT NULL DEFAULT now(),
    UNIQUE (src_id, dst_id, edge_type)
);
CREATE INDEX IF NOT EXISTS ix_edge_src ON graph.edge (src_id);
CREATE INDEX IF NOT EXISTS ix_edge_dst ON graph.edge (dst_id);
CREATE INDEX IF NOT EXISTS ix_edge_dst_type ON graph.edge (dst_id, edge_type);
CREATE INDEX IF NOT EXISTS ix_edge_type ON graph.edge (edge_type);

-- ------------------------------------------------------------- ingest_log --
CREATE TABLE IF NOT EXISTS graph.ingest_log (
    run_id      bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    started_at  timestamptz NOT NULL,
    finished_at timestamptz,
    pipeline_v  text NOT NULL,
    n_nodes     integer,
    n_edges     integer,
    notes       text
);

COMMENT ON SCHEMA graph IS
  'Графовый слой знаний: узлы (работы/концепты/метрики/решения ДКП) и типизированные рёбра с provenance. Обходы — рекурсивные CTE 1-2 хопа; PageRank/кластеры — офлайн NetworkX с записью back. См. kg-graph-layer-design.md.';