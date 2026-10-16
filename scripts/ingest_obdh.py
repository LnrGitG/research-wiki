#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ОБДХ (Росстат) в едином каноне research_wiki: карточки, загрузка рядов, чтение.

Источник — бюллетень Росстата «Доходы, расходы и потребление домашних хозяйств»
(внутри ведомства «ДРП»), обследование бюджетов домашних хозяйств (ОБДХ).
  Прил. 1, лист 1.1 — располагаемые ресурсы домохозяйств, руб. на члена в месяц;
  Прил. 3, лист 3.2 — доля домохозяйств с финансовыми трудностями по платежам;
  Прил. 3, лист 3.3 — условная доля трудностей среди имеющих такой платёж.
Производная proxy_pdn_debt_service (ОБДХ + ЦБ) считается здесь же.

Загрузка идёт с VPS через тоннель db_tunnel.py (порт 15432), схема catalog/data.
Идемпотентность — по sha256 архива в catalog.release.content_hash: повторный
прогон на том же файле не пишет ни строки. Ревизия новым выпуском — отдельные
строки наблюдений, исторические значения не UPDATE/DELETE: старые строки
получают observation_status='superseded'.

Запуск:
    python3 scripts/ingest_obdh.py                 # карточки + загрузка + карточки метрик
    python3 scripts/ingest_obdh.py --catalog-only  # только сущности каталога
    python3 scripts/ingest_obdh.py --no-download   # без сети: только локальный кэш
    python3 scripts/ingest_obdh.py --skip-proxy    # без производной proxy_pdn
"""
import argparse
import datetime as dt
import hashlib
import os
import re
import shutil
import ssl
import subprocess
import sys
import unicodedata
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402

try:
    import pandas as pd
except ImportError:  # pragma: no cover
    raise SystemExit('нужен pandas: %s -m pip install pandas xlrd' % sys.executable)

# --- пути -------------------------------------------------------------------
SRC = os.environ.get('OBDH_SRC', os.path.expanduser('~/macroeconomist/queries/sources'))
CACHE = os.path.join(REPO, 'raw', 'obdh')            # локальный кэш архивов и разбора
EXTRACT = os.path.join(CACHE, 'extracted')
PROXY_IN = os.environ.get('OBDH_PROXY_IN', CACHE)    # входы производной (ЦБ, население)
URL_TMPL = 'https://rosstat.gov.ru/storage/mediabank/DRP_{year}.rar'
URL_TMPL_Q = 'https://rosstat.gov.ru/storage/mediabank/DRP_{year}_4.rar'
PUBLICATION_PAGE = 'https://rosstat.gov.ru/folder/13397'   # раздел «Уровень жизни»
SOURCE_CODE = 'rosstat'
DERIVED_SOURCE_CODE = 'derived_internal'

# Годовые выпуски, которые надо загрузить (старый → новый).
RELEASES = [2024, 2025]
FREQ_A = 'A'

# --- метрики ----------------------------------------------------------------
# (metric_code, name_ru, unit_code, is_derived, metric_type, source_code)
METRICS = [
    ('obdh_resources_pc_month',
     'Располагаемые ресурсы домашних хозяйств (ОБДХ), руб. на члена домохозяйства в месяц',
     'rub_per_person_month', False, 'primary', SOURCE_CODE),
    ('obdh_paydiff_consumer',
     'Доля домохозяйств с финансовыми трудностями по платежу за потребительский кредит (ОБДХ), %',
     'pct', False, 'primary', SOURCE_CODE),
    ('obdh_paydiff_mortgage',
     'Доля домохозяйств с финансовыми трудностями по платежу по ипотеке (ОБДХ), %',
     'pct', False, 'primary', SOURCE_CODE),
    ('obdh_paydiff_any',
     'Доля домохозяйств с финансовыми трудностями хотя бы по одному платежу (ОБДХ), %',
     'pct', False, 'primary', SOURCE_CODE),
    ('obdh_paydiff_none',
     'Доля домохозяйств, не имевших финансовых трудностей по платежам (ОБДХ), %',
     'pct', False, 'primary', SOURCE_CODE),
    ('obdh_paydiff_within_payers',
     'Доля домохозяйств с трудностями среди имеющих соответствующий платёж (ОБДХ), %',
     'pct', False, 'primary', SOURCE_CODE),
    ('proxy_pdn_debt_service',
     'Платёжная нагрузка: прокси долговой нагрузки (поток платежей по кредитам к располагаемым ресурсам домохозяйств, ОБДХ+ЦБ), %',
     'pct', True, 'derived', DERIVED_SOURCE_CODE),
]

PROXY_FORMULA = (
    'proxy_pdn = 100 × (a_ипо × Д_ипотека + a_проч × Д_прочее) / (Р × 12 × Н), '
    'где a(r,T) = r / (1 − (1+r)^(−T)); Д_ипотека, Д_прочее — задолженность '
    'физических лиц по ипотечным и прочим кредитам на 01.08.2026 (ЦБ), '
    'Р — располагаемые ресурсы на члена домохозяйства в месяц (ОБДХ, Прил.1.1), '
    'Н — численность населения на 01.01.2025 (Росстат); базовые допущения '
    'r_ипо = 10 %, T_ипо = 20 лет, r_проч = 22 %, T_проч = 2,5 года '
    '(коэффициенты аннуитета 0,1175 и 0,5616). Прокси популяционный: делится на всё '
    'население, поэтому систематически ниже публикуемого ПДН заёмщика (НБКИ/ЦБ ≈ 25–26 %) '
    'и сопоставим между регионами, а не с публикуемым ПДН.'
)

METRIC_ALIASES = {
    'obdh_resources_pc_month': ['располагаемые ресурсы', 'располагаемые ресурсы домохозяйств',
                                'ресурсы домохозяйств', 'доходы домохозяйств (ОБДХ)'],
    'obdh_paydiff_consumer': ['трудности по потребительскому кредиту',
                              'платёжные трудности потребкредит', 'закредитованность потребительский кредит'],
    'obdh_paydiff_mortgage': ['трудности по ипотеке', 'платёжные трудности ипотека',
                              'закредитованность ипотека'],
    'obdh_paydiff_any': ['платёжные трудности', 'трудности хотя бы по одному платежу',
                         'финансовые трудности домохозяйств'],
    'obdh_paydiff_none': ['нет трудностей по платежам', 'не имели финансовых трудностей'],
    'obdh_paydiff_within_payers': ['доля трудностей среди имеющих платёж',
                                   'условная доля трудностей'],
    'proxy_pdn_debt_service': ['платёжная нагрузка', 'платёжная нагрузка населения',
                               'долговая нагрузка', 'закредитованность', 'прокси ПДН', 'ПДН регионы'],
}

TOPIC_PARENT = ('income', 'Доходы и уровень жизни')
TOPIC_CHILD = ('debt_burden', 'Долговая нагрузка населения')

ENDPOINT = dict(
    url='https://rosstat.gov.ru/storage/mediabank/DRP_{YYYY}[_{N}].rar',
    kind='file_archive',
    poll_cron='0 7 15 2-4 *',
    parser_script='ingest_obdh.py',
    note=('ОБДХ/ДРП: годовой выпуск DRP_{YYYY}.rar (при отсутствии DRP_{YYYY}_4.rar); '
          'внутри 4_ПРИЛОЖЕНИЕ 1.xls (1.1) и 6_ПРИЛОЖЕНИЕ 3.xls (3.2, 3.3). '
          'Страница публикаций: ' + PUBLICATION_PAGE),
)

# --- нормализация имён регионов --------------------------------------------
_HOMO = str.maketrans({'a': 'а', 'e': 'е', 'o': 'о', 'c': 'с', 'p': 'р', 'x': 'х',
                       'y': 'у', 'k': 'к', 'm': 'м', 't': 'т', 'h': 'н', 'b': 'в',
                       'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н', 'K': 'К',
                       'M': 'М', 'O': 'О', 'P': 'Р', 'T': 'Т', 'X': 'Х', 'Y': 'У'})

# Наблюдённые варианты написания, которые не сводятся к catalog.region.name_ru.
# Агрегаты (199/200) — для явного распознавания и отбраковки, не для загрузки.
EXACT_REGION = {
    'архангельская область': 199,
    'архангельская область без автономного округа': 30,
    'ненецкий автономный округ': 31,
    'тюменская область': 200,
    'тюменская область без автономных округов': 70,
    'ханты-мансийский автономный округ - югра': 71,
    'ямало-ненецкий автономный округ': 72,
    'кемеровская область': 80,
    'г. москва': 27,
    'г. санкт-петербург': 38,
    'г. севастополь': 46,
    'кабардино-балкарская республика': 49,
    'карачаево-черкесская республика': 50,
    'республика северная осетия-алания': 51,
    'республика саха (якутия)': 85,
}
AGGREGATE_NAMES = {
    'центральный', 'северо-западный', 'южный', 'северо-кавказский',
    'приволжский', 'уральский', 'сибирский', 'дальневосточный',
}

# Короткие однозначные формы для каталожного поиска (fetch_context сопоставляет
# регион по вхождению алиаса в запрос, поэтому «Республика Башкортостан» не
# ловит запрос «… Башкортостан»).
SHORT_ALIASES = {
    'Башкортостан': 54, 'Татарстан': 57, 'Чувашия': 59, 'Мордовия': 56,
    'Удмуртия': 58, 'Хакасия': 75, 'Тыва': 76, 'Бурятия': 84, 'Якутия': 85,
    'Крым': 41, 'Кемеровская область — Кузбасс': 80, 'ХМАО': 71, 'ЯНАО': 72,
    'Чукотка': 94, 'Камчатка': 87, 'Чечня': 52,
}


def norm_region(s):
    s = unicodedata.normalize('NFC', str(s))
    s = s.replace('\xa0', ' ').replace('\n', ' ')
    s = re.sub(r'\s+', ' ', s).strip().lower()
    s = s.replace('ё', 'е').translate(_HOMO)
    s = re.sub(r'^в том числе\s*:?\s*', '', s)
    return s


# ключ прототипа (norm_regions.key) — для стыковки с рядами ЦБ и населения
def proto_key(name):
    s = str(name)
    s = s.translate(_HOMO)
    s = s.replace('ё', 'е').replace('\n', ' ').replace('—', '-').replace('–', '-')
    s = re.sub(r'\([^)]*\)', ' ', s)
    s = re.sub(r'^\s*г\.?\s*', '', s, flags=re.I)
    s = re.split(r'без данных', s, flags=re.I)[0]
    s = re.sub(r'в том числе\s*:?', ' ', s, flags=re.I)
    s = s.split(' - ')[0]
    s = re.sub(r'[^а-яa-z]', '', s.lower())
    s = s.replace('й', 'и')
    alias = {
        'гсанктпетербург': 'санктпетербург',
        'республикасевернаяосетияалания': 'республикасевернаяосетия',
        'хантымансиискииавтономныиокругюгра': 'хантымансиискииавтономныиокруг',
        'чувашскаяреспубликачувашия': 'чувашскаяреспублика',
        'кемеровскаяобластькузбасс': 'кемеровскаяобласть',
        'тюменскаяобластьбезавтономныхокругов': 'тюменскаяобласть',
        'архангельскаяобластьбезнанецкогоавтономногоокруга': 'архангельскаяобласть',
        'архангельскаяобластьбезавтономногоокруга': 'архангельскаяобласть',
    }
    return alias.get(s, s)


# --- обнаружение и разбор выпуска ------------------------------------------
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for blk in iter(lambda: f.read(1 << 20), b''):
            h.update(blk)
    return h.hexdigest()


def download(url, dest):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE          # у Росстата цепочка не проверяется
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=120, context=ctx) as r, open(dest, 'wb') as f:
        shutil.copyfileobj(r, f)
    return os.path.getsize(dest) > 0


def find_archive(year, allow_download):
    os.makedirs(CACHE, exist_ok=True)
    cands = [os.path.join(CACHE, 'DRP_%d.rar' % year),
             os.path.join(CACHE, 'DRP_%d_4.rar' % year),
             os.path.join(SRC, 'obdh', 'DRP_%d.rar' % year),
             os.path.join(SRC, 'obdh', 'DRP_%d_4.rar' % year)]
    for p in cands:
        if os.path.exists(p):
            return p, None
    if not allow_download:
        return None, None
    for tmpl, name in ((URL_TMPL, 'DRP_%d.rar' % year), (URL_TMPL_Q, 'DRP_%d_4.rar' % year)):
        url = tmpl.format(year=year)
        dest = os.path.join(CACHE, name)
        try:
            if download(url, dest):
                return dest, url
        except Exception as e:
            print('  загрузка не удалась: %s (%s)' % (url, str(e)[:80]))
    return None, None


def extract_archive(archive, year):
    out = os.path.join(EXTRACT, 'DRP_%d' % year)
    if os.path.isdir(out) and any(f.endswith('.xls') for f in os.listdir(out)):
        return out
    unrar = shutil.which('unrar') or shutil.which('unar') or shutil.which('7z')
    if not unrar:
        # уже распакованный каталог рядом с источником
        for p in (os.path.join(SRC, 'obdh', 'DRP_%d' % year),):
            if os.path.isdir(p):
                return p
        raise RuntimeError('нет unrar/unar/7z и нет распакованного каталога для DRP_%d' % year)
    os.makedirs(out, exist_ok=True)
    if os.path.basename(unrar).startswith('unar'):
        cmd = [unrar, '-o', '-D', archive, '-d', out]
    elif os.path.basename(unrar) == '7z':
        cmd = [unrar, 'x', '-y', '-o' + out, archive]
    else:
        cmd = [unrar, 'x', '-o+', archive, out + os.sep]
    subprocess.run(cmd, check=True, capture_output=True)
    return out


def archive_published_at(extracted_dir):
    """Дата публикации — максимум mtime файлов внутри архива (не из головы)."""
    ts = 0.0
    for root, _dirs, files in os.walk(extracted_dir):
        for f in files:
            try:
                ts = max(ts, os.path.getmtime(os.path.join(root, f)))
            except OSError:
                pass
    return dt.date.fromtimestamp(ts) if ts else dt.date.today()


def find_sheet_file(extracted_dir, starts_with):
    for f in sorted(os.listdir(extracted_dir)):
        if f.startswith(starts_with) and f.lower().endswith('.xls'):
            return os.path.join(extracted_dir, f)
    return None


def year_from_label(val):
    m = re.match(r'\s*(\d{4})', str(val))
    return int(m.group(1)) if m else None


def parse_pr1_resources(path):
    """Прил.1, лист 1.1: (регион, {год: руб/член/мес}) — колонки 1 и 2."""
    df = pd.read_excel(path, sheet_name='1.1', header=None)
    y1, y2 = year_from_label(df.iloc[5, 1]), year_from_label(df.iloc[5, 2])
    out = []
    for i in range(6, len(df)):
        name = str(df.iloc[i, 0]).strip()
        if not name or name == 'nan':
            continue
        vals = {}
        for col, yr in ((1, y1), (2, y2)):
            v = df.iloc[i, col]
            if yr and isinstance(v, (int, float)):
                vals[yr] = float(v)
        if vals:
            out.append((name, vals))
    return out


_CANON = [
    ('жилищно-коммунальные', 'жку'),
    ('электроэнергию', 'электро'),
    ('основное или дополнительное', 'образование'),
    ('лекарства', 'лекарства'),
    ('использование банковского кредита', 'потребкредит'),
    ('использование ипотечного кредита', 'ипотека'),
    ('имевшие финансовые трудности', 'хотябы1'),
    ('не имевшие финансовых трудностей', 'ни_одного'),
]


def parse_pr3(path, sheet):
    """Прил.3: (регион, {код_показателя: {год: значение}}). Строка 4 — графы, 5 — годы."""
    df = pd.read_excel(path, sheet_name=sheet, header=None)
    lab_col, last = {}, None
    for j in range(df.shape[1]):
        s = str(df.iloc[4, j]).strip()
        if s and s != 'nan':
            low = re.sub(r'\s+', ' ', s).lower()
            last = next((code for frag, code in _CANON if frag in low), last)
        lab_col[j] = last
    out = []
    for i in range(6, len(df)):
        name = re.sub(r'\s+', ' ', str(df.iloc[i, 0])).strip()
        if not name or name == 'nan':
            continue
        rec = {}
        for j in range(1, df.shape[1]):
            yr = year_from_label(df.iloc[5, j])
            code = lab_col.get(j)
            v = df.iloc[i, j]
            if yr and code and isinstance(v, (int, float)):
                rec.setdefault(code, {})[yr] = float(v)
        if rec:
            out.append((name, rec))
    return out


# --- каталог ----------------------------------------------------------------
def ensure_unit(cur, code, name_ru):
    r = cur.execute('SELECT unit_id FROM catalog.unit WHERE unit_code=%s', (code,)).fetchone()
    if r:
        return r[0]
    return cur.execute('INSERT INTO catalog.unit (unit_code, name_ru) VALUES (%s,%s) '
                       'RETURNING unit_id', (code, name_ru)).fetchone()[0]


def ensure_source(cur, code, name_ru, reliability):
    r = cur.execute('SELECT source_id FROM catalog.source WHERE source_code=%s', (code,)).fetchone()
    if r:
        return r[0]
    return cur.execute(
        'INSERT INTO catalog.source (source_code, name_ru, reliability, is_active) '
        "VALUES (%s,%s,%s,true) RETURNING source_id", (code, name_ru, reliability)).fetchone()[0]


def ensure_topic(cur, code, name_ru, parent_id):
    r = cur.execute('SELECT topic_id FROM catalog.topic WHERE topic_code=%s', (code,)).fetchone()
    if r:
        return r[0]
    return cur.execute('INSERT INTO catalog.topic (topic_code, name_ru, parent_id) '
                       'VALUES (%s,%s,%s) RETURNING topic_id', (code, name_ru, parent_id)).fetchone()[0]


def ensure_metric(cur, code, name_ru, unit_id, source_id, freq_id, is_derived, mtype, formula=None):
    r = cur.execute('SELECT metric_id FROM catalog.metric WHERE metric_code=%s', (code,)).fetchone()
    if r:
        mid = r[0]
        cur.execute('UPDATE catalog.metric SET name_ru=%s, unit_id=%s, source_id=%s, frequency_id=%s, '
                    'is_derived=%s, metric_type=%s, formula_text=%s WHERE metric_id=%s',
                    (name_ru, unit_id, source_id, freq_id, is_derived, mtype, formula, mid))
        return mid
    return cur.execute(
        'INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id, frequency_id, '
        'is_derived, metric_type, status, is_active, formula_text) '
        "VALUES (%s,%s,%s,%s,%s,%s,%s,'active',true,%s) RETURNING metric_id",
        (code, name_ru, unit_id, source_id, freq_id, is_derived, mtype, formula)).fetchone()[0]


def build_catalog(cur):
    """Заводит недостающие сущности каталога. Возвращает (metric_ids, unit/source/freq ids)."""
    unit_ids = {}
    for code, ru in (('rub_per_person_month', 'руб. на члена домохозяйства в месяц'),
                     ('pct', '%')):
        unit_ids[code] = ensure_unit(cur, code, ru)
    src_rosstat = ensure_source(cur, SOURCE_CODE, 'Росстат', 'official')
    src_derived = ensure_source(cur, DERIVED_SOURCE_CODE, 'Расчётные (производные) значения', 'derived')
    src_ids = {SOURCE_CODE: src_rosstat, DERIVED_SOURCE_CODE: src_derived}
    freq_a = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code='A'").fetchone()[0]

    parent = ensure_topic(cur, TOPIC_PARENT[0], TOPIC_PARENT[1], None)
    child = ensure_topic(cur, TOPIC_CHILD[0], TOPIC_CHILD[1], parent)

    metric_ids = {}
    for code, name_ru, unit_code, is_derived, mtype, src_code in METRICS:
        formula = PROXY_FORMULA if code == 'proxy_pdn_debt_service' else None
        mid = ensure_metric(cur, code, name_ru, unit_ids[unit_code], src_ids[src_code],
                            freq_a, is_derived, mtype, formula)
        metric_ids[code] = mid
        for al in METRIC_ALIASES[code]:
            exists = cur.execute('SELECT 1 FROM catalog.metric_alias WHERE metric_id=%s AND lower(alias)=lower(%s)',
                                 (mid, al)).fetchone()
            if not exists:
                cur.execute('INSERT INTO catalog.metric_alias (metric_id, alias, lang, alias_type, weight, created_by) '
                            "VALUES (%s,%s,'ru','synonym',1,'ingest_obdh')", (mid, al))
        cur.execute('INSERT INTO catalog.metric_topic (metric_id, topic_id, weight) VALUES (%s,%s,1) '
                    'ON CONFLICT DO NOTHING', (mid, child))

    # шаблон адреса выпуска
    has_ep = cur.execute('SELECT 1 FROM catalog.source_endpoint WHERE source_id=%s AND url=%s',
                         (src_rosstat, ENDPOINT['url'])).fetchone()
    if not has_ep:
        cur.execute('INSERT INTO catalog.source_endpoint (source_id, url, kind, poll_cron, '
                    'parser_script, is_active, note) VALUES (%s,%s,%s,%s,%s,true,%s)',
                    (src_rosstat, ENDPOINT['url'], ENDPOINT['kind'], ENDPOINT['poll_cron'],
                     ENDPOINT['parser_script'], ENDPOINT['note']))
    return metric_ids, unit_ids, src_ids, freq_a


# --- регионы ----------------------------------------------------------------
def region_index(cur):
    name_map, allowed, meta_alias = {}, set(), {}
    for rid, nm, lvl in cur.execute('SELECT region_id, name_ru, level FROM catalog.region').fetchall():
        if lvl in ('region', 'country'):
            name_map[norm_region(nm)] = rid
        if lvl == 'region' and rid not in (95, 96, 97, 98, 199, 200):
            allowed.add(rid)
    for al, rid, conf in cur.execute('SELECT alias, region_id, confidence FROM meta.region_alias '
                                     'WHERE source_id=(SELECT source_id FROM catalog.source WHERE source_code=%s)',
                                     (SOURCE_CODE,)).fetchall():
        meta_alias.setdefault(norm_region(al), rid)
    return name_map, allowed, meta_alias


def make_resolver(name_map, allowed, meta_alias):
    def resolve(raw):
        k = norm_region(raw)
        if not k:
            return None, 'empty'
        if k == 'российская федерация' or k == 'россия':
            return 1, 'country'
        if k in EXACT_REGION:
            rid = EXACT_REGION[k]
            return (rid, 'alias') if rid in allowed or rid == 1 else (None, 'aggregate')
        if k in AGGREGATE_NAMES or 'федеральный округ' in k:
            return None, 'aggregate'
        if k in name_map:
            rid = name_map[k]
            return (rid, 'name') if rid in allowed or rid == 1 else (None, 'aggregate')
        if k in meta_alias:
            rid = meta_alias[k]
            return (rid, 'meta_alias') if rid in allowed or rid == 1 else (None, 'aggregate')
        return None, 'unmatched'
    return resolve


def seed_aliases(cur, resolve, labels, src_id):
    """Наполняет meta.region_alias наблюдёнными вариантами написаний."""
    n = 0
    for lab in sorted(set(labels)):
        rid, how = resolve(lab)
        if rid is None:
            continue
        cur.execute('INSERT INTO meta.region_alias (alias, region_id, source_id, confidence) '
                    "VALUES (%s,%s,%s,'exact') ON CONFLICT (alias, source_id) DO NOTHING",
                    (re.sub(r'\s+', ' ', str(lab)).strip(), rid, src_id))
        n += cur.rowcount
    for al, rid in SHORT_ALIASES.items():
        cur.execute('INSERT INTO meta.region_alias (alias, region_id, source_id, confidence) '
                    "VALUES (%s,%s,%s,'exact') ON CONFLICT (alias, source_id) DO NOTHING",
                    (al, rid, src_id))
        n += cur.rowcount
    return n


# --- производная proxy_pdn --------------------------------------------------
def annuity(r, t):
    return r / (1 - (1 + r) ** (-t))


def _collect(path, sheet, name_col, val_col, start):
    df = pd.read_excel(path, sheet_name=sheet, header=None)
    d = {}
    for i in range(start, len(df)):
        n = re.sub(r'\s+', ' ', str(df.iloc[i, name_col])).strip()
        v = df.iloc[i, val_col]
        if not n or n == 'nan' or not isinstance(v, (int, float)):
            continue
        d[proto_key(n)] = float(v)
    return d


def compute_proxy(key_to_region):
    """proxy_pdn по регионам из локальных входов ЦБ/населения и ОБДХ (Прил.1.1, 2025)."""
    base = PROXY_IN
    debt_mort = os.path.join(base, 'debt_mort.xlsx')
    debt_tot = os.path.join(base, 'lo_20260801.xlsx')
    popf = os.path.join(base, 'PrPopul2025_Site.xlsx')
    for p in (debt_mort, debt_tot, popf):
        if not os.path.exists(p):
            print('  производная пропущена: нет входа %s' % p)
            return []
    mort = _collect(debt_mort, 'итого', 0, -1, 2)
    tot = _collect(debt_tot, 'Данные', 0, 4, 6)
    pop = _collect(popf, 'Численность-человек', 0, 1, 5)
    # ресурсы — из уже разобранного Прил.1.1 последнего выпуска
    res = {}
    pr1 = find_sheet_file(os.path.join(EXTRACT, 'DRP_%d' % max(RELEASES)), '4_ПРИЛОЖЕНИЕ 1')
    if pr1:
        for name, vals in parse_pr1_resources(pr1):
            if vals:
                yr = max(vals)
                res[proto_key(name)] = vals[yr]
    a_m, a_c = annuity(0.10, 20), annuity(0.22, 2.5)
    rows = []
    for k, (name, d_tot) in ((k, (k, v)) for k, v in tot.items()):
        if k not in mort or k not in pop or k not in res or k not in key_to_region:
            continue
        d_m = mort[k]
        n_pop = pop[k]
        flow = a_m * d_m + a_c * (d_tot - d_m)
        resources = res[k] * 12 * n_pop / 1e6
        if resources <= 0:
            continue
        rows.append((key_to_region[k], 100.0 * flow / resources))
    return rows


# --- производные карточки метрик -------------------------------------------
def refresh_metric_cards(cur, metric_ids):
    themes = {
        'obdh_resources_pc_month': ['уровень жизни'],
        'obdh_paydiff_consumer': ['потребительский спрос'],
        'obdh_paydiff_mortgage': ['потребительский спрос'],
        'obdh_paydiff_any': ['потребительский спрос'],
        'obdh_paydiff_none': ['потребительский спрос'],
        'obdh_paydiff_within_payers': ['потребительский спрос'],
        'proxy_pdn_debt_service': ['кредит и денежная политика', 'региональная экономика'],
    }
    from datetime import date
    for code, mid in metric_ids.items():
        r = cur.execute(
            'SELECT count(*), count(DISTINCT region_id), min(period_start), max(period_start) '
            "FROM data.observation WHERE metric_id=%s AND observation_status <> 'rejected'", (mid,)).fetchone()
        n_obs, n_reg, pmin, pmax = r
        if not n_obs:
            continue
        nm = cur.execute('SELECT name_ru, description FROM catalog.metric WHERE metric_id=%s', (mid,)).fetchone()
        u = cur.execute('SELECT u.unit_code, u.name_ru FROM catalog.metric m JOIN catalog.unit u '
                        'ON u.unit_id=m.unit_id WHERE m.metric_id=%s', (mid,)).fetchone()
        fresh = (date.today() - pmax).days if pmax else None
        level = 'региональный' if (n_reg or 0) > 3 else 'федеральный'
        text = (f'{nm[0]}. Единица: {u[1] or u[0]}. Частота: годовая. Уровень: {level}. '
                f'Темы: {", ".join(themes.get(code, []))}. Охват: {n_obs} наблюдений, '
                f'{n_reg} регионов, период {pmin}..{pmax}. Код метрики: {code}.')
        text = re.sub(r'\s+', ' ', text).strip()
        srcs = cur.execute('SELECT DISTINCT s.source_code FROM data.observation o JOIN catalog.source s '
                           'ON s.source_id=o.source_id WHERE o.metric_id=%s', (mid,)).fetchall()
        src_arr = sorted({x[0] for x in srcs}) or ['rosstat']
        cur.execute(
            'INSERT INTO derived.metric_card (metric_id, metric_code, name_ru, unit_code, unit_ru, '
            'frequency_ru, sources, themes, level, n_obs, n_regions, period_min, period_max, '
            'freshness_days, status, search_text, built_at) '
            "VALUES (%s,%s,%s,%s,%s,'годовая',%s,%s,%s,%s,%s,%s,%s,%s,'active',%s, now()) "
            'ON CONFLICT (metric_id) DO UPDATE SET metric_code=EXCLUDED.metric_code, '
            'name_ru=EXCLUDED.name_ru, unit_code=EXCLUDED.unit_code, unit_ru=EXCLUDED.unit_ru, '
            'sources=EXCLUDED.sources, themes=EXCLUDED.themes, level=EXCLUDED.level, n_obs=EXCLUDED.n_obs, '
            'n_regions=EXCLUDED.n_regions, period_min=EXCLUDED.period_min, period_max=EXCLUDED.period_max, '
            'freshness_days=EXCLUDED.freshness_days, status=EXCLUDED.status, search_text=EXCLUDED.search_text, '
            'built_at=now()',
            (mid, code, nm[0], u[0], u[1], src_arr, themes.get(code, []), level, n_obs, n_reg, pmin, pmax,
             fresh, text))
    # свежесть читается из materialized view — обновляем снимок
    cur.execute('REFRESH MATERIALIZED VIEW derived.v_metric_card')


# --- главный поток ----------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--catalog-only', action='store_true')
    ap.add_argument('--no-download', action='store_true')
    ap.add_argument('--skip-proxy', action='store_true')
    a = ap.parse_args()

    conn = db_tunnel.connect()
    with conn.cursor() as cur:
        metric_ids, unit_ids, src_ids, freq_a = build_catalog(cur)
        conn.commit()
        print('каталог: метрик заведено/обновлено %d' % len(metric_ids))
        if a.catalog_only:
            return 0

        name_map, allowed, meta_alias = region_index(cur)
        resolve = make_resolver(name_map, allowed, meta_alias)
        print('регионов к загрузке: %d (+Россия)' % len(allowed))

        # --- загрузка выпусков ---
        all_labels, key_to_region = set(), {}
        per_release = []
        for year in RELEASES:
            archive, url = find_archive(year, allow_download=not a.no_download)
            if not archive:
                print('выпуск %d: архив не найден (нет локально, загрузка отключена/не удалась)' % year)
                continue
            chash = sha256_file(archive)
            rel = cur.execute('SELECT release_id, status FROM catalog.release WHERE source_id=%s AND content_hash=%s',
                              (src_ids[SOURCE_CODE], chash)).fetchone()
            if rel and rel[1] == 'loaded':
                print('выпуск %d: хеш %s… уже загружен (release_id=%s) — пропуск' % (year, chash[:12], rel[0]))
                continue
            ex = extract_archive(archive, year)
            pr1 = find_sheet_file(ex, '4_ПРИЛОЖЕНИЕ 1')
            pr3 = find_sheet_file(ex, '6_ПРИЛОЖЕНИЕ 3')
            if not pr1 or not pr3:
                print('выпуск %d: не найдены приложения в %s' % (year, ex))
                continue
            res_rows = parse_pr1_resources(pr1)
            pd32 = parse_pr3(pr3, '3.2')
            pd33 = parse_pr3(pr3, '3.3')

            rows, quarantine, years = [], {}, set()
            for name, vals in res_rows:
                all_labels.add(name)
                rid, how = resolve(name)
                if rid is None:
                    if how == 'unmatched':
                        quarantine[name] = quarantine.get(name, 0) + 1
                    continue
                key_to_region.setdefault(proto_key(name), rid)
                for yr, v in vals.items():
                    rows.append((metric_ids['obdh_resources_pc_month'], rid, yr, v, ''))
                    years.add(yr)
            # 3.2 — ко всем домохозяйствам
            map32 = {'потребкредит': 'obdh_paydiff_consumer', 'ипотека': 'obdh_paydiff_mortgage',
                     'хотябы1': 'obdh_paydiff_any', 'ни_одного': 'obdh_paydiff_none'}
            for name, rec in pd32:
                all_labels.add(name)
                rid, how = resolve(name)
                if rid is None:
                    if how == 'unmatched':
                        quarantine[name] = quarantine.get(name, 0) + 1
                    continue
                for code_key, code in map32.items():
                    for yr, v in rec.get(code_key, {}).items():
                        rows.append((metric_ids[code], rid, yr, v, ''))
                        years.add(yr)
            # 3.3 — условные доли среди имеющих платёж
            map33 = {'потребкредит': 'потребительский кредит', 'ипотека': 'ипотека'}
            for name, rec in pd33:
                all_labels.add(name)
                rid, how = resolve(name)
                if rid is None:
                    if how == 'unmatched':
                        quarantine[name] = quarantine.get(name, 0) + 1
                    continue
                for code_key, sub in map33.items():
                    for yr, v in rec.get(code_key, {}).items():
                        rows.append((metric_ids['obdh_paydiff_within_payers'], rid, yr, v, sub))
                        years.add(yr)

            # проверки перед регистрацией релиза и вставкой
            max_year = max(years)
            region_span = {r for (_m, r, _y, _v, _s) in rows}
            pct_ids = {metric_ids[c] for c in ('obdh_paydiff_consumer', 'obdh_paydiff_mortgage',
                                               'obdh_paydiff_any', 'obdh_paydiff_none',
                                               'obdh_paydiff_within_payers')}
            bad = []
            for mid, r, y, v, _sub in rows:
                ok = (0 <= v <= 100) if mid in pct_ids else (v > 0)
                if not ok or y < 2000:
                    bad.append((mid, r, y, v))
            if not rows or len(region_span) < 86 or len(years) < 2 or bad:
                print('выпуск %d: ПРОВЕРКИ НЕ ПРОЙДЕНЫ — регионов %d, лет %s, брак %d; стоп'
                      % (year, len(region_span), sorted(years), len(bad)))
                continue

            # релиз регистрируется только после успешных проверок
            label = 'ОБДХ, ДРП, выпуск %d' % year
            pub = archive_published_at(ex)
            if rel:
                release_id = rel[0]
                cur.execute("UPDATE catalog.release SET status='loaded', ingested_at=now(), label=%s, "
                            'published_at=%s, url=%s, content_hash=%s WHERE release_id=%s',
                            (label, pub, url, chash, release_id))
            else:
                release_id = cur.execute(
                    "INSERT INTO catalog.release (source_id, label, published_at, content_hash, status, "
                    "ingested_at, url) VALUES (%s,%s,%s,%s,'loaded', now(), %s) RETURNING release_id",
                    (src_ids[SOURCE_CODE], label, pub, chash, url)).fetchone()[0]
            conn.commit()

            ins = 0
            for mid, rid, yr, v, sub in rows:
                status = 'preliminary' if yr == max_year else 'final'
                cur.execute(
                    'INSERT INTO data.observation (metric_id, region_id, period_start, period_end, value, '
                    'frequency_id, source_id, release_id, assessment_type, observation_status, sub_dimension) '
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                    'ON CONFLICT (metric_id, region_id, period_start, frequency_id, assessment_type, '
                    'sub_dimension, release_id) DO NOTHING',
                    (mid, rid, dt.date(yr, 1, 1), dt.date(yr, 12, 31), v, freq_a, src_ids[SOURCE_CODE],
                     release_id, status, 'validated', sub))
                ins += cur.rowcount
            # ревизия: перекрытые прошлыми выпусками годы помечаем superseded (без DELETE)
            cur.execute(
                "UPDATE data.observation o SET observation_status='superseded' "
                'WHERE o.metric_id = ANY(%s) AND o.release_id <> %s AND o.observation_status = \'validated\' '
                'AND EXISTS (SELECT 1 FROM data.observation n WHERE n.metric_id=o.metric_id '
                'AND n.region_id=o.region_id AND n.period_start=o.period_start '
                'AND n.sub_dimension=o.sub_dimension '
                'AND n.release_id=%s AND n.release_id > o.release_id)',
                (list(metric_ids.values()), release_id, release_id))
            conn.commit()
            print('выпуск %d: release_id=%s, кандидатов %d, вставлено новых %d, лет %s, регионов %d%s'
                  % (year, release_id, len(rows), ins, sorted(years), len(region_span),
                     ('; карантин: ' + str(sorted(quarantine.items())[:6])) if quarantine else ''))
            per_release.append(release_id)

        # --- простановка наблюдённых вариантов написаний ---
        seeded = seed_aliases(cur, resolve, all_labels, src_ids[SOURCE_CODE])
        conn.commit()
        if seeded:
            print('meta.region_alias: добавлено написаний %d' % seeded)

        # --- производная proxy_pdn ---
        if not a.skip_proxy:
            prows = compute_proxy(key_to_region)
            if prows:
                dh = hashlib.sha256()
                for p in (os.path.join(PROXY_IN, 'debt_mort.xlsx'),
                          os.path.join(PROXY_IN, 'lo_20260801.xlsx'),
                          os.path.join(PROXY_IN, 'PrPopul2025_Site.xlsx')):
                    if os.path.exists(p):
                        dh.update(sha256_file(p).encode())
                dhash = dh.hexdigest()
                rel = cur.execute('SELECT release_id FROM catalog.release WHERE source_id=%s AND content_hash=%s',
                                  (src_ids[DERIVED_SOURCE_CODE], dhash)).fetchone()
                if rel:
                    print('производная proxy_pdn: хеш входов уже загружен — пропуск')
                else:
                    drel = cur.execute(
                        "INSERT INTO catalog.release (source_id, label, published_at, content_hash, status, "
                        "ingested_at) VALUES (%s,%s,%s,%s,'loaded', now()) RETURNING release_id",
                        (src_ids[DERIVED_SOURCE_CODE],
                         'ОБДХ прокси ПДН (расчёт: ОБДХ 2025 + ЦБ 01.08.2026)', dt.date(2026, 8, 1),
                         dhash)).fetchone()[0]
                    ins = 0
                    max_y = 2025
                    for rid, val in prows:
                        if not (0 <= val <= 100):
                            continue
                        cur.execute(
                            'INSERT INTO data.observation (metric_id, region_id, period_start, period_end, value, '
                            'frequency_id, source_id, release_id, assessment_type, observation_status, sub_dimension) '
                            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'final','validated','') "
                            'ON CONFLICT (metric_id, region_id, period_start, frequency_id, assessment_type, '
                            'sub_dimension, release_id) DO NOTHING',
                            (metric_ids['proxy_pdn_debt_service'], rid, dt.date(max_y, 1, 1),
                             dt.date(max_y, 12, 31), val, freq_a, src_ids[DERIVED_SOURCE_CODE], drel))
                        ins += cur.rowcount
                    conn.commit()
                    print('производная proxy_pdn: release_id=%s, вставлено %d регионов' % (drel, ins))

        # --- карточки метрик и свежесть ---
        refresh_metric_cards(cur, metric_ids)
        conn.commit()

        # --- отчёт ---
        print('\nитог по рядам:')
        for code, mid in metric_ids.items():
            got = cur.execute(
                "SELECT count(*) FILTER (WHERE observation_status <> 'superseded'), "
                "count(DISTINCT region_id) FILTER (WHERE observation_status <> 'superseded'), "
                "min(period_start), max(period_start) FROM data.observation WHERE metric_id=%s", (mid,)).fetchone()
            print('  %-30s строк=%4d регионов=%3d период %s..%s' % (code, got[0], got[1], got[2], got[3]))
        fr = cur.execute("SELECT metric_code, freshness, last_observation FROM derived.v_metric_context "
                         "WHERE metric_code = ANY(%s)", (list(metric_ids),)).fetchall()
        print('\nсвежесть (derived.v_metric_context):')
        for c, f, lo in fr:
            print('  %-30s %-10s последнее %s' % (c, f, lo))
    conn.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
