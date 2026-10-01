-- =====================================================================
-- Migration: v2 → core catalog registration (task t_9954c893)
-- Date: 2026-10-01
--
-- ПРОБЛЕМА
--   derived.v_catalog_active строится на core.metric (ids 1..71934).
--   Новые карточки профилей personal/research зарегистрированы в v2.metric
--   (ids 128..139) — ОТДЕЛЬНОЕ пространство id. Совпадение номеров при
--   разном смысле (core#134 «Жилая площадь МКД 50-500 тыс. кв.м» ЕИСЖС
--   против v2#134 «Россия: выдачи по льготным программам»). Из-за этого
--   новые ряды НЕ видны в основном каталоге v_catalog_active.
--
-- РЕШЕНИЕ (вариант 1 решения владельца)
--   Зарегистрировать те же ряды в core.metric со СВЕЖИМИ id (>= 71935,
--   вне диапазона v2.metric, max v2 id = 58064) и добавить строки
--   derived.catalog_facets, чтобы ряды попали в v_catalog_active.
--   v2.metric остаётся как слой версионирования; связь core↔v2
--   фиксируется в derived.metric_crosswalk (link_type = 'v2_pointer').
--
-- ВАЖНО ПРО link_type='v2_pointer'
--   metric_crosswalk.metric_id и canonical_id имеют FK на core.metric.
--   Поэтому в metric_id записан id карточки v2 (128..139), который
--   технически существует и в core.metric (совпадение пространств), но
--   СМЫСЛ берётся из link_type: 'v2_pointer' = metric_id трактуется в
--   пространстве v2.metric, canonical_id — канонический core.metric.
--   Скрытая ловушка (join metric_crosswalk→core.metric по metric_id даст
--   чужую строку ЕИСЖС) — известна и вынесена в примечание миграции.
--
-- Идемпотентность: ON CONFLICT DO NOTHING.
-- Запуск: владелец БД (роль wiki), не viewer.
-- =====================================================================

-- ---------------------------------------------------------------------
-- 1) core.metric — 12 новых рядов, ids 71935..71946 (свежий диапазон)
--    unit/frequency переведены из пространств v2 в core:
--      v2 unit 4 count -> core 29 count ; v2 1 mln_rub -> core 11 mln_rub
--      v2 5 pct / 9 share -> core 12 pct
--      v2 freq 1 W -> core 15 W ; 2 M -> core 5 M ; 4 A -> core 3 A
-- ---------------------------------------------------------------------
-- core.metric.metric_id — GENERATED ALWAYS AS IDENTITY, поэтому явные id
-- требуют OVERRIDING SYSTEM VALUE (иначе GeneratedAlways).
INSERT INTO core.metric
  (metric_id, metric_code, name_ru, short_name_ru, description,
   unit_id, frequency_id, metric_type, is_derived, status, tags)
OVERRIDING SYSTEM VALUE
VALUES
  (71935, 'lgot_count_w',
   'Льготные выдачи, шт (по программам ДОМ.РФ)',
   'Льготные выдачи (шт, нед.)',
   'Еженедельные выдачи по льготным программам ДОМ.РФ (семейная, IT, lgot8, ДВ), шт. Источник: public.domrf_lgot_mortgage (weeklyreport).',
   29, 15, 'primary', false, 'active', ARRAY['v2','housing','mortgage']),
  (71936, 'lgot_volume_w',
   'Льготные выдачи, млн руб (по программам ДОМ.РФ)',
   'Льготные выдачи (млн руб, нед.)',
   'Еженедельный объём выдач по льготным программам ДОМ.РФ, млн руб. Источник: public.domrf_lgot_mortgage (weeklyreport).',
   11, 15, 'primary', false, 'active', ARRAY['v2','housing','mortgage']),
  (71937, 'cbr_housing_loans_count_reg_m',
   'Жилищные кредиты, шт (региональный разрез)',
   'Жилищные кредиты (шт, рег.)',
   'Количество жилищных кредитов по субъектам, шт. Источник: ЦБ формы 02_06/02_07 (public.cbr_housing_loans).',
   29, 5, 'primary', false, 'active', ARRAY['v2','housing','mortgage']),
  (71938, 'cbr_housing_loans_volume_reg_m',
   'Жилищные кредиты, млн руб (региональный разрез)',
   'Жилищные кредиты (млн руб, рег.)',
   'Объём жилищных кредитов по субъектам, млн руб. Источник: ЦБ формы 02_06/02_07 (public.cbr_housing_loans).',
   11, 5, 'primary', false, 'active', ARRAY['v2','housing','mortgage']),
  (71939, 'cbr_mortgage_rate_reg_m',
   'Ставка ИЖК по субъектам (02_13)',
   'Ставка ИЖК (рег.)',
   'Средневзвешенная ставка по ипотечным жилищным кредитам по субъектам, %. Источник: ЦБ 02_13 (public.cbr_mortgage_rates).',
   12, 5, 'primary', false, 'active', ARRAY['v2','housing','mortgage']),
  (71940, 'lshare_m',
   'Доля льготных выдач в жилищных кредитах',
   'Доля льготных выдач',
   'Доля льготных выдач в общем числе жилищных кредитов (Уральский макрорегион, 9 субъектов). Производный ряд public.ufo_panel_lshare.',
   12, 5, 'derived', true, 'active', ARRAY['v2','housing','mortgage']),
  (71941, 'rf_lgot_count_m',
   'Россия: выдачи по льготным программам, шт (месяц)',
   'РФ: льготные выдачи (шт, мес.)',
   'Месячные выдачи по льготным программам в целом по РФ (поток: декумулирование lgot8 + семейная + IT). Производный ряд public.rf_panel_lshare.',
   29, 5, 'derived', true, 'active', ARRAY['v2','housing','mortgage']),
  (71942, 'rf_lshare_m',
   'Россия: доля льготных выдач в жилищных кредитах',
   'РФ: доля льготных выдач',
   'Доля льготных выдач в общем числе жилищных кредитов по РФ, месячная панель. Производный ряд public.rf_panel_lshare.',
   12, 5, 'derived', true, 'active', ARRAY['v2','housing','mortgage']),
  (71943, 'rf_market_count_m',
   'Россия: рыночные выдачи (все минус льготные), шт',
   'РФ: рыночные выдачи (шт)',
   'Рыночные выдачи = все выдачи минус льготные, шт, по РФ. Производный ряд public.rf_panel_lshare.',
   29, 5, 'derived', true, 'active', ARRAY['v2','housing','mortgage']),
  (71944, 'hh_share_3plus',
   'Доля домохозяйств с детьми с 3+ детьми до 18 лет (ВПН-2020)',
   'Доля семей с 3+ детьми',
   'Доля домохозяйств с тремя и более детьми до 18 лет. ВПН-2020, Том 8, Табл.4 (public.vpn_households_children).',
   12, 3, 'derived', true, 'active', ARRAY['v2','demography']),
  (71945, 'kids_share_under7',
   'Доля детей младше 7 лет в числе детей до 17 лет',
   'Доля детей <7 лет',
   'Доля детей младше 7 лет в общей численности детей до 17 лет (возрастная структура). public.rosstat_children_06.',
   12, 3, 'derived', true, 'active', ARRAY['v2','demography']),
  (71946, 'exposure_family_mortgage_2026',
   'Экспозиция реформы семейной ипотеки 01.10.2026 (доля семей, для которых ставка выросла)',
   'Экспозиция реформы 2026',
   'Доля семей, для которых ставка по семейной ипотеке выросла после реформы 01.10.2026. Расчёт public.did_exposure_reform2026.',
   12, 3, 'derived', true, 'active', ARRAY['v2','demography'])
ON CONFLICT (metric_id) DO NOTHING;

-- Сдвинуть identity-последовательность за новые id, чтобы последующие
-- вставки без явного id не столкнулись с 71935..71946.
SELECT setval(pg_get_serial_sequence('core.metric', 'metric_id'),
              (SELECT max(metric_id) FROM core.metric));

-- ---------------------------------------------------------------------
-- 2) derived.catalog_facets — фацеты для новых core id (иначе витрина
--    v_catalog_active их не покажет: она JOIN-ит core.metric × catalog_facets)
--    depth_obs — глубина ряда (число периодов; для кросс-секций — регионов).
--    freshness — по правилу этапа 1 (мес: 4 мес; год: 2 года от max частоты);
--    ВПН-2020 (2021-10) и возрастная структура (2022-01) честно помечены stale.
-- ---------------------------------------------------------------------
INSERT INTO derived.catalog_facets
  (metric_id, measure, unit_canonical, seasonally_adjusted, domain,
   freshness, last_obs_at, depth_obs, is_aggregate, run_id)
VALUES
  (71935, 'level', 'count',   false, 'credit',     'fresh', DATE '2026-09-20', 511, false, 'v2-core-registration-20261001'),
  (71936, 'level', 'mln_rub', false, 'credit',     'fresh', DATE '2026-09-20', 511, false, 'v2-core-registration-20261001'),
  (71937, 'level', 'count',   false, 'credit',     'fresh', DATE '2026-08-01',  92, false, 'v2-core-registration-20261001'),
  (71938, 'level', 'mln_rub', false, 'credit',     'fresh', DATE '2026-08-01',  92, false, 'v2-core-registration-20261001'),
  (71939, 'level', 'pct',     false, 'credit',     'fresh', DATE '2026-08-01',  92, false, 'v2-core-registration-20261001'),
  (71940, 'level', 'pct',     false, 'credit',     'fresh', DATE '2026-08-01',  91, false, 'v2-core-registration-20261001'),
  (71941, 'level', 'count',   false, 'credit',     'fresh', DATE '2026-08-01',  80, true,  'v2-core-registration-20261001'),
  (71942, 'level', 'pct',     false, 'credit',     'fresh', DATE '2026-08-01',  80, true,  'v2-core-registration-20261001'),
  (71943, 'level', 'count',   false, 'credit',     'fresh', DATE '2026-08-01',  80, true,  'v2-core-registration-20261001'),
  (71944, 'level', 'pct',     false, 'demography', 'stale', DATE '2021-10-01',  10, false, 'v2-core-registration-20261001'),
  (71945, 'level', 'pct',     false, 'demography', 'stale', DATE '2022-01-01',  10, false, 'v2-core-registration-20261001'),
  (71946, 'level', 'pct',     false, 'demography', 'fresh', DATE '2026-10-01',  10, false, 'v2-core-registration-20261001')
ON CONFLICT (metric_id) DO NOTHING;

-- ---------------------------------------------------------------------
-- 3) derived.metric_crosswalk — связь карточек v2.metric с каноническими
--    core.metric (link_type='v2_pointer'). metric_id = v2 id (128..139),
--    canonical_id = новый core id (71935..71946).
-- ---------------------------------------------------------------------
INSERT INTO derived.metric_crosswalk
  (metric_id, canonical_id, link_type, frequency_id, decided_by, run_id)
VALUES
  (128, 71935, 'v2_pointer', 15, 'v2_migration', 'v2-core-registration-20261001'),
  (129, 71936, 'v2_pointer', 15, 'v2_migration', 'v2-core-registration-20261001'),
  (130, 71937, 'v2_pointer',  5, 'v2_migration', 'v2-core-registration-20261001'),
  (131, 71938, 'v2_pointer',  5, 'v2_migration', 'v2-core-registration-20261001'),
  (132, 71939, 'v2_pointer',  5, 'v2_migration', 'v2-core-registration-20261001'),
  (133, 71940, 'v2_pointer',  5, 'v2_migration', 'v2-core-registration-20261001'),
  (134, 71941, 'v2_pointer',  5, 'v2_migration', 'v2-core-registration-20261001'),
  (135, 71942, 'v2_pointer',  5, 'v2_migration', 'v2-core-registration-20261001'),
  (136, 71943, 'v2_pointer',  5, 'v2_migration', 'v2-core-registration-20261001'),
  (137, 71944, 'v2_pointer',  3, 'v2_migration', 'v2-core-registration-20261001'),
  (138, 71945, 'v2_pointer',  3, 'v2_migration', 'v2-core-registration-20261001'),
  (139, 71946, 'v2_pointer',  3, 'v2_migration', 'v2-core-registration-20261001')
ON CONFLICT (metric_id, canonical_id) DO NOTHING;
