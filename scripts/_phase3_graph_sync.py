import sys, json
sys.path.insert(0, "/home/ubuntu/research-wiki-private/scripts")
from db_tunnel import connect

conn = connect(); cur = conn.cursor()
log = []


def run(tag, sql, params=None):
    if params is None:
        cur.execute(sql)
    else:
        cur.execute(sql, params)
    log.append("%s -> %d" % (tag, cur.rowcount))


try:
    # 1) Снести узлы удалённых сущностей и их рёбра
    run("delete edges of stale nodes",
        """DELETE FROM graph.edge WHERE src_id IN (SELECT node_id FROM graph.node WHERE ref_key IN ('meeting:64','decision:62'))
           OR dst_id IN (SELECT node_id FROM graph.node WHERE ref_key IN ('meeting:64','decision:62'))""")
    run("delete stale nodes", "DELETE FROM graph.node WHERE ref_key IN ('meeting:64','decision:62')")

    # 2) Пересобрать узлы заседаний и решений по данным БД (update + insert, без ON CONFLICT)
    run("update existing meeting nodes",
        """UPDATE graph.node n SET title = 'Заседание СД ' || m.meeting_date::text,
                  props = jsonb_build_object('meeting_date', m.meeting_date::text, 'decision_kind', m.decision_kind)
           FROM dkp.meeting m WHERE n.ref_key = 'meeting:' || m.meeting_id""")
    run("insert missing meeting nodes",
        """INSERT INTO graph.node (node_type, ref_key, title, props)
           SELECT 'cbr_meeting', 'meeting:' || m.meeting_id,
                  'Заседание СД ' || m.meeting_date::text,
                  jsonb_build_object('meeting_date', m.meeting_date::text, 'decision_kind', m.decision_kind)
           FROM dkp.meeting m
           WHERE NOT EXISTS (SELECT 1 FROM graph.node n WHERE n.ref_key = 'meeting:' || m.meeting_id)""")
    run("update existing decision nodes",
        """UPDATE graph.node n SET title = 'Решение ' || d.meeting_id || ': ' || d.action,
                  props = jsonb_build_object('meeting_id', d.meeting_id, 'action', d.action,
                                             'rate_prev', d.rate_prev::float, 'rate_new', d.rate_new::float)
           FROM dkp.decision d WHERE n.ref_key = 'decision:' || d.decision_id""")
    run("insert missing decision nodes",
        """INSERT INTO graph.node (node_type, ref_key, title, props)
           SELECT 'cbr_decision', 'decision:' || d.decision_id,
                  'Решение ' || d.meeting_id || ': ' || d.action,
                  jsonb_build_object('meeting_id', d.meeting_id, 'action', d.action,
                                     'rate_prev', d.rate_prev::float, 'rate_new', d.rate_new::float)
           FROM dkp.decision d
           WHERE NOT EXISTS (SELECT 1 FROM graph.node n WHERE n.ref_key = 'decision:' || d.decision_id)""")

    # 3) Достроить рёбра has_decision и follows
    run("insert missing has_decision edges",
        """INSERT INTO graph.edge (src_id, dst_id, edge_type, weight, provenance)
           SELECT mn.node_id, dn.node_id, 'has_decision', 1.0,
                  jsonb_build_object('fk', 'dkp.decision.meeting_id=' || m.meeting_id)
           FROM dkp.meeting m
           JOIN dkp.decision d USING (meeting_id)
           JOIN graph.node mn ON mn.ref_key = 'meeting:' || m.meeting_id
           JOIN graph.node dn ON dn.ref_key = 'decision:' || d.decision_id
           WHERE NOT EXISTS (SELECT 1 FROM graph.edge e WHERE e.src_id = mn.node_id AND e.dst_id = dn.node_id AND e.edge_type = 'has_decision')""")

    run("insert missing follows edges",
        """WITH ordered AS (
             SELECT d.decision_id, lag(d.decision_id) OVER (ORDER BY m.meeting_date, d.decision_id) AS prev_id
             FROM dkp.decision d JOIN dkp.meeting m USING (meeting_id)
           )
           INSERT INTO graph.edge (src_id, dst_id, edge_type, weight, provenance)
           SELECT pn.node_id, cn.node_id, 'follows', 1.0,
                  jsonb_build_object('order', 'chronological by meeting_date')
           FROM ordered o
           JOIN graph.node cn ON cn.ref_key = 'decision:' || o.decision_id
           JOIN graph.node pn ON pn.ref_key = 'decision:' || o.prev_id
           WHERE o.prev_id IS NOT NULL
             AND NOT EXISTS (SELECT 1 FROM graph.edge e WHERE e.src_id = pn.node_id AND e.dst_id = cn.node_id AND e.edge_type = 'follows')""")

    conn.commit()
    log.append("COMMIT ok")
except Exception as e:
    conn.rollback()
    log.append("ROLLBACK: %r" % (e,))

cur.execute("SELECT count(*) FROM graph.node"); log.append("узлов: %d" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM graph.edge"); log.append("рёбер: %d" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM graph.edge WHERE edge_type='follows'"); log.append("follows: %d" % cur.fetchone()[0])
cur.execute("SELECT count(*) FROM graph.edge WHERE edge_type='has_decision'"); log.append("has_decision: %d" % cur.fetchone()[0])
cur.execute("SELECT ref_key FROM graph.node WHERE ref_key IN ('meeting:64','decision:62','meeting:119','decision:112','decision:114')")
log.append("проверка: %s" % (cur.fetchall(),))
for line in log:
    print(" -", line)
conn.close()