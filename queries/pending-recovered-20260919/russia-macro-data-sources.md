## Краткосрочные экономические показатели РФ (КЭП) — long RF-wide monthly series
file is `rosstat.gov.ru/storage/mediabank/ind_MM-YYYY.xlsx` (~1.7 MB), plain
`curl -sk`, **no geo-block**. Only the last few issues stay online — older month
files return 404, so a retrospective vintage starts the day you begin collecting.
**What it closes.** RF-wide monthly series from **1999** where the store had
almost nothing:
- sheet **1.7** — volume of works in «Строительство», monthly 1999–2026;
- sheet **1.8** — housing commissioned, monthly;
- sheet **1.6** — fixed-capital investment, monthly 1999–2015 (quarterly after);
- sheet **3.3** — aggregate investment-purpose price index INCLUDING a separate
  1999. **This closes the ИЦСП gap** (see the corrected note below).
Structure: 43 sheets (39 with data); each sheet = one indicator whose vertical
blocks are level → «в % к соответствующему периоду» → «в % к предыдущему
периоду». **A block must become a SEPARATE metric, not a sub-dimension**: the
unit lives on the metric, and the blocks differ (% vs level in rubles/m²).
Parsing is the hard part — stacked sub-tables, three header shapes, year
footnotes. The full identity-key recipe lives in skill
Publication timing: 1st–4th of the month, same day as the «Социально-
экономическое положение» report. The schedule is in Rosstat's OLE2 file
`Grafic_oper_public_YYYY.doc` (decode UTF-16LE, split on `\x07`/`\r`).
Automation recipe: same skill → `references/cron-source-refresh.md`.
- **ИЦСП — было «главным пробелом», но закрыто КЭП (лист 3.3, месячно с 1999)**. Оставшийся нерешённый участок — *региональные* ценовые ряды строительства и средние цены на материалы по субъектам: статические HTML-таблицы Росстата (`free_doc/new_site/prices/stroit/tab10.htm` сводный ИЦСП, `tab11.htm` ИЦП СМР, `tab12.htm` машины/оборудование, `tab13-cen.htm` средние цены ~50 материалов) **заморожены на 1995–2011 / 1996–2011**. Живые месячные РЕГИОНАЛЬНЫЕ ряды (2012–2026) существуют ТОЛЬКО в ЕМИСС: `gks.ru/scripts/db_inet/dbinet.cgi?pl=1926005` (сводный ИЦСП по субъектам), `pl=1926004` (ИЦП СМР по субъектам), `pl=1917001` (средние цены материалов по субъектам) — все 403/000 с ДЦ-IP. Натуральные объёмы материалов уже в `rosstat_construction.db` (`building_materials_monthly`, 2456 строк 2005–2026); не хватает именно **ценовых** рядов в рублях.
- **ИЦСП и ценовые ряды стройматериалов — частично УСТАРЕЛО.** Статические HTML-таблицы Росстата (`free_doc/new_site/prices/stroit/tab10.htm` сводный ИЦСП, `tab11.htm` ИЦП СМР, `tab12.htm` машины/оборудование, `tab13-cen.htm` средние цены ~50 материалов) действительно заморожены на 1995–2011 / 1996–2011. НО живые **РФ-уровневые** месячные ряды ИЦСП и сводного индекса инвестиционных цен с 1999 лежат в КЭП (раздел «КЭП» выше) и берутся без гео-блока. ЕМИСС (`gks.ru/scripts/db_inet/dbinet.cgi?pl=1926005` сводный ИЦСП, `pl=1926004` ИЦП СМР, `pl=1917001` средние цены материалов — все 403/000 с ДЦ-IP) остаётся нужен только для **региональных** разрезов. Натуральные объёмы материалов уже в `rosstat_construction.db` (`building_materials_monthly`, 2456 строк 2005–2026); региональные ценовые ряды в рублях по-прежнему пробел.
- **ИЦСП и ценовые ряды стройматериалов — главный пробел.** Статические HTML-таблицы Росстата (`free_doc/new_site/prices/stroit/tab10.htm` сводный ИЦСП, `tab11.htm` ИЦП СМР, `tab12.htm` машины/оборудование, `tab13-cen.htm` средние цены ~50 материалов) **заморожены на 1995–2011 / 1996–2011**. Для **РФ в целом** живые месячные ряды с 1999 берутся из бюллетеня КЭП, лист 3.3 (см. раздел КЭП выше) — ЕМИСС для этого НЕ нужен. Региональный разрез ИЦСП/цен материалов (2012–2026) — действительно только ЕМИСС: `gks.ru/scripts/db_inet/dbinet.cgi?pl=1926005` (сводный ИЦСП по субъектам), `pl=1926004` (ИЦП СМР по субъектам), `pl=1917001` (средние цены материалов по субъектам) — все 403/000 с ДЦ-IP. Натуральные объёмы материалов уже в `rosstat_construction.db` (`building_materials_monthly`, 2456 строк 2005–2026).