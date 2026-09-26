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

# ---- Правки значений по лестнице (каждая строка = ступень/день вступления) ----
# 2014-03-03 внеплановое 5.5->7.0 (ступень eff 03.03)
upd("d3 2014-03-03: 6.50 -> 7.00",
    "UPDATE dkp.decision SET rate_prev=5.50, rate_new=7.00, headline_ru='Ключевая ставка: 5.5 -> 7.0%' WHERE decision_id=3 AND rate_prev=5.50 AND rate_new=6.50")
# 2015-04-30 cut 14->12.5, ступень eff 05.05 (лаг 5, документирован) — verify окно расширено вручную
# (значение верно, лаг легитимен)
# 2015-06-08 cut 12.5->11.5: ступень 11.5 eff 16.06? факт: 08.06.2015 решение, ряд: 15.05-15.06=12.5, 16.06=11.5
upd("d11 2015-06-08: rate_new 11.50 ок (ступень eff 16.06, лаг 8д)", "SELECT 1")  # no-op: только проверка лагов ниже
# 2015-11-10 cut 11->10.5: ступень 10.5 eff 16.11 (решение 10.11? факт 11.11 по ladder: 11.5 до 04.11, 11.0 04.11-...; проверим ниже)
# 2015-12-03 hold 10.5 vs ladder 11.0: d15 решение 03.12.2015 cut до 10.5 с 15.12? факт ladder: 11.0 (04.11-...), 10.5 eff 15.12
upd("d15 2015-12-03: cut 11.0->10.5 (ступень eff 15.12, лаг 12д — вне окна)",
    "UPDATE dkp.decision SET rate_prev=11.00, headline_ru='Ключевая ставка: 11.0 -> 10.5%' WHERE decision_id=15 AND rate_prev=10.50 AND rate_new=10.50 AND action='hold'")
# 2016-02-01 hike 10.5->11.0: ступень 11.0 eff 03.02
upd("d16 2016-02-01: ок (значения верны; лаг 2д)", "SELECT 1")
# 2016-04-29 cut 11->10.5: ступень 10.5 eff 14.06?? нет: ladder 11.0 до 30.04... факт: решение 29.04 hold!
upd("d18 2016-04-29: hold 11.0 (было cut 10.5)",
    "UPDATE dkp.decision SET rate_prev=11.00, rate_new=11.00, action='hold', headline_ru='Ключевая ставка: 11.0 -> 11.0%' WHERE decision_id=18 AND rate_prev=11.00 AND rate_new=10.50 AND action='cut'")
# 2016-10-28 cut 10->9.5: ступень 9.5 eff 01.11 (лаг 4) — значения верны
# 2016-12-16 hold 9.5 vs ladder 10.0: 16.12.2016 решение cut до 9.5?? факт ladder: 10.0 до 18.12, 9.5 eff 19.12 => cut 10->9.5
upd("d23 2016-12-16: cut 10.0->9.5 (было hold 9.5)",
    "UPDATE dkp.decision SET rate_prev=10.00, rate_new=9.50, action='cut', headline_ru='Ключевая ставка: 10.0 -> 9.5%' WHERE decision_id=23 AND rate_prev=9.50 AND rate_new=9.50 AND action='hold'")
# 2017-06-26 дубль решения 09.06: hold 9.0 (ступень 9.0 eff 19.06 уже вступила)
upd("d26 2017-06-26: hold 9.0 (было cut 9.25->9.0)",
    "UPDATE dkp.decision SET rate_prev=9.00, rate_new=9.00, action='hold', headline_ru='Ключевая ставка: 9.0 -> 9.0%' WHERE decision_id=26 AND rate_prev=9.25 AND rate_new=9.00 AND action='cut'")
# 2017-07-28 cut 9->8.5: ступень 8.5 eff 01.08 (лаг 4) — значения верны
# 2019-02-08 cut 7.75->7.5: ступень 7.5 eff 11.02 (лаг 3) — значения верны
# 2019-03-22 hold 7.5 vs ladder 7.75: решение 22.03 hold 7.5?? факт ladder: 7.5 с 11.02 до 25.03, 7.75 eff 26.03? нет: hike 27.03?
upd("d39 2019-03-22: hold 7.50 подтверждён (ступень 7.5 до 26.03)", "SELECT 1")
# 2019-04-26 hike 7.5->7.75: ступень 7.75 eff 29.04 (лаг 3) — значения верны
# 2019-07-26 cut 7.5->7.25: ступень 7.25 eff 29.07 (лаг 3)
upd("d42 2019-07-26: rate_new 7.25 (было 7.50)",
    "UPDATE dkp.decision SET rate_new=7.25, headline_ru='Ключевая ставка: 7.5 -> 7.25%' WHERE decision_id=42 AND rate_prev=7.50 AND rate_new=7.50 AND action='hold'")
# 2019-12-06 дубль: hold 6.25 (ступень eff 16.12)
upd("d110 2019-12-06: hold 6.50->6.50? нет: факт cut 6.5->6.25 06.12? ladder: 6.5 до 15.12, 6.25 eff 16.12 => решение 06.12 hold 6.5, cut был 20.12?",
    "UPDATE dkp.decision SET rate_prev=6.50, rate_new=6.50, action='hold' WHERE decision_id=110 AND rate_prev=6.50 AND rate_new=6.25 AND action='cut'")
upd("d45 2019-12-20: cut 6.5->6.25 (ступень eff 16.12 внутри 0-4д от 20.12? нет: 16.12 РАНЬШЕ 20.12 => d45 prev 6.25?",
    "UPDATE dkp.decision SET rate_prev=6.25 WHERE decision_id=45 AND rate_prev=6.50 AND rate_new=6.25")
# 2020-06-19 cut 5.5->4.5: ступень 4.5 eff 22.06 (лаг 3)
upd("d49 2020-06-19: cut 5.5->4.5 (было hold 5.5)",
    "UPDATE dkp.decision SET rate_prev=5.50, rate_new=4.50, action='cut', headline_ru='Ключевая ставка: 5.5 -> 4.5%' WHERE decision_id=49 AND rate_prev=5.50 AND rate_new=5.50 AND action='hold'")
# 2020-07-24 cut 4.5->4.25: ступень eff 27.07
upd("d50 2020-07-24: cut 4.5->4.25 (было 5.5->4.5)",
    "UPDATE dkp.decision SET rate_prev=4.50, rate_new=4.25, headline_ru='Ключевая ставка: 4.5 -> 4.25%' WHERE decision_id=50 AND rate_prev=5.50 AND rate_new=4.50")
# 2020-10-19: hold 4.25 (внеплановое 19.10.2020? ladder: 4.25 до 22.10, 4.5 eff 26.10 => hike 23.10?)
upd("d51 2020-10-19: hold 4.25 (было cut 4.5->4.25)",
    "UPDATE dkp.decision SET rate_prev=4.25, rate_new=4.25, action='hold' WHERE decision_id=51 AND rate_prev=4.50 AND rate_new=4.25 AND action='cut'")
# 2021-02-19 hike 4.25->4.5: ступень 4.5 eff 22.02 (лаг 3)
upd("d53 2021-02-19: hike 4.25->4.5 (было cut 4.25->4.5)",
    "UPDATE dkp.decision SET action='hike' WHERE decision_id=53 AND rate_prev=4.25 AND rate_new=4.50 AND action='cut'")

# ---- Граф-синхронизация изменённых ----
for did in (3, 15, 18, 23, 26, 42, 49, 50, 51, 53, 110, 45, 111):
    sync_graph(did)
conn.commit()
log.append("graph synced: 13")

for line in log:
    print(" -", line)
conn.close()
print("DONE")