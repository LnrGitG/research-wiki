#!/usr/bin/env python3
"""
Ремонт скриптов, повреждённых коммитом d44e3d8 («Migrate heavy data to GCS»).

Тогда автоматическая замена абсолютных путей на REPO_ROOT/ensure_db()
обернула выражения в лишние кавычки, превратив код в строковые литералы.
11 файлов перестали парситься (SyntaxError) и не запускались вовсе.

Что делает:
  - DB = 'str(ensure_db('X.db'))'            → DB = str(ensure_db('X.db'))
  - sqlite3.connect('str(ensure_db('X.db'))') → sqlite3.connect(str(ensure_db('X.db')))
  - pd.read_csv('DATA / 'f.csv'', ...)        → pd.read_csv(str(DATA / 'f.csv'), ...)
  - df.to_csv('str(DATA / 'f.csv')', ...)     → df.to_csv(str(DATA / 'f.csv'), ...)
  - RAW = 'str(Path(...) / 'raw' / ...)'      → RAW = str(Path(...) / 'raw' / ...)
  - добавляет REPO_ROOT/DATA/Path там, где они используются, но не определены

Проверяет каждый файл через ast.parse после правки.

Запуск:  python3 scripts/repair_scripts.py [--apply]
Без --apply — сухой прогон.
"""
import re, sys, os, ast
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / 'scripts'
APPLY = '--apply' in sys.argv


def unquote_call(line: str) -> str:
    """
    Снять лишние обрамляющие кавычки вокруг выражения.
      DB = 'str(ensure_db('x.db'))'  ->  DB = str(ensure_db('x.db'))
      pd.read_csv('DATA / 'f.csv'',  ->  pd.read_csv(str(DATA / 'f.csv'),
    """
    orig = line
    # шаблон 1: = 'str(...'  (значение целиком в кавычках)
    m = re.match(r'^(\s*\w+\s*=\s*)\'(str\(.+\))\'\s*$', line)
    if m:
        return m.group(1) + m.group(2)
    # шаблон 2: ...connect('str(...)')
    m = re.match(r"^(\s*.*connect\()'(str\(.+?\))'\)\s*$", line)
    if m:
        return m.group(1) + m.group(2) + ')'
    # шаблон 3: read_csv('DATA / 'x.csv'',  или  to_csv('str(DATA / 'x.csv')',
    m = re.match(r"^(\s*.*(?:read_csv|to_csv)\()'(?:str\()?DATA / '([^']+)''(.*)$", line)
    if m:
        head, fname, tail = m.group(1), m.group(2), m.group(3)
        tail = tail.rstrip()
        if tail.endswith("',"):
            tail = tail[:-1]          # убираем висячую запятую внутри
        return f"{head}str(DATA / '{fname}'){tail}"
    # шаблон 4: to_csv('str(DATA / 'x.csv')', float_format=...)
    m = re.match(r"^(\s*.*to_csv\()'str\(DATA / '([^']+)'\)'(.*)$", line)
    if m:
        return f"{m.group(1)}str(DATA / '{m.group(2)}'){m.group(3)}"
    # шаблон 5: RAW = 'str(Path(...) / 'raw' / ...')
    m = re.match(r"^(\s*\w+\s*=\s*)'(str\(Path\(.+\))'(\s*)$", line)
    if m:
        return m.group(1) + m.group(2) + m.group(3)
    return orig


NEEDS = {
    # файл: (нужен REPO_ROOT/DATA, нужен Path)
    'canonize_regions.py': (False, True),
    'export_dashboard.py': (True, True),
    'export_operational.py': (True, True),
    'parse_tochno_rfsd.py': (False, True),
    'reindex_vacuum_db.py': (False, False),
    'rosstat_prom_monthly_parse.py': (False, False),
    'build_housing_index.py': (False, True),
    'collect_housing_trends.py': (False, True),
}


def ensure_defs(src: str, fname: str) -> str:
    """Добавить REPO_ROOT/DATA/Path, если используются, но не определены."""
    has_repo = bool(re.search(r'^\s*REPO_ROOT\s*=', src, re.M))
    has_data = bool(re.search(r'^\s*DATA\s*=', src, re.M))
    has_path = 'from pathlib import Path' in src
    adds = []
    if 'REPO_ROOT' in src and not has_repo:
        adds.append("from pathlib import Path\nREPO_ROOT = Path(__file__).resolve().parent.parent")
    if 'DATA' in src and not has_data:
        if not has_repo and 'REPO_ROOT' not in src:
            adds.append("from pathlib import Path\nREPO_ROOT = Path(__file__).resolve().parent.parent")
        adds.append("DATA = REPO_ROOT / 'data'")
    if 'Path(' in src and not has_path:
        adds.append("from pathlib import Path")
    if not adds:
        return src

    lines = src.split('\n')
    # вставим после последнего import в начале файла (или после docstring)
    idx = 0
    in_doc = False
    for i, ln in enumerate(lines[:40]):
        st = ln.strip()
        if st.startswith('"""') or st.startswith("'''"):
            in_doc = not in_doc
            if not in_doc:
                idx = i + 1
            continue
        if in_doc:
            continue
        if st.startswith(('import ', 'from ')):
            idx = i + 1
        elif st == '' or st.startswith('#'):
            continue
        else:
            break
    block = '\n'.join(adds)
    lines.insert(idx, '\n' + block)
    return '\n'.join(lines)


def main():
    broken = []
    for f in sorted(SCRIPTS.glob('*.py')):
        src = f.read_text(encoding='utf-8')
        try:
            ast.parse(src)
            continue
        except SyntaxError:
            pass
        lines = src.split('\n')
        new_lines = [unquote_call(l) for l in lines]
        new = '\n'.join(new_lines)
        new = ensure_defs(new, f.name)
        try:
            ast.parse(new)
            status = '✓ чинен'
        except SyntaxError as e:
            status = f'✗ остался сломан (строка {e.lineno})'
        broken.append((f, status, new))
        print(f"  {f.name:34} {status}")

    if not broken:
        print("  сломанных скриптов не найдено")
        return

    print(f"\nвсего: {len(broken)}, исправлено: {sum(1 for _, s, _ in broken if s.startswith('✓'))}")
    if APPLY:
        for f, status, new in broken:
            if status.startswith('✓'):
                f.write_text(new, encoding='utf-8')
        print("\n✓ записано")


if __name__ == '__main__':
    main()
