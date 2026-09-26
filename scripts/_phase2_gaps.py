import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()

print("== заседание без решения ==")
cur.execute("""SELECT m.meeting_id, m.meeting_date::text, m.decision_kind, m.notes FROM dkp.meeting m
LEFT JOIN dkp.decision d USING(meeting_id) WHERE d.decision_id IS NULL""")
for r in cur.fetchall(): print("  ", r)

for y in ("2013","2014","2015","2017","2020"):
    print("== %s ==" % y)
    cur.execute("""SELECT m.meeting_date::text, to_char(m.meeting_date,'Dy'), m.decision_kind,
    d.rate_prev::float, d.rate_new::float, d.action
    FROM dkp.meeting m LEFT JOIN dkp.decision d USING(meeting_id)
    WHERE to_char(m.meeting_date,'YYYY')=%s ORDER BY m.meeting_date""", (y,))
    for r in cur.fetchall(): print("   ", r)
conn.close(); print("DONE")