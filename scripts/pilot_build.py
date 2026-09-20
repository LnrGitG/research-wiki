#!/usr/bin/env python3
"""pilot_build.py — этап 3: сборка стратифицированной пилотной выборки 60 метрик.

Эталон (gold) — из evidence-паспортов этапа 2, сверенных с первоисточниками.
Два условия: name_only (как в старом плане) и evidence (имя+источник+шапка+значения).
Выход: data/etl/metric-review/pilot/pilot_sample.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/scripts")
from db_tunnel import connect

OUT = "data/etl/metric-review/pilot/pilot_sample.json"

# Эталон из паспортов (этап 2): (code, temporal_type, accumulation, comparison_base, tricky)
GOLD = [
    # СМР/ИКВ
    ("kep1_72", "flow", "single_period", "level", ""),
    ("kep1_7_y2", "index", "single_period", "same_period_last_year", ""),
    ("kep1_7_m", "index", "single_period", "previous_period", ""),
    ("kep1_7_m2", "index", "single_period", "previous_period", "суффикс _m при QoQ"),
    ("kep1_7", "flow", "single_period", "level", ""),
    ("vsii", "index", "single_period", "same_period_last_year", ""),
    ("vvdsotrs", "flow", "single_period", "level", ""),
    ("iokmrrk", "flow", "year_to_date", "level", "нарастающий итог"),
    ("y477110107", "flow", "single_period", "level", ""),
    ("kep1_6", "flow", "single_period", "level", ""),
    ("kep1_82", "flow", "single_period", "level", ""),
    ("vztgr", "flow", "single_period", "level", ""),
    ("y477110016", "flow", "single_period", "level", ""),
    ("tkzk", "price", "single_period", "level", ""),
    ("ozszv", "ratio", "single_period", "level", ""),
    # ипотека/эскроу
    ("nikfi_2", "flow", "single_period", "level", ""),
    ("nikfr", "flow", "single_period", "level", ""),
    ("nikfi", "flow", "single_period", "level", ""),
    ("y477030019", "stock", "single_period", "level", ""),
    ("y477030020", "stock", "single_period", "level", ""),
    ("y477030021", "stock", "single_period", "level", ""),
    ("y477030022", "stock", "single_period", "level", ""),
    ("sit", "average", "single_period", "level", "ставка, не темп"),
    ("sibud", "average", "single_period", "level", "ставка"),
    ("sid", "average", "single_period", "level", "ставка"),
    ("eawb", "stock", "single_period", "level", ""),
    ("osse", "stock", "single_period", "level", ""),
    ("kvse", "stock", "single_period", "level", ""),
    ("kvseo", "stock", "single_period", "level", ""),
    ("kvrse", "flow", "single_period", "level", "раскрытия за месяц = поток"),
    ("ssrse", "flow", "single_period", "level", ""),
    ("01_03_04", "stock", "single_period", "level", ""),
    ("01_03_06", "stock", "single_period", "level", ""),
    ("ksdrk", "flow", "single_period", "level", ""),
    # ДКП-макро
    ("kep1_14", "index", "single_period", "previous_period", ""),
    ("kep1_14_s", "index", "single_period", "same_period_last_year", "пара с kep1_14"),
    ("kep1_143", "price", "single_period", "level", ""),
    ("kep1_12", "flow", "single_period", "level", ""),
    ("kep1_1_y2", "index", "single_period", "same_period_last_year", ""),
    ("ippsm", "index", "single_period", "same_period_last_year", ""),
    ("kep1_2__2014_2026_m", "index", "single_period", "previous_period", ""),
    ("snz", "average", "single_period", "level", "зарплата за месяц"),
    ("orspp", "index", "single_period", "previous_period", "близнец kep1_7_m"),
    ("vzep", "flow", "single_period", "level", "1 наблюдение"),
    ("vztp", "flow", "single_period", "level", "1 наблюдение"),
    # проекты/ДДУ ДОМ.РФ
    ("01_03_01", "stock", "single_period", "level", "периметр деклараций"),
    ("01_03_02", "stock", "single_period", "level", ""),
    ("01_03_03", "stock", "single_period", "level", ""),
    ("01_03_05", "stock", "single_period", "level", "периметр жилых"),
    ("01_01_05", "stock", "single_period", "level", ""),
    ("01_01_06", "stock", "single_period", "level", ""),
    ("01_01_07", "stock", "single_period", "level", ""),
    ("01_01_08", "stock", "single_period", "level", ""),
    ("01_02_01", "stock", "single_period", "level", ""),
    ("01_02_02", "stock", "single_period", "level", ""),
    ("01_02_04", "stock", "single_period", "level", ""),
    ("01_02_09", "stock", "single_period", "level", ""),
    ("01_02_10", "stock", "single_period", "level", ""),
    ("01_02_12", "stock", "single_period", "level", ""),
    ("01_02_13", "stock", "single_period", "level", ""),
]
assert len(GOLD) == 60, f"ожидалось 60, получено {len(GOLD)}"
codes = [g[0] for g in GOLD]
assert len(set(codes)) == 60, "дубли кодов"

# Методологические заметки (evidence) из паспортов этапа 2
NOTES = {
    "kep1_72": "КЭП лист 1.7, шапка: «Объем работ по виду деятельности Строительство (в фактических ценах), млрд рублей», блок уровня по месяцам",
    "kep1_7_y2": "КЭП лист 1.7, блок «в % к соответствующему периоду предыдущего года»",
    "kep1_7_m": "КЭП лист 1.7, блок «в % к предыдущему периоду», месячные значения",
    "kep1_7_m2": "КЭП лист 1.7, блок «в % к предыдущему периоду», КВАРТАЛЬНЫЕ значения (суффикс _m обманчив)",
    "kep1_7": "КЭП лист 1.7, колонка «Год»",
    "kep1_6": "КЭП лист 1.6 «Инвестиции в основной капитал, млрд рублей», сноска: до 2001 с НДС; наблюдение квартальное с 2016",
    "kep1_82": "КЭП лист 1.8 «Ввод в действие жилых домов, млн кв.м», сноска: с августа 2019 включая дома на садовых участках",
    "kep1_14": "КЭП лист 1.14, «ИПЦ в % к предыдущему месяцу»",
    "kep1_14_s": "КЭП лист 1.14, ИПЦ «в % к соответствующему месяцу предыдущего года»",
    "kep1_12": "КЭП лист 1.1, «Объем ВВП, млрд рублей», квартальные значения",
    "kep1_1_y2": "КЭП лист 1.1, ВВП «в % к соотв. кварталу предыдущего года»",
    "kep1_2__2014_2026_m": "КЭП лист 1.2, ИПП без исключения сезонности, «в % к предыдущему периоду»",
    "kep1_143": "КЭП лист 1.14.2, «Стоимость фиксированного набора товаров и услуг, рублей»",
    "iokmrrk": "Росстат, инвестиции в основной капитал по регионам; 2024: Q1=5.94, Q2=14.4, Q3=24.1, Q4=39.9 трлн — значения нарастают в течение года",
    "sit": "ЦБ РФ, методология: средневзвешенная по объёму и сроку кредитов ЗА МЕСЯЦ (форма 0409316)",
    "sibud": "ЦБ РФ: средневзвешенная ставка за месяц по ИЖК без учёта ДДУ",
    "sid": "ЦБ РФ: средневзвешенная ставка за месяц по ИЖК под залог прав по ДДУ",
    "nikfi_2": "ЦБ РФ: «сумма средств, предоставленных в течение отчетного месяца» (выдача за месяц)",
    "nikfr": "ЦБ РФ: выдача ИЖК в рублях за месяц",
    "nikfi": "ЦБ РФ: выдача ИЖК в инвалюте за месяц",
    "y477030019": "ЦБ РФ: «остаток задолженности по состоянию на отчетную дату»",
    "y477030020": "ЦБ РФ: остаток задолженности на отчетную дату, рубли",
    "y477030021": "ЦБ РФ: остаток задолженности на отчетную дату, инвалюта",
    "y477030022": "ЦБ РФ: остаток задолженности на отчетную дату, рубли",
    "eawb": "ЦБ/ДОМ.РФ: escrow_accounts_with_balance — число счетов эскроу с ненулевым балансом на дату",
    "osse": "Остатки средств на счетах эскроу на дату",
    "kvse": "Количество счетов эскроу на дату",
    "kvseo": "Количество счетов эскроу с остатком на дату",
    "kvrse": "Количество РАСКРЫТЫХ счетов эскроу (за месяц)",
    "ssrse": "Сумма средств с раскрытых счетов эскроу за месяц",
    "01_03_01": "ДОМ.РФ: действующие ДДУ по данным проектных деклараций, на дату",
    "01_03_02": "ДОМ.РФ: площадь квартир с действующими ДДУ, на дату",
    "01_03_03": "ДОМ.РФ: суммарная цена действующих ДДУ, на дату",
    "01_03_04": "ДОМ.РФ: действующие ДДУ на жилые помещения, на дату",
    "01_03_05": "ДОМ.РФ: площадь квартир с действующими ДДУ (жилые), на дату",
    "01_03_06": "ДОМ.РФ: суммарная цена действующих ДДУ (жилые), на дату",
    "01_01_05": "ДОМ.РФ: количество строящихся МКД с ДДУ-финансированием, на дату",
    "01_01_06": "ДОМ.РФ: общая площадь строящихся МКД, на дату",
    "01_01_07": "ДОМ.РФ: жилая площадь строящихся МКД, на дату",
    "01_01_08": "ДОМ.РФ: количество квартир в строящихся МКД, на дату",
    "01_02_01": "ДОМ.РФ: МКД в составе проектов с размещёнными проектными декларациями, на дату",
    "01_02_02": "ДОМ.РФ: общая площадь МКД в проектах, на дату",
    "01_02_04": "ДОМ.РФ: количество квартир в МКД проектов, на дату",
    "01_02_09": "ДОМ.РФ: МКД в проектах групп застройщиков, на дату",
    "01_02_10": "ДОМ.РФ: общая площадь МКД (группы застройщиков), на дату",
    "01_02_12": "ДОМ.РФ: количество квартир (группы застройщиков), на дату",
    "01_02_13": "ДОМ.РФ: МКД в проектах, на дату",
    "ksdrk": "Росреестр: количество сделок ДКП за квартал",
    "snz": "Росстат: среднемесячная начисленная зарплата (средняя за месяц)",
    "ippsm": "Росстат: ИПП в % к соответствующему месяцу прошлого года",
    "orspp": "socio_economic_report: объём работ Строительство, % к предыдущему периоду",
    "vzep": "Росстат: введено зданий (промышленные) за период",
    "vztp": "Росстат: введено зданий, тыс. кв.м (промышленные) за период",
    "vsii": "ВДС строительства: индекс физического объёма в % к соотв. кварталу прошлого года",
    "vvdsotrs": "ВДС строительства в основных ценах, уровень, млрд руб.",
    "y477110107": "Росстат региональная таблица: инвестиции в основной капитал за год",
    "y477110016": "Росстат: ввод в действие жилых домов за год",
    "vztgr": "Росстат: ввод жилья за год, тыс. кв.м",
    "tkzk": "Росстат: цена 1 кв.м жилья",
    "ozszv": "Росстат: отношение запаса строящегося жилья к вводу",
}


def main():
    c = connect()
    c.execute("SET TRANSACTION READ ONLY")
    rows = c.execute("""
        SELECT m.metric_code, m.metric_id, m.name_ru, u.unit_code, m.frequency_id,
               (array_agg(o.value ORDER BY o.period_start))[1] first_v,
               (array_agg(o.value ORDER BY o.period_start DESC))[1] last_v,
               min(o.period_start), max(o.period_start), count(*)
        FROM core.metric m
        JOIN core.observation_v2 o USING (metric_id)
        LEFT JOIN core.unit u ON u.unit_id = m.unit_id
        WHERE m.metric_code = ANY(%s) AND o.region_id = 1 AND o.sub_dimension = ''
        GROUP BY 1,2,3,4,5
    """, (codes,)).fetchall()
    c.close()
    by_code = {r[0]: r for r in rows}
    missing = [x for x in codes if x not in by_code]
    # для метрик без region_id=1 или пустого subdim — повторный запрос без фильтров
    if missing:
        c = connect()
        c.execute("SET TRANSACTION READ ONLY")
        rows2 = c.execute("""
            SELECT m.metric_code, m.metric_id, m.name_ru, u.unit_code, m.frequency_id,
                   (array_agg(o.value ORDER BY o.period_start))[1],
                   (array_agg(o.value ORDER BY o.period_start DESC))[1],
                   min(o.period_start), max(o.period_start), count(*)
            FROM core.metric m JOIN core.observation_v2 o USING (metric_id)
            LEFT JOIN core.unit u ON u.unit_id = m.unit_id
            WHERE m.metric_code = ANY(%s)
            GROUP BY 1,2,3,4,5
        """, (missing,)).fetchall()
        c.close()
        by_code.update({r[0]: r for r in rows2})

    sample = []
    for code, tt, acc, cb, tricky in GOLD:
        r = by_code.get(code)
        assert r, f"нет данных для {code}"
        sample.append({
            "id": int(r[1]), "code": code, "name_ru": r[2],
            "unit_db": r[3], "freq_id": int(r[4]),
            "first_value": float(r[5]) if r[5] is not None else None,
            "last_value": float(r[6]) if r[6] is not None else None,
            "period_min": str(r[7])[:10], "period_max": str(r[8])[:10],
            "n_obs_rf": int(r[9]),
            "evidence_note": NOTES.get(code, ""),
            "gold": {"temporal_type": tt, "accumulation": acc, "comparison_base": cb},
            "tricky": tricky,
            "stratum": tt,
        })
    # holdout: каждое третье значение внутри каждой stratum (детерминированно)
    from collections import defaultdict
    by_str = defaultdict(list)
    for s in sample:
        by_str[s["stratum"]].append(s["code"])
    holdout = set()
    for stratum, lst in by_str.items():
        for i, code in enumerate(lst):
            if i % 3 == 1:
                holdout.add(code)
    for s in sample:
        s["holdout"] = s["code"] in holdout

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(sample, open(OUT, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(f"60 метрик записано: {OUT}")
    print("страты:", dict(Counter(s['stratum'] for s in sample)))
    print("holdout:", len(holdout), "| tuning:", 60 - len(holdout))


if __name__ == "__main__":
    main()
