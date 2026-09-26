import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

conn = connect()
cur = conn.cursor()

# 30.04.2015: meeting есть (unscheduled), но решения нет — смотрим и вставляем decision
cur.execute("SELECT meeting_id, meeting_date::text, decision_kind, left(coalesce(notes,'-'),80) FROM dkp.meeting WHERE meeting_date='2015-04-30'")
m = cur.fetchall()
print("meeting 2015-04-30:", m)
conn.commit()
mid = m[0][0]
cur.execute("SELECT count(*) FROM dkp.decision WHERE meeting_id=%s", (mid,))
nd = cur.fetchone()[0]
print("decisions at mid %d:" % mid, nd)
if nd == 0:
    cur.execute("INSERT INTO dkp.decision (meeting_id, rate_prev, rate_new, action, headline_ru, source_id) VALUES (%s, 14.00, 12.50, 'cut', %s, 2) RETURNING decision_id",
        (mid, "Ключевая ставка: 14.0 -> 12.5%"))
    did = cur.fetchone()[0]
    cur.execute("UPDATE dkp.rate_level SET decision_id=%s WHERE effective_from='2015-05-05' AND decision_id IS NULL", (did,))
    print("INSERTED d%d, level bound: %d" % (did, cur.rowcount))
conn.commit()

# Ступень 2022-05-04 -> d66
cur.execute("UPDATE dkp.rate_level SET decision_id=66 WHERE effective_from='2022-05-04' AND decision_id IS NULL")
print("level 2022-05-04 -> d66:", cur.rowcount)
conn.commit()

# Итог
cur.execute("SELECT count(*) FROM dkp.decision")
print("decisions:", cur.fetchone()[0])
cur.execute("SELECT level_id, value, effective_from::text, decision_id FROM dkp.rate_level WHERE decision_id IS NULL")
print("remaining NULL FK:", cur.fetchall())
conn.commit()
conn.close()
print("OK")