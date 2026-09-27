import sys, json
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()
log = []

# Дубль 2022-02-11: заседание 64 с решением 62 (hold 9,5) повторяет заседание 62
# с решением 61 (hike 8,5→9,5), которое и есть реальное решение 11.02.2022.
cur.execute("""SELECT d.decision_id, m.meeting_id FROM dkp.decision d JOIN dkp.meeting m USING(meeting_id)
WHERE m.meeting_date='2022-02-11' AND d.action='hold'""")
row = cur.fetchone()
if row:
    did, mid = row
    for sql, tag in (
        ("DELETE FROM dkp.argument WHERE decision_id=%d" % did, "argument"),
        ("DELETE FROM dkp.rate_level WHERE decision_id=%d" % did, "rate_level"),
        ("DELETE FROM dkp.decision WHERE decision_id=%d" % did, "decision"),
        ("DELETE FROM dkp.dissent WHERE meeting_id=%d" % mid, "dissent"),
        ("DELETE FROM dkp.forecast WHERE meeting_id=%d" % mid, "forecast"),
        ("DELETE FROM dkp.minutes WHERE meeting_id=%d" % mid, "minutes"),
        ("DELETE FROM dkp.statement WHERE meeting_id=%d" % mid, "statement"),
        ("DELETE FROM dkp.uncertainty_item WHERE meeting_id=%d" % mid, "uncertainty_item"),
        ("DELETE FROM dkp.meeting WHERE meeting_id=%d" % mid, "meeting"),
    ):
        cur.execute(sql)
        log.append("%s -> %d" % (tag, cur.rowcount))
    conn.commit()
    log.append("удалены meeting %d и decision %d (дубль 2022-02-11)" % (mid, did))
else:
    log.append("дубль не найден — правка не требуется")

cur.execute("SELECT count(*) FROM dkp.meeting"); log.append("заседаний: %d" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.decision"); log.append("решений: %d" % cur.fetchone()[0])
cur.execute("SELECT meeting_date::text, count(*) FROM dkp.meeting GROUP BY 1 HAVING count(*)>1")
log.append("дублей дат: %d" % len(cur.fetchall()))
for line in log:
    print(" -", line)
conn.close()