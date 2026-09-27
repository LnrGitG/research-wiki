import sys
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect
conn = connect(); cur = conn.cursor()
log = []

# Конвенция графа: ребро follows идёт от текущего решения к предыдущему
# (decision:N -> decision:N-1). Вчерашняя вставка сделала обратное направление —
# удаляем и вставляем правильно.
cur.execute("DELETE FROM graph.edge WHERE edge_type='follows' AND created_at >= '2026-09-27'")
log.append("удалены follows неверного направления: %d" % cur.rowcount)

cur.execute("""WITH ordered AS (
     SELECT d.decision_id, lag(d.decision_id) OVER (ORDER BY m.meeting_date, d.decision_id) AS prev_id
     FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
   )
   INSERT INTO graph.edge (src_id, dst_id, edge_type, weight, provenance)
   SELECT cn.node_id, pn.node_id, 'follows', 1.0,
          jsonb_build_object('order', 'chronological by meeting_date')
   FROM ordered o
   JOIN graph.node cn ON cn.ref_key = 'decision:' || o.decision_id
   JOIN graph.node pn ON pn.ref_key = 'decision:' || o.prev_id
   WHERE o.prev_id IS NOT NULL
     AND NOT EXISTS (SELECT 1 FROM graph.edge e WHERE e.src_id = cn.node_id AND e.dst_id = pn.node_id AND e.edge_type = 'follows')""")
log.append("вставлены follows (текущее -> предыдущее): %d" % cur.rowcount)
conn.commit()

cur.execute("SELECT count(*) FROM graph.edge WHERE edge_type='follows'")
log.append("follows всего: %d" % cur.fetchone()[0])
cur.execute("""SELECT s.ref_key, t.ref_key FROM graph.edge e
JOIN graph.node s ON s.node_id=e.src_id JOIN graph.node t ON t.node_id=e.dst_id
WHERE e.edge_type='follows' AND e.created_at >= '2026-09-27' LIMIT 3""")
log.append("пример новых: %s" % (cur.fetchall(),))
cur.execute("SELECT count(*) FROM graph.node"); log.append("узлов: %d" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM graph.edge"); log.append("рёбер: %d" % cur.fetchone()[0])
for line in log:
    print(" -", line)
conn.close()