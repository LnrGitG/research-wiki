#!/usr/bin/env python3
"""Шаблон доклада ГУ: топ-15 регионов против общероссийского тренда.

Формат (утверждён владельцем): по каждой метрике среза v1 —
- общероссийский тренд (медиана/среднее по субъектам, а не только РФ-агрегат);
- топ-15 регионов по абсолютному уровню/скорости;
- лидеры и аутсайдеры (3+3);
- малые регионы — сглаживание 3 мес.

Выход: data/gu_report_template_202610.md — готовый скелет раздела
«регионы против тренда» для доклада начальника ГУ.
"""
import csv
import os
import statistics
from collections import defaultdict

SLICE = os.path.expanduser('~/research-wiki-private/data/region_slice_full_202610.csv')
OUT = os.path.expanduser('~/research-wiki-private/data/gu_report_template_202610.md')

SMALL_POP = 1.0  # порог (млн) для «малых» — упрощённо: регионы с вводом жилья < 100 тыс. м²/год

# метрики, где "выше = хуже" (для знака лидеры/аутсайдеры)
WORSE_HIGHER = {'A_cpi'}

NOMEN = {
    'A_cpi': ('ИПЦ, % к пред. месяцу', 'A', 'мес'),
    'B_wage': ('Номинальная ЗП, руб.', 'B', 'мес'),
    'B_unemp': ('Безработица МОТ 15+, %', 'B', 'кв'),
    'C_kf': ('Кредиты физлицам (потр. и ипотека), задолженность', 'C', 'мес'),
    'C_kyl': ('Кредиты юрлицам и ИП, задолженность', 'C', 'мес'),
    'C_hdebt_long': ('Жилищные кредиты, задолженность (VFS, с 2019)', 'C', 'мес'),
    'C_mdebt_ihk': ('ИЖК, задолженность (ЦБ, с 07.2025)', 'C', 'мес'),
    'C_hnew_long': ('Выдачи жилищных кредитов (VFS, с 2019)', 'C', 'мес'),
    'C_mnew_ihk': ('Объём ИЖК (ЦБ, Т_19)', 'C', 'мес'),
    'C_hrate_long': ('Ставка по жилищным кредитам (VFS)', 'C', 'мес'),
    'C_irate_ihk': ('Ставка по ИЖК (ЦБ, Т_26)', 'C', 'мес'),
    'E_housing': ('Ввод жилья, тыс. кв. м', 'E', 'мес'),
    'E_izhs': ('Ввод ИЖС, тыс. кв. м', 'E', 'мес'),
    'F_snz': ('Средняя ЗП, руб.', 'F', 'мес'),
}


def load():
    data = defaultdict(lambda: defaultdict(dict))  # metric -> region -> period -> value
    with open(SLICE) as f:
        for r in csv.DictReader(f):
            mc, reg, ps, v = (r['block_metric'].strip(), r['region'].strip(),
                              r['period'].strip(), r['value'].strip())
            try:
                data[mc][reg][ps] = float(v)
            except ValueError:
                continue
    return data


def series(d):
    """Регион -> {period: value} -> {region: last value} + изменение к пред. периоду."""
    out = {}
    for reg, per in d.items():
        ps = sorted(per)
        if not ps:
            continue
        last = ps[-1]
        prev = ps[-2] if len(ps) >= 2 else None
        out[reg] = (per[last], prev and per.get(prev), last, prev)
    return out


def fmt(v, nd=1):
    return f'{v:,.{nd}f}'.replace(',', ' ') if v is not None else '—'


KEY_TO_METRIC = {
    'A_cpi': 'emiss_31074_cpi_prevm_m', 'B_wage': 'emiss_57824_wage_m',
    'B_unemp': 'emiss_43062_unemp_q', 'C_kf': 'zkf', 'C_kyl': 'zyi',
    'C_hdebt_long': 'vhdt', 'C_mdebt_ihk': 'vmd',
    'C_hnew_long': 'vhlvt', 'C_mnew_ihk': 'oipflrrivrsrf',
    'C_hrate_long': 'vhrr', 'C_irate_ihk': 'spsipflrrtmrsrf',
    'E_housing': 'rosstat_housing_total_m', 'E_izhs': 'rosstat_housing_pop_m',
    'F_snz': 'snz'}


def block_section(mc, data):
    name, blk, freq = NOMEN[mc]
    d = data.get(KEY_TO_METRIC.get(mc, mc), {})
    if not d:
        return f'## {blk}. {name}\n\nНет данных.\n'
    s = series(d)
    vals = [v for v, p, l, pv in s.values() if v is not None]
    med = statistics.median(vals)
    mean = statistics.mean(vals)
    # лидеры/аутсайдеры по уровню
    ranked = sorted(s.items(), key=lambda kv: (kv[1][0] is None, kv[1][0]), reverse=True)
    top3 = [f'{reg} ({fmt(v)})' for reg, (v, p, l, pv) in ranked[:3] if v is not None]
    bot3 = [f'{reg} ({fmt(v)})' for reg, (v, p, l, pv) in ranked[-3:] if v is not None]
    # динамика
    dyn = []
    for reg, (v, p, l, pv) in ranked:
        if v is not None and p is not None:
            try:
                chg = (v / p - 1) * 100 if p != 0 else None
                if chg is not None:
                    dyn.append((reg, chg, v))
            except ZeroDivisionError:
                pass
    dyn.sort(key=lambda x: x[1], reverse=True)
    up = ', '.join(f'{reg} ({chg:+.1f}%)' for reg, chg, v in dyn[:3])
    dn = ', '.join(f'{reg} ({chg:+.1f}%)' for reg, chg, _ in dyn[-3:])
    # топ-15 по уровню
    top15 = ranked[:15]
    lines = [f'## {blk}. {name} (частота: {freq}, период: {ranked[0][1][2] if ranked else "—"})',
             '',
             f'**Общероссийский тренд**: медиана {fmt(med)}, среднее {fmt(mean)} по {len(vals)} субъектам.',
             '',
             f'**Топ-15 по уровню**:']
    for reg, (v, p, l, pv) in top15:
        chg = ''
        if v is not None and p is not None and p != 0:
            try:
                chg = f' ({(v/p-1)*100:+.1f}% к пред.)'
            except ZeroDivisionError:
                chg = ''
        lines.append(f'- {reg}: {fmt(v)}{chg}')
    lines += ['',
              f'**Лидеры роста** (к пред. периоду): {up or "—"}',
              f'**Аутсайдеры** (к пред. периоду): {dn or "—"}',
              '',
              '_Малые регионы: для устойчивости использовать сглаживание 3 мес (уровень = среднее за 3 последних периода). Пометка: независимый расчёт, не связан с Банком России._',
              '']
    return '\n'.join(lines)


def main():
    data = load()
    header = ['# Регионы против общероссийского тренда — шаблон доклада ГУ',
              '',
              'Дата отсечения данных: 2026-09-25 (срез v1, region_slice_full_202610.csv).',
              'Формат: медиана/среднее по субъектам как «тренд», топ-15, лидеры/аутсайдеры,',
              'сглаживание 3 мес для малых регионов. Пометка независимости обязательна.',
              '']
    body = '\n'.join(block_section(k, data) for k in NOMEN)
    with open(OUT, 'w') as f:
        f.write('\n'.join(header) + '\n' + body)
    print('written', OUT)
    # краткая сводка
    for mc in NOMEN:
        d = data.get(mc, {})
        if d:
            print(f'{mc}: {len(d)} регионов')


if __name__ == '__main__':
    main()