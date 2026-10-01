# Манифест PDF к справке по международной практике (01.10.2026)

К справке `queries/cbr-international-practice-reference-20260930.md` скачаны
открытые версии цитируемых работ. Все файлы лежат в `raw/papers/` (YC Object
Storage, бакет `wiki-research`). Скрипт: `scripts/fetch_reference_pdfs.py`
(идемпотентный, проверяет `%PDF-` заголовок и маркер `%%EOF`).

## Скачано (11)

1. FSB (2020), The Use of Supervisory and Regulatory Technology by Authorities and Regulated Institutions, 1 300 008 Б.
2. BIS Innovation Hub и MAS (2022), Project Ellipse: an integrated regulatory data and analytics platform, 6 668 872 Б.
3. Baker, Bloom, Davis (2016), Measuring Economic Policy Uncertainty, QJE 131(4), 1 135 983 Б.
4. Ahir, Bloom, Furceri (2022), The World Uncertainty Index, NBER WP 29763, 1 436 718 Б.
5. Shapiro, Sudhof, Wilson (2020), Measuring News Sentiment, FRBSF WP 2017-01, 1 038 737 Б.
6. Silva, Moriya, Veyrune (2025), From Text to Quantified Insights, IMF WP/25/109, 7 784 020 Б (93 стр.).
7. Pfeifer, Marohl (2023), CentralBankRoBERTa, arXiv:2310.17691, 1 396 050 Б.
8. Gambacorta, Kwon, Park, Patelli, Zhu (2025), CB-LMs, BIS WP 1215, 677 247 Б.
9. di Castri, Hohl, Kulenkampff, Prenio (2019), The Suptech Generations, FSI Insights 19, 1 024 574 Б.
10. Broeders, Prenio (2018), Innovative Technology in Financial Supervision, FSI Insights 9, 483 608 Б.
11. Loughran, McDonald (2011), When Is a Liability Not a Liability, J. Finance 66(1), 295 472 Б.

## Недоступно (1)

- Chen, Mo, Tang, Li (2023), Measuring Real Estate Policy Uncertainty in China,
  China Economic Quarterly International 3(1), 23-34, DOI 10.1016/j.ceqi.2023.02.003.
  Статус по Unpaywall — gold OA, лицензия CC BY-NC-ND, но `url_for_pdf = null`:
  PDF размещён только на ScienceDirect, закрытом Cloudflare-капчей, зеркал нет
  (проверены Wayback, SSRN, Unpaywall, Semantic Scholar, CORS-прокси). Нужна
  дополнительная проверка: запросить у департамента или взять через
  университетский доступ.

## Технические замечания

- IMF (п. 6): `www.imf.org` за Akamai отдаёт 403 датацентровым клиентам. Файл
  взят из Wayback Machine; сырая копия отдаётся двумя кусками (5 МиБ и
  остаток), поэтому догрузка идёт Range-запросом с конкатенацией. Итог сходится
  с исходным размером 7 784 020 Б.
- BIS (пп. 2, 8, 9, 10): сайт перешёл на новую схему URL `/publications/<slug>.pdf`;
  старые пути `/publ/work1215.pdf` и `/fsi/publ/insightsNN.pdf` теперь отдают HTML.