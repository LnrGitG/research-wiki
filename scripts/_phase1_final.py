# -*- coding: utf-8 -*-
"""Фаза 1, финализация БД: headline_ru, дата mid 106, снятие флагов, граф-синхронизация."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect

conn = connect()
cur = conn.cursor()
log = []

# ---------- 1. headline_ru из тел релизов (первоисточник) ----------
HEADLINES = {
    97: ("Банк России снизил ключевую ставку на 50 б.п., до 16,00% годовых", "2025-12-19"),
    98: ("Банк России снизил ключевую ставку на 50 б.п., до 15,50% годовых", "2026-02-13"),
    99: ("Банк России снизил ключевую ставку на 50 б.п., до 15,00% годовых", "2026-03-20"),
    100: ("Банк России снизил ключевую ставку на 50 б.п., до 14,50% годовых", "2026-04-24"),
    102: ("Банк России снизил ключевую ставку на 25 б.п., до 14,00% годовых", "2026-07-24"),
    92: ("Банк России сохранил ключевую ставку на уровне 21,00% годовых", "2025-04-25"),
    93: ("Банк России снизил ключевую ставку на 100 б.п., до 20,00% годовых", "2025-06-06"),
    69: ("Банк России снизил ключевую ставку на 50 б.п., до 7,50% годовых", "2022-09-16"),
    70: ("Банк России сохранил ключевую ставку на уровне 7,50% годовых", "2022-10-28"),
}
for did, (head, mdate) in HEADLINES.items():
    cur.execute("UPDATE dkp.decision SET headline_ru=%s WHERE decision_id=%s", (head, did))
    log.append("headline d%d: %d" % (did, cur.rowcount))
conn.commit()

# ---------- 2. mid 106: дата решения 11.12.2014 (ступень с 12.12) ----------
cur.execute("UPDATE dkp.meeting SET meeting_date='2014-12-11', notes=%s "
            "WHERE meeting_id=106 AND meeting_date='2014-12-12'",
            ("внеплановое: валютный кризис (решение 11.12, ступень с 12.12); ставка 9.5->10.5%",))
log.append("mid 106 date 12.12->11.12: %d" % cur.rowcount)
conn.commit()

# ---------- 3. Снятие [needs_source_check] с верифицированных заседаний ----------
VERIFIED = [63, 64, 70, 71, 93, 94, 98, 99, 100, 101, 102, 103, 104, 106, 107, 108, 109]
cur.execute("""SELECT meeting_id, notes FROM dkp.meeting
WHERE meeting_id = ANY(%s) AND notes ILIKE '%%needs_source_check%%'""", (VERIFIED,))
rows = cur.fetchall()
for mid, notes in rows:
    new_notes = notes.replace(" [needs_source_check]", "").replace("[needs_source_check]", "").strip()
    cur.execute("UPDATE dkp.meeting SET notes=%s WHERE meeting_id=%s", (new_notes, mid))
conn.commit()
log.append("needs_source_check снят с %d заседаний" % len(rows))

# ---------- 4. Граф: title/props изменённых решений ----------
for did, (head, mdate) in HEADLINES.items():
    cur.execute("""SELECT d.action, d.rate_prev::float, d.rate_new::float, d.meeting_id
    FROM dkp.decision d WHERE decision_id=%s""", (did,))
    action, rprev, rnew, mid = cur.fetchone()
    import json
    props = json.dumps({"meeting_id": mid, "action": action, "rate_prev": rprev, "rate_new": rnew}, ensure_ascii=False)
    title = "Решение %s: %s" % (mid, action)
    cur.execute("""UPDATE graph.node SET title=%s, props=%s::jsonb
    WHERE node_type='cbr_decision' AND ref_key=%s""", (title, props, "decision:%d" % did))
    log.append("graph node decision:%d -> %d" % (did, cur.rowcount))
conn.commit()

# ---------- 5. mid 106 дата в узле meeting ----------
cur.execute("""UPDATE graph.node SET title='Заседание СД 2014-12-11',
props = jsonb_set(jsonb_set(props, '{meeting_date}', '"2014-12-11"'), '{decision_kind}', '"unscheduled"')
WHERE node_type='cbr_meeting' AND ref_key='meeting:106'""")
log.append("graph meeting:106: %d" % cur.rowcount)
conn.commit()

# ---------- 6. follows: пересборка в хронологии meeting_date ----------
cur.execute("DELETE FROM graph.edge WHERE edge_type='follows'")
log.append("follows deleted: %d" % cur.rowcount)
conn.commit()
cur.execute("""SELECT d.decision_id, n.node_id FROM dkp.decision d
JOIN dkp.meeting m ON m.meeting_id=d.meeting_id
JOIN graph.node n ON n.node_type='cbr_decision' AND n.ref_key='decision:' || d.decision_id
ORDER BY m.meeting_date""")
dseq = cur.fetchall()
import json
n_fl = 0
for i in range(1, len(dseq)):
    cur.execute("""INSERT INTO graph.edge (src_id, dst_id, edge_type, provenance)
    VALUES (%s, %s, 'follows', %s::jsonb) ON CONFLICT DO NOTHING""",
        (dseq[i][1], dseq[i-1][1], json.dumps({"rule": "prev meeting chronology"})))
    n_fl += cur.rowcount
conn.commit()
log.append("follows rebuilt: %d (%d решений по хронологии)" % (n_fl, len(dseq)))

# ---------- Отчёт ----------
for line in log:
    print(" -", line)
conn.close()