# Wiki Log — публикации, источники, данные

> Хронологический журнал **содержательных** изменений вики. Append-only.
> Формат: `## [YYYY-MM-DD] действие | тема`
>
> Действия:
> - `ingest` — новая публикация (статья, обзор, отчёт) разобрана и внесена в вики
> - `source` — новый источник данных подключён или разведан
> - `data` — обновление данных из источника
> - `query` — аналитическая записка, обзор литературы, карта пробелов
> - `hypothesis` — изменение реестра гипотез по итогам чтения
>
> **Технические работы** (инфраструктура, базы данных, скрипты, CI, миграции,
> настройка сервисов) сюда **не пишутся** — они идут в отдельный
> технический журнал, который в публичной витрине не публикуется.
> Правило: если запись описывает, *что мы узнали или добавили в знание*, — она
> здесь; если *как устроен инструмент*, — в технический журнал.
>
> При превышении 500 записей — ротация: переименовать в `log-YYYY.md`, начать заново.

## [2026-09-19] ingest | Kawasoe 2026 — Housing Requirements, Hazard Exposure and Resilience Costs (World Bank WPS11451)
- Source: documents.worldbank.org (свободный доступ), PDF 3.2 МБ, 52 с.
- Extraction: pymupdf4llm → markdown, 98 141 символов, без OCR
- DOI: 10.1596/1813-9450-11451; пакет воспроизводимости reproducibility.worldbank.org/catalog/636
- Суть: первая глобальная странового уровня оценка спроса на строительство жилья
  до 2100 с одновременным учётом демографии, климатических опасностей и
  бюджетной способности. Фонд растёт с 2,46–2,48 млрд единиц (2025) до
  4,10–4,55 млрд к 2100; спрос смещается от приростного к восстановительному
  к середине века; фонд в жароопасных зонах +267…412%; 46 стран с тройным
  бременем
- Файлы: papers/kawasoe-2026-housing-requirements-hazard-resilience-2100.md,
  reviews/..., raw/papers/...pdf
- Гипотеза для реестра: доля восстановительного спроса в России достигнет
  приростного не позднее 2050 (с учётом высокого износа фонда — раньше
  мирового тренда)

## [2026-07-16] ingest | Batch: Workpapers (20 PDFs)
- Source: ~/research-wiki/raw/papers/Workpapers/ (20 PDFs uploaded via scp)
- Extraction: pymupdf4llm → markdown (20/20 success)
- SCHEMA.md updated: domain changed to «Экономика жилья, ипотечного кредитования и рынка недвижимости»
- Analysis delegated to 3 parallel sub-agents (ипотека/субсидии, цены/инфляция/стройка, макро/международный)
- Pages to be created after analysis completes

## [2026-07-16] ingest | Wiki pages from batch ingest
- **Entities (2):** bank-rossii.md, lgotnaya-ipoteka.md
- **Concepts (5):** zhilischnaya-inflyaciya.md, dostupnost-zhilya.md, effekt-zamescheniya.md, regionalnaya-differenciaciya.md, ozhidaniya-ceny-zhilya.md
- **Comparisons (1):** subsidirovanie-mezhdunarodnyi-opyt.md
- Total: 8 pages with cross-references
- All pages added to index.md

## [2026-07-16] ingest | Academic literature: monetary policy and housing market
- Sources: 4 seminal papers (Iacoviello 2005, Taylor 2007, Mishkin 2007, Chodorow-Reich & Mehrotra 2026)
- Extracted via pymupdf4llm → raw/papers/workpapers-monetary-policy/
- SCHEMA.md updated: added 4 new tags (monetary-policy, mortgage-pass-through, collateral-constraint, housing-cycle)
- Pages created:
  - concepts/transmisionnyi-mehanizm-dkp-zhile.md — 6 channels Mishkin (2007)
  - concepts/collateral-constraint-channel.md — Iacoviello (2005) DSGE model
  - concepts/shelter-inflation-optimal-monetary-policy.md — Chodorow-Reich & Mehrotra (2026) "unorthodox view"
  - queries/zhilishchnye-cikly-i-monetarnaya-politika.md — Taylor (2007) counterfactual analysis
- Total: 4 new pages, updated 3 existing pages (zhilischnaya-inflyaciya, dostupnost-zhilya, bank-rossii)
- All pages added to index.md (total: 13 pages)

## [2026-07-16] ingest | Russian research cluster: monetary policy transmission to housing
- Sources: 4 Russian papers
  - Sinyakov & Shelovanova (2023, ЦБ РФ WP120 → RJE 2025): interest rate elasticity weak (1.5-2.3% per 1pp)
  - Demidova & Shchankina (2025, HSE/RAS): ECM for 85 regions — transmission broke in COVID/SWO (from 76 to 4 regions)
  - Zvereva (2025, CBR+HSE, RJMF): regional asymmetry + spatial spillovers
  - Smirnova (2025, Econs.online): double function of housing, 5 transmission channels, "irrational exuberance"
- Extracted via web_extract + pymupdf4llm → raw/papers/russian-monetary-policy-housing/
- Pages created:
  - concepts/rossiyskie-issledovaniya-transmissii-dkp.md — synthesis of 4 Russian papers
- Total: 1 new page, total becomes 14 pages

## [2026-07-16] ingest | Macroprudential policy on housing market (Step 3)
- Sources:
  - Kuttner & Shim (2013, BIS WP433): 57 countries, 9 policy tools, DSTI limits most effective for credit, housing taxes for prices
  - ЦБ РФ press release (April 2025): МПЛ and надбавки on mortgages, consumer credit, auto credit
  - Лаптева Е.В. (2025, HSE Economic Journal): GMM dynamic panel, 591 banks, 2015-2021, MPP dampens credit growth with 2-quarter lag
- Pages created:
  - concepts/macroprudentialnaya-politika-rynok-zhilya.md — synthesis of international + Russian experience, policy comparison
- Updated index.md (total: 16 pages) and log.md

## [2026-07-16] query | Role of expectations in monetary-housing transmission
- Created conceptual page synthesizing expectations channel across all 8 papers
- Key findings:
  * Household inflation expectations positively correlated with loan demand (Sinyakov 2025)
  * "Irrational exuberance" particularly strong in Russia (Smirnova 2025): housing as inflation hedge
  * Expectations can dominate interest rate channel → weak monetary transmission
  * Policy implications: forward guidance, communication, expectations management
- Cross-cutting theme connects: Mishkin's expectations channel, Taylor's counterfactual, Chodorow-Reich's measurement issues, Russian evidence (Sinyakov, Demidova, Smirnova, Zvereva)
- File: concepts/rol-ozhidanii-v-monetarnoi-politike-i-zhilishchnom-rynke.md
- Updated index.md (total: 17 pages)

## [2026-07-16] query | Comprehensive analysis of monetary-housing interaction
- Created final synthesis document linking all 8 conceptual pages
- Structure: 6 key findings, connections between concepts, policy implications for CBR
- Key results:
  * Weak monetary transmission in Russia (elasticity 1.5-2.3%, pass-through broken)
  * Double function of housing amplifies effects (consumption + investment)
  * Expectations channel can dominate interest rate channel
  * Macroprudential policy as complement (not substitute)
  * Optimal policy mix: rule-based MP + targeted MPP + improved communication
- Policy recommendations for ЦБ РФ: anchoring expectations, restructuring subsidized mortgages, optimizing MPP, monitoring expectations, looking through shelter inflation
- Diagram of connections between concepts
- Future research directions: empirical (quantifying expectations), theoretical (DSGE with expectations), policy evaluation
- File: queries/sintez-monetarnaya-politika-i-rynok-zhilya.md
- Total pages: 18 (added final synthesis)

## [2026-07-16] query | Bibliography on monetary policy and housing
- Created master bibliography document covering all 13 research papers from Steps 1-3
- Organized by: (1) International theories, (2) Russian empirical studies, (3) Macroprudential policy
- File: queries/monetarnaya-politika-i-rynok-zhilya-kompleksnaya-bibliografiya.md
- Links to all 6 conceptual pages + raw papers inventory
- Key synthesis: monetary policy less effective in Russia (weak transmission, subsidized mortgages), macroprudential tools become primary risk-management instrument
- Updated index.md (total: 16 pages)

## [2026-07-16] ingest | Batch 2: 26 papers (PDF→markdown)
- Sources: ~/research-wiki/raw/papers/ — 26 PDFs uploaded via scp, converted via pymupdf4llm
- New international papers:
  - BIS Bulletin 89 (Banerjee et al., July 2024): "Housing Cost: The Last Hurdle on the Last Mile of Disinflation?" — housing costs as persistent inflation component, policy implications
  - Bank of England Staff WP 1115 (Albuquerque, Lazarowicz, Lenni): "Monetary transmission through the housing sector" — comprehensive review of housing channel
  - NBER WP 33436 (Allen & Arkolakis, Jan 2025): "Quantitative Regional Economics" — unified framework for economic geography
  - SSRN 4679195 (D'Amico, Glaeser, Gyourko, Kerr, Ponzetto, Dec 2023): "Why Has Construction Productivity Stagnated? The Role of Land-Use Regulation" — regulation reduces builder size → limits scale & tech investment
  - ECB WP 3018 (Furbach): "Non-homothetic housing demand and geographic worker sorting" — housing expenditure shares decline with income
  - Harvard JCHS (2024): "America's Rental Housing" — comprehensive US rental market data
  - ADB WP 362 (Doling, Vandenberg, Tolentino, 2013): "Housing and Housing Finance — Links to Economic Development and Poverty Reduction"
  - Bank of Spain WP 2502 (Bardoscia et al., 2025): "Impact of Prudential Regulations on UK Housing — Agent-Based Model" — LTI caps + capital requirements
  - Fed FEDS 2022-061r1: "Beliefs, Aggregate Risk, and the U.S. Housing Boom"
- New Russian papers:
  - Лысенко Г.В. (Вопросы экономики, 2025, №1): "Макроэкономические факторы цен на жилье в России" — BVAR with sign restrictions, 7 structural shocks. Key findings: oil prices → demand channel (1% oil → +0.01% relative house prices); exchange rate explains up to 43% of mortgage credit variance; housing supply shock → +CPI (wealth effect); monetary shock explains up to 30% credit variance
  - Жирнов Г.А. (Вопросы экономики, 2025, №1): "Массовая льготная ипотека: продлевать нельзя завершать" — substitution effect analysis, 9 trln rub portfolio
  - Гафарова Е.А. (Финансы: теория и практика, 2023): "Гетерогенность канала рефинансирования ипотеки в российских регионах" — panel data, refinance channel heterogeneity
  - Ломиворотов Р.В. (Прикладная эконометрика, 2015, №38): "Использование байесовских методов для анализа ДКП в России" — BVAR for monetary policy transmission
  - НРА аналитический обзор (июль 2024): "Жилищное строительство: неопределенность после отмены льготной ипотеки" — construction sector 5% VA, 9% GDP
  - Стерник С.Г., Стерник Г.М. (2018): "Методика прогнозирования ввода на локальном рынке" — forecasting methodology
  - АКРА (2024): "Российские девелоперы" — developer sector analysis
  - Горлова О.С. (Управленческий учет, 2023): соц-экон факторы ввода жилья
  - Малкина М.Ю. (2013): спрос/предложение на рынке недвижимости России
  - Шишкина и др. (2023): региональный рынок при проектном финансировании
  - Ахмедова, Алексеева (2023): эффективность инвестиций в жилищное строительство
  - Шулекин, Шулекина: цифровая трансформация регулирования жилищного строительства
- Concepts updated: econometric-models-housing-market.md, transmisionnyi-mehanizm-dkp-zhile.md
- Index updated. Total papers in raw/papers: ~60

## [2026-08-25] ingest | AI Mindset cases: Academic Research + Research Planning and Content Tagging
- Sources: base.aimindset.org case-Academic-Research, case-AI-for-Research-Planning-and-Content-Tagging (both 21.08.2026)
- Extraction: curl direct, Quartz static HTML -> article block
- Created: queries/ai-mindset-research-planning-case.md (both cases, RU summary + pipeline mapping)
- Updated: index.md (2 new query entries)
- Key takeaway: extraction/publishing stronger than case; gaps = LLM research-plan/gap generation, auto-tagging with confidence, auto-review assembly

## [2026-09-08] query | Gap-map, гипотезы H-002..H-006, противоречия X-002..X-003
- Created: queries/literature-gap-map.md (матрица 9 вопросов, 5 приоритетных пробелов: firm-level эластичность, escrow-канал, mixed-frequency nowcasting, dual system ставок, асимметрия ДКП)
- Updated: hypotheses.yaml: +5 гипотез (H-002 financial-constrained supply elasticity; H-003 escrow release → starts; H-004 замещение × спред; H-005 МПЛ × эластичность региона; H-006 MIDAS Wordstat+GDELT+ЕИСЖС vs AR) и +2 противоречия (X-002 расхождение индексов цен 1.1/1.37/4.1%; X-003 асимметрия ДКП US-литература vs РФ-эмпирика)
- Updated: index.md (1 query entry)

## [2026-09-08] query | Дизайн публикации: nowcasting ВНОК/ИКВ
- Created: queries/vnok-nowcasting-design.md (целевые ряды: ВНОК IFO 56 кв. SA + ИКВ 25 кв. + 96 рег.; 6 блоков предикторов с скорингом пилота; стек bridge/MIDAS/MF-VAR/DFM/ML/firm-level по IMF WP 22/52, Bundesbank DKP 26/2014, Hong et al. 2026, ЦБ WPS 8/КПМ; план 5 этапов; риски: малая выборка, эскроу 2022+, слом 2026Q1)
- Created: models/nowcasting/vnok-icv-midas.md (карточка H-007/H-008, пилотные corr перенесены)
- Updated: hypotheses.yaml +H-007 (эскроу lag2 ≥0.7, testing) +H-008 (firm-level блок −10% RMSE, active)
- Updated: index.md (1 query entry)
- Обзор международного опыта nowcasting GFCF: queries/vnok-nowcasting-international-review.md — 9 классов, ключевые: Kuzin et al. 2011 (MIDAS 0-4 мес > MF-VAR 5-9), MFBVAR лидер РФ (Станкевич 2020, Фокин 2023), Gareev 2020 (ML уже для GFCF РФ), Tarsidin 2018 (цемент-прокси кросс-страново), Макеева-Станкевич 2022 (прямой прототип). Дизайн и карточка обновлены: +MFBVAR в бенчмарки, +горизонты
- Вторая итерация обзора: дополнения в queries/vnok-nowcasting-international-review.md — U-MIDAS границы применимости, Жемков 2021 (MF-FAVAR неустойчив 1.79-2.38), Hong 2026 точные RMSE + bellwether-эффект, Degiannakis 2022 (фондовый рынок→GFCF, структурный аналог эскроу), Polbin-Shumilov 2025 (квантильный MIDAS РФ), ограничение БФО годовой частоты → vintage-дизайн actualBfoDate

## [2026-09-09] ingest | Петрова–Трунин 2023 (EPU-РФ) — разбор + H-009/H-010
- PDF статьи + приложения прочитаны; разбор queries/petrova-trunin-epu-rf.md
- hypotheses.yaml: +H-009 (EPU в nowcast ИКВ, active), +H-010 (EPU × эскроу взаимодействие, proposed)
- Ключевые факты:
  - epu_new (4 СМИ, 1999-2022) vs RVI corr 0.855; epu_bbd vs RVI 0.525 — модифицированный индекс лучше оригинального Бейкера-Блума-Дэвиса
  - Шок EPU → инвестиции −0.45 п.п. через 2 кв. (значимо до 4-го); epu_bbd незначим для инвестиций — канал реальных опционов
  - Расширения категории «политика» робастны (corr 0.992-0.999, Приложение 1)

## [2026-09-11] data | GDELT GKG fetch за 2026-09-10
- Cron-прогон `scripts/gdelt_fetch.py`: 96 hourly-файлов, 119 837 строк GKG, отфильтровано 7 записей по RUS → `data/raw/gdelt/gdelt_gkg_rus_20260910.csv`.
- Уровень в норме для этого фильтра (ср. 20260909: 3 строки, 20260907: 19 строк).

## [2026-09-14] ingest | arXiv-скан по фокусу реестра гипотез + карточка ML-зомби
- arXiv-скан (7 фокусов, после радара 2026-09-14): новых работ по открытым пробелам нет; escrow=0 результатов по всей базе arXiv (ниша свободна); nowcasting construction — ложные срабатывания (метеорология, металлы, GDP)
- Created: queries/ml-zombie-firm-classification.md — Bargagli-Stoffi et al. 2023 (arXiv 2306.08165): XGBoost предсказание дистресса 304 906 итальянских фирм с неслучайными пропусками отчётности как признаками; зомби = 3+ года выше порога; превосходит Z-score/Distance-to-Default
- Применимость: H-002 (зомби-статус как контрол финансовой слабости), H-008 (фильтр слабых фирм перед агрегацией); ключевой перенос — пропуски как признаки для панели ФНС (87% УСН, filed=1 AND line_2110>0)
- Отличие от BIS 1375 комплементарное: BIS — определение класса на firm-bank данных, итальянская работа — предсказание класса из публичной отчётности (доступно нам на ФНС/СПАРК)
- index.md: +1 entry (Queries)

## [2026-09-14] query | Research Radar (еженедельный скан литературы)
- Created: queries/research-radar-2026-09-14.md — 4 работы за 7-дневное окно (NBER/SSRN/arXiv/Philly Fed/BIS); Graybill–Mangum 2026 (WP 26-33R): покупатели чувствительнее к ставке, чем продавцы к lock-in → X-003 evidence_for пополнен (patch в hypotheses.yaml, дата проверки); идеи: survival-модели tenures → эскроу-балансы (H-003), дюрации ЕИСЖС как блок H-006, зомби-классификация BIS 1375 → контрол H-002; пробелы №1 (firm-level эластичность) и №2 (escrow shock) остаются открытыми — конкурентов не появилось

## [2026-09-17] ingest | Разбор Retrieve-for-Train (Google Research)
- Создана queries/retrieve-for-train-google.md: разбор ICML 2026 arXiv:2603.06397.
- Суть: RL-компиляция fan-out поиска в диффузионный ретривер (53.9M), 12-20x быстрее.
- Ключевое: композитная награда из 3 взаимных контр-якорей (groundedness x alignment x diversity через Vendi Score); без diversity модель деградирует (абляция).
- Критические оговорки: домен мультимодальный (fashion/music), не текстовый; обучение 4B-моделей разово, но тяжело; цифры от заинтересованной стороны.
- Применимость: парафразный коллапс в Wordstat-композите (H-001) + мерило разнообразия набора HF-регрессоров.

## [2026-09-20] data | этап 1 конвейера — реестр кандидатов рабочего набора

Создан детерминированный генератор scripts/metric_registry.py и первый реестр статусов всех 2438 метрик (registry.yaml + registry_summary.csv в data/etl/metric-review/): 1833 preliminary (живые, ждут паспортов этапа 2), 601 archive_dead (последний период до 2024-01, включая содержательно ценные — статус данных, не значимости), 4 quarantine_data_error с доказательствами (spv: объявлена годовая/фактически месячная за одну дату; kep1_112: годовые значения колонки «Янв.» как месячные; kep4_45/46: наблюдения в будущем 2026-10..12 — вероятен сдвиг парсинга годовых блоков). Тематические метки единого набора «Экономика и ДКП РФ»: construction 466, housing_mortgage 285, dkp_macro 75 вхождений. Прямая SQL-верификация дефектов против живой БД выполнена; баланс статусов сходится 1833+601+4=2438; YAML-CSV сверены попарно.

## [2026-09-20] data | этап 2, партия 1 — паспорта семейства СМР/ИКВ

Созданы evidence-паспорта 17 метрик семейства СМР/ИКВ (data/metric-review/passports/smr-ikv.yaml): сверка с шапками и сносками ind_07-2026.xlsx (листы 1.6/1.7/1.8) + живой SQL. Находки: (1) orsmr/orssp — дубли kep1_72/kep1_7_y2 (значения совпадают точка в точку) из socio_economic_report с фиктивной квартальной частотой при месячных периодах — карантин, канонические ряды kep1_72/kep1_7_y2; (2) iokmrrk — нарастающий итог с начала года (2024: 5.94→14.4→24.1→39.9 трлн), отдельный квартал только через diff с январским reset; (3) kep1_7_m2 — суффикс _m при QoQ-частоте, суффиксы имён не источник семантики; (4) vsii/vvdsotrs/tkzk — единицы unknown в БД, к проставлению на этапе применения. Статусы реестра обновлены (карантин 6: +orsmr/orssp).

## [2026-09-20] data | этап 2, партия 2 — паспорта ипотека/эскроу/ДДУ

Паспорта 23 метрик контура (data/metric-review/passports/mortgage-escrow.yaml). Находки: (1) ebs в observation_v2 — СМЕШЕНИЕ МАСШТАБОВ: 2022-2024 ~0.3-1.65 млн, 2025-01—2026-01 ~9.4-10.7 (иная величина, вероятно доля в процентах), 2026-02+ ~7.25 млн; карантин, канонический источник — SQLite escrow_monthly (бенчмарки H-007 не затронуты); (2) spsipflrrtmrsrf — точный дубль sit — карантин; (3) nikfi/nikfr/nikfi_2 — раскладка сходится (инвалюта+рубли=итого), инвалюта после 2022 ничтожна; (4) ДДУ ДОМ.РФ (01_03_04/01_03_06) — значения корректны, но sub_dimension замусорен номером строки парсинга; (5) ставки sit/sibud/sid — period_average (средневзвешенные), НЕ темп; история только с 2025-06; (6) ksdrk — subdim дублирует region_id. Реестр: карантин 8, preliminary 1829. Коммит fe2d55a.
## [2026-09-20] data | этап 2, партия 3 — паспорта ДКП-макро

Паспорта 24 метрик макроконтура (data/metric-review/passports/dkp-macro.yaml). Находки: (1) ГЭП — в каталоге НЕТ ключевой ставки, М2, межбанка, курса: ДКП-контур неполный без прямых рядов ЦБ, требуется подключение источника; (2) kep1_14 и kep1_14_s — НЕ дубли (mom 100.5 против yoy 106.0), пара баз сравнения ИПЦ; (3) ippsm — протечка регионов в subdim при region_id=1 (ХМАО, Севастополь внутри РФ-строки), для РФ брать subdim-пусто, чинить загрузчик; (4) orspp — 2 из 3 точек == kep1_7_m, последняя расходится (101.1 vs 100.4) — канон kep1_7_m подтверждён листом 1.7 стр.92, needs_link; (5) vzep/vztp — по 1 наблюдению (low value), vzepz подозрителен на сдвиг дат (1353 на 2026-01 и 2026-06); (6) snz (зарплата) чистый региональный ряд 15 тыс. obs. Реестр статусов не менялся (находки — needs_link/low_value в паспортах).

## [2026-09-20] data | этап 2, партия 4 — паспорта ввод/проекты/демография; этап 2 ЗАВЕРШЁН

Паспорта блоков ДОМ.РФ группами (data/metric-review/passports/housing-demography.yaml): ДДУ по двум периметрам (01_03_01-03 декларации vs 01_03_04-06 жилые помещения — НЕ дубли, разница 1.5 процента легитимна), 39 рядов проектов МКД по стадиям (01_02_*), демография и цены — отсылками. Главный дефект блока — субдим-мусор парсера на всех 01_* (один миграционный скрипт закроет ~50 рядов). Этап 2 конвейера закрыт: 4 партии, ~130 метрик паспортизированы прямо или группами, реестр 1829 preliminary + 601 archive + 8 quarantine.

## [2026-09-20] data | этап 3 — пилот GLM vs Astra завершён

60 метрик, эталон из паспортов этапа 2, 40 tuning / 20 holdout, два условия. Итог: evidence-пакет даёт 100% temporal_type и comparison_base на holdout у обеих моделей (name_only: 0.85–0.875); разница между моделями исчезает при наличии evidence. GLM — пустые ответы в 1 батче из 4 (reasoning-особенность), Astra стабильна. Стоимость полного прогона $0.35. Единственная ошибка обеих моделей в evidence (kvrse) — ошибка моего gold-лейбла (раскрытия за месяц = flow), исправлена. Решение по эскалации: правила → GLM+evidence (ретрай, фолбэк Astra) → Astra для целевых/конфликтных + 10% контроль. Отчёт: queries/pilot-llm-annotation-results.md.

## [2026-09-20] data | этап 4 — массовая разметка 1829 метрик завершена

GLM+evidence 1489, фолбэк Astra 340 (19%), покрытие 1829/1829, стоимость $0.90. Контроль Astra 2% (34 метрики): 18 расхождений, из них 11 несущественные (null-vs-value, консервативность GLM), 7 содержательных — серия «ввод мощностей» (accumulation период vs накопительный, без сверки листа однозначного ответа нет) и один ИЦП-базис (GLM совпадает с паспортом). needs_review: 8 метрик. Главная ценность: 334 ряда накопительного итога опознаны (словарь «накопленным итогом»/«cumulative» — кандидат в детерминированные правила). Распределения: flow 933 / stock 256 / index 381 / ratio 172 / average 51 / price 36. Слой предложений готов к утверждению (этап 5). Отчёт: data/metric-review/mass/MASS-REPORT.md.

## [2026-09-20] data | этап 4б — кросс-контроль фолбэков (Ollama glm-5.3-flash)

GLM на Nous исчерпала кредиты (402 на любом max_tokens, бин. поиск 4000→10). Кросс-контроль 340 фолбэков перенесён на Ollama Cloud glm-5.3-flash ($0.15/$0.50 за 1М; расход прогона ~$0). Выборка 36, батчи по 8: 12 распарсено, 3 батча — пустой ответ (0 байт, reason съеден — ретраи не помогли), итог проверено 12/36. Расхождения 2/12 (16.7%): id=398 y477130016 temporal_type ratio↔average (обоснованно — «в среднем на одного», среднегодовой ряд; прав GLM: average), id=1136 drpotr accumulation ytd↔single (note пустая; drpotr = квартальный поток по прибылиным орг., прав GLM: single_period, накопительный итог — у pnitmk-семейства). Оба решения — за GLM. Вывод: фолбэк-слой 340 требует доработки: 12/36 проверены, 24 не покрыты (GLM на Ollama нестабильна по длинным батчам); следующий шаг — добить оставшиеся 24 малыми батчами по 4.

## [2026-09-20] data | этап 4б-2 — кросс-контроль фолбэков: сверка расхождений по значениям БД

Второй прогон (батч 4): проверено 20/36, расхождений 6 (30%); 4 батча всё ещё пустые (GLM-на-Ollama нестабильна на длинном reasoning). Все 6 расхождений разрешены сверкой фактических рядов в БД: id=1136 drpotr — накопительный (монотонный рост 97.7М→431М в 2025, сброс в январе; прав Astra); id=55892 kep1_14_s2 — ytd + same_period_last_year (январь 101.7≈100, монотонный 2026; обе частично правы); id=398 — average (прав GLM); id=1597 — ytd (прав GLM); id=1606 — single_period (плоский ряд, прав Astra); id=1419 — данных недостаточно. Вердикты записаны в fallback_control.json. Покрытие контроля: 20/36 проверено, 16 остались без перекрёстной проверки (пустые ответы GLM на Ollama) — фолбэк-слой помечается «проверка частичная».

## [2026-09-20] data | этап 5 — семантический слой применён в БД

Создана derived.metric_semantic (1821 строку из 1829; 8 needs_review исключены: 7 ввод-мощностей + y477110132) + вьюха derived.v_metric_semantic (JOIN с core.metric, частота по-русски). Идемпотентная запись (ON CONFLICT, jsonb-чанки по 200). Распределение: glm 1482 / astra_fallback 339; control_status: verified 1482, partial 339 (фолбэк без полного кросс-контроля); temporal_type: flow 926, index 380, stock 256, ratio 172, average 51, price 36. Before-image: data/metric-review/mass/before-image-semantic.json (1829 предложений). Откат: DROP TABLE derived.metric_semantic (таблица отдельная, stat_profile шага-1 не тронут). Шаг-1 разметка в derived.metric_enrichment остаётся как есть.
- 2026-09-20: H-007 перекат на 2026Q2 (corr +0.60, эскроу ближе к факту в точке разворота; протокол queries/h007-escrow-roll-2026q2.md); ikv_rf_quarter + 2026Q2
- 2026-09-20: полный стек benchmarks перекат на 2026Q2: esc+cem RMSE 2.86 vs AR 8.04 (robust), 26Q2 прогноз 96.6 vs факт 93.4 (AR 85.9); детали в queries/ikv-nowcasting-pilot.md
- 2026-09-20: ИБК-сканы (ЦБ мониторинг Строительство): спрос+цемент RMSE 2.42 vs AR 5.58 на Δy; ожидания не работают; прогноз 2026Q3 yoy ИКВ ≈ 90.0; детали в queries/ikv-nowcasting-pilot.md
- 2026-09-20: полный стек с ИБК на Δy: AR+cem+esc 2.61 лучший; ИБК в паре с cem нейтрален на длинном train; комбинации Hellinger-CES 4.17 не бьют сингл; ragged-edge аргумент за ИБК (своевременность)
- 2026-09-20: SA-цель ВНОК IFO 57 кв.: регрессоры стройканала слабеют (цемент +0.10), AR+cem+dem 4.65 vs AR 5.08; вывод — ИКВ основной таргет для стройблока, ВНОК валидация
- 2026-09-20: запущен сбор госрасходов на инфраструктуру: fedbud_naecon_quarter 2011-2021 в БД; делегат добирает раздел 12 (дорожное хоз-во) 2022-2025 из СП/Росавтодора

## 2026-09-21
- queries/github-replication-repos-202609.md: итоги поиска GitHub-репозиториев с репликационным кодом (журнал «Деньги и Кредит» пакетов не публикует; найдены uncertainty_index, seasonal_bankofrussia, REBORN/Economica, massResearch_houses, Sberbank housing benchmark); 2 гипотезы.
- 2026-09-21: недельный прогон rosstat monthly: Prom_08_2026 ещё не опубликован (404, выйдет ~26.09) — физобъёмы августа переносим; обновлён sezon_2023_07-2026.xlsx → rosstat_ind_prod_saar: исправлена июльская запись IPP (переставлены mom_saar/base_fact: 102.9↔100.1), восстановлены SAAR-колонки секций B–E за июль; СС-обработка июль 99.8 м/м. Новый скрипт scripts/rosstat_sezon_parse.py (идемпотентный upsert). Приложение в queries/ikv-nowcasting-pilot.md.
- 2026-09-21: queries/research-radar-2026-09-21.md — недельный скан (nep-hre 14/21.09, NBER, BIS, IMF, CAGE, FRBSF): 7 работ; статусных изменений в hypotheses.yaml нет (все методологическая/контекстная поддержка): CBI LTI-рекалибровка → качественная поддержка H-005 (регион. гетерогенность МПЛ), Datta et al. CAGE 16 млрд housing searches → методологический прецедент H-001/H-006, EREI (Koetter et al.) corr 0.94-0.97 листинг-vs-транзакция → рамка для X-002, Panagiotidis et al. housing-EPU Греция → блок-кандидат H-009/H-010, Louie et al. FRBSF 2026-18: эластичность предложения = LATE, не структурная (дизайн H-002), Ahlfeldt-Baum-Snow-Jedwab высотность (welfare +3.7% развивающиеся), Beyer et al. IMF 2026/177 (supply-side драйверы ЕС, ~1 млн потерянных переездов). Новые идеи: housing-specific EPU-РФ, листинг-vs-транзакция декомпозиция X-002, spatial поисковый спрос. Пробелы №1 (firm-level эластичность) и №2 (escrow) — по-прежнему открыты, конкурентов нет.
## 2026-09-21
- Спрос-первичен: ревизия семантики spatial-разреза поискового спроса (поиск → сделки/выдачи ИЖК → ввод, ступенями) — queries/spatial-search-demand-semantics.md; гипотезы H-012 (насыщение→цены), H-013 (готовность когорт→ввод), H-014 (поиск→выдачи). Разведка платформа.дом.рф (19 наборов, капча на файлах) и ЕРЗ API. Коммит:
## 2026-09-21 (продолж.)
- СберИндекс v2: source sberindex + 48 942 obs / 10 метрик (b399605); карточка ЦБ: source_links из CBR_ИпотекаРФ.txt (6f7d763)

## [2026-09-21] hypothesis | категория публичных прогнозов участников рынка
- Заведён реестр публичных прогнозов `data/market-forecasts.yaml` (схема в шапке:
  published/org/person/period/target_var/forecast/baseline/hypothesis/sources/
  related_h/realized/verdict) — внешний бенчмарк наукастов ИКВ и СМР + источник
  гипотез.
- Постановка задачи на перспективу и место в пайплайне —
  `queries/prognozy-uchastnikov-rynka-plan.md`.
- Первая запись MF-001: Сбер (Исаков), сентябрь 2026 — III кв ИКВ −1,8% yoy,
  «отскок от провального I кв, а не новый цикл», порог оживления — конец 2027
  при ставке ~12%. Фальсифицируемая часть → H-015 (три проверяемых условия
  Г1–Г3 в next_check).

## [2026-09-24] query | модельный sitrep к СД 23.10.2026 (kanban t_a95e2d05)
- Записка `queries/model-sitrep-202610.md`: наукастинг инфляции (август 6,33% г/г,
  базовая 5,37%, устойчивая 5–6% с.к.г.), спроса (реальная розница июль −0,6% г/г,
  ИКВ 2к26 +6,4% г/г номинал, ИБК сентябрь −2,3 п.) и разрыва выпуска (Y_GAP 0±0,3 п.п.).
- Индикатор правила КПМ ДДКП воспроизведён из опубликованного кода ЦБ
  (qpm_model.mod:770–775, parameters_main.mod): implied RS при E3_PIE4_MP=5,38 —
  13,0–13,9% (RN 8–11,5); hard-калибровка (gamma2=1,9) воспроизводит удержание 14,00%.
  Вывод: базовый исход СД 23.10 — пауза; cut 25 б.п. — только при подтверждении
  дезинфляции сентябрьской статистикой; повышение правилом не поддерживается.
- Расшифровка «ИБК −2,3 SA» из постановки: индикатор бизнес-климата (Мониторинг
  предприятий 09/2026, опрос 1–9.09, 13,4 тыс. предприятий), не ИА-комментарий.
- Скачаны в raw/cbr/: CPD_2026-8.pdf («Инфляция в России» №8, 16.09.2026),
  mp_0926.pdf (Мониторинг предприятий, 15.09.2026), inFOM_26-09.pdf (ожидания).
- needs_source_check: сентябрьские ожидания населения (11,0% — с графика inFOM),
  точечный наукастинг сентября 6,3–6,8% г/г до недельной ленты ЦБ.
- Расчётные скрипты — workspace kanban t_a95e2d05 (rule_calc.py, rule_table.py,
  rule_grid.json); при переносе в репозиторий — scripts/model_sitrep_*.py.

## [2026-09-24, вечер] update | модельный sitrep: сняты needs_source_check (kanban t_e8d80e8e)
- inFOM 26-09: точечный разбор рис. 1 из PDF (векторные пути + калибровка оси Y,
  ошибка ≤0,07 п.п. на всех 99 подписях) — scripts/model_sitrep_infom_parse.py,
  данные data/model_sitrep_infom_medians.csv. Сентябрь: ожидания населения 14,2%
  (после 13,7% в августе, 14,7% в июле), наблюдаемая 15,1% (после 14,3%),
  ожидания на 5 лет 10,7% (после 12,4%). Внешняя сверка: пресс-релиз ЦБ 26.08
  (cbr.ru/press/event/?id=32795), RBC 22.09.2026 — значения совпали.
- Исправлена ошибка черновика: там сентябрьские ожидания были прочитаны как ~11,0%
  «с графика» (сдвиг при чтении склеенных чисел текстового слоя), а снижение
  «13,7 против 14,0 в июле» — фактически 14,7. Вывод скорректирован: ожидания
  населения в сентябре выросли, оба канала ожиданий (население и бизнес) повышены.
- Недельная статистика Росстата за сентябрь: 1–7.09 +0,05% (г/г 6,29%), 8–14.09
  +0,02% (6,24–6,27%), 15–21.09 +0,06% (г/г 6,26% на 21.09 по методике ЦБ; МЭР —
  6,22% по среднесуточным), накоплено +0,13% (сентябрь 2025: среднесуточный 0,011).
  Точечный наукастинг сентября уточнён до 6,2–6,3% г/г (черновик: 6,3–6,8);
  ЦБ в комментарии к среднесрочному прогнозу ожидает 6,3%.
- Сентябрьский комментарий ЦБ по ожиданиям и XLSX-статформа на 24.09 ещё не
  опубликованы — сверка при выходе (~конец сентября). БД v2: розница КЭП и ИПЦ
  актуальны по июль (проверено через тоннель).
### 2026-09-25 — Чек решения СД 11.09 и Резюме 23.09
- [sd-check-1109-summary-2309.md](sd-check-1109-summary-2309.md): чек предыдущего решения (ставка 14,00%, пауза) и Резюме обсуждения 23.09; числовые совпадения с пресс-релизом полные, расхождений нет. Ключевые добавления резюме: диагноз топливного импульса (косвенные/вторичные эффекты), дискуссия о повторном открытии положительного разрыва выпуска, раскол по жёсткости ДКП, обоснование отсутствия сигнала. Модельные следствия: implied-ставка диапазоном (базовый/жёсткий), калибровка склонений по устойчивой части инфляции; подтверждение гипотезы 1 о весе базовой инфляции 0,75 в E3_PIE4_MP.
### 2026-09-25 — Загружен доклад ЦБ «Региональная экономика: комментарии ГУ» № 30 (сентябрь 2024)
- raw/papers/cbr_gu_report_30_sep2024.pdf (+.txt извлечённый текст, 51 с., 130,6 тыс. знаков). Структура: «Россия в целом», ключевые тенденции по 7 ГУ, инфляционная карта регионов, врезки (региональные бюджеты, экспортные возможности, производство стали), приложение с показателями. Опора: мониторинг ~15 тыс. предприятий (в августе 2024 — 11 841) плюс качественная информация ГУ. Доклад рассматривается руководством ЦБ при подготовке решения по ставке — прямой образец для нашей задачи t_cad286e7 (прообраз регионального доклада в формате ГУ).
### 2026-09-25 — Перечень отслеживаемых ДДКП макропеременных
- [ddkp-monitored-variables.md](ddkp-monitored-variables.md): 38 переменных в 6 блоках (инфляция/ожидания, спрос-выпуск-разрыв, ДКУ-трансмиссия, внешние, бюджет, опросные) — извлечены из Резюме 23.09 и сверены с мировой практикой IMF (HTN/2025/003 stance: инфляционный разрыв + разрыв выпуска + разрыв ставки; Adrian-Laxton-Obstfeld 2018 ФПАС; WP/25/109 разметка). Каждая позиция сопоставлена с БД v2: покрытие есть по ~30, пробелы до 08.10 — базовая инфляция отдельным рядом, корпоративный кредит, М2, бюджетное исполнение.
### 2026-09-25 — Прогон: региональный срез v0 (ввод жилья, регион × переменная)
- [region-slice-housing-v0.md](region-slice-housing-v0.md) + data/region_slice_housing_202609.csv: первый прогон формата для докладов ГУ. ЕМИСС 34118, 79 регионов, июнь-август 2026. РФ: плато ~6,1-6,2 тыс. кв. м/мес. Лидеры августа по скорости: Ставропольский +81,7%, Ростовская +33,2%, Башкортостан +27,6%. Методологический вывод: помесячные скорости малых регионов шумные - в докладе ГУ сглаживать 3 месяца; номенклатуры ЕМИСС не размечены в БД (берётся максимум=жилые+нежилые), для чистого жилого ряда - догрузка в v1.
### 2026-09-25 — Инвентаризация рядов по видам жилья для наукастинга ИКВ
- [housing-types-rows-inventory.md](housing-types-rows-inventory.md): по каталогу найдены отдельные ряды: jil_dom-oper (всего жильё + ИЖС населением, месячные, накопительные, 96-98 регионов, янв 2025 - июл 2026); С-1 vv-zd-oper по типам зданий (жилые/нежилые: промышленные/коммерческие/сельхозяйственные/административные/учебные/здравоохранение, плюс население vs юрлица) в SQLite rosstat_buildings_vvod; годовые нежилые 2000-2024 (рекорд 38,4 млн м2 в 2024); ввод мощностей (инвестиционная компонента). Расхождение ЕМИСС 34118 (июль 6192) с jil_dom (7867,8) зафиксировано - нужна ревизия инжеста по номенклатуре. Вывод: набор достаточен для жилищного блока MIDAS-наукастинга ИКВ; нежилые здания (рекордный тренд) - недостающая компонента ИКВ.

### 2026-09-25 — Гипотезы, инжест видов строительства в БД v2, региональная ЕМИСС-партия
- Гипотезы H-017 (нежилые опережают ИКВ на 1 квартал), H-018 (доля ИЖС предиктор замедления 2-3 мес), H-019 (коэффициент ЕМИСС 34118 / jil_dom ~0.79 стабилен) — hypotheses.yaml.
- Инжест видов строительства в PG v2: релиз 95 rosstat_housing_types_2026-09 (source 11), 2 941 наблюдение / 28 метрик: rosstat_c1_{slug}_{area,count} (12 категорий С-1, 2026-03/06, накопительно, РФ), rosstat_nonres_annual_{area,count} (2000-2024), rosstat_housing_{total,pop}_m (по 1 359 регион-месяц из 20 листов jil_dom-oper_07-2026.xls, янв 2025 — июль 2026). КТ: РФ июль 7 867,766; C-1 жилые H1 52 539,2. Скрипты: scripts/ingest_housing_types.py (построчный), scripts/ingest_housing_types_batch.py (батч, ON CONFLICT DO NOTHING). Коммит ee3cb8a, push private.
- Уроки: metric_type ∈ {primary,derived,nowcast_model}; release.status ∈ {registered,parsed,validated,loaded,failed,superseded}; release_id NOT NULL в observation_v2; уникальный ключ включает source_id/release_id/assessment_type/sub_dimension; батч 500 строк через тоннель — секунды; широкие листы jil_dom <8 колонок пропускать.
- Следующий шаг запущен: hermes peer run yc run_4d984ff5d54c453eae3f9cdf2f760934 (idempotency regional-emiss-batch1-20260925) — региональные ряды Росстата через ЕМИСС/fedstatAPIr на ВМ (розница, ЗП, безработица, ИПЦ) в БД v2; приёмка: queries/emiss-regional-batch1.md + КТ по РФ/региону.

### 2026-09-25 — Региональный инжест ЕМИСС v2 завершён (релиз 96)
- Исправленный прогон peer yc (idempotency regional-emiss-batch1-v2-20260925) выполнен полностью, ~55 мин.
- Шаг 0: маппинг ЕМИСС→core.region через dim ОКАТО (57831), 0% неразрешённых, Автономные округа → современные родители; /home/ubuntu/raw/emiss/region_map.tsv.
- Шаг 1: snz (metric 1126) разъехался по регионам — UPDATE 14 804 строк, sub_dimension очищен, 316 дублей удалено; КТ: РФ 2026-05=110216.2 неизменна, Башкортостан 83402.5, Московская 131115.0, Москва 183650.6.
- Шаги 2–4: инжест 4 показателей (release 96, source 25, loaded, 43 867 obs, 85 субъектов): emiss_31260_retail_m (розница мес, свежесть субъектов 2025-01, _rfnn до 2026-07); emiss_57824_wage_m (ЗП до 2026-06); emiss_31074_cpi_prevm_m (ИПЦ % к пред. мес., до 2026-08); emiss_43062_unemp_q (безработица МОТ 15+ кв., до 2026-04). РФ/РФ-без-новых — отдельные метрики _rfnn.
- ДНР/ЛНР/Запорожская/Херсонская — не публикуются в этих разделах ЕМИСС (4 субъекта не покрыты).
- КТ проверены из VPS через db_tunnel: РФ snz, Башкортостан snz, ИПЦ Москва 2026-08 = 99.96 — совпали с отчётом.
- Отчёт queries/emiss-regional-batch1.md, коммит 80502ce. Ограничения: розница субъектная отстаёт (2025-01); безработица 43062 — обе возрастные размерности в одной метрике (ревью); ИПЦ = % к пред. месяцу.

### 2026-09-25 — Этап 1: починка cron Росстата + trudvsem-крон
- Cron 4499ed3c70ee (Rosstat industrial indices monthly refresh) починен: 401 «Missing Authentication header» — сбой web-инструмента, не сайта; rosstat.gov.ru доступен. Данные августа 2026 скачаны напрямую curl -k (ind_baza_2023_08-2026, ind_sub_2023_08-2026, sezon_2023_08-2026, публикация 23.09), структура проверена openpyxl, файлы синхронизированы в yc-s3:wiki-research/raw/rosstat/data/. В промпт джоба внесён обходной канал (cron edit 25.09).
- trudvsem: скрипт scripts/trudvsem_weekly.py (opendata API открыт, без ключа; meta.total по регионам, limit=1). Первый срез 2026-09-25: Краснодарский 21482, Свердловская 17740, Московская 14582, СПб 14306, Москва 3778 (мета-пусто). data/trudvsem_counts.csv. Cron f210dbe02e8c создан (среды 07:00 UTC, идемпотентен). Коммит по trudvsem запушен.
- Остаток этапа 1: 4 пробела данных 38-переменных (базовая инфляция рядом, корп. кредит, М2 — частично закрыты cbr-релизами 88-91; бюджетное исполнение — через ВМ), первый полный региональный срез A/B/C/E/F теперь возможен на базе релизов 95-96.

### 2026-09-25 — Региональный срез v1: первый полный прогон A/B/C/E/F
- scripts/region_slice_full.py → data/region_slice_full_202610.csv (5 867 строк, 11 метрик × 85-86 субъектов × 6 мес). A: ИПЦ до 2026-08; B: ЗП 2026-06, безработица МОТ 2026-04; C: кредиты физ/юр, ИЖК (задолженность/выдачи/ставки) до 2026-06..08; E: ввод жилья/ИЖС до 2026-07; F: snz до 2026-05. Розница исключена (свежесть 2025-01).
- Записка queries/region-slice-full-202610.md. Гипотезы H-020 (разброс ставок ИЖК), H-021 (доля ИЖС модулирует трансмиссию), H-022 (кредит юрлицам опережает нежилые) — hypotheses.yaml.
- virtr = vfs_ihc_rate_total_rub (канонический код короткий). Срез перегенерируется скриптом.

### 2026-09-25 — Шаблон доклада ГУ: «регионы против общероссийского тренда»
- scripts/gu_report_template.py → data/gu_report_template_202610.md (291 строка, 11 блоков A/B/C/E/F): медиана/среднее по субъектам как тренд, топ-15 по уровню с % к пред. периоду, лидеры/аутсайдеры, пометка независимости в каждом блоке. Перегенерация одной командой после обновления среза.
- Первый прогон выявил аномалии для ревью: Свердловская безработица +80% м/м (скачок выбытия?), Москва ИЖК-ставки vs Чукотка +99.5% (малые выборки кредитов), Тамбов кредиты юрлиц +5719% (с нуля) — в итоговый доклад ГУ сглаживать 3 мес и/или фильтровать малые значения знаменателя.

## 2026-09-25 (позже)
- Разбор Резюме СД 23.09 + сопоставление с вектор/граф слоем: queries/summary-2309-layer-crosswalk.md. Инвентарь слоя: 21 аргумент 11.09 (48-68), meeting 104 v2-поля заполнены, dkp.forecast 113 строк (24.07, key_rate_avg 2026 14.5-14.6, 2027 10.5-12.5), dkp.forecast_realized заполнен 2025. Векторные пробы (256-dim): кредитный аргумент непрерывен между заседаниями (sim 0.82-0.87), раскол жёсткости тяготеет к апрельскому credit-аргументу (0.76). Дельта слоя: полный текст Резюме в kb, 52 embedding, concern, dkp.dissent. Гипотезы H-signal/H-dissent/H-confirm продвинуты.
- Дельта dkp-слоя выполнена (scripts/dkp_layer_delta.py): 52/52 эмбеддингов dkp.argument (Yandex 256-dim); Резюме 23.09 инжестировано в kb как doc 1401 (20 чанков с эмбеддингами); concern заполнен (5 uncertainty + 1 surprise); создана dkp.dissent и внесён сентябрьский раскол ДКУ (intensity=soft). Векторная КТ: чанк «выводы» Резюме → top-соседи arg 28 signal 19.06 (0,779) и arg 63 external 11.09 (0,771) — «информативное молчание» читается на фоне июньского easing_bias, как в кроссворке.
- Калибровка по Резюме 23.09 (kanban t_08b8132f): model-sitrep-202610.md дополнен разделом 5 — перевод позиций участников в параметры правила: раскол ДКУ = вилка калибровок gamma2 1,5/1,9 (implied 13,0–14,4% по сетке RN, обе ветви содержат 14,00%); повторное открытие разрыва выпуска совместимо с нашей Y_GAP 0±0,3; отсутствие сигнала → implied-ставка подаётся диапазоном. Декомпозиция base→hard при RN=10,5: DEV +0,21, gamma2 +0,19, Y_GAP +0,06 п.п. (rule_sensitivity.py). Гипотезы зарегистрированы: H-023 (H-signal, событийный тест на РУОНИА 11–12.09 и на СД 23.10), H-024 (H-dissent, корп-кредит/М2 к 20.10), H-025 (H-confirm, доля uncertainty-формулировок в Резюме 24.07 vs 11.09; текст 24.07 в kb не инжестирован — ограничение).
- Инжест инфляционных ожиданий в БД v2 (релизы 101-102, source 7, loaded): (1) релиз 101 cbr_infom_expectations_2026-09 — 7 рядов x 32 мес (янв 2024-авг 2026), 224 obs: медианы наблюдаемой/ожидаемой 1г/5л инфляции и разрез по сбережениям (лист «Данные для графиков» Infl_exp_26-08.xlsx, cbr.ru); (2) релиз 102 cbr_macro_survey_2026-09 — макроопрос аналитиков ЦБ (full.xlsx, mo_br), медианы ИПЦ/КС/ВВП по горизонтам 2021-2029 x 43 опроса, 455 точек (horizon в sub_dimension). КТ: ожидания авг 13,67 (июль 14,70), наблюдаемая авг 14,31; аналитики сентябрь: ИПЦ 2026 6,6, КС 2026 ср. 14,5, 2027 12,43; ВВП 2026 нет (горизонт закрыт), 2027+ есть. Скрипт scripts/ingest_expectations.py идемпотентен (ON CONFLICT DO NOTHING). Внешние источники raw/cbr/Infl_exp_26-08.xlsx + raw/cbr/macro_survey_full.xlsx.
- KKT ФНС (geochecki): разведка API, сбор через monitor (peer run_a032c016), инжест релиз 108 (68 мес РФ + 5961x2 региональных), cron 356c0298e19e (8 числа 06:00 UTC), скрипты ingest_kkt.py + kkt_monthly_job.sh
- ЕИСЖС: разведка наш.дом.рф заблокирована WAF (403 с ВМ/VPS/proxy/headless); предварительный перечень показателей дашборда из открытых источников составлен, верификация ждёт доступа с ноутбука. queries/eisjhs-inventory-draft.md
- ЕИСЖС: сверка дублей с domrf отменена владельцем (исходники скачиваются вручную); создан cron-джоб cfb79a948639 — напоминание 10 числа 08:00 UTC о ручной загрузке выгрузок с наш.дом.рф в raw/domrf/ (ссылки в промпте). queries/eisjhs-inventory-draft.md остаётся справкой по перечню показателей.
## 2026-09-25 — iminfin: аудит следов, восстановление скрапера, релиз 110
- Аудит: сырьё живо (raw/iminfin/2026-09-21, 6 json ~109 КБ + зеркало yc-s3), скрапер /tmp ВМ сгнил, БД v2 — пусто.
- Скрапер восстановлен scripts/iminfin_scrape.js (node, POST /redirect/copen-imon/Data?uuid), свежий снапшот 2026-09-25 снят с ВМ, зеркало синхронизировано в бакет.
- scripts/ingest_iminfin.py: source iminfin, релиз 110 iminfin_snapshot_2026-09-25; метрики iminfin_exp_total_ytd_m / exp_plan_ytd_m / exp_exec_share, 294 точки (98 регионов, частота день, period_start=period_end=дата снапшота); алиасы имён (Татарстан, Кузбасс, Югра, Тюмень без ХМАО и ЯНАО и др.).
- Не инжестировано: трансферты (колонки без легенды: 1 098 923 / 2 022 120 / 2 476 662 млн — семантику уточнить), госдолг (доля только по ФО), история (интерактивные клики), нацпроекты.
- КТ: РФ исполнение 972 602,8 млн / план 2 604 580,6 млн / 37,34 %; Башкортостан 16 484,1 / 31 347,9 / 52,58 %.
- Коммиты: dfb0397 (карточка, 21.09), acd277c (скрапер + инжест).

[2026-09-26] Доступ агента к личному Telegram через пользовательскую сессию: разбор статьи
Разобран материал Хабра «Я дал AI-агенту доступ к своему Telegram» (18.08.2026, habr.com/ru/articles/1071576/): конструкция из трёх слоёв (Pyrogram и MTProto с пользовательской сессией, утилита tgcli как обозримый CLI, файл SKILL.md с триггерами и ограничениями), открытый инструмент github.com/ogleonov/pyrogram-cli (MIT, Pyrogram 2.0.100+, Python 3.10+). Ключевое отличие от нашего действующего уклада: это не бот, а программный аналог Telegram Desktop с правами владельца, поэтому наш инвариант «один бот-токен на профиль» остаётся в силе и этой конструкции не противоречит. Зафиксированы методологически ценные вещи: три разных памяти агента (живая сессия MTProto, локальная выгрузка JSONL на дату экспорта, session_search по своим прежним диалогам с агентом) с обязательным указанием источника в ответе; таблица разделения операций по риску с preview, allowlist и подтверждением для отправки; read-back после таймаута вместо слепого повтора; один процесс-владелец сессии из-за блокировки SQLite; входящие сообщения как недоверенные данные. Артефакт: queries/telegram-user-session-agent-access-20260926.md; полный текст статьи — raw/articles/habr-1071576-tgcli-telegram-user-session.txt. Гипотезы H1-H4 (стабильность сессии с VPS во Франкфурте, покрытие запросов живым поиском, конфликт требования одного процесса с нашим параллелизмом, выигрыш профиля общения).## 2026-09-27 — августовская оперативная статистика Росстата (факт-блок к 08.10)
- Добраны файлы, которые недельный джоб забрал бы только в понедельник: raw/rosstat/operational/jil_dom-oper_08-2026.xls (442 368 байт) и raw/prom/ind_baza_2023_08-2026.xlsx, ind_sub_2023_08-2026.xlsx, sezon_2023_08-2026.xlsx.
- Инжест ввод жилья (scripts/ingest_housing_types.py, релиз обновлён): rosstat_housing_total_m и rosstat_housing_pop_m — 1 430 точек каждый, период до 2026-08-01, 71 субъект (полное покрытие файла).
- Август 2026 по субъектам: всего 6 256,7 тыс. м2, ИЖС 4 320,6 тыс. м2 (доля ИЖС 69,1 %). Год к году: август 2025 — 6 437,8 тыс. м2, снижение на 2,8 %.
- Пояснение: РФ и федеральные округа этим скриптом не заполняются (только субъекты); агрегаты за август придут из доклада «Социально-экономическое положение» (недельный джоб, понедельник).
- Промышленные ряды за август скачаны, но в БД v2 ещё не залиты: пайплайн индексов идёт через scripts/rosstat_prom_monthly_parse.py и rosstat_sezon_parse.py.

### 2026-09-28 — Региональный срез v2: глубина 15 мес и устойчивые динамики (этап I цикла СД 23.10)
- [region-slice-full-202610.md](region-slice-full-202610.md): ревью аномалий первого прогона доклада ГУ доведено до исправления пайплайна, а не до пометки в тексте.
- `scripts/region_slice_full.py`: глубина среза MONTHS_BACK 6 → 15 месяцев от последней точки метрики (16 835 строк против 7 652) — окно год к году без одноимённых месяцев прошлого года не строится.
- `scripts/gu_report_template.py` v2: потоки, запасы и уровни сравниваются с одноимённым 3-месячным окном годом ранее (сезонность стройки снята), ставки и нормы — только в п.п., отсев малых знаменателей (база ниже 5 % медианы баз по субъектам) и «малой выборки» по ставкам (объём выдачи ниже 10-го процентиля), флаг аномалии выносит пару из лидеров/аутсайдеров в `data/gu_report_template_202610_flags.csv` (45 пар: 19 аномалий динамики, 12 малых знаменателей, 14 малых выборок).
- Вердикт по аномалиям первого прогона: жилищный блок дал 22 «аномалии» на сравнении с предыдущим окном (17 ввод жилья плюс 5 ИЖС) — при г/г-окне их 4; Свердловская безработица +80 % м/м читается как +1,20 п.п. за квартал; Тамбов кредиты юрлиц +5719 % м/м не воспроизводится (сырой м/м августа +2,2 %, г/г +22,4 %) — следствие дефекта ипотечного блока, закрытого 26.09.
- Связка с диагностикой: правила отсева взяты из ревью аномалий [region-slice-anomaly-review-202610.md](region-slice-anomaly-review-202610.md) (коммит e5def55) — малые знаменатели по значению, «малая выборка» по объёму выдачи, безработица только в п.п., Свердловская 2026-Q2 не выводится как ухудшение без сверки с ЕМИСС 43062.
- Проверка: независимый пересчёт контрольных чисел из CSV совпал с отчётом (Хабаровский край ввод жилья г/г +111,50 %, Свердловская +1,20 п.п., Тамбов +2,24 % м/м); пометка «Независимый расчёт, не связан с Банком России» в шапке и каждом блоке.
## 2026-09-27 — факт-блок к СД 23.10.2026 (черновик v0.1)
- Собран queries/sd-sitrep-202610.md: девять разделов (жильё, кредит и ипотека, строительство и инвестиции, промышленность, инфляция и ожидания, оперативные индикаторы, региональный срез, календарь публикаций до 08.10, открытые вопросы методики). Данные по август включительно, каждый факт с источником и датой, пометка независимости на месте.
- Ключевые числа: ввод жилья август 6 256,7 тыс. м2 (-2,8% г/г), январь-август 40 292,3 тыс. м2 (-12,9%), ИЖС 27 127,0 (-21,4%, доля упала с 74,6% до 67,3%); СМР июль 1 790,5 млрд руб (+0,8% г/г); ИКВ I и II кварталы 6 634,6 и 9 586,0 млрд руб (85,7% и 93,4% г/г); ИПП август 99,4% м/м (99,7% SA), обрабатывающие 97,8% (99,0%); ИПЦ август -0,08% м/м; инфляционные ожидания 13,67% на год и 12,36% на пять лет; ИБК строительства SA -3,11 в августе против -4,99 в июле; ИЖК 22,39 трлн руб на 01.07, выдачи 363 411 млн руб, ставка 10,52%; ККТ август 9,64 трлн руб (+2,6% м/м); стройматериалы: цемент 6,27 млн т, товарный бетон 7,32 млн м3 (-3,5% м/м).
- Вскрыты пробелы: Wordstat-ряд обрывается 24.08 (недельный джоб не пополняет), безработица только по II квартал, зарплата по июнь, квартальная датировка оперативных ИКВ требует сверки.
## 2026-09-28 — региональная часть факт-блока к СД 23.10
- Задача цикла t_8dea3026 разблокирована (статус ready); причина блока не установлена по тексту задачи, при необходимости владелец вернёт.
- Доклад ГУ перегенерирован: data/gu_report_template_202610.md (37 КБ, 16 блоков, дата отсечения 28.09.2026, глубина среза 13 мес). Блок аномалий переписан как ревизия первого прогона: сырой м/м заменён устойчивой динамикой (г/г по 3-месячным окнам, для ставок и норм — п.п.), применены отсев малых знаменателей и фильтр объёма выдачи для ставок ИЖК.
- Содержательные выводы раздела: ввод жилья в августе расходится по регионам сильнее среднего (Подмосковье 699,7 тыс. м2 при -14,3% г/г против Челябинской 162,6 при +39,6%); ипотечный портфель концентрирован — топ-5 даёт 37,1% (8,31 трлн руб из 22,39); ставка ИЖК медиана 10,0% при высоких значениях в регионах малой выборки (Ингушетия 13,8%, Чечня 13,7%); потребительский кредит растёт быстрее в регионах (Татарстан +9,5% г/г) чем в Москве (+6,9%); корпоративный долг Краснодара +29,6% против Москвы +9,7%.
- В queries/sd-sitrep-202610.md раздел 7 переписан из ссылки в полноценный анализ (7.1-7.6 плюс методические ограничения): 6 тезисов с механизмами, открытые вопросы по безработице (Свердловская 2,7% во II квартале требует сверки; разброс 0,9-22,6 наводит на неоднородность методологии).
## 2026-09-28 — инвентаризация ВВП и ВРП
- ВВП: официальная квартальная оценка доступна до I квартала 2026 (файл Росстата GDP-quarters-of-use-1995_1kv-2026.xls): номинал IV кв 2025 — 62 354,1 млрд руб., I кв 2026 — 49 869,5 млрд руб. Наш ряд vvp (36 461 за I кв 2026, почти плоский) — это объём в постоянных ценах, номинальные уровни лежат в КЭП kep1_12 (совпадают с файлом до знака). Единицы у метрик ВВП не проставлены.
- ИФО ВВП I кв 2026 = 99,8 (первый отрицательный за ряд); потребление 103,0, домохозяйства 103,5, ВНОК 87,5; ВДС строительства 90,3. Экспорт/импорт в нашей таблице обрываются на IV кв 2021.
- Прогнозы (макроопрос ЦБ от 01.09.2026, медиана): ВВП 2026 — 0,54%, 2027 — 1,2%, 2028 — 1,7%, 2029 — 1,8%.
- ВРП: в базе отсутствует полностью (0 метрик в PG, нет таблиц в SQLite и staging). Источник найден и проверен: VRP_s1998.xlsx (16 листов) — уровни 1998-2015 и 2016-2024, на душу, ИФО ВРП 1998-2016 и 2017-2024, структура. РФ: ВРП 2024 = 186,5 трлн руб., ИФО 2023 +5,2%, 2024 +4,5%. Задержка публикации ВРП ~2 года структурная.
- Файлы скачаны в raw/rosstat/accounts/. Предложено: загрузить ВРП в базу, развести номинальные и реальные ряды ВВП, добрать экспорт/импорт, зарегистрировать два источника в реестре обновлений.
## 2026-09-28 — ВРП регионов загружен в базу (релиз rosstat_grp_annual_1998-2024)
- Новый скрипт scripts/ingest_grp.py разбирает официальный файл VRP_s1998.xlsx (листы 1-2 уровни, 3-4 на душу, 5-6 ИФО) и грузит в core.observation_v2. Загружено 7 440 точек по 94 территориям (85 субъектов, 8 ФО, строка РФ), 1998-2024: grp_level 2 493, grp_pc 2 460, grp_ifo 2 487. Метрики получили единицы (млн руб., руб., %) и теги rosstat/grp/regional.
- Контроль: ВРП РФ 2024 = 186 545 082,1 млн руб., ИФО ВРП 2024 = 104,5%, на душу 1 276 522,6 руб.; Москва 41,0 трлн (на душу 3,10 млн руб.), ХМАО-Югра 9,93 трлн, Чукотка 224,1 млрд, Ингушетия на душу 204 565,5 руб.
- Нестыковка зафиксирована: сумма субъектов за 2024 даёт 187 144 542,9 млн против строки-итога 186 545 082,1 (+0,32%) — расхождение самой публикации; для сумм использовать строку РФ, для выборок фильтровать level='region' (ФО дают двойной счёт).
- Разрывы сопоставимости по сноскам Росстата: с 2016 методология жилищных услуг и потребления основного капитала, с 2017 добавлены финансовые организации, с 2022 без ДНР/ЛНР/Запорожской/Херсонской.
- В реестр обновлений добавлены позиции rosstat_grp_annual и rosstat_gdp_quarterly (18 позиций всего). Пересборка карточек метрик запущена (три новые метрики).
## 2026-09-28 — свежая точка ВВП: оценка Росстата за II квартал 2026
- ИФО ВВП России во II квартале 2026 года — 101,3% к соответствующему периоду 2025 года (предварительная оценка 12.08.2026; первая оценка 11.09.2026 подтвердила то же значение). Номинал — 56 166,3 млрд руб., индекс-дефлятор — 112,5%. Источник: rosstat.gov.ru/folder/313/document/290165, файл vvp-kommentarij-2-kvartal-2026.pdf.
- В базу добавлено наблюдением метрики vvpi (период 2026-04-01…2026-06-30, тип preliminary, релиз rosstat_gdp_2026q2_first_estimate); номинальный объём в базу не кладётся — метрики номинального уровня ВВП нет, значение зафиксировано в примечании релиза.
- Ряд ИФО ВВП непрерывен: I квартал 2026 — 99,8 (первый отрицательный за ряд), II квартал 2026 — 101,3, то есть квартал вышел из спада. Прогнозы на этот горизонт теперь сверяемы с фактом: МВФ — 1,1% на 2026 год, WDI Всемирного банка прогнозов не даёт, медиана макроопроса ЦБ (01.09.2026) — 0,54%.
- Контекст, поставщики и цикл: queries/gdp-actors-forecasts-cycle-20260928.md, раздел 8.
## 2026-09-28 — research-radar 2026-09-28 (недельный скан литературы)
- Создан queries/research-radar-2026-09-28.md: 5 работ за 7-дневное окно (21–28.09). Честная фиксация тонкого улова: NEP-HRE-2026-09-28 к моменту скана не опубликован, arXiv econ.EM за 22–28.09 без жилья, сентябрьский батч NBER (w35758–w35787) без supply/mortgage-работ.
- Основной урожай — NEP-HRE-2026-09-21 (объявлен ровно 7 дней назад): Coven–Golder–Gupta–Ndiaye 2026 (HCEO WP 2026-010; NBER w35587) налог на недвижимость и распределение жилья под финансовыми ограничениями (down-payment как связывающая маржа, embedded leverage, lock-in пожилых); Bracke–Cocco–Markoska–Tak 2026 (BoE SWP 1203) рефинансирование ипотеки вокруг шока 23.09.2022 (сдвиг к двухлетним фиксациям, 200 б.п. → LTV −2–3 п.п., опцион на снижение ставки); Carrillo–Li 2026 (GWU 2026-013) пространственный разрыв собственности; Devane–O'Toole–Slaymaker 2026 (ESRI WP826) ирландская Cost Rental (аннотация RePEc не раскрыта). Плюс свежая ревизия Zhao–Takahashi 2026 (SSRN 6440818, rev. 12.09): Duty to Serve, одобрения +1.35 п.п., эластичное предложение → плоские цены.
- Патчи hypotheses.yaml (2 записи, дата проверки 2026-09-28): H-002 evidence_for +Coven et al. (финансовое ограничение через маржу down-payment); X-003 evidence_for +Bracke et al. BoE 1203 (поведенческая асимметрия заёмщика к ожидаемой траектории ставки). Статусы гипотез не менялись.
- Пробелы gap-map №1 (firm-level эластичность под финансовыми ограничениями) и №2 (escrow как экзогенный шок) — по-прежнему открыты, конкурентов за неделю не появилось.
## 2026-09-28 — чистка языковых вкраплений в страницах вики
- В 14 местах внутри русских и английских фраз стояли китайские слова вместо нужного (например «эффект» плюс китайское «длительный», «нейтрализует ужесточение», «рыночные данные», «земельные издержки») — сбой генерации, а не язык источника. Все места исправлены по смыслу; векторный слой по двум затронутым запискам пересобран.
- Законный китайский оставлен: он принадлежит четырём источникам на языке оригинала (статья об углеродном налоге и ценах жилья, работы Madsen, Wang, перевод Rossi).
- Правило против повтора добавлено в scripts/lint_wiki.py; технические детали — log-tech.md.
## 2026-09-28 — источник оперативной оценки ВРП найден и зарегистрирован
- Раздел, где Росстат публикует оперативные релизы, — «Срочные информации и справки Росстата по актуальным вопросам» (rosstat.gov.ru/compendium/document/50798). В ленте 219 позиций за сентябрь 2025 — сентябрь 2026: недельные ИПЦ, цены на нефтепродукты, промышленное производство, потребительские ожидания и квартальные выпуски о ВВП.
- Выпусков о ВРП в ленте пока нет ни одного — это согласуется с публичным заявлением управления национальных счетов Росстата: первую оперативную оценку ВРП (только индексы физического объёма, без отраслевой разбивки) ведомство опубликует в ноябре 2026 года за 2025 год, основную оценку — в первой декаде марта 2027 года. В презентации Росстата о разработке показателей ВРП тот же двухступенчатый порядок виден на примере 2021 года: предварительная оценка 30 ноября 2022 года, первая — март 2023 года, вторая — март 2024 года.
- Источник зарегистрирован под кодом rosstat_grp_operational: в каталоге данных (data/catalog.yaml) как условная позиция с адресом раздела, форматом html+pdf и расписанием «ноябрь — оперативная оценка, первая декада марта — основная», в реестре обновлений (data/source_updates.yaml) как напоминание с годовой периодичностью и целью — релиз rosstat_grp_operational_ГОД в метрике grp_ifo.
- Карточки метрик grp_level, grp_pc и grp_ifo получили описание, называющее оба канала — годовой файл VRP_s1998.xlsx и ноябрьскую оперативную оценку; поисковый текст карточек пересобирается, поэтому ряды находятся и по запросу про оперативную оценку.
- Разбор с фактами и гипотезами — queries/rosstat-operational-urgent-releases-20260928.md.
## 2026-09-28 — сюжет по объёму строительных работ в Башкортостане
- Сюжет: длинный ряд 2001–2024 (21,2 → 481,1 млрд руб., доля 2,70 % суммы по субъектам, 11-е место из 87) и провал 2026 года (январь-июль — 188,0 млрд руб., ИФО 80,0 % против 96,1 % по России и 101,7 % по Приволжскому ФО).
- Разворот виден с 2025 года: годовые ИФО 2023 — 122,1 %, 2024 — 107,9 %, 2025 — 86,5 % (по России 109,0 %, 103,8 %, 102,5 %). Внутри 2026 года дно пройдено в первом квартале (62,8 % в январе-марте), к январю-июлю отставание сократилось до 80,0 %.
- Башкортостан — худший среди сравнимых регионов: Пермский край 127,9 %, Самарская область 114,2 %, Татарстан 101,4 %, Свердловская 92,5 %, Челябинская 86,9 %, Тюменская 84,4 %.
- Артефакты: queries/bashkortostan-smr-2026.md (три проверяемые гипотезы), scripts/bashkortostan_smr_story.py (воспроизведение), visualizations/bashkortostan-smr-2026m07.png. Нерешённое: месячные уровни в источнике даны только накопленным итогом.
## 2026-09-28 — что из ленты «Срочные информации» Росстата можно обновить
- Разобрана лента оперативных релизов (219 позиций, 72 типа публикаций). Обновляемо сразу: ИЦП промтоваров, просроченная задолженность по зарплате и промышленное производство отстают на месяц, ВВП по использованию — на квартал.
- Чего нет вовсе: недельный ИПЦ и недельные цены на нефтепродукты (43 выпуска в год каждый), цены на бензин (13), деловая активность организаций (12), месячные финансовые результаты (13), потребительские ожидания и границы бедности.
- Для недельных рядов в core.frequency нужен новый код частоты: сейчас есть только годовая, дневная, месячная и квартальная.
- Артефакт: queries/rosstat-urgent-feed-coverage-20260928.md.
