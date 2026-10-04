#!/usr/bin/env python3
import sys
sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query

print("=== метрики, похожие на ключевые макроагрегаты ===")
pats = {
 "инфляция/ИПЦ": r"индекс потребительских цен|ипц|инфляц",
 "ключевая ставка": r"ключевая ставка",
 "ВВП": r"валовый внутренний продукт|ввп",
 "безработица": r"безработ",
 "потребление": r"потребительские расходы|оборот розничной",
 "инвестиции": r"инвестиции в основной капитал",
 "промпроизводство": r"индекс промышленного производства",
 "зарплата": r"заработная плата|зарплат",
 "ипотека": r"ипотечн",
 "ввод жилья": r"ввод.*жил|введено.*жил",
}
for label, pat in pats.items():
    rows = query("""SELECT metric_id, metric_code, left(name_ru,60), frequency_id
                    FROM catalog.metric
                    WHERE lower(coalesce(name_ru,'')) ~ %s AND is_active
                    ORDER BY metric_id LIMIT 6""", (pat,))
    print(f"\n--- {label} ({len(rows)} показано)")
    for r in rows:
        print(f"   {r[0]:7d} | {r[1][:32]:32s} | {r[2][:52]} | freq={r[3]}")