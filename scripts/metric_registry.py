#!/usr/bin/env python3
"""metric_registry.py — этап 1 конвейера: реестр кандидатов рабочего набора.

Детерминированные правила статусов + тематические метки единого набора
«Экономика и ДКП РФ» (строительство и жильё — приоритетный блок).
Ничего не удаляет и не пишет в БД: выход — YAML-реестр + CSV в репо.

Правила (консервативные, пересматриваются только человеком):
- quarantine_data_error — подтверждённые дефекты загрузки (фictивная частота,
  конфликт частот, будущие периоды);
- archive_dead — последний период < 2024-01 (ряды, не обновлявшиеся 2+ года);
- preliminary — всё живое, до сверки с первоисточником (этап 2 конвейера);
- short — ограничение применимости (< 24 точек), НЕ статус качества.

Запуск: python3 scripts/metric_registry.py [--dry-run]
Вход:  data/etl/metric-review/metric_catalog.csv (2438 строк, аудит 2026-09-20)
Выход: data/metric-review/registry.yaml (+ registry_summary.csv) — версионированные.
"""
import csv
import os
import sys
from collections import Counter

import yaml

CATALOG = "data/etl/metric-review/metric_catalog.csv"  # аудитный вход, вне git
OUT_YAML = "data/metric-review/registry.yaml"  # версионированный выход
OUT_CSV = "data/metric-review/registry_summary.csv"
DEAD_CUTOFF = "2024-01-01"
# Порог будущего = конец текущего месяца на дату генерации (2026-09-20):
# периоды позже 2026-09-30 ещё не могли наблюдаться.
FUTURE_CUTOFF = "2026-09-30"
MIN_POINTS = 24

# Подтверждённые дефекты аудита 2026-09-20 (сверка живой БД + первоисточников):
KNOWN_DEFECTS = {
    "kep1_112": {
        "defect": "fictitious_frequency",
        "evidence": "ind_07-2026.xlsx лист 1.11, кумулятивный блок; в БД freq_id=5 (месячная) при годовых значениях колонки «Янв.»",
        "action": "quarantine до перепаспортизации на этапе 2",
    },
    "spv": {
        "defect": "freq_conflict_declared_vs_obs",
        "evidence": "core.metric.frequency_id=3 (годовая), наблюдения: 5 строк frequency_id=5 за period_start=2026-08-01 (SQL 2026-09-20)",
        "action": "quarantine до выяснения природы «Сводного показателя» на этапе 2",
    },
    "kep4_45": {
        "defect": "future_periods",
        "evidence": "3 наблюдения 2026-10..2026-12 при дате генерации 2026-09-20 — вероятен сдвиг годового блока листа 4.5 при парсинге",
        "action": "quarantine до сверки листа с исходником",
    },
    "kep4_46": {
        "defect": "future_periods",
        "evidence": "1 наблюдение 2026-10 при дате генерации 2026-09-20 — вероятен сдвиг годового блока листа 4.6 при парсинге",
        "action": "quarantine до сверки листа с исходником",
    },
}

# Тематические метки единого набора (ключевые слова по name_ru, lowercase).
# Одна метрика может входить в несколько блоков. Это ПОИСКОВЫЕ метки,
# не решение о включении/исключении.
THEME_KEYWORDS = {
    "dkp_macro": ["ключевая ставка", "денежная massa", "денежная масса", "м2 ", "ввп", "инфляц",
                  "потребительск", "ипц", "дефлятор", "курс рубл", "межбанковск", "безработиц",
                  "занятост", "доходы насел", "зарплат", "пенсии", "промышленн", "объём работ"],
    "construction": ["строительств", "объем работ", "объём работ", "смир", "вдс", "стройматериал",
                     "цемент", "бетон", "кирпич", "жби", "инвестиц", "внок", "икв", "основной капитал"],
    "housing_mortgage": ["ипотек", "жилищн", "жил. здан", "жилых", "жиль", "дду", "эскроу",
                         "долевом", "застройщик", "квартир", "кв. м", "кв.м", "первичн", "вторичн",
                         "льготн", "семейная ипотек", "здани"],
    "regional_panel_hint": [],  # региональность — по n_regions, не по имени
}


def classify(row):
    """(status, flags, themes) для одной метрики."""
    flags = []
    code = row["metric_code"]
    freq = row["frequency"]
    n_obs = int(row["n_obs"] or 0)
    period_max = row["period_max"] or ""
    n_freq_in_obs = int(row["n_freq_in_obs"] or 0)

    # 1. Подтверждённые дефекты
    if code in KNOWN_DEFECTS:
        return "quarantine_data_error", ["known_defect"], None

    # 2. Конфликт частот в наблюдениях (аудит: метрика 160 spv — 5 точек)
    if n_freq_in_obs > 1:
        return "quarantine_data_error", ["freq_conflict_in_obs"], None

    # 3. Будущие периоды (аудит: kep4_45/46 — 2026-10..12)
    if period_max and period_max > FUTURE_CUTOFF:
        flags.append("future_periods")
        return "quarantine_data_error", flags, None

    # 4. Нет наблюдений вообще
    if n_obs == 0:
        return "quarantine_data_error", ["no_observations"], None

    # 5. Пустые значения в значительной доле — не карантин, ограничение
    n_null = int(row["n_null_values"] or 0)
    n_ph = int(row["n_placeholders"] or 0)
    if n_obs and (n_null + n_ph) / n_obs > 0.5:
        flags.append("mostly_empty")

    # 6. Мёртвый ряд → архив (не удаление!)
    if period_max and period_max < DEAD_CUTOFF:
        flags.append("dead")
        status = "archive_dead"
    else:
        status = "preliminary"

    # Ограничения применимости (не статус)
    if n_obs < MIN_POINTS:
        flags.append("short")
    if int(row["n_regions"] or 0) >= 80:
        flags.append("regional_panel")

    return status, flags, None


def themes_for(row):
    name = (row["name_ru"] or "").lower()
    code = (row["metric_code"] or "").lower()
    themes = []
    for theme, kws in THEME_KEYWORDS.items():
        if not kws:
            continue
        if any(k in name for k in kws):
            themes.append(theme)
            continue
    # эскроу-коды ebs/eawb — по коду, имя не содержит слова «эскроу»
    if code.startswith(("ebs", "eawb")):
        if "housing_mortgage" not in themes:
            themes.append("housing_mortgage")
    return themes


def main():
    dry = "--dry-run" in sys.argv
    with open(CATALOG, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2438, f"ожидается 2438 метрик, получено {len(rows)}"

    registry = {"research_set": "Экономика и ДКП РФ (строительство и жильё — приоритет)",
                "generated": "2026-09-20", "input": "metric_catalog.csv (аудит 2026-09-20)",
                "rules": {"dead_cutoff": DEAD_CUTOFF, "min_points": MIN_POINTS,
                          "note": "статусы preliminary до этапа 2 (паспорта источников); "
                                  "архив и карантин не удаляются"},
                "known_defects": KNOWN_DEFECTS,
                "metrics": []}
    summary_rows = []
    dist = Counter()
    theme_dist = Counter()

    for row in rows:
        status, flags, _ = classify(row)
        themes = themes_for(row)
        # quarantine — тема не важна
        entry = {"metric_id": int(row["metric_id"]), "code": row["metric_code"],
                 "status": status, "flags": flags, "themes": themes}
        registry["metrics"].append(entry)
        summary_rows.append({**entry, "name_ru": row["name_ru"], "freq": row["frequency"],
                             "n_obs": row["n_obs"], "period_max": row["period_max"],
                             "source": row["source"]})
        dist[status] += 1
        for t in themes:
            theme_dist[t] += 1

    print(f"метрик: {len(rows)}")
    print(f"статусы: {dict(dist)}")
    print(f"темы (вхождений): {dict(theme_dist)}")
    flagged_q = [r for r in summary_rows if r["status"] == "quarantine_data_error"]
    print(f"карантин ({len(flagged_q)}):")
    for r in flagged_q[:12]:
        print(f"  {r['code']} [{r['flags']}] {r['name_ru'][:50]}")

    if not dry:
        os.makedirs(os.path.dirname(OUT_YAML), exist_ok=True)
        with open(OUT_YAML, "w", encoding="utf-8") as f:
            yaml.safe_dump(registry, f, allow_unicode=True, sort_keys=False)
        with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
            w.writeheader()
            w.writerows(summary_rows)
        print(f"записано: {OUT_YAML}, {OUT_CSV}")
    else:
        print("dry-run: файлы не записаны")


if __name__ == "__main__":
    main()
