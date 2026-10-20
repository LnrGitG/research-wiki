CREATE OR REPLACE VIEW derived.v_metric_context AS
WITH base AS (
         SELECT m.metric_id,
            m.metric_code,
            m.name_ru,
            u.unit_code AS unit,
            s.source_code AS source,
            f.freq_code AS frequency,
            mc.last_observation,
            COALESCE(mc.observations_cnt, (0)::bigint) AS observations,
                CASE f.freq_code
                    WHEN 'D'::text THEN 10
                    WHEN 'W'::text THEN 5
                    WHEN 'M'::text THEN 75
                    WHEN 'Q'::text THEN 160
                    WHEN 'A'::text THEN 550
                    ELSE 120
                END AS tolerance_days
           FROM ((((catalog.metric m
             LEFT JOIN catalog.unit u ON ((u.unit_id = m.unit_id)))
             LEFT JOIN catalog.source s ON ((s.source_id = m.source_id)))
             LEFT JOIN catalog.frequency f ON ((f.frequency_id = m.frequency_id)))
             LEFT JOIN derived.v_metric_card mc ON ((mc.metric_id = m.metric_id)))
          WHERE m.is_active
        )
 SELECT b.metric_id,
    b.metric_code,
    b.name_ru,
    b.unit,
    b.source,
    b.frequency,
    tp.topic_code AS topic,
    al.aliases,
    b.last_observation,
    b.observations,
    (b.last_observation + ((b.tolerance_days || ' days'::text))::interval) AS expected_next,
        CASE
            WHEN (b.last_observation IS NULL) THEN 'нет данных'::text
            WHEN ((now())::date <= (b.last_observation + ((b.tolerance_days || ' days'::text))::interval)) THEN 'свежие'::text
            WHEN ((now())::date <= (b.last_observation + (((b.tolerance_days * 2) || ' days'::text))::interval)) THEN 'отстают'::text
            ELSE 'устарели'::text
        END AS freshness
   FROM ((base b
     LEFT JOIN LATERAL ( SELECT t2.topic_code
           FROM (catalog.metric_topic mt
             JOIN catalog.topic t2 ON ((t2.topic_id = mt.topic_id)))
          WHERE (mt.metric_id = b.metric_id)
          ORDER BY mt.weight DESC
         LIMIT 1) tp ON (true))
     LEFT JOIN LATERAL ( SELECT array_agg(a.alias ORDER BY a.alias) AS aliases
           FROM catalog.metric_alias a
          WHERE (a.metric_id = b.metric_id)) al ON (true));;
