import sys
sys.path.insert(0, "scripts")
import db_tunnel
conn = db_tunnel.connect(); cur = conn.cursor()
# full EXCEPT-сверка v2(is_current) ← → data по домрф-метрикам
r = cur.execute("""SELECT count(*) FROM (
    SELECT o.period_start, o.region_id, o.frequency_id, o.value FROM v2.observation o
      JOIN v2.metric m ON m.metric_id=o.metric_id
      LEFT JOIN v2.region vr ON vr.region_id=o.region_id
      LEFT JOIN catalog.region cr ON LOWER(REPLACE(vr.name_ru,chr(1105),chr(1077)))=LOWER(REPLACE(cr.name_ru,chr(1105),chr(1077)))
      WHERE m.metric_code LIKE 'domrf_%' AND o.is_current
      EXCEPT ALL
    SELECT d.period_start, d.region_id, d.frequency_id, d.value FROM data.observation d
      JOIN catalog.metric m2 ON m2.metric_id=d.metric_id
      WHERE m2.metric_code LIKE 'domrf_%'
  ) x""").fetchone()[0]
print("строк в v2, отсутствующих в canon:", r)
r2 = cur.execute("""SELECT count(*) FROM (
    SELECT d.period_start, d.region_id, d.frequency_id, d.value FROM data.observation d
      JOIN catalog.metric m2 ON m2.metric_id=d.metric_id
      WHERE m2.metric_code LIKE 'domrf_%'
      EXCEPT ALL
    SELECT o.period_start, COALESCE(cr.region_id, 1), o.frequency_id, o.value FROM v2.observation o
      JOIN v2.metric m ON m.metric_id=o.metric_id
      LEFT JOIN v2.region vr ON vr.region_id=o.region_id
      LEFT JOIN catalog.region cr ON LOWER(REPLACE(vr.name_ru,chr(1105),chr(1077)))=LOWER(REPLACE(cr.name_ru,chr(1105),chr(1077)))
      WHERE m.metric_code LIKE 'domrf_%' AND o.is_current
  ) x""").fetchone()[0]
print("строк в canon, отсутствующих в v2:", r2)
# полные counts
print("canon domrf_* наблюдений:", cur.execute("""SELECT count(*) FROM data.observation d
    JOIN catalog.metric m ON m.metric_id=d.metric_id WHERE m.metric_code LIKE 'domrf_%'""").fetchone()[0])
print("v2 domrf_* is_current:", cur.execute("""SELECT count(*) FROM v2.observation o
    JOIN v2.metric m ON m.metric_id=o.metric_id WHERE m.metric_code LIKE 'domrf_%' AND o.is_current""").fetchone()[0])
conn.close()