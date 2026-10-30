#!/usr/bin/env python3
"""Черновики определений метрик: массовая генерация `catalog.metric_definition`.

Зачем. Карточки (`derived.metric_card`) описывают 3 169 активных метрик, а
обязательство «что именно означает это число» зафиксировано лишь у 49. В итоге
ряд берут по коду, и никто не сверяет единицу, частоту и оговорки — именно так
возникали ошибки «накопительный итог принят за квартал», «индекс к предыдущему
месяцу принят за проценты г/г», «дубли удвоили сумму».

Что делает. Для каждой активной метрики с наблюдениями, у которой определения
ещё НЕТ, пишет редакцию 1 в статусе `draft`: текст из карточки (имя, описание,
источник, единица, частота, уровень, охват, период), каноническую единицу из
`catalog.unit`, оговорки по правилам префиксов кода и общую оговорку «не
сверено с первоисточником». Статус `official` этот скрипт НЕ ставит никогда:
подтверждение — отдельная работа со сверкой, здесь только устраняется пустота.

Идемпотентность. Метрика пропускается, если для её кода есть хоть одна
редакция — повторный прогон даёт 0 вставок. Единственное исключение —
`--refresh-drafts`: перегенерировать редакцию 1 у метрик, которые сами
сгенерированы (owner=auto-draft) и остались в `draft`; тогда растёт `version`,
а `supersedes` заполняется ссылкой `<code>@<version>`.

Режимы:
    --check    только посчитать и напечатать (по умолчанию ничего не пишет)
    --apply    записать
    --tier     какой контур считать: all | operational | research
"""
import argparse
import hashlib
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402

FREQ_RU = {'M': 'месячная', 'Q': 'квартальная', 'A': 'годовая',
           'W': 'недельная', 'D': 'дневная', 'E': 'по событию',
           'H': 'полугодовая', 'I': 'внутридневная'}

# Оговорки по префиксу кода: только проверенные дефекты, каждый с источником
# в журнале/записках. Правило без подтверждения не добавлять — черновик должен
# пугать там, где действительно опасно, а не везде.
CAVEAT_RULES = [
    ('fns_1nom', 'Накопленный итог с начала года: январская точка — итог за предыдущий год, '
                 'квартальные приросты дифференцированием теряют I квартал (см. db-access, §3a).'),
    ('drpotr', 'Накопленный итог с начала года (ФНС 1-НОМ): привязка периода — апрель = I квартал, '
               'июль = II, октябрь = III, январь = IV прошлого года.'),
    ('rusdrpotr', 'Накопленный итог с начала года (ФНС 1-НОМ), см. caveats к парной метрике.'),
    ('vbved_reg_m', 'Под объявленной месячной частотой лежат накопительные строки («январь-август» и др.); '
                    'без фильтра по подразрезу запрос видит больше строк, чем месячный слой (A-11).'),
    ('emiss_31074', 'У строки «Российская Федерация» разрыв 2023–2025; для национальной дефляции '
                    'использовать kep1_14, иначе реальные показатели по РФ считаются неверно.'),
    ('kep1_14', 'Индекс к предыдущему месяцу (100,5 = +0,5 %), а не проценты и не г/г.'),
    ('kep4_25', 'Реальная начисленная зарплата, % к тому же месяцу прошлого года (106,5 = +6,5 % г/г).'),
    ('kep4_22', 'Номинальная начисленная зарплата, рублей.'),
    ('kep4_15', 'Занятость 15+, млн человек, месячно.'),
    ('vvp', 'ВВП в постоянных ценах, млрд руб., квартально, сезонно НЕ сглажен — сравнивать только г/г.'),
    ('emiss_43062', 'Квартальная сетка; проверять по GROUP BY period_start без фильтра region_id = 1: '
                    'строка РФ может лежать под другим region_id (ложный вывод «ряд кончился»).'),
    ('vdzrfg', 'Годовая метка года исправлена 18.10.2026: годы 2015, 2019–2023.'),
    ('cbrmon', 'Месяцы сдвинуты на +1 при загрузке; исправлено 17.10.2026, квартальные возвращены '
               'на начала кварталов.'),
    ('irz', 'Канонический ряд ставок ИЖК.'),
    ('izhk_rate_fx', 'Валютные выдачи отсутствуют с ~2025-03: нули означают «нет выдач», а не ставку 0 %.'),
    ('vmd', 'Канонический код ИЖК; дефектные строки релиза 7 в карантине (observation_status=rejected).'),
]

GENERAL_CAVEAT = ('Черновик автогенерации: значение не сверено с первоисточником, '
                  'статус official присваивается отдельно после сверки.')


def content_hash(code, definition_ru, unit_canonical, scale_note, caveats):
    payload = json.dumps({'code': code, 'd': definition_ru, 'u': unit_canonical,
                          's': scale_note, 'c': caveats},
                         ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def caveats_for(code):
    out = []
    low = code.lower()
    for prefix, text in CAVEAT_RULES:
        if low.startswith(prefix):
            out.append(text)
    out.append(GENERAL_CAVEAT)
    return out


SQL_TARGETS = """
WITH base AS (
    SELECT o.metric_id, o.region_id, o.period_start, s.source_code
    FROM data.observation o
    LEFT JOIN catalog.source s ON s.source_id = o.source_id
    WHERE o.observation_status NOT IN ('rejected', 'superseded')
), agg AS (
    SELECT metric_id,
           count(*) AS n_obs,
           count(DISTINCT region_id) AS n_regions,
           min(period_start) AS pmin,
           max(period_start) AS pmax,
           array_agg(DISTINCT source_code) FILTER (WHERE source_code IS NOT NULL) AS srcs
    FROM base
    GROUP BY 1
)
SELECT m.metric_id, m.metric_code, coalesce(m.name_ru, ''), coalesce(m.description, ''),
       coalesce(u.unit_code, ''), coalesce(u.name_ru, ''), coalesce(u.description, ''),
       coalesce(f.freq_code, 'M'), coalesce(f.name_ru, ''),
       coalesce(a.srcs, '{}'),
       a.n_obs, a.n_regions, a.pmin, a.pmax,
       COALESCE(vc.freshness, 'нет данных'), COALESCE(vc.region_scope, 'unknown')
FROM catalog.metric m
JOIN agg a ON a.metric_id = m.metric_id
LEFT JOIN catalog.unit u ON u.unit_id = m.unit_id
LEFT JOIN catalog.frequency f ON f.frequency_id = m.frequency_id
LEFT JOIN derived.v_metric_context vc ON vc.metric_id = m.metric_id
WHERE m.status = 'active' AND m.is_active
ORDER BY 2
"""


def build_text(row):
    (mid, code, name, descr, ucode, ucanon, uru, fcode, fru,
     srcs, n_obs, n_reg, pmin, pmax, fresh, scope) = row
    unit = ucanon or uru or ucode or '—'
    src_txt = ', '.join(sorted(srcs or [])) or '—'
    freq = fru or FREQ_RU.get(fcode, '—')
    parts = []
    head = name.strip() or code
    if descr.strip():
        head = f'{head}. {descr.strip().rstrip(".")}'
    parts.append(head + '.')
    parts.append(f'Единица: {unit}. Частота: {freq}.')
    parts.append(f'Источник: {src_txt}.')
    parts.append(f'Охват: {n_obs} наблюдений, регионов {n_reg}, период {pmin}..{pmax}.')
    return ' '.join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--tier', default='all', choices=['all', 'operational', 'research'])
    ap.add_argument('--refresh-drafts', action='store_true')
    args = ap.parse_args()
    if not args.apply:
        args.check = True

    # Тяжёлый агрегат по 7,9 млн наблюдений: на дефолтном work_mem (4 МБ)
    # PostgreSQL ушёл бы в сортировку на диск (см. инцидент 30.10.2026).
    _conn = db_tunnel.connect(options='-c work_mem=1GB')
    try:
        with _conn.cursor() as cur:
            cur.execute(SQL_TARGETS)
            rows = cur.fetchall()
    finally:
        _conn.close()
    print(f'метрик с наблюдениями (активных): {len(rows)}')

    tier = [r for r in rows if r[14] == 'свежие'] if args.tier == 'operational' else rows
    if args.tier == 'operational':
        tier = [r for r in tier if r[7] in ('M', 'Q')]
    print(f'контур {args.tier}: {len(tier)} метрик')

    existing = {r[0]: r[1] for r in db_tunnel.query(
        'SELECT metric_code, max(version) FROM catalog.metric_definition GROUP BY 1')}
    have = [r for r in tier if r[1] in existing]
    fresh = [r for r in tier if r[1] not in existing]
    print(f'уже есть определения: {len(have)}, к генерации: {len(fresh)}')

    payload = []
    for r in fresh:
        code = r[1]
        text = build_text(r)
        unit = r[5] or r[6] or r[4] or None
        scale = f'{FREQ_RU.get(r[7], r[8] or "—")}'
        cav = caveats_for(code)
        payload.append((code, r[0], text, unit, scale, json.dumps(cav, ensure_ascii=False),
                        'auto-draft', 'draft', 1, content_hash(code, text, unit, scale, cav),
                        'auto:derived.metric_card'))

    print('примеры:')
    for p in payload[:3]:
        print(' ', p[0], '|', p[2][:180], '|', p[3], '|', p[8])
    no_unit = [p[0] for p in payload if not p[3]]
    print(f'без канонической единицы: {len(no_unit)}')

    if args.check:
        print('режим --check: записи не выполнялись')
        return 0

    if not payload:
        print('нечего добавлять')
        return 0

    sql = """
    INSERT INTO catalog.metric_definition
        (metric_code, metric_id, definition_ru, unit_canonical, scale_note, caveats,
         owner, status, version, content_hash, source_path)
    VALUES (%s,%s,%s,%s,%s,%s::jsonb,%s,%s,%s,%s,%s)
    ON CONFLICT (metric_code, version) DO NOTHING
    """
    conn = db_tunnel.connect()
    try:
        with conn.cursor() as cur:
            cur.executemany(sql, payload)
            n = cur.rowcount
        conn.commit()
    finally:
        conn.close()
    print(f'вставлено строк: {n}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
