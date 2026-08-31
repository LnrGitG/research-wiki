#!/usr/bin/env python3
"""Парсер кэша Prom_07_2026 (Firecrawl markdown ~2 млн знаков) в rosstat_construction.db.
Схема файла: '| Продукт | код |' затем '| Единица | код |', затем '| Федеральный округ | код | v_июль | v_июнь | ytd |'
Мы берём строку РФ ('Российская Федерация без учета') в первой единице измерения (обычно тыс.тонн/тыс.м3/млн м3)"""
import re, sqlite3, datetime

T = open('/home/lnr/.hermes/cache/web/rosstat.gov.ru-8fbd06702e.md').read()
con = sqlite3.connect('/home/lnr/research-wiki/data/rosstat_construction.db')
now = datetime.datetime.now().isoformat()

# Интересующие продукты для стройцикла (продукт-подстрока в md): (название в базе, regex якорь)
WANT = [
    'Портландцемент, цемент глиноземистый',
    'Бетон, готовый для заливки',
    'Кирпич керамический неогнеупорный',
    'Блоки стеновые силикатные',
    'Блоки и прочие изделия сборные строительные',
    'Кирпич строительный (включая камни) из цемента',
    'Стекло листовое термически полированное',
    'Плитки керамические глазурованные',
    'Плитки керамические для полов',
    'Трубы и муфты хризотилцементные',
    'Прокат готовый',
    'Трубы, профили пустотелые',
    'Лифты',
    'Подшипники',
    'Пески природные',
    'Гранулы, крошка и порошок',
    'Конструкции и детали конструкций из черных металлов',
    'Двери, их коробки',
    'Окна и их коробки деревянные',
    'Фанера',
    'Плиты древесностружечные',
    'Лифты, тыс. штук',
]

def parse_block(start):
    """От начала продукта до следующего продукта: найти строку РФ."""
    chunk = T[start:start+6000]
    m = re.search(r'\| Тысяча [^|]+\| \d+ \|\s*\|\n\| Российская Федерация[^|]*\| 643004[^|]*\| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|', chunk)
    if not m:
        m = re.search(r'Российская Федерация[^|]*\|[^|]*\|\s*([\d.Eе+]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|', chunk)
    return (float(m.group(1)), float(m.group(2)), float(m.group(3))) if m else None

rows = []
for name in set(WANT):
    # найти ПОСЛЕДНЮЮ единицу-заголовок перед РФ-строкой продукта; проще: поискать якорь имени продукта
    for m in re.finditer(re.escape(name), T):
        blk = parse_block(m.start())
        if blk:
            rows.append((name, *blk))
            break

seen = {}
for name, jul, jun, ytd in rows:
    if name in seen: continue
    seen[name] = (jul, jun, ytd)
    print(f'{name}: июль={jul} июнь={jun} 7м={ytd}')

con.execute('''CREATE TABLE IF NOT EXISTS prom_products_monthly (
  product TEXT, year INTEGER, month INTEGER,
  value_month REAL, value_prev_month REAL, value_ytd REAL,
  source TEXT, ingested_at TEXT DEFAULT (datetime('now')),
  PRIMARY KEY (product, year, month))''')
for name, (jul, jun, ytd) in seen.items():
    con.execute("INSERT OR REPLACE INTO prom_products_monthly (product,year,month,value_month,value_prev_month,value_ytd,source,ingested_at) VALUES (?,?,?,?,?,?,?,?)"
                .replace('value_month','value_month'), (name, 2026, 7, jul, jun, ytd, 'rosstat_Prom_07_2026', now))
con.commit()
print('\nЗаписано:', len(seen))