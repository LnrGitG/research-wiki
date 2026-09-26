import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()

cur.execute("SELECT count(*) FROM dkp.meeting"); print("meetings:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.decision"); print("decisions:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.rate_level"); print("rate_level:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.argument"); print("arguments:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.statement"); print("statements:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.minutes"); print("minutes:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM graph.node"); print("graph nodes:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM graph.edge"); print("graph edges:", cur.fetchone()[0])

print("== заседаний по годам ==")
cur.execute("""SELECT to_char(meeting_date,'YYYY') y, count(*), string_agg(DISTINCT decision_kind, ',')
FROM dkp.meeting GROUP BY 1 ORDER BY 1""")
for r in cur.fetchall(): print("  ", r)

print("== дубли дат заседаний ==")
cur.execute("""SELECT meeting_date::text, count(*) FROM dkp.meeting GROUP BY 1 HAVING count(*)>1 ORDER BY 1""")
rows = cur.fetchall()
print("  дублей:", len(rows))
for r in rows: print("  ", r)

print("== заседания вне пятницы (день недели != 5) ==")
cur.execute("""SELECT meeting_date::text, to_char(meeting_date,'Dy'), decision_kind FROM dkp.meeting
WHERE extract(dow FROM meeting_date) <> 5 ORDER BY meeting_date""")
rows = cur.fetchall()
print("  не-пятниц:", len(rows))
for r in rows: print("  ", r)

print("== решения без заседания / заседания без решения ==")
cur.execute("SELECT count(*) FROM dkp.meeting m LEFT JOIN dkp.decision d USING(meeting_id) WHERE d.decision_id IS NULL")
print("  заседаний без решения:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.decision d LEFT JOIN dkp.meeting m USING(meeting_id) WHERE m.meeting_id IS NULL")
print("  решений без заседания:", cur.fetchone()[0])

print("== rate_level без решения ==")
cur.execute("SELECT count(*) FROM dkp.rate_level r LEFT JOIN dkp.decision d USING(decision_id) WHERE d.decision_id IS NULL")
print("  висячих ступеней:", cur.fetchone()[0])

print("== хвост 2026 ==")
cur.execute("""SELECT m.meeting_date::text, to_char(m.meeting_date,'Dy'), m.decision_kind, d.rate_prev::float, d.rate_new::float, d.action
FROM dkp.meeting m JOIN dkp.decision d USING(meeting_id) WHERE m.meeting_date >= '2026-01-01' ORDER BY 1""")
for r in cur.fetchall(): print("  ", r)
conn.close(); print("DONE")