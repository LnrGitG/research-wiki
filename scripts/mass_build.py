#!/usr/bin/env python3
"""mass_build.py — этап 4: evidence-пакет для массовой разметки.

Собирает по всем preliminary-метрикам реестра: имя, код, частота, единица,
значения (перв./посл./n), период, число регионов + evidence-заметки из
паспортов этапа 2 (индивидуальные и групповые).
Выход: data/etl/metric-review/mass/evidence_pack.json
"""
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import connect

OUT = "data/etl/metric-review/mass/evidence_pack.json"

# Индивидуальные заметки из паспортов (ключевые; полный источник — passports/)
NOTES = {
    "kep1_72": "КЭП лист 1.7: объём работ по виду деятельности Строительство, млрд руб., уровень за месяц",
    "kep1_7_y2": "КЭП лист 1.7: в % к соответствующему периоду предыдущего года",
    "kep1_7_m": "КЭП лист 1.7: в % к предыдущему периоду (месяц)",
    "kep1_7_m2": "КЭП лист 1.7: в % к предыдущему периоду (КВАРТАЛ; суффикс _m обманчив)",
    "kep1_7": "КЭП лист 1.7, колонка Год: объём за год",
    "kep1_6": "КЭП лист 1.6: инвестиции в основной капитал, млрд руб.; сноска: до 2001 с НДС, с 2016 квартальное наблюдение",
    "kep1_82": "КЭП лист 1.8: ввод жилых домов, млн кв.м за месяц; с августа 2019 включая садовые дома",
    "kep1_14": "КЭП лист 1.14: ИПЦ в % к предыдущему месяцу",
    "kep1_14_s": "КЭП лист 1.14: ИПЦ в % к соответствующему месяцу прошлого года",
    "kep1_12": "КЭП лист 1.1: объём ВВП, млрд руб., за квартал",
    "kep1_1_y2": "КЭП лист 1.1: ВВП в % к соотв. кварталу прошлого года",
    "kep1_2__2014_2026_m": "КЭП лист 1.2: ИПП без исключения сезонности, в % к предыдущему периоду",
    "kep1_143": "КЭП лист 1.14.2: стоимость фиксированного набора, руб.",
    "iokmrrk": "Росстат: инвестиции в основной капитал по регионам, НАРАСТАЮЩИЙ ИТОГ с начала года (2024: 5.94→14.4→24.1→39.9 трлн)",
    "sit": "ЦБ: средневзвешенная ставка по ИЖК ЗА МЕСЯЦ (форма 0409316), не темп",
    "sibud": "ЦБ: средневзвешенная ставка за месяц, ИЖК без ДДУ",
    "sid": "ЦБ: средневзвешенная ставка за месяц, ИЖК под залог ДДУ",
    "nikfi_2": "ЦБ: выдача ИЖК за месяц (сумма средств, предоставленных в течение месяца)",
    "nikfr": "ЦБ: выдача ИЖК в рублях за месяц",
    "nikfi": "ЦБ: выдача ИЖК в инвалюте за месяц",
    "y477030019": "ЦБ: остаток задолженности на отчётную дату",
    "y477030020": "ЦБ: остаток задолженности на отчётную дату, рубли",
    "y477030021": "ЦБ: остаток задолженности на отчётную дату, инвалюта",
    "y477030022": "ЦБ: остаток задолженности на отчётную дату, рубли",
    "eawb": "Число счетов эскроу с балансом НА ДАТУ",
    "osse": "Остатки на счетах эскроу НА ДАТУ",
    "kvse": "Количество счетов эскроу НА ДАТУ",
    "kvseo": "Количество счетов эскроу с остатком НА ДАТУ",
    "kvrse": "Количество РАСКРЫТЫХ счетов эскроу ЗА МЕСЯЦ (поток раскрытий)",
    "ssrse": "Сумма средств с раскрытых счетов эскроу ЗА МЕСЯЦ",
    "vsii": "ИФО ВДС строительства, % к соотв. кварталу прошлого года",
    "vvdsotrs": "ВДС строительства в основных ценах, уровень млрд руб.",
    "snz": "Росстат: среднемесячная начисленная зарплата (средняя ЗА МЕСЯЦ)",
    "ippsm": "ИПП в % к соответствующему месяцу прошлого года",
    "ksdrk": "Росреестр: количество сделок ДКП ЗА КВАРТАЛ",
    "tkzk": "Росстат: цена 1 кв.м жилья",
    "ozszv": "Росстат: отношение запаса строящегося жилья к вводу",
}

# Групповые заметки по префиксам кода (блоки ДОМ.РФ и др.)
GROUP_NOTES = [
    ("01_0", "ДОМ.РФ: показатель по проектам/ДДУ строительства, значение НА ОТЧЁТНУЮ ДАТУ (stock)"),
    ("kep1_", "КЭП Росстата; блок листа в коде; семантику смотри по значениям и базам сравнения блоков листа"),
    ("kep3_", "КЭП Росстата, раздел 3 (цены)"),
    ("kep4_", "КЭП Росстата, раздел 4 (доходы/население)"),
    ("y477", "Региональная таблица Росстата: годовое значение за год"),
]

FLOW_NAME_HINTS = ("выдач", "объем", "объём", "сделк", "введено", "выдано", "за месяц", "за квартал", "за год")


def note_for(code, name):
    if code in NOTES:
        return NOTES[code]
    for pref, note in GROUP_NOTES:
        if code.startswith(pref):
            return note
    return ""


def main():
    reg = list(csv.DictReader(open("data/metric-review/registry_summary.csv")))
    codes = [r["code"] for r in reg if r["status"] == "preliminary"]
    print(f"preliminary метрик: {len(codes)}")

    c = connect()
    c.execute("SET TRANSACTION READ ONLY")
    # основной проход: РФ + пустой разрез
    rows = c.execute("""
        SELECT m.metric_code, m.metric_id, m.name_ru, u.unit_code, m.frequency_id,
               (array_agg(o.value ORDER BY o.period_start))[1] fv,
               (array_agg(o.value ORDER BY o.period_start DESC))[1] lv,
               min(o.period_start), max(o.period_start), count(*),
               count(DISTINCT o.region_id)
        FROM core.metric m
        JOIN core.observation_v2 o ON o.metric_id = m.metric_id AND o.region_id = 1 AND o.sub_dimension = ''
        LEFT JOIN core.unit u ON u.unit_id = m.unit_id
        WHERE m.metric_code = ANY(%s)
        GROUP BY 1,2,3,4,5
    """, (codes,)).fetchall()
    by_code = {r[0]: r for r in rows}
    # добор без фильтров для пропущенных
    missing = [x for x in codes if x not in by_code]
    print(f"с РФ/чистым разрезом: {len(by_code)}; добор: {len(missing)}")
    if missing:
        rows2 = c.execute("""
            SELECT m.metric_code, m.metric_id, m.name_ru, u.unit_code, m.frequency_id,
                   (array_agg(o.value ORDER BY o.period_start))[1],
                   (array_agg(o.value ORDER BY o.period_start DESC))[1],
                   min(o.period_start), max(o.period_start), count(*),
                   count(DISTINCT o.region_id)
            FROM core.metric m JOIN core.observation_v2 o USING (metric_id)
            LEFT JOIN core.unit u ON u.unit_id = m.unit_id
            WHERE m.metric_code = ANY(%s)
            GROUP BY 1,2,3,4,5
        """, (missing,)).fetchall()
        by_code.update({r[0]: r for r in rows2})
    c.close()

    pack = []
    for code in codes:
        r = by_code.get(code)
        if not r:
            continue  # нет наблюдений — уже не preliminary, пропустить
        name = r[2] or ""
        pack.append({
            "id": int(r[1]), "code": code, "name_ru": name,
            "unit_db": r[3], "freq_id": int(r[4]),
            "first_value": float(r[5]) if r[5] is not None else None,
            "last_value": float(r[6]) if r[6] is not None else None,
            "period_min": str(r[7])[:10], "period_max": str(r[8])[:10],
            "n_obs_rf": int(r[9]), "n_regions": int(r[10]),
            "note": note_for(code, name),
            "flow_name_hint": any(h in (name or "").lower() for h in FLOW_NAME_HINTS),
        })
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(pack, open(OUT, "w"), ensure_ascii=False, indent=0)
    print(f"записано {len(pack)} метрик: {OUT}")


if __name__ == "__main__":
    main()
