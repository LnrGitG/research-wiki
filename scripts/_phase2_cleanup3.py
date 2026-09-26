import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

conn = connect()
cur = conn.cursor()

# 1. 2015-04-30 (mid 115? нет — проверим). Вставка была '2015-04-30' у агента ВМ,
#    но "NO decision at 2015-04-30" — смотрим, что реально вставлено.
cur.execute("SELECT m.meeting_id, m.meeting_date::text, d.decision_id, d.rate_prev, d.rate_new, d.action FROM dkp.meeting m JOIN dkp.decision d USING(meeting_id) WHERE m.meeting_date BETWEEN '2015-04-25' AND '2015-05-05' ORDER BY m.meeting_date")
print("2015-04/05:", cur.fetchall())
conn.commit()

# 2. Вставить 30.04.2015 (14.0->12.5) если отсутствует
cur.execute("SELECT count(*) FROM dkp.decision d JOIN dkp.meeting m USING(meeting_id) WHERE m.meeting_date='2015-04-30'")
n = cur.fetchone()[0]
print("decisions at 2015-04-30:", n)
if n == 0:
    cur.execute("INSERT INTO dkp.meeting (meeting_date, decision_kind, is_pillar, notes) VALUES ('2015-04-30','unscheduled',false,%s) RETURNING meeting_id",
        ("внеплановое: снижение c 14,0% до 12,5% (пресс-релиз 30.04.2015)",))
    mid = cur.fetchone()[0]
    cur.execute("INSERT INTO dkp.decision (meeting_id, rate_prev, rate_new, action, headline_ru, source_id) VALUES (%s, 14.00, 12.50, 'cut', %s, 2) RETURNING decision_id",
        (mid, "Ключевая ставка: 14.0 -> 12.5%"))
    did = cur.fetchone()[0]
    cur.execute("UPDATE dkp.rate_level SET decision_id=%s WHERE effective_from='2015-05-05' AND decision_id IS NULL", (did,))
    print("INSERTED 2015-04-30: mid %d, d%d, level bound: %d" % (mid, did, cur.rowcount))
conn.commit()

# 3. Ступень 2022-05-04 (14.0) -> d66 (29.04.2022, 17->14)
cur.execute("UPDATE dkp.rate_level SET decision_id=66 WHERE effective_from='2022-05-04' AND decision_id IS NULL")
print("level 2022-05-04 -> d66:", cur.rowcount)
conn.commit()

# 4. Итог
cur.execute("SELECT count(*) FROM dkp.decision")
print("decisions:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.rate_level WHERE decision_id IS NULL")
print("null FK:", cur.fetchone()[0])
cur.execute("SELECT level_id, value, effective_from::text, decision_id FROM dkp.rate_level WHERE decision_id IS NULL")
print("remaining NULL FK:", cur.fetchall())
conn.commit()
conn.close()
print("OK")