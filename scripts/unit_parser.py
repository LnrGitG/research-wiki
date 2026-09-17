"""Разбор единиц из текста: единица часто указана в скобках в конце названия."""
import os, re, psycopg, collections
os.environ.setdefault('PGPASSFILE', os.path.expanduser('~/.pgpass'))

# единица внутри скобок → код
UNIT_IN_TEXT = [
    (r'процент|%', 'pct'),
    (r'тысяча квадратных метр|тыс\.?\s*м2|тыс\.?\s*м²', 'ths_sqm'),
    (r'миллион квадратных метр|млн\.?\s*м2|млн\.?\s*м²', 'mln_sqm'),
    (r'квадратн\w+ метр|кв\.?\s*м|м2\b|м²', 'sqm'),
    (r'тысяча рублей|тыс\.?\s*руб', 'ths_rub'),
    (r'миллиард\w* рублей|млрд\.?\s*руб', 'bln_rub'),
    (r'миллион\w* рублей|млн\.?\s*руб', 'mln_rub'),
    (r'рубл', 'rub'),
    (r'единиц|штук', 'units'),
    (r'тысяча человек|тыс\.?\s*чел', 'ths_persons'),
    (r'человек|чел\.', 'persons'),
    (r'коэффициент|раз\b', 'ratio'),
    (r'индекс', 'index'),
    (r'п\.?\s*п\.|процентн\w+ пункт', 'pct_pts'),
]

BRACKET = re.compile(r'[\(\[]([^\)\]]{3,90})[\)\]]')


def unit_from_text(*texts):
    """Искать единицу в названии и в поле unit. Возвращает код или None."""
    for t in texts:
        if not t:
            continue
        t = str(t).lower()
        # сначала в скобках
        for m in BRACKET.finditer(t):
            inner = m.group(1)
            for pat, code in UNIT_IN_TEXT:
                if re.search(pat, inner):
                    return code
        # затем по всему тексту
        for pat, code in UNIT_IN_TEXT:
            if re.search(pat, t):
                return code
    return None



# ── смысловые правила: единица выводится из характера показателя ────
# Применяются, когда единица не найдена ни в скобках, ни в тексте.
SEMANTIC = [
    # счётные показатели
    (r'^количество|^число\b|количеств\w+ (домов|квартир|договоров|зданий|сделок)|'
     r'числ\w+ (зданий|домов|квартир)', 'units'),
    # доли, уровни, готовность, структура — проценты
    (r'^доля|^уровень|^структура|готовност|распределение|удельн\w+ вес|'
     r'обеспеченност|^темп|прирост|снижени', 'pct'),
    # индексы
    (r'^индекс|индекс физического|индекс цен', 'index'),
    # площади
    (r'^площадь|общая площадь|жилая площадь|площад\w+ квартир|м2|м²', 'sqm'),
    # деньги
    (r'^суммарная цена|^цена|^стоимость|задолженность|объ[её]м (выданных|кредитов)|'
     r'рублевая|руб\.', 'mln_rub'),
    # отношения
    (r'^отношение|коэффициент|^на\b.*человек', 'ratio'),
]


def unit_from_semantics(name: str):
    """Вывести единицу из смысла названия."""
    if not name:
        return None
    t = str(name).lower()
    for pat, code in SEMANTIC:
        if re.search(pat, t):
            return code
    return None


def resolve_unit(name, *texts):
    """
    Полное определение единицы: скобки/текст → смысл → None.
    Порядок важен: явное указание приоритетнее вывода по смыслу.
    """
    u = unit_from_text(*texts)
    if u:
        return u
    return unit_from_semantics(name)


if __name__ == '__main__':
    conn = psycopg.connect("host=127.0.0.1 port=15432 dbname=research_wiki user=wiki")
    cur = conn.cursor()
    cur.execute("""SELECT indicator_name, unit FROM staging.rosstat_construction__indicators
                   ORDER BY id""")
    rows = cur.fetchall()
    print(f"проверяю {len(rows)} записей справочника\n")
    stat = collections.Counter()
    examples = {}
    for name, unit in rows:
        c = unit_from_text(name, unit)
        stat[c or 'НЕ ОПРЕДЕЛЕНО'] += 1
        examples.setdefault(c or 'НЕ ОПРЕДЕЛЕНО', (name, unit))
    for code, n in stat.most_common():
        print(f"  {str(code):14} {n:>4}")
        nm, u = examples[code]
        print(f"       пример: {(nm or '')[:58]!r}")
        if u:
            print(f"       unit-поле: {u[:58]!r}")

    print("\n=== остальные группы ===")
    for tbl, nmcol in (('cbr_lending__mortgage_monthly','indicator'),
                       ('cbr_lending__escrow_monthly','indicator'),
                       ('regions_panel__panel','indicator_name'),
                       ('rosstat_construction__housing_input_operational_monthly','indicator')):
        cur.execute(f"SELECT DISTINCT {nmcol}, unit FROM staging.{tbl} WHERE {nmcol} IS NOT NULL LIMIT 60")
        c = collections.Counter()
        for nm, u in cur.fetchall():
            c[unit_from_text(nm, u) or 'НЕ ОПРЕДЕЛЕНО'] += 1
        print(f"  {tbl.split('__')[1]}: {dict(c.most_common(4))}")
    conn.close()
