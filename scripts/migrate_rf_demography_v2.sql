-- Migration: register Russia-wide mortgage panel + demography/exposure layer
-- (profiles personal/research, 01.10.2026). Idempotent: ON CONFLICT DO NOTHING.
-- Tables stay in public; v2 catalog gets pointer cards + load_run versioning.
--
-- Карточки: 15 rf-panel-lshare (производный ряд РФ), 16 vpn-children-households
-- (демография ВПН-2020 + возрастная структура + экспозиция реформы 2026).
-- Порядок как в migrate_personal_layers_v2.sql: источник -> датасет -> load_run
-- -> метрики -> маппинг -> GRANT (source_id NOT NULL, поэтому source первым).

-- 1) датасеты
INSERT INTO v2.dataset (dataset_id, source_id, dataset_code, name_ru, release_url, schedule, is_active)
VALUES (15, 10, 'rf-panel-lshare',
        'Россия в целом — месячная панель льготных выдач, ставки и доли льготных',
        NULL, 'monthly', true)
ON CONFLICT (dataset_id) DO NOTHING;

INSERT INTO v2.dataset (dataset_id, source_id, dataset_code, name_ru, release_url, schedule, is_active)
VALUES (16, 1, 'vpn-children-households',
        'ВПН-2020 Том 8 + возрастная структура: домохозяйства по числу детей, экспозиция реформы 2026',
        'https://rosstat.gov.ru/vpn/2020/Tom8_Chislo_i_sostav_domohozyajstv', 'decennial', true)
ON CONFLICT (dataset_id) DO NOTHING;

-- 2) load_run (версионные указатели)
INSERT INTO v2.load_run (run_id, dataset_id, loaded_at, source_file, parser_version, status, notes)
VALUES
  (64, 15, '2026-10-01 00:00:00+00', 'public.rf_panel_lshare', 'personal-derive-v2', 'ok',
   'Ряд РФ 2019-12..2026-08 (80 мес, 77 годных). Льготные = поток lgot8 (декумулирование) + семейная + ИТ, ДВ отдельным вариантом. Выбросы 2022-11 и 2023-03 помечены is_excluded. Цены — каталог, метрика 1099.'),
  (65, 16, '2026-10-01 00:00:00+00', 'public.vpn_households_children + public.rosstat_children_06 + public.did_exposure_reform2026', 'personal-derive-v2', 'ok',
   'ВПН-2020 Tom8 Табл.4 по 87 регионам + агрегат РФ (11,8% семей с 3+ детьми); возрастная структура на 1.01.2022; экспозиция реформы 01.10.2026: РФ 0,551, диапазон Урала 0,530..0,576.')
ON CONFLICT (run_id) DO NOTHING;

-- 3) метрики (домен 4 credit / 9 demography)
INSERT INTO v2.metric (metric_id, metric_code, name_ru, name_en, domain_id, unit_id, frequency_id, is_aggregate, priority)
VALUES
  (134, 'rf_lgot_count_m', 'Россия: выдачи по льготным программам, шт (месяц)', 'Russia: subsidized mortgage issuances, count (monthly)', 4, 4, 2, true, 'core'),
  (135, 'rf_lshare_m', 'Россия: доля льготных выдач в жилищных кредитах', 'Russia: share of subsidized issuances in housing loans', 4, 9, 2, true, 'core'),
  (136, 'rf_market_count_m', 'Россия: рыночные выдачи (все минус льготные), шт', 'Russia: market issuances (all minus subsidized), count', 4, 4, 2, true, 'extended'),
  (137, 'hh_share_3plus', 'Доля домохозяйств с детьми с 3+ детьми до 18 лет (ВПН-2020)', 'Share of households with 3+ children under 18 (census 2020)', 9, 9, 4, false, 'core'),
  (138, 'kids_share_under7', 'Доля детей младше 7 лет в числе детей до 17 лет', 'Share of children under 7 among children under 18', 9, 9, 4, false, 'extended'),
  (139, 'exposure_family_mortgage_2026', 'Экспозиция реформы семейной ипотеки 01.10.2026 (доля семей, для которых ставка выросла)', 'Exposure to the family mortgage reform of 01.10.2026', 9, 9, 4, false, 'core')
ON CONFLICT (metric_id) DO NOTHING;

-- 4) маппинг метрик на датасеты
INSERT INTO v2.metric_dataset_map (metric_id, dataset_id, native_code, scale_factor)
VALUES
  (134, 15, 'rf_panel_lshare:lgot_total', 1.0),
  (135, 15, 'rf_panel_lshare:lshare', 1.0),
  (136, 15, 'rf_panel_lshare:market_cnt', 1.0),
  (137, 16, 'vpn_households_children:share_3p', 1.0),
  (138, 16, 'rosstat_children_06:share_kids06', 1.0),
  (139, 16, 'did_exposure_reform2026:exposure_gross', 1.0)
ON CONFLICT DO NOTHING;

-- 5) доступ на чтение для роли viewer
GRANT SELECT ON public.rf_panel_lshare TO viewer;
GRANT SELECT ON public.vpn_households_children TO viewer;
GRANT SELECT ON public.rosstat_children_06 TO viewer;
GRANT SELECT ON public.did_exposure_reform2026 TO viewer;