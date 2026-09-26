import sys, json
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

conn = connect(); cur = conn.cursor()
log = []

def run(tag, sql, params=None):
    if params is None:
        cur.execute(sql)
    else:
        cur.execute(sql, params)
    log.append("%s -> %d" % (tag, cur.rowcount))

def sync_graph(did):
    cur.execute("SELECT action, rate_prev::float, rate_new::float, meeting_id FROM dkp.decision WHERE decision_id=%s", (did,))
    row = cur.fetchone()
    if not row:
        return
    action, rprev, rnew, mid = row
    props = json.dumps({"meeting_id": mid, "action": action, "rate_prev": rprev, "rate_new": rnew}, ensure_ascii=False)
    cur.execute("UPDATE graph.node SET title=%s, props=%s::jsonb WHERE node_type='cbr_decision' AND ref_key=%s",
                ("Решение %s: %s" % (mid, action), props, "decision:%d" % did))

try:
    # ---------- 1. Значения ----------
    run("d23 16.12.2016 hold 10.0",
        "UPDATE dkp.decision SET rate_new=10.00, action='hold', headline_ru='Ключевая ставка: 10.0 -> 10.0%' WHERE decision_id=23 AND rate_prev=10.00 AND rate_new=9.50")
    run("d19 10.06.2016 cut 11.0->10.5",
        "UPDATE dkp.decision SET rate_prev=11.00, rate_new=10.50, action='cut', headline_ru='Ключевая ставка: 11.0 -> 10.5%' WHERE decision_id=19 AND rate_prev=10.50 AND rate_new=10.50")
    run("d28 hold -> cut 9.0->8.5",
        "UPDATE dkp.decision SET rate_prev=9.00, rate_new=8.50, action='cut', headline_ru='Ключевая ставка: 9.0 -> 8.5%' WHERE decision_id=28")
    run("d45->13.12.2019 6.5->6.25 приведено (hold/cut)",
        "UPDATE dkp.decision SET rate_prev=6.50, rate_new=6.25, action='cut' WHERE decision_id=45")
    run("d53 12.02.2021 hold 4.25 (было hike 4.25->4.5)",
        "UPDATE dkp.decision SET rate_prev=4.25, rate_new=4.25, action='hold', headline_ru='Ключевая ставка: 4.25 -> 4.25%' WHERE decision_id=53")
    run("d54 19.03.2021 hike 4.25->4.5",
        "UPDATE dkp.decision SET rate_prev=4.25, rate_new=4.50, action='hike', headline_ru='Ключевая ставка: 4.25 -> 4.5%' WHERE decision_id=54")
    run("d102 prev 14.25",
        "UPDATE dkp.decision SET rate_prev=14.25 WHERE decision_id=102 AND rate_prev=14.50")

    # ---------- 2. Даты заседаний ----------
    run("meeting 28: 2017-09-18 -> 2017-09-15",
        "UPDATE dkp.meeting SET meeting_date='2017-09-15' WHERE meeting_id=28 AND meeting_date='2017-09-18'")
    run("meeting 115: 2017-06-09 -> 2017-06-16 + scheduled",
        "UPDATE dkp.meeting SET meeting_date='2017-06-16', decision_kind='scheduled', notes='заседание 16.06.2017: cut 9,25→9,00 (вступление 19.06) [ladder-verified]' WHERE meeting_id=115")
    run("meeting 45: 2019-12-13 -> 2019-10-25",
        "UPDATE dkp.meeting SET meeting_date='2019-10-25', notes='заседание 25.10.2019: cut 7,00→6,50 (вступление 28.10) [ladder-verified]' WHERE meeting_id=45")
    run("meeting 46: 2019-12-20 -> 2019-12-13",
        "UPDATE dkp.meeting SET meeting_date='2019-12-13', notes='заседание 13.12.2019: cut 6,50→6,25 (вступление 16.12) [ladder-verified]' WHERE meeting_id=46")
    run("meeting 54: 2021-02-19 -> 2021-02-12",
        "UPDATE dkp.meeting SET meeting_date='2021-02-12', notes='заседание 12.02.2021: ставка 4,25 без изменений [ladder-verified]' WHERE meeting_id=54")
    run("meeting 55: unscheduled -> scheduled",
        "UPDATE dkp.meeting SET decision_kind='scheduled', notes='заседание 19.03.2021: hike 4,25→4,50 (вступление 22.03) [ladder-verified]' WHERE meeting_id=55")

    # ---------- 3. Удаление фантомов: meeting 26 (2017-06-26) и meeting 116 (2019-12-06) ----------
    for mid in (26, 116):
        run("child: argument(meeting %d)" % mid,
            "DELETE FROM dkp.argument WHERE decision_id IN (SELECT decision_id FROM dkp.decision WHERE meeting_id=%d)" % mid)
        for tbl in ("dissent", "forecast", "minutes", "statement", "uncertainty_item"):
            run("child: %s(meeting %d)" % (tbl, mid), "DELETE FROM dkp.%s WHERE meeting_id=%d" % (tbl, mid))
    run("child: rate_level(decision 26/110)",
        "DELETE FROM dkp.rate_level WHERE decision_id IN (26,110)")
    run("delete decision 26/110", "DELETE FROM dkp.decision WHERE decision_id IN (26,110)")
    run("delete meeting 26/116", "DELETE FROM dkp.meeting WHERE meeting_id IN (26,116)")

    # ---------- 4. Граф ----------
    run("graph: edges to decision:26/meeting:26",
        """DELETE FROM graph.edge WHERE src_id IN (SELECT node_id FROM graph.node WHERE ref_key IN ('decision:26','meeting:26','decision:110','meeting:116'))
           OR dst_id IN (SELECT node_id FROM graph.node WHERE ref_key IN ('decision:26','meeting:26','decision:110','meeting:116'))""")
    run("graph: nodes", "DELETE FROM graph.node WHERE ref_key IN ('decision:26','meeting:26','decision:110','meeting:116')")
    for did in (19, 23, 28, 44, 45, 53, 54, 102, 109):
        sync_graph(did)
    log.append("graph sync: done")

    conn.commit()
    log.append("COMMIT ok")
except Exception as e:
    conn.rollback()
    log.append("ROLLBACK: %r" % (e,))

for line in log:
    print(" -", line)
conn.close()
print("DONE")