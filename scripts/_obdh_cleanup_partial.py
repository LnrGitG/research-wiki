#!/usr/bin/env python3
"""Откат частичного прогона ingest_obdh (релизы без валидных наблюдений)."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel

REL = (178, 179, 180)
with db_tunnel.connect() as c:
    with c.cursor() as cur:
        cur.execute('SELECT release_id, label FROM catalog.release WHERE release_id = ANY(%s)', (list(REL),))
        print('к удалению:', cur.fetchall())
        cur.execute('DELETE FROM data.observation WHERE release_id = ANY(%s)', (list(REL),))
        print('удалено наблюдений:', cur.rowcount)
        cur.execute('DELETE FROM catalog.release WHERE release_id = ANY(%s)', (list(REL),))
        print('удалено релизов:', cur.rowcount)
    c.commit()
