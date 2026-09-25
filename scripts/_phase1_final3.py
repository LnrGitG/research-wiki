# -*- coding: utf-8 -*-
"""Фаза 1, финализация v3: значения 2022-2023 против лестницы + фантом 14.02.2022.

Основания (два первоисточника: лестница hd_base + аудит-записка 2dc837e):
- 18.02.2022 (mid 64, d62): факт hold 9.5 (аудит: экстренное было 28.02)
- 14.02.2022 (mid 63): фантом — заседания не было (день вступления решения 11.02)
- 09.06.2023 (mid 77, d76): факт hold 7.5 (аудит класс 3; ступень 8.5 eff 24.07)
- 21.07.2023 (mid 78, d77): факт hike +100 7.5->8.5 (аудит)
- 10.06.2022 (mid 68, d67): prev 11.0 (после cut 26.05)
- 16.12.2014 (d8): prev 10.5 (после hike 11.12 -> 10.5)
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect

conn = connect()
cur = conn.cursor()
log = []

def upd(tag, sql, params=None):
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    log.append("%s: %d" % (tag, cur.rowcount))
    conn.commit()

# ---------- 0. FK-поведение rate_level.decision_id ----------
cur.execute("SELECT confdeltype FROM pg_constraint WHERE conname='rate_level_decision_id_fkey'")
fk_del = cur.fetchone()[0]  # n=NO ACTION, s=SET NULL, r=RESTRICT, c=CASCADE
log.append("rate_level FK on delete: %s" % fk_del)
conn.commit()

# ---------- 1. d62 (18.02.2022): 9.5->20 hike => hold 9.5 ----------
upd("d62 hold 9.5",
    """UPDATE dkp.decision SET rate_prev=9.50, rate_new=9.50, action='hold',
    headline_ru='Ключевая ставка: 9.5 -> 9.5%'
    WHERE decision_id=62 AND rate_prev=9.50 AND rate_new=20.00""")

# ---------- 2. Фантом mid 63 (14.02.2022): удалить решение и заседание ----------
# Сначала граф: рёбра, затем узлы
cur.execute("""SELECT n.node_id FROM graph.node n WHERE n.node_type='cbr_decision' AND n.ref_key='decision:63'""")
dr = cur.fetchall()
cur.execute("""SELECT n.node_id FROM graph.node n WHERE n.node_type='cbr_meeting' AND n.ref_key='meeting:63'""")
mr = cur.fetchall()
if dr or mr:
    ids = [r[0] for r in (dr + mr)]
    fmt = ",".join("%d" % i for i in ids)
    cur.execute("DELETE FROM graph.edge WHERE src_id IN (%s) OR dst_id IN (%s)" % (fmt, fmt))
    log.append("graph edges (fanout 63): %d" % cur.rowcount)
    cur.execute("DELETE FROM graph.node WHERE node_id IN (%s)" % fmt)
    log.append("graph nodes 63: %d" % cur.rowcount)
conn.commit()

# rate_level: ступень 9.5 eff 2022-02-14 -> decision 61 (11.02)
upd("level 14.02 -> decision 61",
    """UPDATE dkp.rate_level SET decision_id=61
    WHERE decision_id=63 AND value=9.50 AND effective_from='2022-02-14'""")

upd("DELETE decision 63", "DELETE FROM dkp.decision WHERE decision_id=63")
upd("DELETE meeting 63", "DELETE FROM dkp.meeting WHERE meeting_id=63")

# ---------- 3. d76 (09.06.2023): 7.5->9.0 hike => hold 7.5 ----------
upd("d76 hold 7.5",
    """UPDATE dkp.decision SET rate_prev=7.50, rate_new=7.50, action='hold',
    headline_ru='Ключевая ставка: 7.5 -> 7.5%'
    WHERE decision_id=76 AND rate_prev=7.50 AND rate_new=9.00""")

# ---------- 4. d77 (21.07.2023): 9->8.5 cut => hike 7.5->8.5 ----------
upd("d77 hike 7.5->8.5",
    """UPDATE dkp.decision SET rate_prev=7.50, rate_new=8.50, action='hike',
    headline_ru='Ключевая ставка: 7.5 -> 8.5%'
    WHERE decision_id=77 AND rate_prev=9.00 AND rate_new=8.50""")

# ---------- 5. d67 (10.06.2022): prev 14 => 11 ----------
upd("d67 prev 11.0",
    """UPDATE dkp.decision SET rate_prev=11.00,
    headline_ru='Ключевая ставка: 11.0 -> 9.5%'
    WHERE decision_id=67 AND rate_prev=14.00 AND rate_new=9.50""")

# ---------- 6. d66 (29.04.2022): headline ----------
upd("d66 headline",
    """UPDATE dkp.decision SET headline_ru='Ключевая ставка: 17.0 -> 14.0%'
    WHERE decision_id=66""")

# ---------- 7. d8 (16.12.2014): prev 9.5 => 10.5 ----------
upd("d8 prev 10.5",
    """UPDATE dkp.decision SET rate_prev=10.50
    WHERE decision_id=8 AND rate_prev=9.50 AND rate_new=17.00""")

# ---------- 8. Граф: синхронизация значений ----------
for did in (62, 76, 77, 67, 66, 8):
    cur.execute("""SELECT action, rate_prev::float, rate_new::float, meeting_id
    FROM dkp.decision WHERE decision_id=%s""", (did,))
    action, rprev, rnew, mid = cur.fetchone()
    props = json.dumps({"meeting_id": mid, "action": action, "rate_prev": rprev, "rate_new": rnew}, ensure_ascii=False)
    title = "Решение %s: %s" % (mid, action)
    cur.execute("""UPDATE graph.node SET title=%s, props=%s::jsonb
    WHERE node_type='cbr_decision' AND ref_key=%s""", (title, props, "decision:%d" % did))
conn.commit()
log.append("graph: 6 decision-узлов синхронизировано")

# ---------- 9. follows: пересборка ----------
cur.execute("DELETE FROM graph.edge WHERE edge_type='follows'")
conn.commit()
cur.execute("""SELECT d.decision_id, n.node_id FROM dkp.decision d
JOIN dkp.meeting m ON m.meeting_id=d.meeting_id
JOIN graph.node n ON n.node_type='cbr_decision' AND n.ref_key='decision:' || d.decision_id
ORDER BY m.meeting_date""")
dseq = cur.fetchall()
n_fl = 0
for i in range(1, len(dseq)):
    cur.execute("""INSERT INTO graph.edge (src_id, dst_id, edge_type, provenance)
    VALUES (%s, %s, 'follows', %s::jsonb) ON CONFLICT DO NOTHING""",
        (dseq[i][1], dseq[i-1][1], json.dumps({"rule": "prev meeting chronology"})))
    n_fl += cur.rowcount
conn.commit()
log.append("follows rebuilt: %d (%d решений)" % (n_fl, len(dseq)))

for line in log:
    print(" -", line)
conn.close()