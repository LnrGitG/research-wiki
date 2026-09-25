# -*- coding: utf-8 -*-
"""Фаза 1, верификация v2: честные критерии приёмки.

Критерии A1/A2 в интерпретации «значения и уровни верны»:
- A1: все решения 2022-2026 имеют верные rate_prev/rate_new/action
      относительно лестницы (hold на неизменной ступени, изменение на
      ступени, вступившей в окне 0-4 дней);
- A2: решений 107;
- цепочка prev[i] == new[i-1] внутри каждой непрерывной фазы
  (список легитимных разрывов: вставленные внеплановые + неразмеченный
  период между класс-3 датами);
- лестница: 0 перекрытий, 66 ступеней.
Класс-3 строки 2013-2021 — вне фазы 1 (фаза 2), в критерии не входят.
"""
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect

conn = connect()
cur = conn.cursor()

ladder = []
with open("/tmp/keyrate_ladder.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        to = parts[1] if len(parts) > 1 and parts[1] else None
        ladder.append((parts[0], to, float(parts[2])))

cur.execute("""SELECT d.decision_id, m.meeting_date::text, d.rate_prev::float, d.rate_new::float,
d.delta_bp, d.action FROM dkp.decision d JOIN dkp.meeting m ON m.meeting_id=d.meeting_id
ORDER BY m.meeting_date""")
dec = cur.fetchall()
conn.commit()

fails = []

# A2
print("A2 (107 решений):", "PASS" if len(dec) == 107 else "FAIL %d" % len(dec))

# Значения против лестницы для каждого решения: ожидаемая ступень на дату решения =
# значение ряда на дату вступления в окне 0-4 дней (изменение) ИЛИ текущее значение
# (hold — ступени не менялись на дату решения).
def ladder_value_on(date_iso):
    d = datetime.date.fromisoformat(date_iso)
    for frm, to, val in ladder:
        fd = datetime.date.fromisoformat(frm)
        td = datetime.date.fromisoformat(to) if to else datetime.date(2999, 12, 31)
        if fd <= d <= td:
            return val
    return None

def expected_after_decision(date_iso):
    """Значение ступени, вступившей в окне 0-4 дней после решения (или None)."""
    d = datetime.date.fromisoformat(date_iso)
    for frm, to, val in ladder:
        lag = (datetime.date.fromisoformat(frm) - d).days
        if 0 <= lag <= 4:
            return val, frm
    return None, None

checked = 0
mismatch = 0
for did, md, rprev, rnew, dbp, act in dec:
    if md < "2022-01-01":
        continue  # класс-3 период — фаза 2
    cur_val = ladder_value_on(md)
    exp_val, exp_frm = expected_after_decision(md)
    if exp_val is not None:
        # изменение должно отразить новую ступень
        if abs(rnew - exp_val) > 1e-9:
            fails.append((md, did, "change expected to %s (eff %s), db rate_new=%s" % (exp_val, exp_frm, rnew)))
            mismatch += 1
        else:
            checked += 1
    else:
        # hold: значение на дату решения = текущая ступень и не меняется
        if abs(rnew - rprev) < 1e-9:
            if cur_val is not None and abs(rnew - cur_val) > 1e-9:
                fails.append((md, did, "hold level %.2f but ladder at %s is %.2f" % (rnew, md, cur_val)))
                mismatch += 1
            else:
                checked += 1
        else:
            # решение изменило ставку, но ступень не вступила в окне 0-4д
            # — допустимо только для известного лага (2014-12-11 уже поправлен)
            if md == "2014-12-11":
                checked += 1
            else:
                fails.append((md, did, "db changed %.2f->%.2f but no ladder step within 0-4d" % (rprev, rnew)))
                mismatch += 1

print("A1 (значения 2022-2026): %d проверено, %d несоответствий" % (checked, mismatch))
for f in fails:
    print("  A1 FAIL:", f)

# Цепочка: разрывы только на легитимных вставках
LEGIT_BREAK_AFTER = {"2014-12-11", "2022-02-14", "2023-08-15"}
chain_breaks = []
prev_new = None
prev_md = None
for did, md, rprev, rnew, dbp, act in dec:
    if prev_new is not None and abs(rprev - prev_new) > 1e-9:
        # prev должен равняться лестнице на prev_md (состояние рынка), а new[i-1] — факту
        chain_breaks.append((md, did, "prev=%.2f prev_meeting=%s prev.new=%.2f" % (rprev, prev_md, prev_new)))
    prev_new, prev_md = rnew, md
print("chain breaks:", len(chain_breaks))
for cb in chain_breaks:
    print("  ", cb)

# Перекрытия
cur.execute("""SELECT count(*) FROM dkp.rate_level a JOIN dkp.rate_level b
ON a.effective_from < b.effective_from AND COALESCE(a.effective_to,'2999-12-31'::date) >= b.effective_from""")
print("перекрытий ступеней:", cur.fetchone()[0])
conn.commit()

cur.execute("SELECT count(*) FROM dkp.rate_level")
print("лестница:", cur.fetchone()[0], "ступеней")
cur.execute("SELECT count(*) FROM graph.node WHERE node_type='cbr_decision'")
print("graph cbr_decision:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM graph.edge WHERE edge_type='follows'")
print("graph follows:", cur.fetchone()[0])
conn.commit()

conn.close()