# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-09-11] update | GDELT GKG fetch за 2026-09-10
- Cron-прогон `scripts/gdelt_fetch.py`: 96 hourly-файлов, 119 837 строк GKG, отфильтровано 7 записей по RUS → `data/raw/gdelt/gdelt_gkg_rus_20260910.csv`.
- Уровень в норме для этого фильтра (ср. 20260909: 3 строки, 20260907: 19 строк).

## [2026-09-10] update | YC VP для скрейпинга и хранения research-wiki
- Актуализирован план `/home/lnr/.hermes/plans/2026-09-09-yc-vm-bucket-setup.md` на основе YC-инфраструктурного skill, локальных MD и контекста прошлых сессий.
- Добавлены raw/staging/curated-слои Object Storage, manifests/checksum, SQLite → Parquet/DuckDB, systemd timers и acceptance-критерии.
- Зафиксировано: YC VP не является резидентным IP и не должна использоваться для обхода антибота/геоблокировок; API-first для ЦБ, Росстата, ДОМ.РФ/ЕИСЖС, Росреестра.
- Cloud Functions/API Gateway оставлены только в историческом архиве плана; публичные управляющие POST не использовать.

## [2026-07-16] create | Wiki initialized
- Domain: AI/ML research → updated to: Экономика жилья / ипотека / недвижимость
- Path: ~/research-wiki
- Structure: SCHEMA.md, index.md, log.md + raw/, entities/, concepts/, comparisons/, queries/, _archive/
- WIKI_PATH set in ~/.hermes/.env

## [2026-07-16] ingest | Batch: Workpapers (20 PDFs)
- Source: ~/research-wiki/raw/papers/Workpapers/ (20 PDFs uploaded via scp)
- Extraction: pymupdf4llm → markdown (20/20 success)
- SCHEMA.md updated: domain changed to «Экономика жилья, ипотечного кредитования и рынка недвижимости»
- Analysis delegated to 3 parallel sub-agents (ипотека/субсидии, цены/инфляция/стройка, макро/международный)
- Pages to be created after analysis completes

## [2026-07-16] create | Wiki pages from batch ingest
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
- SCHEMA.md: added tags macroprudential (not needed, existing tags sufficient)
- Updated index.md (total: 16 pages) and log.md

## [2026-07-16] step 5 | Role of expectations in monetary-housing transmission
- Created conceptual page synthesizing expectations channel across all 8 papers
- Key findings:
  * Household inflation expectations positively correlated with loan demand (Sinyakov 2025)
  * "Irrational exuberance" particularly strong in Russia (Smirnova 2025): housing as inflation hedge
  * Expectations can dominate interest rate channel → weak monetary transmission
  * Policy implications: forward guidance, communication, expectations management
- Cross-cutting theme connects: Mishkin's expectations channel, Taylor's counterfactual, Chodorow-Reich's measurement issues, Russian evidence (Sinyakov, Demidova, Smirnova, Zvereva)
- File: concepts/rol-ozhidanii-v-monetarnoi-politike-i-zhilishchnom-rynke.md
- Updated index.md (total: 17 pages) and log.md

## [2026-07-16] final synthesis | Comprehensive analysis of monetary-housing interaction
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

## [2026-07-16] summary | Step 4: Comprehensive bibliography on monetary policy and housing
- Created master bibliography document covering all 13 research papers from Steps 1-3
- Organized by: (1) International theories, (2) Russian empirical studies, (3) Macroprudential policy
- File: queries/monetarnaya-politika-i-rynok-zhilya-kompleksnaya-bibliografiya.md
- Links to all 6 conceptual pages + raw papers inventory
- Key synthesis: monetary policy less effective in Russia (weak transmission, subsidized mortgages), macroprudential tools become primary risk-management instrument
- Updated index.md (total: 16 pages) and log.md

## [2026-07-16] ingest | Batch 2: 26 new papers (PDF→markdown)
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
- Index and log updated. Total papers in raw/papers: ~60 (34 PDF+MD pairs + additional workpapers)

## [2026-07-25] create | Economical wiki maintenance scaffold
- Added warm-layer catalog: raw/papers/_catalog.md (short card per extracted source; no page per PDF).
- Added templates: templates/concept.md, templates/query.md, templates/paper-card.md.
- Added scripts: scripts/convert_pdfs.py (idempotent PDF→MD, skips _archive/Workpapers, flags error-page/image-only) and scripts/lint_wiki.py (non-blocking by default; --strict fails on broken wikilinks).
- Cleanup: moved two bad extracted sources to _archive/rejected/2026-07-25/ (chodorow-reich-2025-cpi-housing = access denied; dipasquale-wheaton-1992 = image-only/empty extraction).
- Verified: convert_pdfs.py --no-recursive → converted=0 skipped=33 failed=0; lint_wiki.py → problems=0 warnings=170 (mostly missing catalog cards for existing raw sources).

## [2026-08-25] ingest | AI Mindset cases: Academic Research + Research Planning and Content Tagging
- Sources: base.aimindset.org case-Academic-Research, case-AI-for-Research-Planning-and-Content-Tagging (both 21.08.2026)
- Extraction: curl direct (web_extract not configured), Quartz static HTML -> article block
- Created: queries/ai-mindset-research-planning-case.md (both cases, RU summary + pipeline mapping)
- Updated: index.md (2 new query entries)
- Key takeaway: extraction/publishing stronger than case; gaps = LLM research-plan/gap generation, auto-tagging with confidence, auto-review assembly -> fit llm_pipeline.py

## 2026-09-08 — Gap-map, гипотезы H-002..H-006, противоречия X-002..X-003
- Created: queries/literature-gap-map.md (матрица 9 вопросов, 5 приоритетных пробелов: firm-level эластичность, escrow-канал, mixed-frequency nowcasting, dual system ставок, асимметрия ДКП)
- Updated: hypotheses.yaml: +5 гипотез (H-002 financial-constrained supply elasticity; H-003 escrow release → starts; H-004 замещение × спред; H-005 МПЛ × эластичность региона; H-006 MIDAS Wordstat+GDELT+ЕИСЖС vs AR) и +2 противоречия (X-002 расхождение индексов цен 1.1/1.37/4.1%; X-003 асимметрия ДКП US-литература vs РФ-эмпирика)
- Updated: index.md (1 query entry)
- Параллельно: каталогизация papers/ (424 файла) в papers/catalog.md — 3 делегата, идёт

## 2026-09-08 — Каталогизация papers/ в papers/catalog.md (фаза 2, delegation)
- 3 параллельных делегата обработали 423 .md из papers/ → 319 карточек (8-10 строк: title/authors/year/method/data/key_result/relevance/status) + 63 dup-ссылки на файлы-близнецы (например Bailey/Balcilar/Cepni/Corsetti/Eickmeier/Das — карточка на первом имени пары)
- Дедупликация: пары "_/-" имён схлопнуты; литовский HPI 4 варианта, Корея 3, BIS bull 3 — по одной карточке с dup-пометками
- Проверка: 0 дубликатов заголовков, 0 битых dup-ссылок, покрытие 423/423 (карточка или dup-ссылка); файл 3317 строк
- Пропуски: NBER-CRIW-2026-Ch4 отсутствует на диске (корректно); пустые/error-экстракции (dipasquale-wheaton-1994, rbnz-2025-dfm) помечены relevance: low

## 2026-09-08 — Пересборка векторного слоя
- scripts/rebuild_embeddings.py: 633 файлов (papers 423 + ru_papers + queries + новый literature-gap-map) → docs/embeddings-f32.json (1523 KB) + docs/search-index.json (633 entries)
- Смоук-тест косинусного поиска по запросу про эластичность/финансовые ограничения — релевантные статьи найдены (Iacoviello SVAR, глэзер supply, monetary transmission), индекс согласован

## 2026-09-08 — Models, CI, Obsidian, research-radar (элементы плана Qwen)
- Created: models/nowcasting/midas-wordstat-smr.md (H-006), models/transmission/dev-supply-elasticity-panel.md (H-002/H-003), models/transmission/did-mpl-elasticity-regions.md (H-005/H-004); шаблон templates/model-card.md; SCHEMA.md: тип model + раздел Model Pages
- Created: scripts/ci/check_wiki_links.py (wikilinks/frontmatter/catalog dup/hypotheses; exit 0: 0 errors, 139 warnings — legacy frontmatter и маркеры сносок) и .github/workflows/wiki-ci.yml (wiki check + markdownlint non-blocking)
- Исправлено: 5 unquoted YAML title (модели + 2 queries + review), добавлены типы review/news/reference/annotation в схему линтера
- Obsidian: MOC.md (тематическая карта), docs/obsidian-setup.md (vault-настройки, Dataview/Kanban/Obsidian Git), .gitignore дополнен (workspace, cache, plugin-байнари)
- Cron research-radar-weekly (job 54ce92865069): понедельник 10:00 UTC — скан arXiv/NBER/SSRN/CBR, сверка с hypotheses.yaml, запись queries/research-radar-*

## 2026-09-08 — Дизайн публикации: nowcasting ВНОК/ИКВ
- Created: queries/vnok-nowcasting-design.md (целевые ряды: ВНОК IFO 56 кв. SA + ИКВ 25 кв. + 96 рег.; 6 блоков предикторов с скорингом пилота; стек bridge/MIDAS/MF-VAR/DFM/ML/firm-level по IMF WP 22/52, Bundesbank DKP 26/2014, Hong et al. 2026, ЦБ WPS 8/КПМ; план 5 этапов; риски: малая выборка, эскроу 2022+, слом 2026Q1)
- Created: models/nowcasting/vnok-icv-midas.md (карточка H-007/H-008, пилотные corr перенесены)
- Updated: hypotheses.yaml +H-007 (эскроу lag2 ≥0.7, testing) +H-008 (firm-level блок −10% RMSE, active)
- Updated: index.md (1 query entry)
- Делегат по литературе (MIDAS/bridge/DFM для инвестиций) работает параллельно — итоги влить в дизайн по завершении
- Обзор международного опыта nowcasting GFCF (deleg_64c9f9c5, deepseek): queries/vnok-nowcasting-international-review.md — 9 классов, ключевые: Kuzin et al. 2011 (MIDAS 0-4 мес > MF-VAR 5-9), MFBVAR лидер РФ (Станкевич 2020, Фокин 2023), Gareev 2020 (ML уже для GFCF РФ), Tarsidin 2018 (цемент-прокси кросс-страново), Макеева-Станкевич 2022 (прямой прототип). Дизайн и карточка обновлены: +MFBVAR в бенчмарки, +горизонты
- Вторая итерация обзора (deleg_834a732c): дополнения в queries/vnok-nowcasting-international-review.md — U-MIDAS границы применимости, Жемков 2021 (MF-FAVAR неустойчив 1.79-2.38), Hong 2026 точные RMSE + bellwether-эффект, Degiannakis 2022 (фондовый рынок→GFCF, структурный аналог эскроу), Polbin-Shumilov 2025 (квантильный MIDAS РФ), ограничение БФО годовой частоты → vintage-дизайн actualBfoDate
- Инфраструктурная записка queries/yandex-cloud-data-infra.md: прерываемая ВМ+Object Storage+Yandex Disk, ~300-800₽/мес, пилот-план ЕМИСС/БФО/СПАРК

## 09.09: Петрова–Трунин 2023 (EPU-РФ) — разбор + H-009/H-010

- PDF статьи + приложения прочитаны; разбор queries/petrova-trunin-epu-rf.md
- hypotheses.yaml: +H-009 (EPU в nowcast ИКВ, active), +H-010 (EPU × эскроу взаимодействие, proposed)

### Ключевые факты
- epu_new (4 СМИ, 1999-2022) vs RVI corr 0.855; epu_bbd vs RVI 0.525 — модифицированный индекс лучше оригинального Бейкера-Блума-Дэвиса
- Шок EPU → инвестиции −0.45 п.п. через 2 кв. (значимо до 4-го); epu_bbd незначим для инвестиций — канал реальных опционов
- Расширения категории «политика» робастны (corr 0.992-0.999, Приложение 1)

## 09.09: clearspending перепроверка + чеклист YC-ВМ

- API clearspending (openapi/v3) всё ещё 500 (Starlette/Sphinx-авария) с VPS; legacy v1/v2 — 404; веб под Anubis 200
- OFDATA 401 без ключа (жив), github зеркала 200 (не активны с 2024-02)
- Решение: clearspending-тест включён в task.json YC-ВМ (резидентный IP различит гео-блок от аварии сервера); при 200/401 — сбор ОКПД2 41/42/43 с ВМ

## 14.09: Гайд по настройке и использованию Hermes Agent

- Created: docs/hermes-agent-setup-guide.md (~35K, 12 разделов): установкa на VPS (RAM/CPU из реальных замеров), 5 стратегий LLM-провайдеров и роутинг (дешёвый движок + эскалация флагманом, aux.approval слой), инструменты и MCP, скиллы и Curator (практики и предостережения), слоистая память (SOUL/USER/MEMORY/AGENTS + session search, анти-паттерн «память 2200 символов»), профили/мультиагентность, автоматизация (cron/loops/heartbeats/webhooks), безопасность (approvals, vault, изоляция, каналы доверия), сводная таблица 28 грабель из 3-частной саги Paspartu, чеклист внедрения
- Источники: Habr (5 статей: neodavinchi 1032656, AMLAI 1044574/1045892/1065282, ohld 1053846), дайджест r/hermesagent (The Lurk Report, май 2026), Medium/JIN разбор архитектуры, официальные доки llms.txt; Reddit-треды через дайджесты (прямой доступ к reddit.com блокирован с этого IP)
- База для дальнейших решений: роутинг моделей у нас (glm-5.3-flash/ollama-cloud + fallback), слоистая память, cron-джобы на пинненых моделях

## 14.09: Справка по сервисным командам Hermes

- Created: docs/help.md (~16K): все CLI-команды v0.21.2 (gathered from live --help) по 12 разделам — глобальные флаги, сессии, модели/провайдеры, gateway, автоматизация (cron/kanban/webhook), skills+curator, память, инструменты, безопасность (vault/security/pause), обслуживание (doctor/backup/logs/prompt-size), инфраструктура (dashboard/serve/acp/profile), типовые операции нашего сетапа; плюс полная таблица slash-команд из skill-референса
- Заодно зафиксировано: skills.write_approval=true гейт, curator consolidate=true, типовые команды обслуживания

## 14.09: arXiv-скан по фокусу реестра гипотез + карточка ML-зомби

- arXiv-скан (7 фокусов, после радара 2026-09-14): новых работ по открытым пробелам нет; escrow=0 результатов по всей базе arXiv (ниша свободна); nowcasting construction — ложные срабатывания (метеорология, металлы, GDP)
- Created: queries/ml-zombie-firm-classification.md — Bargagli-Stoffi et al. 2023 (arXiv 2306.08165): XGBoost предсказание дистресса 304 906 итальянских фирм с неслучайными пропусками отчётности как признаками; зомби = 3+ года выше порога; превосходит Z-score/Distance-to-Default
- Применимость: H-002 (зомби-статус как контрол финансовой слабости), H-008 (фильтр слабых фирм перед агрегацией); ключевой перенос — пропуски как признаки для панели ФНС (87% УСН, filed=1 AND line_2110>0)
- Отличие от BIS 1375 комплементарное: BIS — определение класса на firm-bank данных, итальянская работа — предсказание класса из публичной отчётности (доступно нам на ФНС/СПАРК)
- index.md: +1 entry (Queries)

## 14.09: Research Radar (еженедельный скан литературы)
- Created: queries/research-radar-2026-09-14.md — 4 работы за 7-дневное окно (NBER/SSRN/arXiv/Philly Fed/BIS); Graybill–Mangum 2026 (WP 26-33R): покупатели чувствительнее к ставке, чем продавцы к lock-in → X-003 evidence_for пополнен (patch в hypotheses.yaml, дата проверки); идеи: survival-модели tenures → эскроу-балансы (H-003), дюрации ЕИСЖС как блок H-006, зомби-классификация BIS 1375 → контрол H-002; пробелы №1 (firm-level эластичность) и №2 (escrow shock) остаются открытыми — конкурентов не появилось

## 2026-09-16 — Целевая архитектура БД (техзадание + проект)
- Создан `queries/database-target-spec.md` — ТЗ: назначение (аналитический + исследовательский режимы), 17 сущностей, пайплайн, критерии приёмки; §15 заполнен замерами.
- Создан `queries/database-architecture.md` — проект: слои staging/core/derived/marts, DDL PostgreSQL (18 таблиц), as-of витрины, ключ гранулярности с source+release+assessment_type, план миграции 6 SQLite → PG через db_compat, демонтаж GCS, стоимость YC ~2600-3300 ₽/мес.
- Замер: 80 пользовательских таблиц / 5 903 489 строк / ~1.45 ГБ (уточнено против 81 — включала sqlite_sequence).
- Открытые вопросы: 8 (бюджет ВМ, судьба 23 фантомных таблиц, канонизация регионов, link-коэффициенты ИФО).

## 2026-09-16 — Канонический справочник регионов
- Построен справочник: 98 записей (1 страна + 8 ФО + 89 регионов), иерархия country→fd→region.
- Карта 435 сырых написаний → канонический код; покрытие 2 375 368 наблюдений.
- Обработано 646 уникальных значений: омоглифы, аббревиатуры АО, родительный падеж, английские слоги ФНС, исторические АО 2005-2008.
- 211 значений исключены как не-региональные (подписи строк в колонке региона).
- 4 спецслучая на ревью: Малороссийский ФО (115), Байконур (37), Сочи (1), составные названия Росреестра.
- Скрипт scripts/build_region_reference.py — воспроизводимый, идемпотентный.
- Закрыт последний открытый вопрос архитектуры БД (14.8).

## 2026-09-17 — Постановка на развёртывание БД в YC (Ф0 выполнена)
- Создана queries/database-deployment-plan.md: 6 фаз (канал → ВМ → PG+справочники → миграция → скрипты → демонтаж GCS → бэкапы).
- Ф0 выполнена: проверен обмен VDS ↔ YC через S3-бакет agent-vm-exchange (PUT/GET/head работают, etag совпал).
- Зафиксированы ресурсы: зона ru-central1-b, подсеть e2lihlksrvl26ukhrcef, SG ssh-access-sg, образ fd8nj6iro13qffg31not.
- Целевая ВМ: 4x20% vCPU / 8 ГБ / 60 ГБ SSD ~4300 ₽/мес (постоянная).
- Объём: 6 баз 1452 МБ, 5 903 507 строк, 80 таблиц; оценка PostgreSQL ~2.4 ГБ.

## 2026-09-17 — Разбор Retrieve-for-Train (Google Research)
- Создана queries/retrieve-for-train-google.md: разбор ICML 2026 arXiv:2603.06397.
- Суть: RL-компиляция fan-out поиска в диффузионный ретривер (53.9M), 12-20x быстрее.
- Ключевое: композитная награда из 3 взаимных контр-якорей (groundedness x alignment x diversity через Vendi Score); без diversity модель деградирует (абляция).
- Критические оговорки: домен мультимодальный (fashion/music), не текстовый; обучение 4B-моделей разово, но тяжело; цифры от заинтересованной стороны.
- Применимость: парафразный коллапс в Wordstat-композите (H-001) + мерило разнообразия набора HF-регрессоров.

## 2026-09-17 — Обзор сервисов Yandex Cloud для пайплайна
- Создана queries/yandex-cloud-services.md: разбор 38 групп yc CLI + цены.
- Рекомендовано: pgvector в существующем PostgreSQL (0 руб сверху) вместо OpenSearch (~7800 руб/мес минимум); DataLens (1 место бесплатно) вместо GitHub Pages; Search API отложенный режим 30,5 руб/1000 для библиографии.
- Векторизация AI Studio: 0,0101 руб/1000 токенов; для вики 15,1 млн токенов = ~153 руб разово.
- Managed PostgreSQL с PITR рассмотрен как альтернатива (дороже ВМ ~7200 руб/мес).

## 2026-09-17 — Проектирование пользовательского пути поиска
- Создана queries/search-user-flow.md.
- ДИАГНОЗ: текущий поиск идёт по title+abstract, покрытие текста 0.1%; в 515 из 629 записей abstract = первая строка md.
- Ключевой замер: полный инвертированный индекс по 709 файлам (32.3 МБ, 3.35 млн слов, 90 549 терминов) = 3.1 МБ, со сжатием 0.8 МБ. Влезает в браузер.
- Путь: строка поиска -> сниппеты с подсветкой -> viewer.html с Text Fragments (#:~:text=) для прокрутки к совпадению.
- Три варианта: клиентский индекс (рекомендован), серверный на YC, гибрид.

## 2026-09-17 — Дедупликация papers/ (112 файлов)
- Причина дублей: двойная конвертация одних PDF — старый стиль имени («Имя. Заголовок») и новый («Имя-Заголовок»).
- Удалено 112 файлов, освобождено 9.5 МБ; papers/ 587 -> 475 md.
- Починено 39 wikilinks в 9 файлах (карта переименований по хешу тела).
- Проверка: 0 ссылок на удалённые файлы.
- Скрипт scripts/dedupe_papers.py (сухой прогон по умолчанию, --apply для удаления).
- Манифест: data/dupes_removed.json. Бэкап-тег: backup/before-dedupe-20260917.
- Создан scripts/build_search_index.py: индекс со стеммингом + корпус абзацев для сниппетов.

## 2026-09-17 — Полнотекстовый поиск по вики
- `scripts/build_search_index.py`: сбор md → дедупликация → лемматизация pymorphy3 → инвертированный индекс + корпус абзацев + словарь форм→лемм.
- Исправлен дефект стеммера: самодельный Snowball давал несогласованные основы («предложения»→предложен, «предложение»→предпол), запрос «эластичность предложения жилья» возвращал 0 результатов. После замены на pymorphy3 — 52.
- `docs/search-full.html` (13 КБ): строка поиска, морфология, сниппеты с подсветкой, фильтры по типу, ранжирование tf·idf.
- `docs/viewer.html`: переход к месту совпадения через Text Fragments с fallback для Firefox.
- Индекс: 602 документа, 44 697 лемм; файлы 485 КБ + 947 КБ + 5.1 МБ.
- Проверено сквозным тестом в jsdom: поиск, фильтры, сниппеты, ссылки, подсветка.

## 2026-09-17 — Миграция SQLite → PostgreSQL (этап staging)
- Шесть баз (1.4 ГБ, 5 903 489 строк, 80 таблиц) перенесены в схему staging PostgreSQL 16.15 на ВМ research-db.
- Сверка COUNT(*) по каждой таблице: расхождений нет (80/80).
- Канал: S3-бакет agent-vm-exchange (SSH недоступен из-за гео-фильтра). Агент опрашивает _cmd/command.sh.
- Большие файлы загружались через rclone (yc s3api put-object падает с tcsetattr на файлах >100 МБ).
- Уточнение: у rosstat_construction 36 таблиц, не 37 — 37-й объект sqlite_sequence (служебный).

## 2026-09-17 — Ремонт 11 скриптов, повреждённых при миграции на GCS
- Обнаружено при подготовке Ф4: 11 скриптов не парсились (SyntaxError) и не запускались с 12.09.
- Причина: коммит d44e3d8 («Migrate heavy data to GCS») автоматически заменял абсолютные пути на REPO_ROOT/ensure_db(), но обернул выражения в лишние кавычки — код стал строковым литералом.
- Пример: `DB = 'str(ensure_db('rosstat_construction.db'))'` вместо `DB = str(ensure_db('rosstat_construction.db'))`.
- Починено: 14 повреждённых строк в 11 файлах + добавлены отсутствовавшие определения REPO_ROOT/DATA/Path.
- Дополнительно: в build_housing_index.py определение DATA стояло после использования (строка 59 vs 6) — блок перенесён наверх.
- Инструмент: scripts/repair_scripts.py (идемпотентный, сухой прогон по умолчанию).
- Проверка: 74/74 скрипта синтаксически валидны; export_operational, export_dashboard, wordstat_core_index, build_housing_index запущены успешно.

## 2026-09-17 — Слой совместимости db_compat.py (Ф4)
- SSH к YC-ВМ теперь работает (гео-фильтр снят); подключение к PostgreSQL через туннель ssh -L 15432.
- scripts/db_compat.py: прокси sqlite3 → psycopg (плейсхолдеры ?, квалификация имён таблиц в staging.<db>__<t>, PRAGMA, Decimal→float, классы исключений).
- Сверка: export_operational и export_dashboard через PostgreSQL дали ИДЕНТИЧНЫЙ результат SQLite.
- Обкатка 8 читающих скриптов: 7 успешно. midas_ddu_wordstat падает и на SQLite — предсуществующий дефект, не регрессия.
- Ротация пароля роли wiki (был случайно выведен в терминал при настройке).

## 2026-09-17 — Демонтаж GCS, переход на YC Object Storage (Ф5)
- Перенесено 3.47 ГБ / 1244 объекта из GCS в новый бакет YC `wiki-research` (стримингом через rclone, диск не расходовался).
- Сверка: raw/ 1228 файлов (2161 МБ) и data/archive/ 8 файлов (110 МБ) совпали по размеру; выборочная проверка 19 файлов по md5 — расхождений нет.
- data/db/: шесть баз (1450 МБ) в бакете, размеры совпадают с локальными.
- `scripts/yc_sync.py` заменил `gcs_sync.py` (удалён); импорты в 10 скриптах переключены на yc_sync.
- Монтирование: rclone mount в ~/yc-wiki, systemd user-юнит `yc-wiki-mount.service` (enabled).
- Симлинк raw/ → ~/yc-wiki/raw (было ~/gcs-wiki/raw); gcsfuse отключён.
- Обновлены AGENTS.md и .gitignore.

## 2026-09-17 — Бэкапы PostgreSQL с фактической проверкой (Ф6)
- scripts/pg_backup.py: pg_dump -Fc → загрузка в бакет → восстановление во временную базу research_wiki_verify → сверка счётчиков по 19 таблицам → удаление временной базы.
- Восстановление проверено фактически: дамп 100.3 МБ, 19 таблиц, расхождений 0, цикл ~121 с.
- systemd-таймер pg-backup.timer на ВМ: 03:30 UTC ежедневно, Persistent=true; ретенция 30 дампов через ExecStartPost.
- Роли wiki выдано CREATEDB; .pgpass расширен маской * (покрывает postgres и временную базу).
- На ВМ установлен rclone 1.75.1, конфиг скопирован с VDS.
