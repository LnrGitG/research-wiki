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
     LEFT JOIN core.metric_legacy m ON ((m.metric_id = o.metric_id)))
     LEFT JOIN core.region_legacy r ON ((r.region_id = o.region_id)))
     LEFT JOIN core.frequency_legacy f ON ((f.frequency_id = o.frequency_id)))
     LEFT JOIN core.unit_legacy u ON ((u.unit_id = m.unit_id)))
     LEFT JOIN core.source_legacy s ON ((s.source_id = o.source_id)))
     LEFT JOIN core.release_legacy rl ON ((rl.release_id = o.release_id)));