import sys, json
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()
log = []
def run(tag, sql):
    cur.execute(sql); log.append("%s -> %d" % (tag, cur.rowcount))
def show(tag, did):
    cur.execute("SELECT d.decision_id, m.meeting_date::text, d.rate_prev::float, d.rate_new::float, d.action FROM dkp.decision d JOIN dkp.meeting m USING(meeting_id) WHERE d.decision_id=%s", (did,))
    log.append("%s: %s" % (tag, cur.fetchone()))
def sync_graph(did):
    cur.execute("SELECT action, rate_prev::float, rate_new::float, meeting_id FROM dkp.decision WHERE decision_id=%s", (did,))
    r = cur.fetchone()
    if r:
        props = json.dumps({"meeting_id": r[3], "action": r[0], "rate_prev": r[1], "rate_new": r[2]}, ensure_ascii=False)
        cur.execute("UPDATE graph.node SET title=%s, props=%s::jsonb WHERE ref_key=%s", ("Решение %s: %s" % (r[3], r[0]), props, "decision:%d" % did))

show("d15 before", 15); show("d24 before", 24)
# d15 03.12.2015: по лестнице 11,0 действует с 03.08.2015 до 13.06.2016 => hold 11,0
run("d15 03.12.2015 hold 11.0 (cut 11.0->10.5 снят: ступени 10.5 нет)",
    "UPDATE dkp.decision SET rate_new=11.00, action='hold', headline_ru='Ключевая ставка: 11.0 -> 11.0%' WHERE decision_id=15 AND rate_new=10.50")
# d24 27.03.2017: ступень 9,75 вступает 27.03.2017 (лаг 0) => cut 10,0->9,75
show("d24 after d15 fix", 24)
run("d24 27.03.2017 cut 10.0->9.75",
    "UPDATE dkp.decision SET rate_prev=10.00, rate_new=9.75, action='cut', headline_ru='Ключевая ставка: 10.0 -> 9.75%' WHERE decision_id=24 AND rate_new=9.50")
sync_graph(15); sync_graph(24)
conn.commit()
log.append("COMMIT ok")
show("d15 after", 15); show("d24 after", 24)
for l in log:
    print(" -", l)
conn.close(); print("DONE")