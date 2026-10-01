#!/usr/bin/env python3
"""Apply scripts/migrate_v2_core_catalog.sql and verify (task t_9954c893)."""
import sys
sys.path.insert(0, '/home/lnr/research-wiki-private/scripts')
import db_tunnel

MIG = '/home/lnr/research-wiki-private/scripts/migrate_v2_core_catalog.sql'


def one(sql, params=None):
    return db_tunnel.query(sql, params)[0]


print("=== BEFORE ===")
print("core.metric:", one("SELECT count(*), max(metric_id) FROM core.metric"))
print("catalog_facets:", one("SELECT count(*) FROM derived.catalog_facets"))
print("crosswalk:", one("SELECT count(*) FROM derived.metric_crosswalk"))
print("v_catalog_active:", one("SELECT count(*) FROM derived.v_catalog_active"))

n = db_tunnel.load_sql_file(MIG)
print("\napplied sql file, statements executed (rowcount-based):", n)

print("\n=== AFTER ===")
print("core.metric:", one("SELECT count(*), max(metric_id) FROM core.metric"))
print("catalog_facets:", one("SELECT count(*) FROM derived.catalog_facets"))
print("crosswalk:", one("SELECT count(*) FROM derived.metric_crosswalk"))
print("v_catalog_active:", one("SELECT count(*) FROM derived.v_catalog_active"))

print("\n=== ACCEPTANCE 1: search v_catalog_active by code ===")
codes = ['rf_lgot_count_m', 'rf_lshare_m', 'hh_share_3plus', 'kids_share_under7',
         'exposure_family_mortgage_2026', 'lgot_count_w', 'cbr_mortgage_rate_reg_m',
         'lshare_m', 'lgot_volume_w', 'cbr_housing_loans_count_reg_m',
         'cbr_housing_loans_volume_reg_m', 'rf_market_count_m']
for c in codes:
    rows = db_tunnel.query(
        "SELECT metric_id, metric_code, name_ru, domain, unit_canonical, freshness, is_aggregate "
        "FROM derived.v_catalog_active WHERE metric_code = %s", (c,))
    status = "OK" if len(rows) == 1 else "!!! %d rows" % len(rows)
    print("%-34s %s -> %s" % (c, status, rows[0] if rows else None))

print("\n=== ACCEPTANCE 2: id intersection v2.metric x NEW core.metric (>=71935) ===")
print("new-core-vs-v2 overlap:",
      one("SELECT count(*) FROM v2.metric v JOIN core.metric c ON c.metric_id = v.metric_id "
          "WHERE c.metric_id >= 71935"))
print("full-table v2<->core overlap (pre-existing, unchanged):",
      one("SELECT count(*) FROM v2.metric v JOIN core.metric c ON c.metric_id = v.metric_id"))

print("\n=== crosswalk v2_pointer rows ===")
for r in db_tunnel.query(
        "SELECT metric_id, canonical_id, link_type FROM derived.metric_crosswalk "
        "WHERE link_type='v2_pointer' ORDER BY metric_id"):
    print(r)

print("\n=== idempotency: re-run ===")
db_tunnel.load_sql_file(MIG)
print("core.metric after re-run:", one("SELECT count(*), max(metric_id) FROM core.metric"))
print("catalog_facets after re-run:", one("SELECT count(*) FROM derived.catalog_facets"))
print("crosswalk after re-run:", one("SELECT count(*) FROM derived.metric_crosswalk"))