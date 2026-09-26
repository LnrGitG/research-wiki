import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

conn = connect()
cur = conn.cursor()

# Снять флаг с верифицированных вставок 2017/2019 (релизы найдены агентом ВМ)
cur.execute("UPDATE dkp.meeting SET notes=replace(notes, ' [needs_source_check]', '') WHERE meeting_id IN (115,116)")
print("flags cleared:", cur.rowcount)
conn.commit()

# Итоговое состояние
cur.execute("SELECT count(*) FROM dkp.meeting")
print("meetings:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.decision")
print("decisions:", cur.fetchone()[0])
cur.execute("SELECT count(*) FROM dkp.rate_level WHERE decision_id IS NULL")
print("null FK levels:", cur.fetchone()[0])
cur.execute("SELECT value, effective_from::text FROM dkp.rate_level WHERE decision_id IS NULL ORDER BY effective_from")
for r in cur.fetchall():
    print("  NULL FK:", r)
cur.execute("SELECT count(*) FROM dkp.meeting WHERE notes ILIKE '%needs_source_check%'")
print("needs_source_check:", cur.fetchone()[0])
conn.commit()
conn.close()
print("OK")