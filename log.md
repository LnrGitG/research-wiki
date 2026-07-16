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
