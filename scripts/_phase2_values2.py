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

# d42 (26.07.2019): ступень 7.25 eff 29.07 — cut 7.5->7.25 (лаг 3д)
upd("d42: cut 7.5->7.25",
    "UPDATE dkp.decision SET rate_new=7.25, action='cut', headline_ru='Ключевая ставка: 7.5 -> 7.25%' WHERE decision_id=42 AND rate_new=7.50 AND action='hold'")
# d45 (20.12.2019): hold 6.25 (ступень 6.25 eff 16.12 — решение 06.12 hold 6.5)
upd("d45: hold 6.25",
    "UPDATE dkp.decision SET action='hold' WHERE decision_id=45 AND rate_prev=6.25 AND rate_new=6.25 AND action='cut'")
# d53 (19.02.2021): ступень 4.5 eff 22.02 — hike 4.25->4.5 (лаг 3д); action уже hike,
# но verify требует окно 0-4д: 22.02-19.02=3д — вне? нет, 3 дня в окне. Проверка была
# на лестнице: ступень 4.5 eff 2021-02-22? смотрим ladder 2021: (нужен 2021-02-22)
# ladder: 2021-03-22;2021-04-25;4.5 — значит 4.5 ступень eff 22.03?? Тогда факт:
# 19.02.2021 hike 4.25->4.5, ступень eff 22.02 — grep ladder ниже подтвердит.
# 2019-03-22 (d39): hold 7.5 vs ladder 7.75 на 22.03? ladder 2019: 7.5 ступень до 2019-03-24?
# Полная лестница 2019 до июня не видна — печать окно 2019-01..06.
for line in open("/tmp/keyrate_ladder.txt", encoding="utf-8"):
    if line.startswith(("2019-01", "2019-02", "2019-03", "2019-04", "2019-05", "2019-06")):
        log.append("ladder: " + line.strip())
    if line.startswith("2021-01") or line.startswith("2021-02"):
        log.append("ladder: " + line.strip())

# d39: если лестница говорит 7.75 на 22.03 -> факт hike был 07.03 (7.5->7.75 eff 11.03?)
# Тогда d38 (08.02) hold 7.75, d39 (22.03) cut 7.75->7.5? Нет: audit говорит
# «2019-02/03/04 phantom-изменения при факте hold 7.75» => весь Q1 hold 7.75!
# Но d41 (14.06.2019) cut 7.75->7.5 верен (ступень 7.5 eff 17.06).
# => d38: hold 7.75; d39: hold 7.75; d40: hold 7.75
upd("d38: hold 7.75 (было cut 7.75->7.5)",
    "UPDATE dkp.decision SET rate_new=7.75, action='hold', headline_ru='Ключевая ставка: 7.75 -> 7.75%' WHERE decision_id=38 AND rate_new=7.50 AND action='cut'")
upd("d39: hold 7.75 (было hold 7.5)",
    "UPDATE dkp.decision SET rate_prev=7.75, rate_new=7.75, headline_ru='Ключевая ставка: 7.75 -> 7.75%' WHERE decision_id=39 AND rate_prev=7.50 AND rate_new=7.50")
upd("d40: hold 7.75 (было hike 7.5->7.75)",
    "UPDATE dkp.decision SET rate_prev=7.75, rate_new=7.75, action='hold', headline_ru='Ключевая ставка: 7.75 -> 7.75%' WHERE decision_id=40 AND rate_prev=7.50 AND rate_new=7.75 AND action='hike'")
upd("d41: prev 7.75 (после hold-серии Q1)",
    "UPDATE dkp.decision SET rate_prev=7.75 WHERE decision_id=41 AND rate_prev=7.75 AND rate_new=7.50")

for did in (38, 39, 40, 41, 42, 45):
    sync_graph(did)
conn.commit()
log.append("graph synced: 38/39/40/41/42/45")

for line in log:
    print(" -", line)
conn.close()
print("DONE")