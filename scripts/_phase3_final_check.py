import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()

print("== целостность цепочки follows ==")
cur.execute("""WITH ordered AS (
     SELECT d.decision_id, lag(d.decision_id) OVER (ORDER BY m.meeting_date, d.decision_id) AS prev_id
     FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id))
   SELECT count(*) FROM ordered o WHERE o.prev_id IS NOT NULL
     AND NOT EXISTS (SELECT 1 FROM graph.edge e
                     JOIN graph.node s ON s.node_id=e.src_id JOIN graph.node t ON t.node_id=e.dst_id
                     WHERE e.edge_type='follows' AND s.ref_key='decision:'||o.decision_id AND t.ref_key='decision:'||o.prev_id)""")
print("  решений без ребра к предыдущему:", cur.fetchone()[0])
cur.execute("""SELECT s.ref_key, t.ref_key, count(*) FROM graph.edge e
   JOIN graph.node s ON s.node_id=e.src_id JOIN graph.node t ON t.node_id=e.dst_id
   WHERE e.edge_type='follows' GROUP BY 1,2 HAVING count(*)>1""")
print("  дублирующихся рёбер follows:", len(cur.fetchall()))
cur.execute("""SELECT s.ref_key, t.ref_key FROM graph.edge e
   JOIN graph.node s ON s.node_id=e.src_id JOIN graph.node t ON t.node_id=e.dst_id
   WHERE e.edge_type='follows' AND s.ref_key='decision:1'""")
print("  у первого решения входящих follows:", len(cur.fetchall()))

print("== висячие узлы (нет ни одного ребра) ==")
cur.execute("""SELECT count(*) FROM graph.node n WHERE NOT EXISTS (SELECT 1 FROM graph.edge e WHERE e.src_id=n.node_id OR e.dst_id=n.node_id)""")
print("  изолированных узлов:", cur.fetchone()[0])

print("== итог ==")
for q, lbl in (("SELECT count(*) FROM graph.node", "узлов"), ("SELECT count(*) FROM graph.edge", "рёбер"),
               ("SELECT count(*) FROM dkp.meeting", "заседаний"), ("SELECT count(*) FROM dkp.decision", "решений")):
    cur.execute(q); print("  %s: %d" % (lbl, cur.fetchone()[0]))
cur.execute("SELECT ref_key FROM graph.node WHERE ref_key IN ('meeting:64','decision:62')")
print("  остатки удалённых:", cur.fetchall())
conn.close()