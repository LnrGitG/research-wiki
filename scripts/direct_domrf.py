#!/usr/bin/env python3
"""Прямой загрузчик ДОМ.РФ: сырьё raw/domrf/price_index/*.csv → канон.

Заменяет две прежние дороги одной: (1) инжест рубежа 6 из SQLite-лендинга
`domrf_price_index` (метрики itzdr/itzdrpm/csdr), (2) разовый перенос
`transfer_domrf_price.py` из v2-CSV. Обе несли один и тот же ряд, поэтому
в каноне он лежал дважды: под именами рубежа 6 и под именами переноса
(domrf_price_index_m / domrf_price_index_mom / ddu_count_m, 5 100 строк каждая).
Оставляем именованный набор переноса — на него ссылаются скрипты гипотез
(h034_price_cost_gap.py) и витрина метрик.

Ключевые отличия от прежних дорог:

1. Частота. У карточек рубежа 6 стояла квартальная частота (frequency_id 6)
   при месячных данных; здесь частота M.
2. Ключ итерации. Перенос делал одну вставку на прогон без снятия прежних
   строк; здесь перед вставкой снимаются строки пары «метрика — релиз»
   (в ux_observation входит sub_dimension, NULL-ы Postgres считает
   различными — при пустом подразрезе уникальность не работает).
3. Регионы. Алиасы ДОМ.РФ («город Москва» → «Москва», «Ямало-Ненецкий АО» →
   «Ямало-Ненецкий автономный округ» и др.) переносятся в meta.region_alias,
   то есть становятся общими для всех загрузчиков, а не живут в одном скрипте.

Запуск:
    python3 scripts/direct_domrf.py                  # сухой прогон
    APPLY=1 python3 scripts/direct_domrf.py          # запись
    APPLY=1 REPLACE=1 python3 scripts/direct_domrf.py  # со снятием прежних наборов

Точка возврата: attic/domrf_before_*.csv.gz (снимается в режиме REPLACE).
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(REPO, 'raw', 'domrf', 'price_index',
                        'domrf_priceindex_all_regions.csv')
APPLY = os.environ.get('APPLY') == '1'
REPLACE = os.environ.get('REPLACE') == '1'
SOURCE = 'domrf'
RELEASE = 'domrf_priceindex_api'
SUB = 'источник: ДОМ.РФ API priceindex/living'

# Оставляемый набор имён (совпадает с карточками переноса, коды
# domrf_price_index_m / _mom / ddu_count_m).
METRICS = [
    ('index_value', 'ДОМ.РФ: индекс цен на новостройки, первичный рынок (уровень 2021-01=100)'),
    ('mom_pct', 'ДОМ.РФ: индекс цен на новостройки, м/м, %'),
    ('n_deals', 'ДОМ.РФ: число ДДУ (n_deals), шт, за месяц'),
]

# Набор имён рубежа 6 — снимается вместе со строками (дубль того же ряда).
LEGACY = [
    'Индекс цен на жильё ДОМ.РФ',
    'Индекс цен на жильё ДОМ.РФ, % к предыдущему месяцу',
    'Число сделок, ДОМ.РФ',
]

# Алиасы ДОМ.РФ → канонические имена регионов. Регистрируются в
# meta.region_alias, чтобы работать во всех загрузчиках.
ALIAS = {
    'архангельская область': 'архангельская область (без нао)',
    'город москва': 'москва',
    'город санкт-петербург': 'санкт-петербург',
    'кемеровская область - кузбасс': 'кемеровская область — кузбасс',
    'республика северная осетия': 'республика северная осетия — алания',
    'тюменская область': 'тюменская область (без хмао и янао)',
    'ханты-мансийский ао - югра': 'ханты-мансийский автономный округ — югра',
    'ямало-ненецкий ао': 'ямало-ненецкий автономный округ',
}


def register_aliases(w):
    """Алиасы ДОМ.РФ → meta.region_alias (идемпотентно)."""
    added = 0
    for alias, target in ALIAS.items():
        rid = w.reg.get(norm(target))
        if not rid:
            print('   ПРЕДУПРЕЖДЕНИЕ: не найден регион-цель %r' % target)
            continue
        if norm(alias) in w.reg:
            continue
        if not w.simulate:
            w.cur.execute("""INSERT INTO meta.region_alias (alias, region_id)
                VALUES (%s, %s) ON CONFLICT (alias) DO NOTHING""", (alias, rid))
            w.conn.commit()
        w.reg[norm(alias)] = rid
        added += 1
    return added


def read_rows(w):
    """CSV ДОМ.РФ → список записей для ядра."""
    if not os.path.exists(CSV_PATH):
        raise SystemExit('нет CSV ДОМ.РФ: %s — сначала domrf_fetch_monthly.py' % CSV_PATH)
    rows, stats = [], {'matched': 0, 'unmatched': {}, 'rf': 0}
    with open(CSV_PATH, newline='', encoding='utf-8') as fh:
        for rec in csv.DictReader(fh):
            reg = (rec.get('region') or '').strip()
            month = (rec.get('month') or '').strip()[:10]
            rid = w.reg.get(norm(reg))
            if rid:
                stats['matched'] += 1
            elif norm(reg) in ('российская федерация', 'россия'):
                rid = w.RU
                stats['rf'] += 1
            else:
                stats['unmatched'][reg] = stats['unmatched'].get(reg, 0) + 1
                continue
            y, m = month.split('-')[0], month.split('-')[1]
            for col, name in METRICS:
                v = rec.get(col)
                if v in (None, '', 'nan'):
                    continue
                rows.append(dict(metric_name=name, value=float(v), ps=(int(y), int(m)),
                                 region=rid, freq='M', source=SOURCE,
                                 release=RELEASE, sub=SUB, unit='unknown'))
    stats['months'] = len({r['ps'] for r in rows})
    stats['regions'] = len({r['region'] for r in rows})
    return rows, stats


def main():
    w = Writer(tag='direct_domrf', simulate=not APPLY)
    print('== алиасы ДОМ.РФ → meta.region_alias: добавлено %d' % register_aliases(w))
    rows, stats = read_rows(w)
    print('== domrf_price_index: строк %d | регионов %d | месяцев %d | сопоставлено %d'
          % (len(rows), stats['regions'], stats['months'], stats['matched']))
    if stats['unmatched']:
        print('   НЕ сопоставлены: %s' % list(stats['unmatched'])[:10])
    if not APPLY:
        print('   СУХОЙ ПРОГОН (APPLY=1 — запись)')
        w.close()
        return
    if REPLACE:
        kept = [n for _, n in METRICS]
        for names, label in ((LEGACY, 'domrf_legacy'), (kept, 'domrf_kept')):
            dump = os.path.join(REPO, 'attic', 'domrf_before_%s.csv.gz' % label)
            n = w.dump_group(names, dump)
            print('   снято прежних строк (%s): %d → %s' % (label, n, dump))
    prep, ins, conf, newm = w.ingest(rows, group='domrf_price_index')
    print('   подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, newm))
    # карточки рубежа 6 остаются без строк — помечаем, чтобы не искать их заново
    w.cur.execute("""UPDATE core.metric SET status='deprecated'
        WHERE name_ru = ANY(%s) AND status <> 'deprecated'""", (LEGACY,))
    print('   помечено deprecated: %d (карточки рубежа 6 без строк)'
          % w.cur.rowcount)
    w.conn.commit()
    w.close()


if __name__ == '__main__':
    main()
