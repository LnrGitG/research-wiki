"""Создание BI-витрины derived.v_bi_observation и грантов роли metabase_ro.

Идемпотентно: CREATE OR REPLACE VIEW + GRANT (повторный прогон безопасен).
Откат: DROP VIEW derived.v_bi_observation; REVOKE USAGE ON SCHEMA meta FROM metabase_ro;
       REVOKE SELECT ON ALL TABLES IN SCHEMA meta FROM metabase_ro;
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
import db_tunnel as d

VIEW_SQL = """
CREATE OR REPLACE VIEW derived.v_bi_observation AS
SELECT
  o.observation_id,
  m.metric_code,
  m.name_ru        AS metric_name,
  m.short_name_ru  AS metric_short_name,
  f.freq_code,
  f.name_ru        AS freq_name,
  o.period_start,
  o.period_end,
  EXTRACT(year    FROM o.period_start)::int AS year,
  EXTRACT(month   FROM o.period_start)::int AS month,
  EXTRACT(quarter FROM o.period_start)::int AS quarter,
  r.region_code,
  r.name_ru        AS region_name,
  r.level          AS region_level,
  o.region_id,
  u.unit_code,
  u.name_ru        AS unit_name,
  s.source_code,
  s.name_ru        AS source_name,
  rel.label        AS release_label,
  rel.published_at,
  o.value,
  o.value_str,
  o.sub_dimension,
  o.assessment_type,
  o.observation_status,
  o.quality_flags,
  o.release_id
FROM data.observation o
JOIN catalog.metric m    ON m.metric_id    = o.metric_id
JOIN catalog.frequency f ON f.frequency_id = o.frequency_id
LEFT JOIN catalog.region  r   ON r.region_id   = o.region_id
LEFT JOIN catalog.unit    u   ON u.unit_id     = m.unit_id
LEFT JOIN catalog.source  s   ON s.source_id   = o.source_id
LEFT JOIN catalog.release rel ON rel.release_id = o.release_id
WHERE o.observation_status <> 'rejected'
"""


def main() -> int:
    if not d.available():
        print("тоннель недоступен")
        return 1
    d.execute(VIEW_SQL)
    d.execute("GRANT SELECT ON derived.v_bi_observation TO metabase_ro")
    d.execute("GRANT USAGE ON SCHEMA meta TO metabase_ro")
    d.execute("GRANT SELECT ON ALL TABLES IN SCHEMA meta TO metabase_ro")
    print("вид создан и гранты выданы")

    rows = d.query("""
        SELECT count(*),
               count(*) FILTER (WHERE metric_code IS NULL),
               count(*) FILTER (WHERE region_code IS NULL),
               min(period_start), max(period_start)
        FROM derived.v_bi_observation
    """)
    print("строки/битые метрики/битые регионы/мин/макс:", rows[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
