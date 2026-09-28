#!/usr/bin/env python3
"""Сверка метрики базы с первоисточником ЕМИСС.

Зачем: разово найденные расхождения (подмена метки региона, смена определения,
«ревизии», которых нет) повторяются от батча к батчу. Скрипт делает сверку
воспроизводимой: берёт метрику из core.observation_v2, тянет соответствующий
показатель ЕМИСС через emiss_loader, сопоставляет по региону и периоду и
печатает итог — сколько совпало, сколько расхождений, у кого и каких.

Сопоставление регионов идёт по data/emiss_region_aliases.yaml: сначала точное
имя, затем карта. Никаких нечётких подборов — именно они дали подмену полного
агрегата остаточной меткой.

Виды значений различаются отдельно (месячное против годового и накопленного):
в базе годовое лежит 01.01 … 31.12, накопленное помечено флагом cumulative_*.

Использование:
    python3 emiss_compare.py emiss_57824_wage_m 57824 \
        --select "Классификатор видов экономической деятельности=Всего по обследуемым видам деятельности"
    python3 emiss_compare.py emiss_31260_retail_m 31260 --select "Хозяйствующие субъекты в торговле=Всего"
    python3 emiss_compare.py emiss_31074_cpi_prevm_m 31074 \
        --select "Виды товаров и услуг=Все товары и услуги" --monthly --save-raw /tmp/31074.xml
"""

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from emiss_loader import Emiss  # noqa: E402
from db_tunnel import query   # noqa: E402

MONTHS = {"январь": 1, "февраль": 2, "март": 3, "апрель": 4, "май": 5, "июнь": 6,
          "июль": 7, "август": 8, "сентябрь": 9, "октябрь": 10, "ноябрь": 11, "декабрь": 12}
ALIASES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                            "data", "emiss_region_aliases.yaml")


def load_aliases():
    """Читает карту названий без внешних зависимостей (плоский yaml на два уровня)."""
    alias, skip = {}, []
    path = os.path.normpath(ALIASES_PATH)
    if not os.path.exists(path):
        return alias, skip
    section = None
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\S", line):
            section = line.split(":")[0].strip()
            continue
        if section == "aliases":
            m = re.match(r'^\s+"(.*?)":\s+"(.*?)"\s*$', line)
            if m:
                alias[m.group(1)] = m.group(2)
        elif section == "skip":
            m = re.match(r'^\s+-\s+"(.*?)"\s*$', line)
            if m:
                skip.append(m.group(1))
    return alias, skip


def source_rows(indicator_id, wanted, save_raw=None, view=None):
    e = Emiss()
    d = e.load(indicator_id, wanted=wanted or None, retries=3, pause=20, save_raw=save_raw)
    rows = d["rows"]
    if view:
        # вид показателя (например «К предыдущему месяцу») лежит в колонках
        # раскладки, а такие поля источник сужать не даёт: в ответе приходят все
        # виды сразу, поэтому нужный отбирается уже после загрузки — по коду
        # значения из структуры фильтров.
        field_title, value_title = view
        meta = d.get("meta") or {}
        vid = None
        for fid, field in (meta.get("filters") or {}).items():
            if (field.get("title") or "").strip().lower() != field_title.strip().lower():
                continue
            for v_id, v in (field.get("values") or {}).items():
                if (v.get("title") or "").strip().lower() == value_title.strip().lower():
                    vid = v_id
        if vid is None:
            raise SystemExit("вид показателя не найден: %s = %s" % (field_title, value_title))
        before = len(rows)
        rows = [r for r in rows if vid in {str(v) for k, v in r.items() if k.startswith("s_")}]
        print("отбор вида показателя «%s» (код %s): %d из %d точек" % (value_title, vid, len(rows), before))
    print("источник %s: точек %d | байт %d | попыток %d" % (indicator_id, len(rows), d["bytes"], d["attempts"]))
    return rows


def key_of(year, period, monthly):
    """Ключ периода: (YYYY-MM-01, вид) либо (YYYY-01-01, annual)."""
    p = (period or "").strip().lower()
    if p in MONTHS:
        return "%04d-%02d-01" % (int(year), MONTHS[p]), "monthly"
    m = re.match(r"^([а-я]+)-([а-я]+)$", p)
    if m and m.group(1) in MONTHS and m.group(2) in MONTHS:
        # «январь-декабрь» — это годовой итог, и в базе он лежит как 01.01 … 31.12
        # (годовое значение). Месячные ключи он не должен перекрывать: иначе
        # январское значение подменяется годовым.
        if MONTHS[m.group(2)] == 12:
            return "%04d-01-01" % int(year), "annual"
        return "%04d-%02d-01" % (int(year), MONTHS[m.group(2)]), "cumulative"
    if "год" in p:
        return "%04d-01-01" % int(year), "annual"
    return None, None


def main():
    ap = argparse.ArgumentParser(description="Сверка метрики базы с ЕМИСС")
    ap.add_argument("metric_code")
    ap.add_argument("indicator_id")
    ap.add_argument("--select", action="append", default=[],
                    help='отбор значения в источнике: "Поле=значение" (можно несколько)')
    ap.add_argument("--monthly", action="store_true", help="ряд месячный (иначе вид берётся из периода базы)")
    ap.add_argument("--view", default=None,
                    help='вид показателя для отбора после загрузки: "Поле=значение" (для полей из колонок)')
    ap.add_argument("--save-raw", default=None, help="сохранить сырой ответ ЕМИСС")
    ap.add_argument("--limit", type=int, default=10, help="сколько примеров расхождений печатать")
    args = ap.parse_args()

    wanted = {}
    for s in args.select:
        k, v = s.split("=", 1)
        wanted[k.strip()] = [x.strip() for x in v.split("|")]

    view = None
    if args.view:
        k, v = args.view.split("=", 1)
        view = (k.strip(), v.strip())

    alias, skip = load_aliases()
    src = {}
    for r in source_rows(args.indicator_id, wanted, args.save_raw, view):
        nm = (r.get("s_OKATO_name") or "").strip()
        y = (r.get("time") or "").strip()
        if not nm or not y.isdigit() or nm in skip:
            continue
        key, kind = key_of(y, r.get("PERIOD"), args.monthly)
        if key:
            src[(nm, key, kind)] = r.get("value")

    db = query("""SELECT o.obs_id, r.name_ru, o.period_start::text, o.period_end::text,
            o.value::float, coalesce(array_to_string(o.quality_flags,';'),'')
        FROM core.observation_v2 o JOIN core.metric m USING (metric_id)
        JOIN core.region r USING (region_id)
        WHERE m.metric_code=%s ORDER BY o.period_start""", (args.metric_code,))
    print("в базе строк: %d" % len(db))

    def kind_of(ps, pe, flags):
        if "cumulative" in (flags or ""):
            return "cumulative"
        if ps[5:7] == "01" and pe[5:7] == "12":
            return "annual"
        return "monthly"

    same = diff = unknown = 0
    bad = []
    unknown_names = collections.Counter()
    for obs_id, name, ps, pe, val, flags in db:
        kind = kind_of(ps, pe, flags)
        v = src.get((alias.get(name, name), ps, kind))
        if v is None:
            unknown += 1
            unknown_names[name] += 1
            continue
        if abs(v - val) < 0.005:
            same += 1
        else:
            diff += 1
            bad.append((name, ps, kind, val, v))

    print("\nсовпадает %d | расхождений %d | нет в источнике %d" % (same, diff, unknown))
    if bad:
        print("расхождения по регионам:", collections.Counter(b[0] for b in bad).most_common(10))
        for b in bad[:args.limit]:
            print("   %-34s %s %-9s база %s -> источник %s" % b)
    if unknown_names:
        print("без пары в источнике по регионам:", unknown_names.most_common(8))


if __name__ == "__main__":
    main()