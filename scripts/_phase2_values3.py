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

# === Сверка против ladder (окончательные значения) ===

# d4 2014-04-25: hold 7.0 (ступень 7.0 до 27.04) — было 6.5 (phantom prev)
upd("d4 25.04.2014: hold 7.0 (prev 6.5 -> 7.0)",
    "UPDATE dkp.decision SET rate_prev=7.00, rate_new=7.00, headline_ru='Ключевая ставка: 7.0 -> 7.0%' WHERE decision_id=4 AND rate_prev=6.50 AND rate_new=6.50")
sync_graph(4)

# d14 10.11.2015: cut 11.5->11.0 (ступень 11.0 eff 03.08? нет — 10.11.2015 решение,
# ladder: 11.5 до 02.08, 11.0 eff 03.08. Решение 10.11?? факт: 30.10.2015? Нет.
# БР 15.11.2015 cut до 10.5? нет. Реально: решение 30.10.2015? Не буду угадывать:
# 10.11.2015 — внеплановое cut 11.5->11.0? Но ступень 11.0 eff 03.08, ЗАДАНГО раньше.
# => значение 11.0 на 10.11 уже действует: d14 = hold 11.0!
upd("d14 10.11.2015: hold 11.0 (было cut 11.0->10.5; ступень 11.0 действует с 03.08)",
    "UPDATE dkp.decision SET rate_new=11.00, action='hold' WHERE decision_id=14 AND rate_prev=11.00 AND rate_new=10.50 AND action='cut'")
sync_graph(14)

# d15 03.12.2015: cut 11.0->10.5 (ступень 10.5 eff 15.12? нет в ladder!)
# ladder 2015: 11.0 (03.08-13.06.16). 10.5 нет => факт: 03.12.2015 hold 11.0!
upd("d15 03.12.2015: hold 11.0 (было cut 11.0->10.5; ступени 10.5 нет в 2015)",
    "UPDATE dkp.decision SET rate_new=11.00, action='hold', headline_ru='Ключевая ставка: 11.0 -> 11.0%' WHERE decision_id=15 AND rate_prev=11.00 AND rate_new=10.50 AND action='cut'")
sync_graph(15)

# d19 10.06.2016: hold 10.5 (ступень 10.5 eff 14.06, лаг 4д — решение 10.06 hold,
# но фактически 10.06.2016 было внеплановое? Нет: 10.06.2016 scheduled cut до 10.5 с 14.06)
upd("d19 10.06.2016: cut 11.0->10.5 (ступень eff 14.06, лаг 4д — значения верны, окно на границе)",
    "UPDATE dkp.decision SET rate_prev=11.00, rate_new=10.50, action='cut' WHERE decision_id=19 AND rate_prev=10.50 AND rate_new=11.00 AND action='hike'")
sync_graph(19)

# d16 01.02.2016: hold 11.0 (ступень 11.0 действует с 03.08.2015; 01.02.2016 внеплановое?)
# Факт 2016: 14.01? Реально ladder 11.0 до 13.06.2016 => любые «изменения» до 10.06 phantom
upd("d16 01.02.2016: hold 11.0 (было hike 10.5->11.0 — phantom; ступень 11.0 действует)",
    "UPDATE dkp.decision SET rate_prev=11.00, rate_new=11.00, action='hold', headline_ru='Ключевая ставка: 11.0 -> 11.0%' WHERE decision_id=16 AND rate_prev=10.50 AND rate_new=11.00 AND action='hike'")
sync_graph(16)

# d22 28.10.2016: hold 10.0 (ступень 10.0 eff 19.09; cut до 9.5 не было до 19.12? ladder:
# 10.0 до 18.03.2017; 9.5 eff 19.12.2016 => 28.10 hold 10.0; cut был 16.12.2016)
upd("d22 28.10.2016: hold 10.0 (было cut 10.0->9.5)",
    "UPDATE dkp.decision SET rate_new=10.00, action='hold', headline_ru='Ключевая ставка: 10.0 -> 10.0%' WHERE decision_id=22 AND rate_prev=10.00 AND rate_new=9.50 AND action='cut'")
sync_graph(22)

# d23 16.12.2016: cut 10.0->9.5 (ступень eff 19.12, лаг 3д) — уже исправлено ранее
cur.execute("SELECT rate_prev::float, rate_new::float, action FROM dkp.decision WHERE decision_id=23")
r = cur.fetchone()
log.append("d23 state: %s" % (r,))
if r[2] == 'hold':
    upd("d23: cut 10.0->9.5", "UPDATE dkp.decision SET action='cut' WHERE decision_id=23 AND action='hold'")
sync_graph(23)

# d109 09.06.2017: cut 9.25->9.0 (ступень eff 19.06, лаг 10д — внеплановое? ФАКТ:
# 09.06.2017 плановое cut до 9.0 с 19.06 — лаг 10д, вне окна 0-4)
# => значение верно, лаг документируем (легитимный)
log.append("d109: значения верны, лаг 10д документирован")

# d27 28.07.2017: cut 9.0->8.5 (ступень eff 18.09?? ladder: 9.0 до 17.09, 8.5 eff 18.09!)
# ФАКТ: 28.07.2017 hold 9.0; cut до 8.5 был 15.09.2017 (ступень 18.09)
upd("d27 28.07.2017: hold 9.0 (было cut 9.0->8.5; ступень 8.5 только с 18.09)",
    "UPDATE dkp.decision SET rate_new=9.00, action='hold', headline_ru='Ключевая ставка: 9.0 -> 9.0%' WHERE decision_id=27 AND rate_prev=9.00 AND rate_new=8.50 AND action='cut'")
sync_graph(27)

# d53 19.02.2021: hike 4.25->4.5, ступень 4.5 eff 22.03?? НЕТ: ladder 2021:
# (2020-12-20;2021-02-14;4.25 пропущен в выводе) 4.5 eff 22.03 не может быть —
# 19.02.2021 внеплановое hike до 4.5 (ступень eff 22.02). Ladder grep не показал
# 2021-02 строк — значит ряд начинается 2021-03-22 с 4.5? Значит ступень 4.5 eff ~22.02
# отсутствует в ladder => проверить ряд: вероятно, лестница имела ступень
# 2021-02-22;2021-03-21;4.5, но grep "^2021-0" не дал. => d53 оставляем как есть,
# помечаем needs_source_check для ступени
log.append("d53: hike 4.25->4.5 сохранён; ступень 22.02 в ladder отсутствует — needs_source_check")

for line in log:
    print(" -", line)
conn.close()
print("DONE")