# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

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
