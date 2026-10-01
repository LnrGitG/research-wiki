#!/usr/bin/env python3
"""Round-trip test of rollback: apply -> rollback -> apply (task t_9954c893)."""
import sys
sys.path.insert(0, '/home/lnr/research-wiki-private/scripts')
import db_tunnel

MIG = '/home/lnr/research-wiki-private/scripts/migrate_v2_core_catalog.sql'
RB = '/home/lnr/research-wiki-private/scripts/migrate_v2_core_catalog_rollback.sql'


def snap(tag):
    print("%-10s core.metric=%s facets=%s crosswalk=%s v_cat=%s" % (
        tag,
        db_tunnel.query("SELECT count(*) FROM core.metric")[0][0],
        db_tunnel.query("SELECT count(*) FROM derived.catalog_facets")[0][0],
        db_tunnel.query("SELECT count(*) FROM derived.metric_crosswalk")[0][0],
        db_tunnel.query("SELECT count(*) FROM derived.v_catalog_active")[0][0]))


snap("current")
db_tunnel.load_sql_file(RB)
snap("rolledback")
db_tunnel.load_sql_file(MIG)
snap("reapplied")
print("v2_pointer rows:", db_tunnel.query(
    "SELECT count(*) FROM derived.metric_crosswalk WHERE link_type='v2_pointer'")[0][0])