# -*- coding: utf-8 -*-
"""Фаза 1, финализация v2: значения решений против лестницы (окна 2022/2023)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect

conn = connect()
cur = conn.cursor()
log = []

def upd(tag, sql, params=()):
    cur.execute(sql, params)
    log.append("%s: %d" % (tag, cur.rowcount))
    conn.commit()

# d63 14.02.2022: prev 20->9.5 (14.02 — день вступления 9.5; решение 11.02.2022, 8.5->9.5)
upd("d63 14.02: prev 8.50->9.50",
    """UPDATE dkp.decision SET rate_prev=8.50, rate_new=9.50, action='hike'
    WHERE decision_id=63 AND rate_prev=20.00 AND rate_new=20.00""")

# d66 29.04.2022: 17.00 -> 14.00 (внеплановое; ступень 14.0 с 04.05)
upd("d66 29.04: rate_new 14->11 => 17->14",
    """UPDATE dkp.decision SET rate_prev=17.00, rate_new=14.00
    WHERE decision_id=66 AND rate_prev=17.00 AND rate_new=14.00""")

# d76 09.06.2023: 7.50 -> 9.00 (+200 hike)
upd("d76 09.06.2023: rate_new 9.00 => hike",
    """UPDATE dkp.decision SET action='hike'
    WHERE decision_id=76 AND rate_prev=7.50 AND rate_new=9.00 AND action='cut'""")

# d67 10.06.2022: 14.00 -> 9.50 (cut -450)
upd("d67 10.06.2022: rate_new 9.50 => 14->9.50",
    """UPDATE dkp.decision SET rate_prev=14.00, rate_new=9.50
    WHERE decision_id=67 AND rate_prev=14.00 AND rate_new=9.50""")

# d64 18.03.2022: 20->20 hold — верно (проверить)
cur.execute("SELECT rate_prev, rate_new, action FROM dkp.decision WHERE decision_id=64")
r = cur.fetchone()
assert (float(r[0]), float(r[1]), r[2]) == (20.00, 20.00, 'hold'), "d64: %s" % r
log.append("d64 hold 20 подтверждён")

# d78 15.09.2023: prev 8.5 при лестнице 12.0 -> 12.0 -> 13.0 (+100)
upd("d78 15.09.2023: prev 8.50->12.00",
    """UPDATE dkp.decision SET rate_prev=12.00
    WHERE decision_id=78 AND rate_prev=8.50 AND rate_new=13.00""")

# Граф-синхронизация значений
import json
for did in (63, 66, 76, 78):
    cur.execute("""SELECT d.action, d.rate_prev::float, d.rate_new::float, d.meeting_id
    FROM dkp.decision d WHERE decision_id=%s""", (did,))
    action, rprev, rnew, mid = cur.fetchone()
    props = json.dumps({"meeting_id": mid, "action": action, "rate_prev": rprev, "rate_new": rnew}, ensure_ascii=False)
    title = "Решение %s: %s" % (mid, action)
    cur.execute("""UPDATE graph.node SET title=%s, props=%s::jsonb
    WHERE node_type='cbr_decision' AND ref_key=%s""", (title, props, "decision:%d" % did))
    log.append("graph d%d: %d" % (did, cur.rowcount))
conn.commit()

for line in log:
    print(" -", line)
conn.close()