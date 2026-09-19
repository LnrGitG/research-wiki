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
