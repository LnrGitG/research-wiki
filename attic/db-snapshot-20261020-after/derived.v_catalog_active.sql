CREATE OR REPLACE VIEW derived.v_catalog_active AS
SELECT (m.metric_id)::bigint AS metric_id,
    m.metric_code,
    m.name_ru,
    (m.frequency_id)::bigint AS frequency_id,
    (m.unit_id)::bigint AS unit_id,
    f.measure,
    COALESCE(f.unit_canonical, u.unit_code) AS unit_canonical,
    f.domain,
    f.freshness,
    f.last_obs_at,
    f.depth_obs,
    f.is_aggregate,
    p.source_metric_ids
   FROM (((catalog.metric m
     LEFT JOIN derived.catalog_facets f ON ((f.metric_id = m.metric_id)))
     LEFT JOIN catalog.unit u ON ((u.unit_id = m.unit_id)))
     LEFT JOIN derived.metric_provenance p ON ((p.canonical_id = m.metric_id)))
  WHERE ((m.status = 'active'::text) AND m.is_active AND (NOT (EXISTS ( SELECT 1
           FROM derived.catalog_quarantine q
          WHERE (q.metric_id = m.metric_id)))));;
