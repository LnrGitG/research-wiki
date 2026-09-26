import sys, json
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()
def run(tag, sql):
    cur.execute(sql); print(" -", tag, "->", cur.rowcount)
run("d24 27.03.2017: prev 10.0, action cut (new 9.75 по лестнице, вступление 27.03 — лаг 0)",
    "UPDATE dkp.decision SET rate_prev=10.00, action='cut', headline_ru='Ключевая ставка: 10.0 -> 9.75%' WHERE decision_id=24 AND rate_new=9.75")
cur.execute("SELECT m.meeting_id FROM dkp.decision d JOIN dkp.meeting m USING(meeting_id) WHERE d.decision_id=24")
mid = cur.fetchone()[0]
cur.execute("SELECT action, rate_prev::float, rate_new::float FROM dkp.decision WHERE decision_id=24")
a, rp, rn = cur.fetchone()
props = json.dumps({"meeting_id": mid, "action": a, "rate_prev": rp, "rate_new": rn}, ensure_ascii=False)
cur.execute("UPDATE graph.node SET title=%s, props=%s::jsonb WHERE ref_key='decision:24'", ("Решение %s: %s" % (mid, a), props))
print(" - graph sync ->", cur.rowcount)
conn.commit(); print("COMMIT ok")
cur.execute("SELECT d.decision_id, m.meeting_date::text, d.rate_prev::float, d.rate_new::float, d.action FROM dkp.decision d JOIN dkp.meeting m USING(meeting_id) WHERE d.decision_id=24")
print(" - d24 after:", cur.fetchone())
conn.close(); print("DONE")