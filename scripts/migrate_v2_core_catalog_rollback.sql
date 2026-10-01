-- =====================================================================
-- Rollback for scripts/migrate_v2_core_catalog.sql (task t_9954c893)
-- Точка возврата: удаляет ровно то, что добавила миграция (run_id
-- 'v2-core-registration-20261001', crosswalk link_type='v2_pointer',
-- core.metric ids 71935..71946). Идемпотентно (DELETE по ключу).
-- Наблюдения и прочие данные НЕ трогаются (миграция была чисто
-- регистрационной — строки в core.observation_v2 не добавлялись).
-- Порядок: crosswalk -> catalog_facets -> core.metric (снять FK).
-- =====================================================================

DELETE FROM derived.metric_crosswalk
 WHERE run_id = 'v2-core-registration-20261001'
   AND link_type = 'v2_pointer';

DELETE FROM derived.catalog_facets
 WHERE run_id = 'v2-core-registration-20261001'
   AND metric_id BETWEEN 71935 AND 71946;

DELETE FROM core.metric
 WHERE metric_id BETWEEN 71935 AND 71946
   AND metric_code IN (
     'lgot_count_w','lgot_volume_w','cbr_housing_loans_count_reg_m',
     'cbr_housing_loans_volume_reg_m','cbr_mortgage_rate_reg_m','lshare_m',
     'rf_lgot_count_m','rf_lshare_m','rf_market_count_m',
     'hh_share_3plus','kids_share_under7','exposure_family_mortgage_2026');

-- Вернуть identity-последовательность к прежнему максимуму.
SELECT setval(pg_get_serial_sequence('core.metric', 'metric_id'),
              (SELECT max(metric_id) FROM core.metric));
