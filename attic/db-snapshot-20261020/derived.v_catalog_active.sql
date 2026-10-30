CREATE OR REPLACE VIEW derived.v_catalog_active AS
SELECT m.metric_id,
    m.metric_code,
    m.name_ru,
    m.frequency_id,
    m.unit_id,
    f.measure,
    f.unit_canonical,
    f.domain,
    f.freshness,
    f.last_obs_at,
    f.depth_obs,
    f.is_aggregate,
    p.source_metric_ids
   FROM ((core.metric_legacy m
     JOIN derived.catalog_facets f ON ((f.metric_id = m.metric_id)))
     LEFT JOIN derived.metric_provenance p ON ((p.canonical_id = m.metric_id)))
  WHERE ((m.status = 'active'::text) AND (NOT (m.metric_id IN ( SELECT catalog_quarantine.metric_id
           FROM derived.catalog_quarantine))));;
