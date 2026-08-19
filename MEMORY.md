User is a researcher/analyst working on Russian housing market economics. Maintains a research wiki (research-wiki repo) with papers, catalog.yaml, and queries. Focus: supply elasticity estimation, demographic forecasting, mortgage markets.
§
User prefers: bilingual RU/EN structure preserved; exact quantitative values with citations; cross-references to existing papers (Baum-Snow & Han 2024, Saiz 2010, etc.); tags for vector search/query layer; catalog.yaml updated with metadata; git commits with detailed messages.
§
Construction TFP: CBR Vikharev (2026) — TFP main growth driver, labor negative to 2035. Expert RA (Aug 2026): dev margins 7-8% (was 12-15%), Net Debt/EBITDA >4x. Regional devs zero profit (cost ~150k/m², labor ×2-3, credit 5%→13%). Refs: queries/tfp-construction-data-sources.md, queries/developers-public-reporting.md (12-co panel ~35-40% market). Wiki ~250+ papers.
§
Price puzzle (RU): Sims 1992; Шестаков 2017; Борзых 2016; Банникова 2024; Колесник/Картаев/Зубарев 2025. All show it disappears on RU data. CBR Mogilat (Nov 2024) synthesizes. Cost channel < interest rate + communication channels.
§
Access: NBER WPs — curl works; gated return ~63KB HTML → stub until user sends PDF. DOM.RF blocks all. Rosstat=JS SPA. EMISS 403. Some ECB PDFs use custom font encoding (Gill Sans MT) without ToUnicode → garbled extraction. Translations in papers/ru_papers/, named: topic_author1_author2_year.RU.md. No tesseract (no sudo).
§
Hermes venv Python: /home/lnr/.hermes/hermes-agent/venv/bin/python3 (3.11). System python3 (3.12) is PEP 668 externally-managed. Install packages for execute_code in venv: /home/lnr/.hermes/hermes-agent/venv/bin/python3 -m pip install <pkg>. pymupdf4llm + deep_translator installed in venv.
§
Git push failures with "Invalid username or token" = expired GitHub token. User updates token externally; retry push after user confirms.