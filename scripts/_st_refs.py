import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()

print("== таблицы со ссылкой на decision_id / meeting_id ==")
cur.execute("""SELECT tc.table_schema, tc.table_name, kcu.column_name, ccu.table_name AS ref_table
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu ON kcu.constraint_name = tc.constraint_name
JOIN information_schema.constraint_column_usage ccu ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type='FOREIGN KEY' AND ccu.table_name IN ('decision','meeting')
ORDER BY tc.table_schema, tc.table_name""")
for r in cur.fetchall():
    print(" FK:", r)

print("== ссылки на удаляемые решения 26, 110 ==")
for tbl_col in [("dkp.rate_level", "decision_id"), ("graph.node", None)]:
    pass
cur.execute("SELECT count(*) FROM dkp.rate_level WHERE decision_id IN (26,110)")
print("rate_level -> 26/110:", cur.fetchone()[0])
cur.execute("""SELECT node_id, node_type, ref_key, title FROM graph.node
WHERE ref_key IN ('decision:26','decision:110','meeting:26','meeting:116','decision:19','decision:23','decision:28','decision:44','decision:45','decision:53','decision:54','decision:102','decision:109')
ORDER BY ref_key""")
print("== graph.node ==")
for r in cur.fetchall():
    print(" node:", r)
cur.execute("""SELECT count(*) FROM graph.edge e
WHERE e.src_id IN (SELECT node_id FROM graph.node WHERE ref_key IN ('decision:26','decision:110','meeting:26','meeting:116'))
   OR e.dst_id IN (SELECT node_id FROM graph.node WHERE ref_key IN ('decision:26','decision:110','meeting:26','meeting:116'))""")
print("edges touching removed nodes:", cur.fetchone()[0])
conn.close()