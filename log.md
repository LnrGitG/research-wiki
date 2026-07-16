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
