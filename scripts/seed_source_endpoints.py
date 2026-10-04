#!/usr/bin/env python3
"""Наполнение catalog.source_endpoint — точки публикации и расписание опроса.

Это фундамент автообновления: таблица говорит, куда ходить, как часто и
каким скриптом разбирать. Пока заполнены те источники, для которых разбор
уже существует; наполнение расширяется по мере появления парсеров.
"""
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import execute, query

EP = [
 # source_code, url, kind, poll_cron, parser_script, note
 ("rosstat", "https://rosstat.gov.ru/compendium/document/50798", "html_feed",
  "0 */2 * * *", "kep_collect.py",
  "Лента «Срочные информации»: пары PDF+HTML; обновляет ИЦП, ИПП, задолженность по ЗП — месячно, ВВП по использованию — квартально"),
 ("rosstat", "https://rosstat.gov.ru/storage/mediabank/", "file_store", "0 */2 * * *",
  None, "Хранилище файлов ленты; ссылки берутся из страницы ленты"),
 ("fedstat_emiss", "https://www.fedstat.ru/indicator/31074", "api_post", "0 6 * * *",
  "step2_ingest_all.py",
  "ИПЦ — все товары и услуги, % к пред. мес. Протокол: GET страницы показателя ради токена, затем POST downloadData.do"),
 ("cbr", "https://www.cbr.ru/hd_base/KeyRate/", "html_table", "0 12 * * *",
  "load_cbr_keyrate.py",
  "Ключевая ставка: решения по календарю, 8 раз в год"),
 ("cbr", "https://www.cbr.ru/statistics/", "html_section", "0 12 * * *",
  "load_cbr_lending.py", "Денежно-кредитная статистика Банка России"),
 ("fns", "https://www.nalog.gov.ru/opendata/", "opendata_index", "0 4 * * 1",
  "fns_opendata_collect.py", "Открытые данные ФНС, недельный обход индекса"),
 ("domrf", "https://дом.рф/analytics/", "html_section", "0 5 * * 1",
  "ingest_domrf.py", "Аналитика ДОМ.РФ: жилищный слой"),
 ("rosreestr", "https://rosreestr.gov.ru/opendata/", "opendata_index", "0 5 * * 1",
  None, "Открытые данные Росреестра"),
]

print("=== добавление точек публикации ===")
added = 0
for code, url, kind, cron, parser, note in EP:
    sid = query("SELECT source_id FROM catalog.source WHERE source_code=%s", (code,))
    if not sid:
        print(f"   пропуск {code}: нет источника")
        continue
    sid = sid[0][0]
    try:
        execute("""INSERT INTO catalog.source_endpoint
                   (source_id, url, kind, poll_cron, parser_script, note)
                   VALUES (%s,%s,%s,%s,%s,%s)""",
                (sid, url, kind, cron, parser, note))
        added += 1
        print(f"   OK {code:14s} {kind:16s} {url[:52]}")
    except Exception as e:
        print(f"   ERR {code}: {str(e)[:140]}")

print(f"\n   добавлено: {added}")
print("   всего точек:", query("SELECT count(*) FROM catalog.source_endpoint")[0][0])

print("\n=== сводка по источникам ===")
for r in query("""SELECT s.source_code, count(*) AS точек,
                         string_agg(DISTINCT e.kind, ', ') AS виды
                  FROM catalog.source_endpoint e
                  JOIN catalog.source s ON s.source_id = e.source_id
                  GROUP BY 1 ORDER BY 2 DESC"""):
    print(f"   {r[0]:14s} {r[1]}  ({r[2]})")

try:
    execute("GRANT SELECT ON catalog.source_endpoint TO viewer, datalens_ro, agent_ro")
    print("\n   права выданы")
except Exception as e:
    print("\n   ERR прав:", str(e)[:150])