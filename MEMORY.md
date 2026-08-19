User is a researcher/analyst working on Russian housing market economics. Maintains a research wiki (research-wiki repo) with papers, catalog.yaml, and queries. Focus: supply elasticity estimation, demographic forecasting, mortgage markets.
§
User prefers: bilingual RU/EN structure preserved; exact quantitative values with citations; cross-references to existing papers (Baum-Snow & Han 2024, Saiz 2010, etc.); tags for vector search/query layer; catalog.yaml updated with metadata; git commits with detailed messages.
§
Construction TFP: Refs: queries/tfp-construction-data-sources.md, queries/developers-public-reporting.md (12-co panel ~35-40% market). Wiki ~250+ papers.
§
Access: NBER WPs — curl works; gated return ~63KB HTML → stub until user sends PDF. DOM.RF blocks all. Rosstat=JS SPA. EMISS 403. Some ECB PDFs use custom font encoding (Gill Sans MT) without ToUnicode → garbled extraction. Translations in papers/ru_papers/, named: topic_author1_author2_year.RU.md. No tesseract (no sudo).
§
Hermes venv Python: /home/lnr/.hermes/hermes-agent/venv/bin/python3 (3.11). System python3 (3.12) is PEP 668 externally-managed. Install packages for execute_code in venv: /home/lnr/.hermes/hermes-agent/venv/bin/python3 -m pip install <pkg>. pymupdf4llm + deep_translator installed in venv.
