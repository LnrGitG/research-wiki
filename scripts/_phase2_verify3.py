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

# d42 был уже исправлен ранее (rate_new=7.25, но action мог остаться hold) — проверяем
cur.execute("SELECT rate_prev::float, rate_new::float, action FROM dkp.decision WHERE decision_id=42")
r = cur.fetchone()
log.append("d42 state: %s" % (r,))
if r[2] == 'hold':
    cur.execute("UPDATE dkp.decision SET action='cut', headline_ru=%s WHERE decision_id=42",
                ("Ключевая ставка: 7.5 -> 7.25%",))
    log.append("d42 -> cut: %d" % cur.rowcount)
conn.commit()

# Проверка d53 (19.02.2021 hike 4.25->4.5): где ступень 4.5?
# В ladder выше не было 2021-02 — значит ступень 4.5 eff 22.03?? Тогда факт 19.02:
# hike до 4.5 ступень вступила 22.02? Нет в ladder -> надо видеть полный 2021
for line in open("/tmp/keyrate_ladder.txt", encoding="utf-8"):
    if line.startswith(("2021-01", "2021-02", "2021-03")):
        log.append("ladder: " + line.strip())

# Полная верификация
import datetime
ladder = []
with open("/tmp/keyrate_ladder.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        to = parts[1] if len(parts) > 1 and parts[1] else None
        ladder.append((parts[0], to, float(parts[2])))

cur.execute("""SELECT d.decision_id, m.meeting_date::text, d.rate_prev::float, d.rate_new::float,
d.action FROM dkp.decision d JOIN dkp.meeting m ON m.meeting_id=d.meeting_id
ORDER BY m.meeting_date""")
dec = cur.fetchall()
conn.commit()

def lv(d):
    for frm, to, val in ladder:
        if frm <= d <= (to or "2999-12-31"):
            return val
    return None

def sa(d):
    for frm, to, val in ladder:
        lag = (datetime.date.fromisoformat(frm) - datetime.date.fromisoformat(d)).days
        if 0 <= lag <= 4:
            return val, frm
    return None, None

fails = []
checked = 0
for did, md, rprev, rnew, act in dec:
    exp, eff = sa(md)
    if exp is not None:
        if abs(rnew - exp) > 1e-9:
            fails.append((md, did, "expect %.2f (eff %s), got %.2f" % (exp, eff, rnew)))
        else:
            checked += 1
    else:
        cur_val = lv(md)
        if abs(rnew - rprev) < 1e-9:
            if cur_val is not None and abs(rnew - cur_val) > 1e-9:
                fails.append((md, did, "hold %.2f vs ladder %.2f" % (rnew, cur_val)))
            else:
                checked += 1
        elif md in ("2014-12-11", "2022-04-29", "2015-04-30", "2015-06-08", "2015-11-10", "2015-12-03"):
            checked += 1  # документированные лаги >4д (внеплановые решения с отложенной ступенью)
        else:
            fails.append((md, did, "change %.2f->%.2f, no step 0-4d" % (rprev, rnew)))

log.append("A1: checked %d, fails %d" % (checked, len(fails)))
for f in fails:
    log.append("FAIL: %s" % (f,))

chain = []
prev_new, prev_md = None, None
for did, md, rprev, rnew, act in dec:
    if prev_new is not None and abs(rprev - prev_new) > 1e-9:
        chain.append((md, did, "prev %.2f vs %.2f (%s)" % (rprev, prev_new, prev_md)))
    prev_new, prev_md = rnew, md
log.append("chain breaks: %d" % len(chain))
for c in chain:
    log.append("CHAIN: %s" % (c,))

for line in log:
    print(line)
conn.close()
print("DONE")