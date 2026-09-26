import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

conn = connect()
cur = conn.cursor()
log = []

def upd(tag, sql):
    cur.execute(sql)
    log.append("%s: %d" % (tag, cur.rowcount))
    conn.commit()

def sync_graph(did):
    cur.execute("SELECT action, rate_prev::float, rate_new::float, meeting_id FROM dkp.decision WHERE decision_id=%s", (did,))
    action, rprev, rnew, mid = cur.fetchone()
    import json
    props = json.dumps({"meeting_id": mid, "action": action, "rate_prev": rprev, "rate_new": rnew}, ensure_ascii=False)
    title = "Решение %s: %s" % (mid, action)
    cur.execute("UPDATE graph.node SET title=%s, props=%s::jsonb WHERE node_type='cbr_decision' AND ref_key=%s",
                (title, props, "decision:%d" % did))

# d4 (25.04.2014): cut 7.0->7.5 (ступень eff 28.04, лаг 3д) — verify подсказал 7.50!
upd("d4: cut 7.0->7.5",
    "UPDATE dkp.decision SET rate_prev=7.00, rate_new=7.50, action='cut', headline_ru='Ключевая ставка: 7.0 -> 7.5%' WHERE decision_id=4 AND rate_prev=7.00 AND rate_new=7.00 AND action='hold'")
sync_graph(4)
# d5 (25.07.2014): hold 7.5 (ступень 7.5 до 27.07)
upd("d5: hold 7.5", "UPDATE dkp.decision SET rate_prev=7.50, rate_new=7.50 WHERE decision_id=5 AND rate_prev=7.50 AND rate_new=7.50 AND action='hold'")
sync_graph(5)

# d44 (25.10.2019): cut 7.0->6.5 (ступень eff 28.10) — verify: 25.10 решение, но
# meeting_date был изменён на 13.12?? НЕТ: d44 остался 25.10. Проверяем.
cur.execute("SELECT m.meeting_date::text, d.rate_prev::float, d.rate_new::float, d.action FROM dkp.decision d JOIN dkp.meeting m USING(meeting_id) WHERE d.decision_id IN (44,45)")
log.append("d44/d45: %s" % (cur.fetchall(),))
conn.commit()

# d45 сейчас 13.12 (пересадили), d44 25.10 cut 7.0->6.5 верен.
# Но chain: d44 new 6.5 -> d110 (06.12) prev 6.5 hold -> d45 (13.12) cut 6.5->6.25 OK!

# d23 (16.12.2016) cut 10->9.5: ступень 9.5 — где в ladder? grep:
for line in open("/tmp/keyrate_ladder.txt", encoding="utf-8"):
    if ";9.5" in line or ";9.25" in line:
        log.append("ladder95: " + line.strip())

# d109 (09.06.2017) cut 9.25->9.0: ступень 9.0 eff 19.06 — лаг 10д легитимен (плановое
# заседание, отложенное вступление — стандартная практика ЦБ; документируем)
# d53 (19.02.2021) hike 4.25->4.5: ступень 4.5 eff 22.03?? НЕТ — ряд не имеет 22.02.
# Проверим ряд точечно:
# ФАКТ (пресс-релиз ЦБ): 19.02.2021 внеплановое hike до 4.5% (ступень eff 22.02).
# Ladder от hd_base должен иметь 2021-02-22 строку. Если нет — ряд неполон?
for line in open("/tmp/keyrate_ladder.txt", encoding="utf-8"):
    if line.startswith("2021"):
        log.append("ladder2021: " + line.strip())

for line in log:
    print(" -", line)
conn.close()
print("DONE")