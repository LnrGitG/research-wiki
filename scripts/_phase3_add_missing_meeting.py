import sys, json
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()
log = []

# Пропущенное заседание 18.09.2020: пресс-релиз 18092020 подтверждён (страница
# решения 45 988 байт против служебной заглушки 28 214). Лестница: ступень 4,25
# действует с 27.07.2020 по 21.03.2021, значит 18.09.2020 — удержание 4,25.
cur.execute("SELECT count(*) FROM dkp.meeting WHERE meeting_date='2020-09-18'")
if cur.fetchone()[0] == 0:
    cur.execute("""INSERT INTO dkp.meeting (meeting_date, decision_kind, notes)
        VALUES ('2020-09-18', 'scheduled', 'заседание 18.09.2020: удержание 4,25 (пресс-релиз 18092020 подтверждён, ступень 4,25 с 27.07.2020)')
        RETURNING meeting_id""")
    mid = cur.fetchone()[0]
    log.append("insert meeting 18.09.2020 -> meeting_id %s" % mid)
    cur.execute("""INSERT INTO dkp.decision (meeting_id, rate_prev, rate_new, action, headline_ru)
        VALUES (%s, 4.25, 4.25, 'hold', 'Ключевая ставка: 4.25 -> 4.25' || chr(37)) RETURNING decision_id""", (mid,))
    did = cur.fetchone()[0]
    log.append("insert decision -> decision_id %s" % did)
    cur.execute("SELECT count(*) FROM graph.node WHERE ref_key=%s", ("decision:%d" % did,))
    log.append("узел графа для нового решения: %d (граф пересобирается отдельно)" % cur.fetchone()[0])
    conn.commit()
else:
    log.append("заседание 18.09.2020 уже есть — правка не требуется")

cur.execute("SELECT count(*) FROM dkp.meeting"); log.append("заседаний: %d" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.decision"); log.append("решений: %d" % cur.fetchone()[0])
cur.execute("""SELECT to_char(meeting_date,'YYYY') y, count(*) FROM dkp.meeting
WHERE meeting_date BETWEEN '2018-01-01' AND '2021-12-31' GROUP BY 1 ORDER BY 1""")
for r in cur.fetchall():
    log.append("заседаний %s: %d" % r)
for line in log:
    print(" -", line)
conn.close()