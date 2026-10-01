#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lnr/research-wiki-private/scripts')
import db_tunnel

print("identity seq:", db_tunnel.query(
    "SELECT pg_get_serial_sequence('core.metric','metric_id')"))
print("seq last_value:", db_tunnel.query(
    "SELECT last_value, is_called FROM core.metric_metric_id_seq"))
print("new core rows:", db_tunnel.query(
    "SELECT metric_id, metric_code, metric_type, is_derived, status, tags, unit_id, frequency_id "
    "FROM core.metric WHERE metric_id BETWEEN 71935 AND 71946 ORDER BY metric_id"))
# cross-check FK integrity of crosswalk canonical ids
print("crosswalk orphans:", db_tunnel.query(
    "SELECT count(*) FROM derived.metric_crosswalk c "
    "LEFT JOIN core.metric m ON m.metric_id=c.canonical_id WHERE m.metric_id IS NULL"))
# ensure no duplicate metric_code created
print("dup codes:", db_tunnel.query(
    "SELECT metric_code, count(*) FROM core.metric GROUP BY metric_code HAVING count(*)>1"))
# ensure quarantine does not contain new ids
print("new ids in quarantine:", db_tunnel.query(
    "SELECT count(*) FROM derived.catalog_quarantine WHERE metric_id BETWEEN 71935 AND 71946"))
# unit/freq validity
print("unit/freq present:", db_tunnel.query(
    "SELECT count(*) FROM core.metric m JOIN core.unit u ON u.unit_id=m.unit_id "
    "JOIN core.frequency f ON f.frequency_id=m.frequency_id WHERE m.metric_id BETWEEN 71935 AND 71946"))