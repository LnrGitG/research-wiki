import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

conn = connect()
cur = conn.cursor()

# FK на rate_level.decision_id блокирует DELETE — сначала отцепить ступени
# Дубль 2014-12-12 (d108): какую ступень он себе присвоил?
cur.execute("SELECT level_id, value, effective_from::text, decision_id FROM dkp.rate_level WHERE decision_id=108")
print("levels of dup d108:", cur.fetchall())
conn.commit()

# отцепить: ступень 2014-12-12 -> decision 104 (правильное, 11.12)
cur.execute("UPDATE dkp.rate_level SET decision_id=104 WHERE decision_id=108")
print("rebind levels to d104:", cur.rowcount)
conn.commit()

# теперь удалить дубль
cur.execute("DELETE FROM dkp.decision WHERE decision_id=108 AND meeting_id=114")
print("del dup decision 108:", cur.rowcount)
cur.execute("DELETE FROM dkp.meeting WHERE meeting_id=114 AND meeting_date='2014-12-12'")
print("del dup meeting 114:", cur.rowcount)
conn.commit()

# Привязать ступени к вставленным решениям
for mdate, eff in [('2015-04-30', '2015-05-05'), ('2017-06-09', '2017-06-19'), ('2019-12-06', '2019-12-16')]:
    cur.execute("SELECT d.decision_id FROM dkp.meeting m JOIN dkp.decision d USING(meeting_id) WHERE m.meeting_date=%s", (mdate,))
    r = cur.fetchall()
    if r:
        cur.execute("UPDATE dkp.rate_level SET decision_id=%s WHERE effective_from=%s AND decision_id IS NULL", (r[0][0], eff))
        print("level %s -> d%d: %d" % (eff, r[0][0], cur.rowcount))
    else:
        print("NO decision at", mdate)
conn.commit()

# Дубль 29.04.2022 (агент вставил 14->12 поверх существующего d66 17->14)?
cur.execute("SELECT d.decision_id, m.meeting_id, d.rate_prev, d.rate_new FROM dkp.decision d JOIN dkp.meeting m USING(meeting_id) WHERE m.meeting_date='2022-04-29'")
rows = cur.fetchall()
print("29.04.2022 decisions:", rows)
conn.commit()
if len(rows) > 1:
    # дубль — тот, что не d66
    dup = [r for r in rows if r[0] != 66][0]
    dup_did, dup_mid = dup[0], dup[1]
    cur.execute("UPDATE dkp.rate_level SET decision_id=66 WHERE decision_id=%s", (dup_did,))
    print("rebind levels of dup to d66:", cur.rowcount)
    conn.commit()
    cur.execute("DELETE FROM dkp.decision WHERE decision_id=%s", (dup_did,))
    cur.execute("DELETE FROM dkp.meeting WHERE meeting_id=%s", (dup_mid,))
    print("deleted dup:", dup_did, dup_mid)
    conn.commit()

# 2015-06-08 (d11): prev должен быть 12.50
cur.execute("UPDATE dkp.decision SET rate_prev=12.50 WHERE decision_id=11 AND rate_prev=14.00 AND rate_new=11.50")
print("d11 prev 12.50:", cur.rowcount)
conn.commit()

# Снять флаг с верифицированных вставок (релиз найден агентом)
for mid in (115, 116):
    cur.execute("UPDATE dkp.meeting SET notes=replace(notes, ' [needs_source_check]', '') WHERE meeting_id=%s AND notes ILIKE '%пресс-рел%'", (mid,))
print("flags 115/116:", cur.rowcount)
conn.commit()

conn.close()
print("OK")