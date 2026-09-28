#!/usr/bin/env python3
"""Шаблон доклада ГУ: топ-15 регионов против общероссийского тренда (v2 — устойчивые динамики).

Формат (утверждён владельцем): по каждой метрике среза —
- общероссийский тренд (медиана/среднее по субъектам, а не только РФ-агрегат);
- топ-15 регионов по уровню;
- лидеры и аутсайдеры;
- малые регионы — сглаживание 3 мес.

Явные предпосылки v2 (ревью аномалий первого прогона, этап I цикла СД 23.10):
1. Динамика считается только по 3-месячным окнам (сумма для потоков,
   среднее для уровней, запасов и ставок), а не сырым м/м: одиночный
   месяц в малом регионе шумит.
2. Для потоков, запасов и уровней (ввод жилья, выдачи, задолженность, ЗП)
   окно сравнивается с ОДНОИМЁННЫМ окном годом ранее (г/г) — это главный
   фильтр аномалий первого прогона: сравнение с предыдущим окном внутри
   года ловит сезонность стройки и объявляло аномалиями половину регионов.
   Если года истории в срезе нет (ряды ЦБ по ИЖК с 07.2025), используется
   предыдущее окно, и это явно помечено в отчёте как неочищенное от сезонности.
3. Для ставок и норм (безработица, ипотечные ставки) динамика подаётся
   в п.п. (уровень, не темп): процентный рост от ставки — бессмысленная
   величина, именно она давала «Свердловская безработица +80 % м/м»
   и «ставки ИЖК +99,5 %» по малым регионам.
4. Фильтр малых знаменателей: относительная динамика не публикуется,
   если база окна ниже 5 % медианы баз по субъектам (SMALL_SHARE).
   Для ставок по ИЖК порог строится не на самой ставке, а на объёме выдачи
   (10-й процентиль за 3 месяца, SMALL_VOL_PCT): малая выборка сделок
   определяет средневзвешенную ставку в регионе, а не экономика региона.
5. Флаг аномалии: |динамика| выше порога по виду ряда (60 % поток,
   40 % запас, 30 % уровень, 2 п.п. ставка) помечается ⚠ и исключается
   из лидеров/аутсайдеров; полный перечень — в
   data/gu_report_template_202610_flags.csv.

Выход: data/gu_report_template_202610.md — скелет раздела «регионы против
тренда» для доклада начальника ГУ.

Пометка независимости обязательна на каждой публикации цикла.
"""
import csv
import os
import statistics
from collections import defaultdict

SLICE = os.path.expanduser('~/research-wiki-private/data/region_slice_full_202610.csv')
OUT = os.path.expanduser('~/research-wiki-private/data/gu_report_template_202610.md')
FLAGS = os.path.expanduser('~/research-wiki-private/data/gu_report_template_202610_flags.csv')

SMALL_SHARE = 0.05    # база < 5 % медианы баз по субъектам → малый знаменатель (уровневые ряды)
SMALL_VOL_PCT = 0.10  # ставки: объём выдачи ниже 10-го процентиля → «малая выборка»
OUTLIER = {'flow': 60.0, 'stock': 40.0, 'level': 30.0}  # % для уровневых видов
OUTLIER_RATE = 2.0    # п.п. для ставок и норм

# ставка → ряд объёма, по которому определяется «малая выборка» (правило ревью
# аномалий от 28.09: средневзвешенная ставка в регионах с малым числом выдач
# определяется несколькими сделками и прыгает от месяца к месяцу)
VOLUME_PROXY = {'C_hrate_long': 'C_hnew_long', 'C_irate_ihk': 'C_mnew_ihk'}

TAG = '_Независимый расчёт, не связан с Банком России._'

# метрика → (название, блок, частота, вид ряда)
# вид: index (% к пред. мес.), rate (ставка, %), rate_q (квартальная норма, %),
#      level (уровень, руб.), stock (запас, млн руб.), flow (поток)
NOMEN = {
    'A_cpi': ('ИПЦ, % к пред. месяцу', 'A', 'мес', 'index'),
    'B_wage': ('Номинальная ЗП, руб.', 'B', 'мес', 'level'),
    'B_unemp': ('Безработица МОТ 15+, %', 'B', 'кв', 'rate_q'),
    'C_kf': ('Кредиты физлицам (потр. и ипотека), задолженность', 'C', 'мес', 'stock'),
    'C_kyl': ('Кредиты юрлицам и ИП, задолженность', 'C', 'мес', 'stock'),
    'C_hdebt_long': ('Жилищные кредиты, задолженность (VFS, с 2019)', 'C', 'мес', 'stock'),
    'C_mdebt_ihk': ('ИЖК, задолженность (ЦБ, с 07.2025)', 'C', 'мес', 'stock'),
    'C_hnew_long': ('Выдачи жилищных кредитов (VFS, с 2019)', 'C', 'мес', 'flow'),
    'C_mnew_ihk': ('Объём ИЖК (ЦБ, Т_19)', 'C', 'мес', 'flow'),
    'C_hrate_long': ('Ставка по жилищным кредитам (VFS)', 'C', 'мес', 'rate'),
    'C_irate_ihk': ('Ставка по ИЖК (ЦБ, Т_26)', 'C', 'мес', 'rate'),
    'E_housing': ('Ввод жилья, тыс. кв. м', 'E', 'мес', 'flow'),
    'E_izhs': ('Ввод ИЖС, тыс. кв. м', 'E', 'мес', 'flow'),
    'F_snz': ('Средняя ЗП, руб.', 'F', 'мес', 'level'),
}

KEY_TO_METRIC = {
    'A_cpi': 'emiss_31074_cpi_prevm_m', 'B_wage': 'emiss_57824_wage_m',
    'B_unemp': 'emiss_43062_unemp_q', 'C_kf': 'zkf', 'C_kyl': 'zyi',
    'C_hdebt_long': 'vhdt', 'C_mdebt_ihk': 'vmd',
    'C_hnew_long': 'vhlvt', 'C_mnew_ihk': 'oipflrrivrsrf',
    'C_hrate_long': 'vhrr', 'C_irate_ihk': 'spsipflrrtmrsrf',
    'E_housing': 'rosstat_housing_total_m', 'E_izhs': 'rosstat_housing_pop_m',
    'F_snz': 'snz'}

FLOWISH = ('flow', 'stock', 'level')

# контрольные пары аномалий первого прогона (для отчётной проверки)
ANOMALY_PAIRS = [
    ('B_unemp', 'Свердловская область'),
    ('C_kyl', 'Тамбовская область'),
    ('C_irate_ihk', 'Чукотский автономный округ'),
    ('C_hrate_long', 'Москва'),
    ('E_housing', 'Амурская область'),
]


DEFN_FLAGS = defaultdict(lambda: defaultdict(dict))


def load():
    data = defaultdict(lambda: defaultdict(dict))
    with open(SLICE) as f:
        for r in csv.DictReader(f):
            mc, reg, ps, v = (r['block_metric'].strip(), r['region'].strip(),
                              r['period'].strip(), r['value'].strip())
            try:
                data[mc][reg][ps] = float(v)
            except ValueError:
                continue
            flag = (r.get('quality_flag') or '').strip()
            if flag:
                DEFN_FLAGS[mc][reg][ps] = flag
    return data


def definition_notes():
    """Пометки определения ряда: точка с пометкой публикуется только с нею."""
    if not DEFN_FLAGS:
        return []
    name_by_code = {v: NOMEN[k][0] for k, v in KEY_TO_METRIC.items()}
    out = ['## Пометки определения ряда', '']
    for mc, regs in DEFN_FLAGS.items():
        name = name_by_code.get(mc, mc)
        n = sum(len(v) for v in regs.values())
        flags = sorted({f for v in regs.values() for f in v.values()})
        periods = sorted({p for v in regs.values() for p in v})
        out.append(f'- **{name}**: точек с пометкой {n} ({periods[0]} … {periods[-1]}), '
                   f'пометки: {", ".join(flags)}.')
    out += ['', 'Правило: `old_definition_15_72` — значение получено по прежнему '
            'определению показателя (безработица в возрасте 15-72 лет, до 2017 года). '
            'Текущее определение — «15 лет и старше», с 2017 года. В исследованиях и '
            'прогнозах старый отрезок допустим, но только с этой пометкой; как '
            'непрерывный ряд метрика до 2017 и после читаться не должна.', '']
    return out


def fmt(v, nd=1):
    return f'{v:,.{nd}f}'.replace(',', ' ') if v is not None else '—'


def measure(vals, ps, kind, freq):
    """Устойчивые уровень и динамика. Возвращает (уровень, база, динамика, единица, окно)."""
    n = len(vals)
    idx = {p: i for i, p in enumerate(ps)}
    if kind in FLOWISH:
        w = 3 if n >= 3 else n
        cur_p = ps[-w:]
        yoy_p = [f'{int(p[:4]) - 1}{p[4:]}' for p in cur_p]
        if all(q in idx for q in yoy_p):
            cur, base = [vals[idx[p]] for p in cur_p], [vals[idx[q]] for q in yoy_p]
            win = f'г/г, {w} мес'
        else:
            base_p = ps[-2 * w:-w] if n >= 2 * w else []
            if not base_p:
                return vals[-1], None, None, None, 'нет базы'
            cur, base = vals[-w:], [vals[idx[p]] for p in base_p]
            win = f'к пред. окну, {w} мес (не очищено от сезонности)'
        level = vals[-1]
        c = sum(cur) if kind == 'flow' else statistics.mean(cur)
        b = sum(base) if kind == 'flow' else statistics.mean(base)
        return level, b, ((c / b - 1) * 100 if b else None), '%', win
    w = 3 if n >= 6 else 1
    if n < 2 * w:
        return vals[-1], None, None, None, 'нет базы'
    cur, base = vals[-w:], vals[-2 * w:-w]
    level, bl = statistics.mean(cur), statistics.mean(base)
    unit_p = 'кв' if kind == 'rate_q' else 'мес'
    return level, bl, level - bl, 'п.п.', f'{w} {unit_p} к пред. {w} {unit_p}'


def volume_index(data, key):
    """Регион → сумма объёма за последние 3 периода (для порога «малой выборки»)."""
    out = {}
    for reg, per in data.get(key, {}).items():
        ps = sorted(per)
        out[reg] = sum(per[p] for p in ps[-3:])
    return out


def pctl(values, share):
    """Простой процентиль по отсортированному ряду (без интерполяции)."""
    if not values:
        return 0.0
    vals = sorted(values)
    i = max(0, min(len(vals) - 1, int(round(share * len(vals))) - 1))
    return vals[i]


def block_section(mc, data, flags):
    name, blk, freq, kind = NOMEN[mc]
    d = data.get(KEY_TO_METRIC.get(mc, mc), {})
    if not d:
        return f'## {blk}. {name}\n\nНет данных.\n'
    vol = volume_index(data, KEY_TO_METRIC.get(mc, mc))
    if kind in ('rate', 'rate_q') and mc in VOLUME_PROXY:
        vk = VOLUME_PROXY[mc]
        vol = volume_index(data, KEY_TO_METRIC.get(vk, vk))
    vol_floor = pctl(list(vol.values()), SMALL_VOL_PCT) if vol else 0.0
    rows = []
    for reg, per in d.items():
        ps = sorted(per)
        vals = [per[p] for p in ps]
        level, base, dyn, unit, win = measure(vals, ps, kind, freq)
        rows.append({'reg': reg, 'level': level, 'base': base, 'dyn': dyn,
                     'unit': unit, 'win': win, 'last': ps[-1] if ps else None,
                     'n': len(vals), 'seasonal': 'не очищено' in win,
                     'vol': vol.get(reg)})
    bases = [abs(r['base']) for r in rows if r['base']]
    med_base = statistics.median(bases) if bases else 0.0
    floor = SMALL_SHARE * med_base
    levels = [r['level'] for r in rows if r['level'] is not None]
    med_lvl = statistics.median(levels) if levels else 0.0
    mean_lvl = statistics.mean(levels) if levels else 0.0
    limit = OUTLIER_RATE if kind in ('rate', 'rate_q', 'index') else OUTLIER[kind]
    for r in rows:
        if kind in ('rate', 'rate_q') and mc in VOLUME_PROXY:
            r['small'] = bool(r['vol'] is not None and vol_floor > 0
                              and r['vol'] < vol_floor)
        elif kind in ('rate', 'rate_q', 'index'):
            r['small'] = False
        else:
            r['small'] = bool(r['base'] is not None and floor > 0
                              and abs(r['base']) < floor)
        r['outlier'] = bool(r['dyn'] is not None and abs(r['dyn']) >= limit
                            and not r['small'])
        if r['small']:
            flags.append((mc, name, r['reg'], 'малая выборка' if kind in ('rate', 'rate_q')
                          and mc in VOLUME_PROXY else 'малый знаменатель',
                          r['vol'] if mc in VOLUME_PROXY else r['base'],
                          r['dyn'], r['last'], r['win']))
        elif r['outlier']:
            flags.append((mc, name, r['reg'], 'аномалия динамики', r['base'],
                          r['dyn'], r['last'], r['win']))

    usable = [r for r in rows if r['dyn'] is not None
              and not r['small'] and not r['outlier']]
    usable.sort(key=lambda r: r['dyn'], reverse=True)
    ranked = sorted([r for r in rows if r['level'] is not None],
                    key=lambda r: r['level'], reverse=True)
    up = ', '.join(f"{r['reg']} ({r['dyn']:+.1f} {r['unit']})" for r in usable[:3])
    dn = ', '.join(f"{r['reg']} ({r['dyn']:+.1f} {r['unit']})"
                   for r in usable[-3:]) if usable else '—'
    period = ranked[0]['last'] if ranked else '—'
    win_note = usable[0]['win'] if usable else '—'
    lines = [f'## {blk}. {name} (частота: {freq}, период: {period}, вид ряда: {kind})', '',
             f'**Общероссийский тренд**: медиана уровня {fmt(med_lvl)}, '
             f'среднее {fmt(mean_lvl)} по {len(levels)} субъектам.', '',
             '**Топ-15 по уровню** (уровень — последнее значение; в скобках '
             f'устойчивая динамика, окно: {win_note}):']
    for r in ranked[:15]:
        dyn = f" ({r['dyn']:+.1f} {r['unit']})" if r['dyn'] is not None else ''
        mark = ' ⚠' if r['outlier'] else (' ※' if r['small'] else '')
        lines.append(f"- {r['reg']}: {fmt(r['level'])}{dyn}{mark}")
    if kind in ('rate', 'rate_q') and mc in VOLUME_PROXY:
        drop_note = (f'малая выборка (объём выдачи за 3 мес ниже 10-го процентиля '
                     f'{fmt(vol_floor, 0)})')
    elif kind in ('rate', 'rate_q', 'index'):
        drop_note = 'отсев по малым знаменателям не применяется (вид ряда — норма или индекс)'
    else:
        drop_note = (f'малый знаменатель (база ниже 5 % медианы {fmt(med_base, 0)})')
    lines += ['',
              f'**Лидеры роста** (устойчивая динамика, {win_note}, без отсева): {up or "—"}',
              f'**Аутсайдеры** (устойчивая динамика, {win_note}, без отсева): {dn or "—"}',
              '',
              f'_Отсев по метрике: {drop_note} — {sum(1 for r in rows if r["small"])} '
              f'субъектов (※), флаг аномалии (⚠) — {sum(1 for r in rows if r["outlier"])}. '
              f'Сглаживание 3 мес применено ко всем регионам (потоки — сумма, '
              f'уровни и ставки — среднее). {TAG}_', '']
    return '\n'.join(lines)


def anomaly_check(data):
    """Проверка поименованных аномалий первого прогона: сырой м/м против устойчивой динамики."""
    out = ['## Проверка аномалий первого прогона (ревизия 28.09.2026)', '',
           'Сырой м/м прошлого формата против устойчивой динамики v2. Первый прогон дал '
           '«Свердловская безработица +80 % м/м», «Тамбов кредиты юрлиц +5719 % м/м», '
           '«ставки ИЖК малых регионов +99,5 %» и массовые «аномалии» по вводу жилья; '
           'ниже — что из этого воспроизводится на срезе от 28.09.2026:', '']
    for mc, reg in ANOMALY_PAIRS:
        name, blk, freq, kind = NOMEN[mc]
        d = data.get(KEY_TO_METRIC.get(mc, mc), {}).get(reg, {})
        if not d:
            out.append(f'- {name} / {reg}: нет в срезе ({blk}).')
            continue
        ps = sorted(d)
        vals = [d[p] for p in ps]
        level, base, dyn, unit, win = measure(vals, ps, kind, freq)
        raw = (vals[-1] / vals[-2] - 1) * 100 if len(vals) >= 2 and vals[-2] else None
        raw_s = f'{raw:+.1f} %' if raw is not None else 'н/д'
        dyn_s = f'{dyn:+.2f} {unit} ({win})' if dyn is not None else 'н/д'
        out.append(f'- {name} / {reg}: последние точки {[round(v, 2) for v in vals[-3:]]}; '
                   f'сырой м/м {raw_s}; устойчивая динамика {dyn_s}.')
    out += ['',
            'Правило чтения: для ставок и норм (безработица, ипотечные ставки) темп в '
            'процентах не публикуется вовсе — только п.п., потому что процентный рост от '
            'ставки 5,7 до 11,0 % не является содержательной величиной. Ставки по ИЖК '
            'дополнительно фильтруются по объёму выдачи (10-й процентиль за 3 месяца): '
            'в регионах ниже порога средневзвешенная ставка определяется несколькими '
            'сделками и сравнения со средним по стране не выдерживает.', '',
            'Открытые вопросы к факт-блоку (ревью аномалий 28.09, '
            'queries/region-slice-anomaly-review-202610.md):', '',
            '1. Значение Свердловской области за 2026-Q2 (2,7 % против коридора 1,3–1,7 '
            'в предыдущих восьми кварталах) сверено с публикацией: ЕМИСС 43062 отдаёт '
            'тот же ряд, это не дефект загрузки. Оговорка не про 2026 год, а про 2017-й: '
            'там меняется определение показателя (см. раздел «Пометки определения ряда»).',
            '2. Разброс метрики безработицы 0,9–22,6 при медиане 1,9 объясняется '
            'структурой показателя: в метрике соседствуют две возрастные градации с '
            'разным охватом лет («15 лет и старше» с 2017 года, «15-72 лет» до 2017). '
            'До 2017 года точки помечены флагом old_definition_15_72 и как непрерывный '
            'ряд с последующими читаться не должны.', '',
            TAG, '']
    return '\n'.join(out)


def main():
    data = load()
    flags = []
    header = ['# Регионы против общероссийского тренда — шаблон доклада ГУ', '',
              'Дата отсечения данных: 2026-09-28 (срез region_slice_full_202610.csv, '
              'глубина 13 мес).',
              'Формат: медиана/среднее по субъектам как «тренд», топ-15 по уровню, '
              'лидеры/аутсайдеры по устойчивой динамике (г/г по 3-месячным окнам, '
              'для ставок — п.п.), отсев малых знаменателей и аномалий.', TAG, '']
    body = '\n'.join(block_section(k, data, flags) for k in NOMEN)
    tail = anomaly_check(data) + '\n' + '\n'.join(definition_notes())
    with open(OUT, 'w') as f:
        f.write('\n'.join(header) + '\n' + body + '\n' + tail)
    with open(FLAGS, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['metric', 'name', 'region', 'reason', 'base_window', 'dynamics',
                    'period', 'window'])
        for row in flags:
            w.writerow(row)
    print('written', OUT)
    print('written', FLAGS, 'flags:', len(flags))
    for mc in NOMEN:
        d = data.get(KEY_TO_METRIC.get(mc, mc), {})
        if d:
            print(f'{mc}: {len(d)} регионов')


if __name__ == '__main__':
    main()