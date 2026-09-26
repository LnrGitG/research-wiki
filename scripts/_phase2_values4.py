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

# Остатки:
# 1) d4 (25.04.2014): hold 7.0 — UPDATE не сработал (условие 6.5/6.5 не совпало)
cur.execute("SELECT rate_prev::float, rate_new::float, action FROM dkp.decision WHERE decision_id=4")
r = cur.fetchone()
log.append("d4 state: %s" % (r,))
if abs(r[0] - 6.50) < 1e-9 or abs(r[1] - 6.50) < 1e-9:
    upd("d4: hold 7.0", "UPDATE dkp.decision SET rate_prev=7.00, rate_new=7.00, action='hold' WHERE decision_id=4")
    sync_graph(4)

# 2) d23 (16.12.2016) cut 10->9.5: ступень 9.5 eff 19.12 — лаг 3д, но verify не нашёл?
#    Проверить ladder: 9.5 ступень
for line in open("/tmp/keyrate_ladder.txt", encoding="utf-8"):
    if line.startswith(("2016-1", "2016-12", "2017-01", "2017-03")):
        log.append("ladder: " + line.strip())

# 3) d28 (18.09.2017): prev 8.5 — факт hold 8.5 (ступень 8.5 eff 18.09)
cur.execute("SELECT rate_prev::float, rate_new::float, action FROM dkp.decision WHERE decision_id=28")
r = cur.fetchone()
log.append("d28 state: %s" % (r,))
if abs(r[0] - 8.50) > 1e-9:
    upd("d28: hold 8.5 (prev -> 8.5)",
        "UPDATE dkp.decision SET rate_prev=8.50, rate_new=8.50, action='hold' WHERE decision_id=28")
    sync_graph(28)

# 4) d19 (10.06.2016): состояние?
cur.execute("SELECT rate_prev::float, rate_new::float, action FROM dkp.decision WHERE decision_id=19")
r = cur.fetchone()
log.append("d19 state: %s" % (r,))
# Факт: 10.06.2016 cut 11.0->10.5 (ступень eff 14.06)
if abs(r[0] - 10.50) < 1e-9 and r[2] == 'hike':
    upd("d19: cut 11.0->10.5", "UPDATE dkp.decision SET rate_prev=11.00, rate_new=10.50, action='cut' WHERE decision_id=19")
    sync_graph(19)

# 5) d110 (06.12.2019) hold 6.5 — уже ок; chain break из-за d45 prev 6.25 при 6.50:
#    ФАКТ: 06.12.2019 hold 6.5; 20.12.2019?? Нет — ladder: 6.5 до 15.12, 6.25 eff 16.12.
#    Единственное решение декабря = 06.12? БР 20.12 не заседал?? d45 (20.12) hold 6.25 неверен:
#    Факт: cut 6.5->6.25 был 13.12.2019 (ступень eff 16.12)!
cur.execute("SELECT m.meeting_date::text, m.decision_kind FROM dkp.meeting m WHERE m.meeting_id=45")
r = cur.fetchone()
log.append("d45 meeting: %s" % (r,))
# Пересадка d45: 20.12 -> 13.12 (дата релиза cut 6.5->6.25)
cur.execute("SELECT count(*) FROM dkp.meeting WHERE meeting_date='2013-12-13'")
log.append("check 2013-12-13: %d" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.meeting WHERE meeting_date='2019-12-13'")
cnt = cur.fetchone()[0]
log.append("meetings at 2019-12-13: %d" % cnt)
if cnt == 0:
    cur.execute("UPDATE dkp.meeting SET meeting_date='2019-12-13', notes=%s WHERE meeting_id=45",
        ("заседание 13.12.2019: cut 6,5→6,25 (пресс-релиз 13.12.2019; ступень с 16.12) [needs_source_check]",))
    log.append("d45 meeting 20.12 -> 13.12: %d" % cur.rowcount)
    conn.commit()
    upd("d45: cut 6.5->6.25", "UPDATE dkp.decision SET rate_prev=6.50, rate_new=6.25, action='cut' WHERE decision_id=45")
    sync_graph(45)

# 6) d43 (06.09.2019) cut 7.5->7.0: ступень 7.0 eff 09.09 — верно, но prev 7.5 vs d42 new 7.25
#    ФАКТ 26.07.2019: cut 7.25->7.5?? НЕТ: ladder 7.25 eff 29.07 => d42 (26.07) cut 7.5->7.25;
#    d43 (06.09) cut 7.25->7.0! prev должен быть 7.25
cur.execute("SELECT rate_prev::float, rate_new::float FROM dkp.decision WHERE decision_id=43")
r = cur.fetchone()
if abs(r[0] - 7.50) < 1e-9:
    upd("d43: prev 7.25", "UPDATE dkp.decision SET rate_prev=7.25 WHERE decision_id=43")
    sync_graph(43)

for line in log:
    print(" -", line)
conn.close()
print("DONE")