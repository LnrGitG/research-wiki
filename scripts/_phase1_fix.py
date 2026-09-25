# -*- coding: utf-8 -*-
"""Фаза 1 ремонта лестницы dkp: UPDATE/INSERT решений + перестройка rate_level.

Источники: тела пресс-релизов dkp.statement (первоисточник 1),
дневной ряд hd_base /tmp/keyrate_ladder.txt (первоисточник 2, 66 ступеней).
Точка возврата: backups/dkp_pre_ladder_fix_20260925.sql (коммит 8acbfe1).
Идемпотентен: INSERT INSERT-only, UPDATE-условия по значению.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect, query, execute

conn = connect()
cur = conn.cursor()
log = []

def upd(sql, tag):
    cur.execute(sql)
    n = cur.rowcount
    conn.commit()
    log.append("%s: %d rows" % (tag, n))
    if n == 0:
        print("[WARN] 0 rows: %s" % tag)

# ============================================================
# Блок 1. Цепочка 2025-12 ... 2026-07 (decision 97..103, mid 98..104)
# Хроника по релизам и ряду (проверено в 2dc837e):
#   19.12.2025 cut -50 -> 16.00 (эфф. 22.12)
#   13.02.2026 cut -50 -> 15.50 (эфф. 16.02)
#   20.03.2026 cut -50 -> 15.00 (эфф. 23.03)
#   24.04.2026 cut -50 -> 14.50 (эфф. 27.04)
#   19.06.2026 cut -25 -> 14.25 (эфф. 22.06)
#   24.07.2026 cut -25 -> 14.00 (эфф. 27.07)
#   11.09.2026 hold 14.00
# ============================================================

upd("""UPDATE dkp.decision SET rate_prev=16.50, rate_new=16.00, action='cut'
WHERE decision_id=97 AND rate_prev=16.50 AND rate_new=16.50 AND delta_bp=0""", "d97 19.12.2025 cut->16.00")

upd("""UPDATE dkp.decision SET rate_prev=16.00, rate_new=15.50, action='cut'
WHERE decision_id=98 AND rate_prev=16.50 AND rate_new=16.50 AND delta_bp=0""", "d98 13.02.2026 cut->15.50")

upd("""UPDATE dkp.decision SET rate_prev=15.50, rate_new=15.00, action='cut'
WHERE decision_id=99 AND rate_prev=16.50 AND rate_new=16.50 AND delta_bp=0""", "d99 20.03.2026 cut->15.00")

upd("""UPDATE dkp.decision SET rate_prev=15.00, rate_new=14.50, action='cut', signal_kind=NULL
WHERE decision_id=100 AND rate_prev=16.50 AND rate_new=15.00 AND delta_bp=-150""", "d100 24.04.2026 cut->14.50 (-150->-50)")

upd("""UPDATE dkp.decision SET rate_prev=14.50, rate_new=14.00, action='cut'
WHERE decision_id=102 AND rate_prev=14.00 AND rate_new=14.00 AND delta_bp=0""", "d102 24.07.2026 cut->14.00")

# d101 (19.06.2026) уже верно: 14.50->14.25 -25 cut — проверяем
cur.execute("""SELECT rate_prev, rate_new, delta_bp, action FROM dkp.decision WHERE decision_id=101""")
r = cur.fetchall()[0]
assert (float(r[0]), float(r[1]), r[2], r[3]) == (14.50, 14.25, -25, 'cut'), "d101 неожиданно изменён: %s" % r
log.append("d101 проверен без изменений (14.50->14.25 -25 cut)")
conn.commit()

# ============================================================
# Блок 2. 2025-04-25 / 2025-06-06: решения 92/93 перепутаны
# Факт: 25.04.2025 hold 21.00 (эфф. ступень 21.0 до 08.06);
#       06.06.2025 cut -100 -> 20.00 (эфф. 09.06)
# В БД: d92 (25.04) cut -100 -> 20.00; d93 (06.06) hold 20.00
# ============================================================

upd("""UPDATE dkp.decision SET rate_prev=21.00, rate_new=21.00, action='hold'
WHERE decision_id=92 AND rate_prev=21.00 AND rate_new=20.00 AND delta_bp=-100""", "d92 25.04.2025 -> hold 21.00")

upd("""UPDATE dkp.decision SET rate_prev=21.00, rate_new=20.00, action='cut'
WHERE decision_id=93 AND rate_prev=20.00 AND rate_new=20.00 AND delta_bp=0""", "d93 06.06.2025 -> cut -100 -> 20.00")

# ============================================================
# Блок 3. 2022-09/10: 16.09.2022 cut -50 -> 7.50 (эфф. 19.09);
#         28.10.2022 hold 7.50
# ============================================================

upd("""UPDATE dkp.decision SET rate_prev=8.00, rate_new=7.50, action='cut'
WHERE decision_id=69 AND meeting_id=69 AND rate_prev=8.00 AND rate_new=8.00 AND delta_bp=0""", "d69 16.09.2022 cut->7.50")

upd("""UPDATE dkp.decision SET rate_prev=7.50, rate_new=7.50, action='hold'
WHERE decision_id=70 AND meeting_id=70 AND rate_prev=8.00 AND rate_new=7.50 AND delta_bp=-50""", "d70 28.10.2022 hold 7.50")

# ============================================================
# Блок 4. 2022-02: пересадка дат (meeting 63 -> 64; meeting 64 -> 63)
# d62 (mid 63, 14.02): экстренное 9.50->20.00 -> к mid 64 (18.02)
# d63 (mid 64, 18.02): hold 20->20 -> к mid 63 (14.02)
# Потомков FK нет (проверено _phase1_facts.py: 0 stmts/mins/args/fcts)
# ============================================================

cur.execute("SELECT meeting_id FROM dkp.statement WHERE meeting_id IN (63,64)")
assert not cur.fetchall(), "у заседаний 63/64 появились потомки — пересадку отменить"
cur.execute("SELECT meeting_id FROM dkp.minutes WHERE meeting_id IN (63,64)")
assert not cur.fetchall(), "minutes у 63/64 появились — отменить"
conn.commit()

upd("""UPDATE dkp.decision SET meeting_id=64 WHERE decision_id=62 AND meeting_id=63""", "d62 (экстренное 9.5->20) mid 63->64 (18.02)")
upd("""UPDATE dkp.decision SET meeting_id=63 WHERE decision_id=63 AND meeting_id=64""", "d63 (hold 20) mid 64->63 (14.02)")

# Ярлыки заседаний: 63 (14.02) = hold (регулярный цикл продолжался до 28.02),
# 64 (18.02) = внеплановое экстренное
upd("""UPDATE dkp.meeting SET decision_kind='scheduled', notes='запланированное заседание; фактический hold 9.5% — экстренное решение принято 28.02.2022 (см. meeting 64)'
WHERE meeting_id=63 AND decision_kind='unscheduled'""", "meeting 63 14.02 scheduled")
upd("""UPDATE dkp.meeting SET decision_kind='unscheduled', notes='внеплановое экстренное заседание: ставка 9.5->20.0% [needs_source_check]'
WHERE meeting_id=64 AND decision_kind='scheduled'""", "meeting 64 18.02 unscheduled экстренное")

# ============================================================
# Блок 5. INSERT 4 отсутствующих внеплановых заседаний с решениями
# 12.12.2014 (9.5->10.5, решение 12.12, эфф. там же в ряду),
# 28.02.2022 (9.5->20.0, экстренное),
# 26.05.2022 (14.0->11.0), 15.08.2023 (8.5->12.0, -350)
# ============================================================

def insert_meeting_decision(mdate, decision_kind, note, rprev, rnew, delta, action, headline=None):
    cur.execute("""SELECT meeting_id FROM dkp.meeting WHERE meeting_date=%s""", (mdate,))
    if cur.fetchall():
        log.append("meeting %s уже существует — пропущен" % mdate)
        conn.commit()
        return None
    cur.execute("""INSERT INTO dkp.meeting (meeting_date, decision_kind, is_pillar, notes)
        VALUES (%s, %s, %s, %s) RETURNING meeting_id""",
        (mdate, decision_kind, False, note))
    mid = cur.fetchone()[0]
    cur.execute("""INSERT INTO dkp.decision (meeting_id, rate_prev, rate_new, action, headline_ru, source_id)
        VALUES (%s, %s, %s, %s, %s, 2) RETURNING decision_id""",
        (mid, rprev, rnew, action, headline or "Ключевая ставка: %s -> %s%%" % (rprev, rnew)))
    did = cur.fetchone()[0]
    conn.commit()
    log.append("INSERT meeting %s (mid %d) + decision %d (%s %s->%s)" % (mdate, mid, did, action, rprev, rnew))
    return mid, did

r12 = insert_meeting_decision('2014-12-12', 'unscheduled',
    'внеплановое: валютный кризис; ставка 9.5->10.5% [needs_source_check]',
    9.50, 10.50, 100, 'hike',
    'Ключевая ставка: 9.5 -> 10.5%')
r28 = insert_meeting_decision('2022-02-28', 'unscheduled',
    'внеплановое экстренное: геополитический кризис; ставка 9.5->20.0% [needs_source_check]',
    9.50, 20.00, 1050, 'hike',
    'Ключевая ставка: 9.5 -> 20.0%')
r26 = insert_meeting_decision('2022-05-26', 'unscheduled',
    'внеплановое: ставка 14.0->11.0% [needs_source_check]',
    14.00, 11.00, -300, 'cut',
    'Ключевая ставка: 14.0 -> 11.0%')
r15 = insert_meeting_decision('2023-08-15', 'unscheduled',
    'внеплановое: ставка 8.5->12.0% (+350 б.п.) [needs_source_check]',
    8.50, 12.00, 350, 'hike',
    'Ключевая ставка: 8.5 -> 12.0%')

# ============================================================
# Блок 6. dkp.rate_level — полный rebuild из 66 ступеней дневного ряда
# ============================================================

cur.execute("SELECT count(*) FROM dkp.rate_level")
old_levels = cur.fetchone()[0]
conn.commit()

# Сохранить маппинг level_id -> decision_id для восстановления FK
cur.execute("SELECT level_id, decision_id FROM dkp.rate_level")
old_map = dict(cur.fetchall())
conn.commit()

ladder = []
with open("/tmp/keyrate_ladder.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        frm = parts[0]
        to = parts[1] if len(parts) > 1 and parts[1] else None
        val = float(parts[2])
        ladder.append((frm, to, val))

assert len(ladder) == 66, "ожидалось 66 ступеней, получено %d" % len(ladder)

# Маппинг ступень -> решение: по effective_from в окне даты заседания +/-1 день
# (конвенция БД: ступень вступает на следующий день после объявления)
cur.execute("""SELECT d.decision_id, m.meeting_date::text FROM dkp.decision d
JOIN dkp.meeting m ON m.meeting_id=d.meeting_id ORDER BY m.meeting_date""")
dec_by_date = [(r[0], r[1]) for r in cur.fetchall()]
conn.commit()

def find_decision_for_level(eff_from):
    """Решение, объявление которого предшествует effective_from (в окне 0-4 дней)."""
    eff = eff_from  # 'YYYY-MM-DD'
    import datetime
    ed = datetime.date.fromisoformat(eff)
    best = None
    for did, md in dec_by_date:
        d = datetime.date.fromisoformat(md)
        lag = (ed - d).days
        if 0 <= lag <= 4:
            if best is None or lag < best[1]:
                best = (did, lag)
    return best[0] if best else None

cur.execute("TRUNCATE dkp.rate_level RESTART IDENTITY CASCADE")
conn.commit()
log.append("TRUNCATE dkp.rate_level (было %d строк)" % old_levels)

inserted = 0
for frm, to, val in ladder:
    did = find_decision_for_level(frm)
    cur.execute("""INSERT INTO dkp.rate_level
        (decision_id, rate_code, rate_group, value, annualized, effective_from, effective_to, source_id)
        VALUES (%s, 'key_rate', 'key', %s, true, %s, %s, 2)""", (did, val, frm, to))
    inserted += 1
conn.commit()
log.append("INSERT %d ступеней (FK decision_id по окну 0-4 дней)" % inserted)

# Верификация FK
cur.execute("""SELECT count(*) FROM dkp.rate_level r
LEFT JOIN dkp.decision d ON d.decision_id=r.decision_id
WHERE r.decision_id IS NOT NULL AND d.decision_id IS NULL""")
orph = cur.fetchone()[0]
cur.execute("SELECT count(*) FROM dkp.rate_level WHERE decision_id IS NULL")
nulls = cur.fetchone()[0]
conn.commit()
log.append("FK check: orphan=%d, decision_id NULL=%d" % (orph, nulls))

# ============================================================
# Отчёт
# ============================================================
print("ИТОГ фазы 1:")
for line in log:
    print(" -", line)
print()
print("Ожидаемое число решений: 107 (103 + 4 INSERT)")