#!/usr/bin/env python3
"""Точечная чистка дублей рубежа 6: iokmrrkri и ksddrk (релиз 50)."""
import os, psycopg, shutil

os.environ.setdefault('PGPASSFILE', os.path.expanduser('~/.pgpass'))
DSN = "host=localhost port=5432 dbname=research_wiki user=wiki"
conn = psycopg.connect(DSN)
cur = conn.cursor()

def n(sql, args=None):
    cur.execute(sql, args or ())
    return cur.fetchone()[0]

print("=== ДО ===")
total0 = n('SELECT count(*) FROM core.observation_v2')
print("   всего: %s" % format(total0, ','))

# 1. iokmrrkri — дубль iokmrrk (значения совпали 2400/2400)
mid_iok = None
try:
    mid_iok = n("SELECT metric_id FROM core.metric WHERE metric_code='iokmrrkri'")
except Exception:
    mid_iok = None
mid_ok = n("SELECT metric_id FROM core.metric WHERE metric_code='iokmrrk'")
n_dup = n('SELECT count(*) FROM core.observation_v2 WHERE metric_id=%s', (mid_iok,)) if mid_iok else 0
pairs_equal = n("""SELECT count(*) FROM core.observation_v2 a
    JOIN core.observation_v2 b ON b.region_id=a.region_id
      AND b.period_start=a.period_start AND b.value=a.value
    WHERE a.metric_id=%s AND b.metric_id=%s""", (mid_iok, mid_ok))
print("\n1. iokmrrkri: %s строк, совпавших по значению с iokmrrk: %s" % (format(n_dup, ','), format(pairs_equal, ',')))
if n_dup == pairs_equal:
    cur.execute('DELETE FROM core.observation_v2 WHERE metric_id=%s', (mid_iok,))
    conn.commit()
    print("   УДАЛЕНО (полный дубль)")
else:
    print("   НЕ удаляю: совпадение неполное")

# 2. ksddrk релиз 50 — дубль релиза 4
mid_ks = n("SELECT metric_id FROM core.metric WHERE metric_code='ksddrk'")
rel_old = n("""SELECT release_id FROM core.release WHERE source_id=(
    SELECT source_id FROM core.source WHERE source_code='rosreestr')
    AND release_label LIKE 'Срез Росреестра%%' LIMIT 1""")
rel_new = n("""SELECT release_id FROM core.release WHERE source_id=(
    SELECT source_id FROM core.source WHERE source_code='rosreestr')
    AND release_label='rosreestr ряды' LIMIT 1""")
keys_old = set(cur.execute("""SELECT region_id, period_start FROM core.observation_v2
    WHERE metric_id=%s AND release_id=%s""", (mid_ks, rel_old)).fetchall())
keys_new = set(cur.execute("""SELECT region_id, period_start FROM core.observation_v2
    WHERE metric_id=%s AND release_id=%s""", (mid_ks, rel_new)).fetchall())
print("\n2. ksddrk: старый релиз %s ключей=%d, новый релиз %s ключей=%d, общих=%d, только-новых=%d"
      % (rel_old, len(keys_old), rel_new, len(keys_new), len(keys_old & keys_new), len(keys_new - keys_old)))
if len(keys_new - keys_old) == 0:
    cur.execute('DELETE FROM core.observation_v2 WHERE metric_id=%s AND release_id=%s', (mid_ks, rel_new))
    conn.commit()
    print("   УДАЛЕНО (новый релиз полностью перекрыт старым)")
else:
    print("   НЕ удаляю: новый релиз добавляет %d ключей" % len(keys_new - keys_old))

print("\n=== ПОСЛЕ ===")
total1 = n('SELECT count(*) FROM core.observation_v2')
print("   всего: %s (было %s, удалено %s)" % (format(total1, ','), format(total0, ','), format(total0 - total1, ',')))
print("   истинных дублей: %s" % n("""SELECT coalesce(sum(c-1),0) FROM (
    SELECT count(*) c FROM core.observation_v2
    GROUP BY metric_id, region_id, frequency_id, period_start, source_id,
             release_id, assessment_type, sub_dimension HAVING count(*)>1) x"""))
print("   метрик: %s" % n('SELECT count(*) FROM core.metric'))
print("   по источникам:")
cur.execute("""SELECT s.source_code, count(*) FROM core.observation_v2 o
               JOIN core.source s ON s.source_id=o.source_id GROUP BY 1 ORDER BY 2 DESC""")
for sc, c in cur.fetchall():
    print("      %-10s %s" % (sc, format(c, ',')))
conn.close()
