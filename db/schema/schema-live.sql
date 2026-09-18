--
-- PostgreSQL database dump
--

\restrict x4etc7kN8FPrY9ZzbV6eEKv1IM0I6GR2kVIez6MkK0webcnG96hZPdp6hb0Tw8r

-- Dumped from database version 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: core; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA core;


--
-- Name: derived; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA derived;


--
-- Name: marts; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA marts;


--
-- Name: meta; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA meta;


--
-- Name: pipeline; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA pipeline;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: document; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.document (
    document_id bigint NOT NULL,
    doc_code text NOT NULL,
    title_ru text NOT NULL,
    doc_type text NOT NULL,
    file_id bigint,
    url text,
    sha256 text,
    published_at date,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT document_doc_type_check CHECK ((doc_type = ANY (ARRAY['wiki_page'::text, 'paper'::text, 'report'::text, 'methodology'::text, 'news'::text, 'other'::text])))
);


--
-- Name: document_document_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.document ALTER COLUMN document_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.document_document_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: file_registry; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.file_registry (
    file_id bigint NOT NULL,
    source_id bigint,
    release_id bigint,
    uri text NOT NULL,
    file_name text NOT NULL,
    mime_type text,
    sha256 text NOT NULL,
    size_bytes bigint NOT NULL,
    downloaded_at timestamp with time zone DEFAULT now() NOT NULL,
    status text DEFAULT 'registered'::text NOT NULL,
    CONSTRAINT file_registry_size_bytes_check CHECK ((size_bytes >= 0)),
    CONSTRAINT file_registry_status_check CHECK ((status = ANY (ARRAY['registered'::text, 'processing'::text, 'processed'::text, 'failed'::text, 'archived'::text])))
);


--
-- Name: file_registry_file_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.file_registry ALTER COLUMN file_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.file_registry_file_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: frequency; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.frequency (
    frequency_id bigint NOT NULL,
    frequency_code text NOT NULL,
    name_ru text NOT NULL,
    period_type text NOT NULL,
    months_per_period integer,
    CONSTRAINT frequency_months_per_period_check CHECK (((months_per_period >= 1) AND (months_per_period <= 12))),
    CONSTRAINT frequency_period_type_check CHECK ((period_type = ANY (ARRAY['date'::text, 'month'::text, 'quarter'::text, 'year'::text, 'cumulative'::text])))
);


--
-- Name: frequency_frequency_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.frequency ALTER COLUMN frequency_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.frequency_frequency_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: hypothesis; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.hypothesis (
    hypothesis_id bigint NOT NULL,
    hyp_code text NOT NULL,
    kind text,
    title_ru text NOT NULL,
    statement text,
    status text DEFAULT 'open'::text NOT NULL,
    evidence_for text[],
    evidence_against text[],
    tags text[] DEFAULT '{}'::text[] NOT NULL,
    next_check date,
    methodology_ref text,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT hypothesis_status_check CHECK ((status = ANY (ARRAY['open'::text, 'testing'::text, 'supported'::text, 'refuted'::text, 'archived'::text])))
);


--
-- Name: hypothesis_hypothesis_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.hypothesis ALTER COLUMN hypothesis_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.hypothesis_hypothesis_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: metric; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.metric (
    metric_id bigint NOT NULL,
    metric_code text NOT NULL,
    name_ru text NOT NULL,
    short_name_ru text,
    description text,
    unit_id bigint NOT NULL,
    frequency_id bigint NOT NULL,
    metric_type text DEFAULT 'primary'::text NOT NULL,
    index_base text,
    is_derived boolean DEFAULT false NOT NULL,
    formula_text text,
    status text DEFAULT 'active'::text NOT NULL,
    tags text[] DEFAULT '{}'::text[] NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT metric_check CHECK ((NOT ((metric_type = 'primary'::text) AND (index_base IS NULL) AND (tags && '{index}'::text[])))),
    CONSTRAINT metric_metric_type_check CHECK ((metric_type = ANY (ARRAY['primary'::text, 'derived'::text, 'nowcast_model'::text]))),
    CONSTRAINT metric_status_check CHECK ((status = ANY (ARRAY['active'::text, 'deprecated'::text, 'merged'::text])))
);


--
-- Name: metric_metric_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.metric ALTER COLUMN metric_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.metric_metric_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: note; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.note (
    note_id bigint NOT NULL,
    metric_id bigint,
    region_id bigint,
    source_id bigint,
    file_id bigint,
    document_id bigint,
    hypothesis_id bigint,
    obs_id bigint,
    body text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


--
-- Name: note_note_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.note ALTER COLUMN note_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.note_note_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: observation_v2; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.observation_v2 (
    obs_id bigint NOT NULL,
    metric_id bigint NOT NULL,
    region_id bigint NOT NULL,
    frequency_id bigint NOT NULL,
    period_start date NOT NULL,
    period_end date NOT NULL,
    value numeric,
    value_str text,
    assessment_type text DEFAULT 'final'::text NOT NULL,
    observation_status text DEFAULT 'loaded'::text NOT NULL,
    source_id bigint NOT NULL,
    release_id bigint NOT NULL,
    quality_flags text[] DEFAULT '{}'::text[] NOT NULL,
    sub_dimension text DEFAULT ''::text NOT NULL,
    notes text,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT observation_assessment_type_check CHECK ((assessment_type = ANY (ARRAY['flash'::text, 'preliminary'::text, 'revised'::text, 'final'::text, 'nowcast'::text, 'forecast'::text, 'estimated'::text]))),
    CONSTRAINT observation_check CHECK ((period_end >= period_start)),
    CONSTRAINT observation_observation_status_check CHECK ((observation_status = ANY (ARRAY['raw'::text, 'validated'::text, 'rejected'::text, 'superseded'::text])))
);


--
-- Name: observation_v2_old; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.observation_v2_old (
    obs_id bigint NOT NULL,
    metric_id bigint NOT NULL,
    region_id bigint NOT NULL,
    frequency_id bigint NOT NULL,
    period_start date NOT NULL,
    period_end date NOT NULL,
    value numeric,
    value_str text,
    assessment_type text DEFAULT 'final'::text NOT NULL,
    observation_status text DEFAULT 'loaded'::text NOT NULL,
    source_id bigint NOT NULL,
    release_id bigint NOT NULL,
    quality_flags text[] DEFAULT '{}'::text[] NOT NULL,
    sub_dimension text DEFAULT ''::text NOT NULL,
    notes text,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT observation_assessment_type_check CHECK ((assessment_type = ANY (ARRAY['flash'::text, 'preliminary'::text, 'revised'::text, 'final'::text, 'nowcast'::text, 'forecast'::text, 'estimated'::text]))),
    CONSTRAINT observation_check CHECK ((period_end >= period_start)),
    CONSTRAINT observation_observation_status_check CHECK ((observation_status = ANY (ARRAY['raw'::text, 'validated'::text, 'rejected'::text, 'superseded'::text])))
);


--
-- Name: observation_v2_obs_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.observation_v2_old ALTER COLUMN obs_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.observation_v2_obs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: observation_v3_obs_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.observation_v2 ALTER COLUMN obs_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.observation_v3_obs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: person; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.person (
    person_id bigint NOT NULL,
    full_name text NOT NULL,
    organization text,
    role text,
    source_url text,
    notes text,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


--
-- Name: person_person_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.person ALTER COLUMN person_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.person_person_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: region; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.region (
    region_id bigint NOT NULL,
    region_code text NOT NULL,
    name_ru text NOT NULL,
    short_name text,
    level text NOT NULL,
    parent_id bigint,
    is_active boolean DEFAULT true NOT NULL,
    valid_from date,
    valid_to date,
    oktmo text,
    okato text,
    iso_code text,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    aggregation text DEFAULT 'base'::text,
    aggregate_of text DEFAULT ''::text,
    CONSTRAINT region_check CHECK (((level <> 'country'::text) OR (parent_id IS NULL))),
    CONSTRAINT region_level_check CHECK ((level = ANY (ARRAY['country'::text, 'federal_district'::text, 'region'::text, 'foreign_country'::text, 'foreign_region'::text, 'aggregate'::text, 'city'::text])))
);


--
-- Name: region_region_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.region ALTER COLUMN region_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.region_region_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: release; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.release (
    release_id bigint NOT NULL,
    source_id bigint NOT NULL,
    release_label text,
    published_at timestamp with time zone,
    ingested_at timestamp with time zone DEFAULT now() NOT NULL,
    url text,
    content_hash text,
    status text DEFAULT 'loaded'::text NOT NULL,
    notes text,
    CONSTRAINT release_status_check CHECK ((status = ANY (ARRAY['registered'::text, 'parsed'::text, 'validated'::text, 'loaded'::text, 'failed'::text, 'superseded'::text])))
);


--
-- Name: release_release_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.release ALTER COLUMN release_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.release_release_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: source; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.source (
    source_id bigint NOT NULL,
    source_code text NOT NULL,
    name_ru text NOT NULL,
    publisher text,
    url text,
    license text,
    reliability text,
    is_active boolean DEFAULT true NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT source_reliability_check CHECK ((reliability = ANY (ARRAY['official'::text, 'primary'::text, 'secondary'::text, 'derived'::text, 'unknown'::text])))
);


--
-- Name: source_source_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.source ALTER COLUMN source_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.source_source_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: unit; Type: TABLE; Schema: core; Owner: -
--

CREATE TABLE core.unit (
    unit_id bigint NOT NULL,
    unit_code text NOT NULL,
    name_ru text NOT NULL,
    description text,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


--
-- Name: unit_unit_id_seq; Type: SEQUENCE; Schema: core; Owner: -
--

ALTER TABLE core.unit ALTER COLUMN unit_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME core.unit_unit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: v_datalens_observations; Type: VIEW; Schema: core; Owner: -
--

CREATE VIEW core.v_datalens_observations AS
 SELECT o.obs_id,
    o.period_start,
    o.period_end,
    (EXTRACT(year FROM o.period_start))::integer AS year,
    (EXTRACT(month FROM o.period_start))::integer AS month,
    (EXTRACT(quarter FROM o.period_start))::integer AS quarter,
    f.frequency_code,
    f.name_ru AS frequency_name,
    m.metric_code,
    m.name_ru AS metric_name,
    m.short_name_ru AS metric_short_name,
    m.metric_type,
    m.is_derived,
    m.tags AS metric_tags,
    u.unit_code,
    u.name_ru AS unit_name,
    r.region_code,
    r.name_ru AS region_name,
    r.level AS region_level,
    r.oktmo,
    o.value,
    o.value_str,
    o.sub_dimension,
    o.assessment_type,
    o.observation_status,
    o.quality_flags,
    s.source_code,
    s.name_ru AS source_name,
    rl.release_label,
    rl.published_at
   FROM ((((((core.observation_v2 o
     LEFT JOIN core.metric m ON ((m.metric_id = o.metric_id)))
     LEFT JOIN core.region r ON ((r.region_id = o.region_id)))
     LEFT JOIN core.frequency f ON ((f.frequency_id = o.frequency_id)))
     LEFT JOIN core.unit u ON ((u.unit_id = m.unit_id)))
     LEFT JOIN core.source s ON ((s.source_id = o.source_id)))
     LEFT JOIN core.release rl ON ((rl.release_id = o.release_id)));


--
-- Name: derived_metric; Type: TABLE; Schema: derived; Owner: -
--

CREATE TABLE derived.derived_metric (
    dm_id bigint NOT NULL,
    output_metric_id bigint NOT NULL,
    input_metric_ids bigint[] NOT NULL,
    transform_type text NOT NULL,
    formula_text text NOT NULL,
    params jsonb DEFAULT '{}'::jsonb NOT NULL,
    code_version text NOT NULL,
    code_path text,
    computed_at timestamp with time zone DEFAULT now() NOT NULL,
    output_release_id bigint,
    notes text,
    CONSTRAINT derived_metric_transform_type_check CHECK ((transform_type = ANY (ARRAY['mom'::text, 'yoy'::text, 'ytd'::text, 'sa'::text, 'x13_arima'::text, 'link_relative'::text, 'aggregate_sum'::text, 'aggregate_avg'::text, 'custom'::text])))
);


--
-- Name: derived_metric_dm_id_seq; Type: SEQUENCE; Schema: derived; Owner: -
--

ALTER TABLE derived.derived_metric ALTER COLUMN dm_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME derived.derived_metric_dm_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: classifier; Type: TABLE; Schema: meta; Owner: -
--

CREATE TABLE meta.classifier (
    classifier_id bigint NOT NULL,
    cls_code text NOT NULL,
    edition text NOT NULL,
    name_ru text NOT NULL,
    valid_from date,
    valid_to date,
    source_url text
);


--
-- Name: classifier_classifier_id_seq; Type: SEQUENCE; Schema: meta; Owner: -
--

ALTER TABLE meta.classifier ALTER COLUMN classifier_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME meta.classifier_classifier_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: metric_classifier_mapping; Type: TABLE; Schema: meta; Owner: -
--

CREATE TABLE meta.metric_classifier_mapping (
    id bigint NOT NULL,
    metric_id bigint NOT NULL,
    classifier_id bigint NOT NULL,
    classifier_entry_code text NOT NULL,
    valid_from date,
    valid_to date,
    notes text
);


--
-- Name: metric_classifier_mapping_id_seq; Type: SEQUENCE; Schema: meta; Owner: -
--

ALTER TABLE meta.metric_classifier_mapping ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME meta.metric_classifier_mapping_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: region_alias; Type: TABLE; Schema: meta; Owner: -
--

CREATE TABLE meta.region_alias (
    alias text NOT NULL,
    region_id bigint NOT NULL,
    source_id bigint NOT NULL,
    confidence text DEFAULT 'manual'::text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT region_alias_confidence_check CHECK ((confidence = ANY (ARRAY['exact'::text, 'manual'::text, 'inferred'::text, 'needs_review'::text])))
);


--
-- Name: series_comparability; Type: TABLE; Schema: meta; Owner: -
--

CREATE TABLE meta.series_comparability (
    sc_id bigint NOT NULL,
    metric_id bigint NOT NULL,
    region_id bigint,
    break_date date NOT NULL,
    break_type text NOT NULL,
    description text NOT NULL,
    pre_break_base text,
    post_break_base text,
    conversion_rule text,
    source_id bigint,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT series_comparability_break_type_check CHECK ((break_type = ANY (ARRAY['classifier_change'::text, 'index_base_change'::text, 'methodology_change'::text, 'boundary_change'::text, 'unit_change'::text])))
);


--
-- Name: series_comparability_sc_id_seq; Type: SEQUENCE; Schema: meta; Owner: -
--

ALTER TABLE meta.series_comparability ALTER COLUMN sc_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME meta.series_comparability_sc_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: source_metric_mapping; Type: TABLE; Schema: meta; Owner: -
--

CREATE TABLE meta.source_metric_mapping (
    mapping_id bigint NOT NULL,
    source_id bigint NOT NULL,
    raw_metric text NOT NULL,
    raw_region text,
    metric_id bigint NOT NULL,
    region_id bigint,
    unit_convert_rule text,
    frequency_convert_rule text,
    confidence text DEFAULT 'needs_review'::text NOT NULL,
    review_status text DEFAULT 'pending'::text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT source_metric_mapping_confidence_check CHECK ((confidence = ANY (ARRAY['exact'::text, 'manual'::text, 'inferred'::text, 'needs_review'::text]))),
    CONSTRAINT source_metric_mapping_review_status_check CHECK ((review_status = ANY (ARRAY['pending'::text, 'approved'::text, 'rejected'::text])))
);


--
-- Name: source_metric_mapping_mapping_id_seq; Type: SEQUENCE; Schema: meta; Owner: -
--

ALTER TABLE meta.source_metric_mapping ALTER COLUMN mapping_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME meta.source_metric_mapping_mapping_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: pipeline_log; Type: TABLE; Schema: pipeline; Owner: -
--

CREATE TABLE pipeline.pipeline_log (
    log_id bigint NOT NULL,
    release_id bigint,
    stage smallint NOT NULL,
    status text NOT NULL,
    started_at timestamp with time zone DEFAULT now() NOT NULL,
    finished_at timestamp with time zone,
    rows_affected bigint,
    error_text text,
    CONSTRAINT pipeline_log_stage_check CHECK (((stage >= 1) AND (stage <= 9))),
    CONSTRAINT pipeline_log_status_check CHECK ((status = ANY (ARRAY['ok'::text, 'failed'::text, 'skipped'::text])))
);


--
-- Name: pipeline_log_log_id_seq; Type: SEQUENCE; Schema: pipeline; Owner: -
--

ALTER TABLE pipeline.pipeline_log ALTER COLUMN log_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME pipeline.pipeline_log_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: document document_doc_code_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.document
    ADD CONSTRAINT document_doc_code_key UNIQUE (doc_code);


--
-- Name: document document_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.document
    ADD CONSTRAINT document_pkey PRIMARY KEY (document_id);


--
-- Name: file_registry file_registry_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.file_registry
    ADD CONSTRAINT file_registry_pkey PRIMARY KEY (file_id);


--
-- Name: file_registry file_registry_uri_sha256_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.file_registry
    ADD CONSTRAINT file_registry_uri_sha256_key UNIQUE (uri, sha256);


--
-- Name: frequency frequency_frequency_code_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.frequency
    ADD CONSTRAINT frequency_frequency_code_key UNIQUE (frequency_code);


--
-- Name: frequency frequency_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.frequency
    ADD CONSTRAINT frequency_pkey PRIMARY KEY (frequency_id);


--
-- Name: hypothesis hypothesis_hyp_code_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.hypothesis
    ADD CONSTRAINT hypothesis_hyp_code_key UNIQUE (hyp_code);


--
-- Name: hypothesis hypothesis_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.hypothesis
    ADD CONSTRAINT hypothesis_pkey PRIMARY KEY (hypothesis_id);


--
-- Name: metric metric_metric_code_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.metric
    ADD CONSTRAINT metric_metric_code_key UNIQUE (metric_code);


--
-- Name: metric metric_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.metric
    ADD CONSTRAINT metric_pkey PRIMARY KEY (metric_id);


--
-- Name: note note_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.note
    ADD CONSTRAINT note_pkey PRIMARY KEY (note_id);


--
-- Name: observation_v2_old observation_v2_metric_id_region_id_frequency_id_period_star_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.observation_v2_old
    ADD CONSTRAINT observation_v2_metric_id_region_id_frequency_id_period_star_key UNIQUE (metric_id, region_id, frequency_id, period_start, source_id, release_id, assessment_type, sub_dimension);


--
-- Name: observation_v2_old observation_v2_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.observation_v2_old
    ADD CONSTRAINT observation_v2_pkey PRIMARY KEY (obs_id);


--
-- Name: observation_v2 observation_v3_metric_id_region_id_frequency_id_period_star_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.observation_v2
    ADD CONSTRAINT observation_v3_metric_id_region_id_frequency_id_period_star_key UNIQUE (metric_id, region_id, frequency_id, period_start, source_id, release_id, assessment_type, sub_dimension);


--
-- Name: observation_v2 observation_v3_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.observation_v2
    ADD CONSTRAINT observation_v3_pkey PRIMARY KEY (obs_id);


--
-- Name: person person_full_name_organization_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.person
    ADD CONSTRAINT person_full_name_organization_key UNIQUE (full_name, organization);


--
-- Name: person person_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (person_id);


--
-- Name: region region_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.region
    ADD CONSTRAINT region_pkey PRIMARY KEY (region_id);


--
-- Name: region region_region_code_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.region
    ADD CONSTRAINT region_region_code_key UNIQUE (region_code);


--
-- Name: release release_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.release
    ADD CONSTRAINT release_pkey PRIMARY KEY (release_id);


--
-- Name: release release_source_id_release_label_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.release
    ADD CONSTRAINT release_source_id_release_label_key UNIQUE (source_id, release_label);


--
-- Name: source source_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.source
    ADD CONSTRAINT source_pkey PRIMARY KEY (source_id);


--
-- Name: source source_source_code_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.source
    ADD CONSTRAINT source_source_code_key UNIQUE (source_code);


--
-- Name: unit unit_pkey; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.unit
    ADD CONSTRAINT unit_pkey PRIMARY KEY (unit_id);


--
-- Name: unit unit_unit_code_key; Type: CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.unit
    ADD CONSTRAINT unit_unit_code_key UNIQUE (unit_code);


--
-- Name: derived_metric derived_metric_pkey; Type: CONSTRAINT; Schema: derived; Owner: -
--

ALTER TABLE ONLY derived.derived_metric
    ADD CONSTRAINT derived_metric_pkey PRIMARY KEY (dm_id);


--
-- Name: classifier classifier_cls_code_edition_key; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.classifier
    ADD CONSTRAINT classifier_cls_code_edition_key UNIQUE (cls_code, edition);


--
-- Name: classifier classifier_pkey; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.classifier
    ADD CONSTRAINT classifier_pkey PRIMARY KEY (classifier_id);


--
-- Name: metric_classifier_mapping metric_classifier_mapping_metric_id_classifier_id_classifie_key; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.metric_classifier_mapping
    ADD CONSTRAINT metric_classifier_mapping_metric_id_classifier_id_classifie_key UNIQUE (metric_id, classifier_id, classifier_entry_code);


--
-- Name: metric_classifier_mapping metric_classifier_mapping_pkey; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.metric_classifier_mapping
    ADD CONSTRAINT metric_classifier_mapping_pkey PRIMARY KEY (id);


--
-- Name: region_alias region_alias_pkey; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.region_alias
    ADD CONSTRAINT region_alias_pkey PRIMARY KEY (alias, source_id);


--
-- Name: series_comparability series_comparability_metric_id_region_id_break_date_break_t_key; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.series_comparability
    ADD CONSTRAINT series_comparability_metric_id_region_id_break_date_break_t_key UNIQUE (metric_id, region_id, break_date, break_type);


--
-- Name: series_comparability series_comparability_pkey; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.series_comparability
    ADD CONSTRAINT series_comparability_pkey PRIMARY KEY (sc_id);


--
-- Name: source_metric_mapping source_metric_mapping_pkey; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.source_metric_mapping
    ADD CONSTRAINT source_metric_mapping_pkey PRIMARY KEY (mapping_id);


--
-- Name: source_metric_mapping source_metric_mapping_source_id_raw_metric_raw_region_key; Type: CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.source_metric_mapping
    ADD CONSTRAINT source_metric_mapping_source_id_raw_metric_raw_region_key UNIQUE (source_id, raw_metric, raw_region);


--
-- Name: pipeline_log pipeline_log_pkey; Type: CONSTRAINT; Schema: pipeline; Owner: -
--

ALTER TABLE ONLY pipeline.pipeline_log
    ADD CONSTRAINT pipeline_log_pkey PRIMARY KEY (log_id);


--
-- Name: idx_file_release; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX idx_file_release ON core.file_registry USING btree (release_id);


--
-- Name: idx_region_level; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX idx_region_level ON core.region USING btree (level);


--
-- Name: idx_region_name_trgm; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX idx_region_name_trgm ON core.region USING gin (name_ru public.gin_trgm_ops);


--
-- Name: idx_region_parent; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX idx_region_parent ON core.region USING btree (parent_id);


--
-- Name: observation_v2_metric_id_region_id_period_start_assessment__idx; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX observation_v2_metric_id_region_id_period_start_assessment__idx ON core.observation_v2_old USING btree (metric_id, region_id, period_start DESC, assessment_type, release_id DESC);


--
-- Name: observation_v2_quality_flags_idx; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX observation_v2_quality_flags_idx ON core.observation_v2_old USING gin (quality_flags);


--
-- Name: observation_v2_release_id_idx; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX observation_v2_release_id_idx ON core.observation_v2_old USING btree (release_id);


--
-- Name: observation_v3_metric_id_region_id_period_start_assessment__idx; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX observation_v3_metric_id_region_id_period_start_assessment__idx ON core.observation_v2 USING btree (metric_id, region_id, period_start DESC, assessment_type, release_id DESC);


--
-- Name: observation_v3_quality_flags_idx; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX observation_v3_quality_flags_idx ON core.observation_v2 USING gin (quality_flags);


--
-- Name: observation_v3_release_id_idx; Type: INDEX; Schema: core; Owner: -
--

CREATE INDEX observation_v3_release_id_idx ON core.observation_v2 USING btree (release_id);


--
-- Name: idx_dm_output; Type: INDEX; Schema: derived; Owner: -
--

CREATE INDEX idx_dm_output ON derived.derived_metric USING btree (output_metric_id, computed_at DESC);


--
-- Name: idx_smm_raw_metric; Type: INDEX; Schema: meta; Owner: -
--

CREATE INDEX idx_smm_raw_metric ON meta.source_metric_mapping USING gin (raw_metric public.gin_trgm_ops);


--
-- Name: document document_file_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.document
    ADD CONSTRAINT document_file_id_fkey FOREIGN KEY (file_id) REFERENCES core.file_registry(file_id);


--
-- Name: file_registry file_registry_release_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.file_registry
    ADD CONSTRAINT file_registry_release_id_fkey FOREIGN KEY (release_id) REFERENCES core.release(release_id);


--
-- Name: file_registry file_registry_source_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.file_registry
    ADD CONSTRAINT file_registry_source_id_fkey FOREIGN KEY (source_id) REFERENCES core.source(source_id);


--
-- Name: metric metric_frequency_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.metric
    ADD CONSTRAINT metric_frequency_id_fkey FOREIGN KEY (frequency_id) REFERENCES core.frequency(frequency_id);


--
-- Name: metric metric_unit_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.metric
    ADD CONSTRAINT metric_unit_id_fkey FOREIGN KEY (unit_id) REFERENCES core.unit(unit_id);


--
-- Name: note note_document_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.note
    ADD CONSTRAINT note_document_id_fkey FOREIGN KEY (document_id) REFERENCES core.document(document_id);


--
-- Name: note note_file_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.note
    ADD CONSTRAINT note_file_id_fkey FOREIGN KEY (file_id) REFERENCES core.file_registry(file_id);


--
-- Name: note note_hypothesis_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.note
    ADD CONSTRAINT note_hypothesis_id_fkey FOREIGN KEY (hypothesis_id) REFERENCES core.hypothesis(hypothesis_id);


--
-- Name: note note_metric_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.note
    ADD CONSTRAINT note_metric_id_fkey FOREIGN KEY (metric_id) REFERENCES core.metric(metric_id);


--
-- Name: note note_region_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.note
    ADD CONSTRAINT note_region_id_fkey FOREIGN KEY (region_id) REFERENCES core.region(region_id);


--
-- Name: note note_source_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.note
    ADD CONSTRAINT note_source_id_fkey FOREIGN KEY (source_id) REFERENCES core.source(source_id);


--
-- Name: region region_parent_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.region
    ADD CONSTRAINT region_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES core.region(region_id);


--
-- Name: release release_source_id_fkey; Type: FK CONSTRAINT; Schema: core; Owner: -
--

ALTER TABLE ONLY core.release
    ADD CONSTRAINT release_source_id_fkey FOREIGN KEY (source_id) REFERENCES core.source(source_id);


--
-- Name: derived_metric derived_metric_output_metric_id_fkey; Type: FK CONSTRAINT; Schema: derived; Owner: -
--

ALTER TABLE ONLY derived.derived_metric
    ADD CONSTRAINT derived_metric_output_metric_id_fkey FOREIGN KEY (output_metric_id) REFERENCES core.metric(metric_id);


--
-- Name: derived_metric derived_metric_output_release_id_fkey; Type: FK CONSTRAINT; Schema: derived; Owner: -
--

ALTER TABLE ONLY derived.derived_metric
    ADD CONSTRAINT derived_metric_output_release_id_fkey FOREIGN KEY (output_release_id) REFERENCES core.release(release_id);


--
-- Name: metric_classifier_mapping metric_classifier_mapping_classifier_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.metric_classifier_mapping
    ADD CONSTRAINT metric_classifier_mapping_classifier_id_fkey FOREIGN KEY (classifier_id) REFERENCES meta.classifier(classifier_id);


--
-- Name: metric_classifier_mapping metric_classifier_mapping_metric_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.metric_classifier_mapping
    ADD CONSTRAINT metric_classifier_mapping_metric_id_fkey FOREIGN KEY (metric_id) REFERENCES core.metric(metric_id);


--
-- Name: region_alias region_alias_region_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.region_alias
    ADD CONSTRAINT region_alias_region_id_fkey FOREIGN KEY (region_id) REFERENCES core.region(region_id);


--
-- Name: region_alias region_alias_source_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.region_alias
    ADD CONSTRAINT region_alias_source_id_fkey FOREIGN KEY (source_id) REFERENCES core.source(source_id);


--
-- Name: series_comparability series_comparability_metric_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.series_comparability
    ADD CONSTRAINT series_comparability_metric_id_fkey FOREIGN KEY (metric_id) REFERENCES core.metric(metric_id);


--
-- Name: series_comparability series_comparability_region_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.series_comparability
    ADD CONSTRAINT series_comparability_region_id_fkey FOREIGN KEY (region_id) REFERENCES core.region(region_id);


--
-- Name: series_comparability series_comparability_source_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.series_comparability
    ADD CONSTRAINT series_comparability_source_id_fkey FOREIGN KEY (source_id) REFERENCES core.source(source_id);


--
-- Name: source_metric_mapping source_metric_mapping_metric_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.source_metric_mapping
    ADD CONSTRAINT source_metric_mapping_metric_id_fkey FOREIGN KEY (metric_id) REFERENCES core.metric(metric_id);


--
-- Name: source_metric_mapping source_metric_mapping_region_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.source_metric_mapping
    ADD CONSTRAINT source_metric_mapping_region_id_fkey FOREIGN KEY (region_id) REFERENCES core.region(region_id);


--
-- Name: source_metric_mapping source_metric_mapping_source_id_fkey; Type: FK CONSTRAINT; Schema: meta; Owner: -
--

ALTER TABLE ONLY meta.source_metric_mapping
    ADD CONSTRAINT source_metric_mapping_source_id_fkey FOREIGN KEY (source_id) REFERENCES core.source(source_id);


--
-- PostgreSQL database dump complete
--

\unrestrict x4etc7kN8FPrY9ZzbV6eEKv1IM0I6GR2kVIez6MkK0webcnG96hZPdp6hb0Tw8r

