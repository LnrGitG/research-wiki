-- Оригинальное определение derived.v_observation_latest до правки 29.10.2026
-- (снято из pg_views). Нужно для отката: psql -f этот файл.
-- Дефект оригинала: нет фильтра по observation_status, поэтому строка со статусом
-- rejected может победить в DISTINCT ON как «самая свежая» и попасть в витрину.
DROP VIEW IF EXISTS derived.v_observation_latest CASCADE;
CREATE VIEW derived.v_observation_latest AS
 SELECT DISTINCT ON (o.metric_id, o.region_id, o.period_start, o.frequency_id, o.assessment_type, o.sub_dimension) o.observation_id,
    o.metric_id,
    o.region_id,
    o.period_start,
    o.period_end,
    o.value,
    o.value_str,
    o.observation_status,
    o.assessment_type,
    o.sub_dimension,
    o.quality_flags,
    o.frequency_id,
    o.source_id,
    o.release_id,
    o.event_id,
    o.created_at
   FROM (data.observation o
     LEFT JOIN catalog.release r ON ((r.release_id = o.release_id)))
  ORDER BY o.metric_id, o.region_id, o.period_start, o.frequency_id, o.assessment_type, o.sub_dimension, COALESCE(r.published_at, r.ingested_at, o.created_at) DESC NULLS LAST, o.release_id DESC, o.observation_id DESC;
