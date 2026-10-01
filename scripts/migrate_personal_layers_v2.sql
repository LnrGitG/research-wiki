-- Migration: register 4 new datasets from personal profile (30.09.2026)
-- into v2 catalog. Tables remain in public; v2.dataset gets pointer cards.
-- Run as owner (not viewer) — viewer has no INSERT on v2.dataset.
-- Idempotent: ON CONFLICT DO NOTHING.
--
-- ИСПРАВЛЕНО 01.10.2026 (при применении профилем personal): два дефекта порядка
-- и ограничений. (1) v2.source (id=10 'derived') вставляется ПЕРВЫМ — иначе
-- v2.dataset.source_id NOT NULL отвергает карточку 13. (2) Карточка 13 идёт с
-- source_id=10, а не NULL (NOT NULL constraint). Применённая версия — эта.

-- 0) источник 'derived' — ДО карточек датасетов
INSERT INTO v2.source (source_id, source_code, name_ru, access_method)
VALUES (10, 'derived', 'Производные датасеты (расчётные)', 'sql')
ON CONFLICT (source_id) DO NOTHING;

-- 1) domrf-lgot-weeklyreport (dataset_id=11)
INSERT INTO v2.dataset (dataset_id, source_id, dataset_code, name_ru, release_url, schedule, is_active)
VALUES (11, 3, 'domrf-lgot-weeklyreport',
        'ДОМ.РФ weeklyreport — еженедельные снимки льготных программ (psm/itm/sip/dfo)',
        'https://наш.дом.рф/аналитика/weeklyreport', 'weekly', true)
ON CONFLICT (dataset_id) DO NOTHING;

-- 2) cbr-vfs-regional (dataset_id=12)
INSERT INTO v2.dataset (dataset_id, source_id, dataset_code, name_ru, release_url, schedule, is_active)
VALUES (12, 2, 'cbr-vfs-regional',
        'ЦБ РФ формы 02_06/02_07/02_13 — региональный разрез ЖИК и ставки ИЖК',
        'https://cbr.ru/vfs/statistics/BankSector/Mortgage/', 'monthly', true)
ON CONFLICT (dataset_id) DO NOTHING;

-- 3) ufo-panel-lshare (dataset_id=13)
-- source: derived (source_id=10 — вставлен первым, см. шаг 0)
INSERT INTO v2.dataset (dataset_id, source_id, dataset_code, name_ru, release_url, schedule, is_active)
VALUES (13, 10, 'ufo-panel-lshare',
        'Панель доли льготных выдач (Уральский макрорегион, 9 субъектов)',
        NULL, 'monthly', true)
ON CONFLICT (dataset_id) DO NOTHING;

-- 4) rosstat-housing-prices-q (dataset_id=14)
INSERT INTO v2.dataset (dataset_id, source_id, dataset_code, name_ru, release_url, schedule, is_active)
VALUES (14, 1, 'rosstat-housing-prices-q',
        'Росстат — средние цены 1 кв.м жилья (первичка/вторичка, квартальные)',
        'https://rosstat.gov.ru/statistics/zhilishchnoe-stroitelstvo', 'quarterly', true)
ON CONFLICT (dataset_id) DO NOTHING;

-- Add 'derived' source if not present (for ufo-panel-lshare)
-- (перенесено в шаг 0 — источник вставляется ДО карточек датасетов)
-- UPDATE ufo-panel-lshare source_id to 10 (derived) — уже задано в карточке 13

-- Register load_run entries (run_id 60-63) to create versioning pointers
INSERT INTO v2.load_run (run_id, dataset_id, loaded_at, source_file, parser_version, status, rows_parsed, rows_inserted, rows_rejected, notes)
VALUES
  (60, 11, '2026-09-30 00:00:00+00', 'public.domrf_lgot_mortgage', 'personal-collect-v1', 'ok', 1090000, 1090000, 0,
   'Сбор профилем personal 30.09.2026: 1023 еженедельных снимка ДОМ.РФ, 4 программы, ~1.09 млн строк. Сверка семейная июнь 2026: 2.4%.'),
  (61, 12, '2026-09-30 00:00:00+00', 'public.cbr_housing_loans + public.cbr_mortgage_rates', 'personal-collect-v1', 'ok', NULL, NULL, NULL,
   'Сбор профилем personal 30.09.2026: ЦБ 02_06/02_07/02_13, 92 мес (2019-01..2026-08), по субъектам. Сверка Тюменская ветка 3 строки: сходится.'),
  (62, 13, '2026-09-30 00:00:00+00', 'public.ufo_panel_lshare', 'personal-derive-v1', 'ok', NULL, NULL, NULL,
   'Производный датасет профиля personal 30.09.2026: 9 уральских регионов × 91 мес, доля льготных выдач. 2022-11 исключён, доли >105% отфильтрованы.'),
  (63, 14, '2026-09-30 00:00:00+00', 'public.rosstat_housing_prices', 'personal-collect-v1', 'ok', NULL, NULL, NULL,
   'Сбор профилем personal 30.09.2026: квартальные цены 1 кв.м, 2021-2026, 9 регионов. Дубль метрик 17/18, даёт последний квартал раньше.')
ON CONFLICT (run_id) DO NOTHING;

-- v2.metric: new metrics for subsidized mortgage programs (домен 4 credit)
-- lgot_count_w: количество выдач по льготным программам (недельный, по программам)
INSERT INTO v2.metric (metric_id, metric_code, name_ru, name_en, domain_id, unit_id, frequency_id, is_aggregate, priority)
VALUES
  (128, 'lgot_count_w', 'Льготные выдачи, шт (по программам ДОМ.РФ)', 'Subsidized mortgage issuances, count (DOM.RF programs)', 4, 4, 1, false, 'core'),
  (129, 'lgot_volume_w', 'Льготные выдачи, млн руб (по программам ДОМ.РФ)', 'Subsidized mortgage issuances, mln rub (DOM.RF programs)', 4, 1, 1, false, 'core'),
  (130, 'cbr_housing_loans_count_reg_m', 'Жилищные кредиты, шт (региональный разрез)', 'Housing loans count (regional)', 4, 4, 2, false, 'extended'),
  (131, 'cbr_housing_loans_volume_reg_m', 'Жилищные кредиты, млн руб (региональный разрез)', 'Housing loans volume (regional)', 4, 1, 2, false, 'extended'),
  (132, 'cbr_mortgage_rate_reg_m', 'Ставка ИЖК по субъектам (02_13)', 'Mortgage rate by region (02_13)', 4, 5, 2, false, 'core'),
  (133, 'lshare_m', 'Доля льготных выдач в жилищных кредитах', 'Share of subsidized mortgages in housing loans', 4, 9, 2, false, 'core')
ON CONFLICT (metric_id) DO NOTHING;

-- Map metrics to datasets
INSERT INTO v2.metric_dataset_map (metric_id, dataset_id, native_code, scale_factor)
VALUES
  (128, 11, 'domrf_lgot_mortgage:count', 1.0),
  (129, 11, 'domrf_lgot_mortgage:mln', 1.0),
  (130, 12, 'cbr_housing_loans:count', 1.0),
  (131, 12, 'cbr_housing_loans:volume', 1.0),
  (132, 12, 'cbr_mortgage_rates:rate', 1.0),
  (133, 13, 'ufo_panel_lshare:lshare', 1.0)
ON CONFLICT DO NOTHING;

-- Map rosstat_housing_prices to EXISTING metrics 17/18 (not new ones)
INSERT INTO v2.metric_dataset_map (metric_id, dataset_id, native_code, scale_factor)
VALUES
  (17, 14, 'rosstat_housing_prices:price_new_m2', 1.0),
  (18, 14, 'rosstat_housing_prices:price_secondary_m2', 1.0)
ON CONFLICT DO NOTHING;

-- Grant viewer SELECT on the 4 public tables (so v2 queries can join)
GRANT SELECT ON public.domrf_lgot_mortgage TO viewer;
GRANT SELECT ON public.cbr_housing_loans TO viewer;
GRANT SELECT ON public.cbr_mortgage_rates TO viewer;
GRANT SELECT ON public.ufo_panel_lshare TO viewer;
GRANT SELECT ON public.rosstat_housing_prices TO viewer;