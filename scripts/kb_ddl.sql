-- ============================================================================
-- kb_ddl.sql — единый векторный KB-слой в research_wiki (pgvector 0.6.0)
-- Дизайн: ~/macroeconomist/queries/kb-vector-layer-design.md
-- Применение: транзакционно (см. _kb_apply_ddl.py). Дата: 2026-09-24
-- Модель эмбеддингов: Yandex text-search-doc, 256-dim (text-search-query для запросов)
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS kb;

-- ---------------------------------------------------------------- document --
CREATE TABLE IF NOT EXISTS kb.document (
    doc_id       bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    doc_type     text NOT NULL,              -- wiki_paper | wiki_concept | wiki_query | wiki_other |
                                              -- repo_note | cbr_raw | dkp_text | metric_card
    title        text NOT NULL,
    lang         text NOT NULL DEFAULT 'ru', -- 'ru' | 'en'
    published_at date,                       -- если известна
    ingested_at  timestamptz NOT NULL DEFAULT now(),
    url_or_path  text NOT NULL,              -- абсолютный/репозиторный путь или URL
    origin_repo  text NOT NULL,              -- research-wiki | macroeconomist | research-wiki-private
    sha256       char(64) NOT NULL,          -- дедупликация контента
    n_chunks     integer NOT NULL DEFAULT 0,
    meta         jsonb NOT NULL DEFAULT '{}'::jsonb,  -- год, темы, paper_code...
    created_at   timestamptz NOT NULL DEFAULT now(),
    UNIQUE (origin_repo, url_or_path)
);
CREATE INDEX IF NOT EXISTS ix_document_type ON kb.document (doc_type);
CREATE INDEX IF NOT EXISTS ix_document_sha ON kb.document (sha256);

-- ------------------------------------------------------------------- chunk --
CREATE TABLE IF NOT EXISTS kb.chunk (
    chunk_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    doc_id     bigint NOT NULL REFERENCES kb.document(doc_id) ON DELETE CASCADE,
    seq_no     integer NOT NULL,            -- позиция в документе
    kind       text NOT NULL DEFAULT 'paragraph',
               -- paragraph | finding | method | headline | full
    text       text NOT NULL,
    tsv        tsvector,                    -- гибридный поиск (russian)
    embedding  vector(256),                 -- Yandex text-search-doc
    meta       jsonb NOT NULL DEFAULT '{}'::jsonb,
    created_at timestamptz NOT NULL DEFAULT now(),
    UNIQUE (doc_id, seq_no)
);
-- лексический поиск: russian-морфология + вес по полю (пока единый)
CREATE INDEX IF NOT EXISTS ix_chunk_tsv ON kb.chunk USING gin (tsv);
-- триграммы: опечатки и подстроки (коды, ИНН, метрики)
CREATE INDEX IF NOT EXISTS ix_chunk_trgm ON kb.chunk USING gin (text gin_trgm_ops);

-- Объём корпуса ~34 тыс. чанков. ВАЖНО (замер 04.10.2026): поиск фактически
-- идёт ПО ЭТОМУ HNSW-индексу, а не точным сканом, как предполагалось при
-- создании схемы, — планировщик выбирает Index Scan using ix_chunk_emb.
-- Следствие: условие по doc_type применяется ПОСЛЕ индекса (hnsw.ef_search=40),
-- и для мелких типов (metric_card 127 чанков, dkp_text 664, wiki_query 2039)
-- векторный канал возвращал 0 строк из 40. Поэтому в kb_search.py пул
-- кандидатов материализуется (WITH pool AS MATERIALIZED) до сортировки по
-- расстоянию — без этого фильтр по типу глушит поиск. Подъём ef_search до 400
-- проблему НЕ решает (проверено).
CREATE INDEX IF NOT EXISTS ix_chunk_emb ON kb.chunk USING hnsw (embedding vector_cosine_ops);

-- -------------------------------------------------------------- ingest_log --
CREATE TABLE IF NOT EXISTS kb.ingest_log (
    run_id        bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    started_at    timestamptz NOT NULL,
    finished_at   timestamptz,
    pipeline_v    text NOT NULL,             -- 'kb_loader_v1'
    embed_model   text NOT NULL,             -- 'yandex:text-search-doc:latest'
    n_docs        integer,
    n_chunks      integer,
    n_embedded    integer,
    n_skipped     integer,                   -- дедуп по sha256
    notes         text
);

-- --------------------------------------------------------------- вьюхи ------
CREATE OR REPLACE VIEW kb.v_document_stats AS
SELECT d.doc_type, count(*) AS docs, sum(d.n_chunks) AS chunks,
       max(d.ingested_at) AS last_ingested
FROM kb.document d
GROUP BY d.doc_type
ORDER BY 1;

COMMENT ON SCHEMA kb IS
  'Единый векторный KB-слой: все знания (wiki, репо, тексты ЦБ, метрики) для нативного обогащения контекста агента. Модель: Yandex text-search-doc 256-dim; поиск: точный скан (0.6) + tsvector(russian) + pg_trgm, слияние RRF в kb_search.py.';