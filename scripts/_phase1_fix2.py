# -*- coding: utf-8 -*-
"""Фаза 1, продолжение: d69/d70, пересадка 63<->64 через temp-meeting, INSERT 4,
rebuild rate_level. Блоки 1-2 (_phase1_fix.py) уже применены и верифицированы."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect, query, execute

conn = connect()
cur = conn.cursor()
log = []

def upd(sql, params, tag):
    cur.execute(sql, params)
    n = cur.rowcount
    conn.commit()
    log.append("%s: %d rows" % (tag, n))
    if n == 0:
        print("[WARN] 0 rows: %s" % tag)

def chk(tag, cond, detail=""):
    if not cond:
        print("[FATAL] %s %s" % (tag, detail))
        sys.exit(1)
    log.append("CHECK OK: %s %s" % (tag, detail))

# ---------- Проверка состояния блоков 1-2 ----------
cur.execute("SELECT rate_prev, rate_new, delta_bp, action FROM dkp.decision WHERE decision_id=92")
r = cur.fetchone()
chk("d92 hold 21", (float(r[0]), float(r[1]), r[2], r[3]) == (21.00, 21.00, 0, 'hold'), str(r))
cur.execute("SELECT rate_prev, rate_new, delta_bp, action FROM dkp.decision WHERE decision_id=93")
r = cur.fetchone()
chk("d93 cut -100 -> 20", (float(r[0]), float(r[1]), r[2], r[3]) == (21.00, 20.00, -100, 'cut'), str(r))

# ---------- Блок 3b. d69 (mid 70, 16.09.2022): hold -> cut -50 -> 7.5 ----------
cur.execute("SELECT rate_prev, rate_new, delta_bp, action FROM dkp.decision WHERE decision_id=69")
r = cur.fetchone()
if (float(r[0]), float(r[1]), r[2], r[3]) == (8.00, 8.00, 0, 'hold'):
    upd("""UPDATE dkp.decision SET rate_prev=8.00, rate_new=7.50, action='cut'
        WHERE decision_id=69 AND rate_prev=8.00 AND rate_new=8.00""", (), "d69 16.09.2022 cut->7.50")
else:
    chk("d69 уже исправлен", (float(r[0]), float(r[1]), r[2], r[3]) == (8.00, 7.50, -50, 'cut'), str(r))

# ---------- Блок 3c. d70 (mid 71, 28.10.2022): cut -> hold 7.5 ----------
cur.execute("SELECT rate_prev, rate_new, delta_bp, action FROM dkp.decision WHERE decision_id=70")
r = cur.fetchone()
if (float(r[0]), float(r[1]), r[2], r[3]) == (8.00, 7.50, -50, 'cut'):
    upd("""UPDATE dkp.decision SET rate_prev=7.50, rate_new=7.50, action='hold'
        WHERE decision_id=70 AND rate_prev=8.00 AND rate_new=7.50""", (), "d70 28.10.2022 hold 7.50")
else:
    chk("d70 уже исправлен", (float(r[0]), float(r[1]), r[2], r[3]) == (7.50, 7.50, 0, 'hold'), str(r))

# ---------- Блок 4b. Пересадка дат через temp meeting ----------
# d62 (экстренное 9.5->20) mid 63 -> 64; d63 (hold 20) mid 64 -> 63
cur.execute("SELECT meeting_id FROM dkp.decision WHERE decision_id IN (62,63) ORDER BY decision_id")
mids = tuple(r[0] for r in cur.fetchall())
conn.commit()
if mids == (63, 64):
    # потомков нет (проверено) — но перестрахуемся
    cur.execute("SELECT count(*) FROM dkp.statement WHERE meeting_id IN (63,64)")
    chk("no stmts 63/64", cur.fetchone()[0] == 0)
    cur.execute("SELECT count(*) FROM dkp.minutes WHERE meeting_id IN (63,64)")
    chk("no minutes 63/64", cur.fetchone()[0] == 0)
    cur.execute("SELECT count(*) FROM dkp.forecast WHERE meeting_id IN (63,64)")
    chk("no forecasts 63/64", cur.fetchone()[0] == 0)
    cur.execute("SELECT count(*) FROM dkp.dissent WHERE meeting_id IN (63,64)")
    chk("no dissents 63/64", cur.fetchone()[0] == 0)
    conn.commit()

    # 1) temp-строка meeting
    cur.execute("""INSERT INTO dkp.meeting (meeting_date, decision_kind, is_pillar, notes)
        VALUES ('1970-01-01', 'scheduled', false, 'TEMP: peresadka dat 2022-02') RETURNING meeting_id""")
    tmp_mid = cur.fetchone()[0]
    conn.commit()
    # 2) d62 -> temp
    cur.execute("UPDATE dkp.decision SET meeting_id=%s WHERE decision_id=62", (tmp_mid,))
    conn.commit()
    # 3) d63 -> 63
    cur.execute("UPDATE dkp.decision SET meeting_id=63 WHERE decision_id=63 AND meeting_id=64")
    conn.commit()
    # 4) d62 -> 64
    cur.execute("UPDATE dkp.decision SET meeting_id=64 WHERE decision_id=62 AND meeting_id=%s", (tmp_mid,))
    conn.commit()
    # 5) temp удалить
    cur.execute("DELETE FROM dkp.meeting WHERE meeting_id=%s", (tmp_mid,))
    conn.commit()
    log.append("пересадка: d62 -> mid 64 (18.02 экстренное), d63 -> mid 63 (14.02 hold)")

    # ярлыки заседаний
    upd("UPDATE dkp.meeting SET decision_kind='scheduled', notes=%s WHERE meeting_id=63 AND decision_kind='unscheduled'",
        ("запланированное заседание; фактический hold 9.5% — экстренное решение принято 28.02.2022 (см. meeting с датой 28.02)",),
        "meeting 63 -> scheduled")
    upd("UPDATE dkp.meeting SET decision_kind='unscheduled', notes=%s WHERE meeting_id=64 AND decision_kind='scheduled'",
        ("внеплановое экстренное заседание: ставка 9.5->20.0% [needs_source_check]",),
        "meeting 64 -> unscheduled экстренное")
else:
    chk("пересадка уже сделана", mids == (64, 63), str(mids))

# ---------- Блок 5. INSERT 4 внеплановых ----------
def insert_meeting_decision(mdate, decision_kind, note, rprev, rnew, action, headline):
    cur.execute("SELECT meeting_id FROM dkp.meeting WHERE meeting_date=%s", (mdate,))
    if cur.fetchall():
        conn.commit()
        log.append("meeting %s уже существует" % mdate)
        return
    cur.execute("""INSERT INTO dkp.meeting (meeting_date, decision_kind, is_pillar, notes)
        VALUES (%s, %s, %s, %s) RETURNING meeting_id""", (mdate, decision_kind, False, note))
    mid = cur.fetchone()[0]
    cur.execute("""INSERT INTO dkp.decision (meeting_id, rate_prev, rate_new, action, headline_ru, source_id)
        VALUES (%s, %s, %s, %s, %s, 2) RETURNING decision_id""", (mid, rprev, rnew, action, headline))
    did = cur.fetchone()[0]
    conn.commit()
    log.append("INSERT %s: mid %d, decision %d (%s %s->%s)" % (mdate, mid, did, action, rprev, rnew))

insert_meeting_decision('2014-12-12', 'unscheduled',
    'внеплановое: валютный кризис; ставка 9.5->10.5% [needs_source_check]',
    9.50, 10.50, 'hike', 'Ключевая ставка: 9.5 -> 10.5%')
insert_meeting_decision('2022-02-28', 'unscheduled',
    'внеплановое экстренное: геополитический кризис; ставка 9.5->20.0% [needs_source_check]',
    9.50, 20.00, 'hike', 'Ключевая ставка: 9.5 -> 20.0%')
insert_meeting_decision('2022-05-26', 'unscheduled',
    'внеплановое: ставка 14.0->11.0% [needs_source_check]',
    14.00, 11.00, 'cut', 'Ключевая ставка: 14.0 -> 11.0%')
insert_meeting_decision('2023-08-15', 'unscheduled',
    'внеплановое: ставка 8.5->12.0% (+350 б.п.) [needs_source_check]',
    8.50, 12.00, 'hike', 'Ключевая ставка: 8.5 -> 12.0%')

# ---------- Блок 6. rebuild rate_level ----------
cur.execute("SELECT count(*) FROM dkp.rate_level")
old_levels = cur.fetchone()[0]
conn.commit()

cur.execute("SELECT decision_id, m.meeting_date::text FROM dkp.decision d JOIN dkp.meeting m ON m.meeting_id=d.meeting_id ORDER BY m.meeting_date")
dec_by_date = [(r[0], r[1]) for r in cur.fetchall()]
conn.commit()

import datetime
def find_decision_for_level(eff_from):
    ed = datetime.date.fromisoformat(eff_from)
    best = None
    for did, md in dec_by_date:
        d = datetime.date.fromisoformat(md)
        lag = (ed - d).days
        if 0 <= lag <= 4:
            if best is None or lag < best[1]:
                best = (did, lag)
    return best[0] if best else None

ladder = []
with open("/tmp/keyrate_ladder.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        frm = parts[0]
        to = parts[1] if len(parts) > 1 and parts[1] else None
        val = float(parts[2])
        ladder.append((frm, to, val))
assert len(ladder) == 66, "ожидалось 66 ступеней, получено %d" % len(ladder)

cur.execute("TRUNCATE dkp.rate_level RESTART IDENTITY")
conn.commit()
log.append("TRUNCATE dkp.rate_level (было %d)" % old_levels)

inserted = 0
null_fk = 0
for frm, to, val in ladder:
    did = find_decision_for_level(frm)
    if did is None:
        null_fk += 1
    cur.execute("""INSERT INTO dkp.rate_level
        (decision_id, rate_code, rate_group, value, annualized, effective_from, effective_to, source_id)
        VALUES (%s, 'key_rate', 'key', %s, true, %s, %s, 2)""", (did, val, frm, to))
    inserted += 1
conn.commit()
log.append("INSERT %d ступеней; без FK-решения: %d" % (inserted, null_fk))

# ---------- Отчёт ----------
print("ИТОГ:")
for line in log:
    print(" -", line)