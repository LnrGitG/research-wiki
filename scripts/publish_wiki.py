#!/usr/bin/env python3
"""Публикация базы знаний из приватного главного репозитория в публичный.

Схема (решение 19.09.2026): рабочий репозиторий — приватный
`research-wiki-private`; публичный `research-wiki` — витрина знаний.
Правило раздела: публикуется то, что читает человек (статьи, рецензии,
концепты, сущности, сравнения, аннотации, модели, новости, визуализации,
данные, витрина docs/); не публикуется то, что читает машина или её
обслуживает (scripts/, db/, queries/, templates/, журналы, конвенции).

Состав задан списками KEEP_* — явно, а не подразумеваемо. Всё, что не
перечислено, в публичный не попадает и попадает в отчёт как
«вне классификации» — это сигнал дополнить списки.

Запуск:  python3 publish_wiki.py            # сухой прогон (отчёт + фильтр)
         APPLY=1 python3 publish_wiki.py     # публикация

Механика: срез собирается БЕЗ переключения рабочей ветки — через временный
индекс (GIT_INDEX_FILE) от дерева HEAD: убираем служебное, пишем дерево
(`git write-tree`), делаем коммит через `git commit-tree` и пушим результат
в публичный `main` с force. Рабочее дерево и текущая ветка не трогаются,
неотслеживаемые файлы не мешают.

Почему так, а не веткой: при переключении на ветку с другим составом git
отказывается работать из-за неотслеживаемых файлов (служебные каталоги,
существующие в рабочем дереве, но отсутствующие в срезе), и рабочее
состояние приходится восстанавливать вручную.
"""
import os
import re
import subprocess
import sys
import tempfile

APPLY = os.environ.get("APPLY") == "1"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_REMOTE = "public"
PUBLIC_BRANCH = "main"
BASE_REF = "HEAD"

# --- Состав публичного (знания) ---
KEEP_DIRS = [
    "papers", "reviews", "concepts", "entities", "comparisons",
    "annotations", "models", "news", "visualizations",
    "data", "docs", ".github",
]
KEEP_FILES = [
    "index.md", "MOC.md", "README.md",
    "bibliography_references.md", "bibliography_ru.md",
    "hypotheses.yaml", ".gitignore",
    # Документация вики и журнал содержательных правок — читаются человеком,
    # на них ссылаются README.md, MOC.md и страницы концептов. Служебных
    # деталей не содержат (в отличие от log-tech.md, который остаётся
    # приватным: там IP и идентификаторы ВМ).
    "SCHEMA.md", "log.md",
]

# --- Служебное: остаётся только в приватном ---
DROP_DIRS = ["scripts", "db", "queries", "templates", "db_docs", "raw"]
DROP_FILES = [
    "AGENTS.md", "MEMORY.md", "USER.md",
    "log-tech.md",
    "latest.zip", "nowcast_investments_housing_sep2026.pdf",
    "gdelt_fetch_final.py", "gdelt_fetch_fixed.py", "gdelt_fetch_hourly.py",
    "gdelt_fetch_latest.py", "gdelt_fetch_robust.py", "gdelt_fetch_yesterday.py",
]
DROP_DATA_FILES = [
    "data/backup_log.jsonl", "data/archive/cleanup_report.json",
    "data/dupes_removed.json", "data/developers_ifrs.db",
    # Внутренние файлы дедупликации: содержат ссылки на служебные файлы
    # (AGENTS.md, MEMORY.md, USER.md, SCHEMA.md, log.md), которых в публичном
    # нет — в витрине это выглядело бы как битые ссылки.
    "data/search_dedupe.json",
]

# --- Фильтр чувствительного: ни одного совпадения ---
SENSITIVE_PATTERNS = [
    (r"89\.169\.168\.214", "IP рабочей ВМ"),
    (r"46\.243\.210\.160", "IP ВМ research-db"),
    (r"\bid_yc\b", "ssh-ключ YC"),
    (r"epd1a9b94", "идентификатор ВМ"),
    (r"ubuntu@", "учётка на ВМ"),
    (r"~/\.hermes", "пути сетапа агента"),
    (r"\.pgpass", "файл паролей PostgreSQL"),
    (r"research-db", "имя хоста"),
    (r"datalens_ro", "роль DataLens"),
    (r"\bAIza[0-9A-Za-z_\-]{10,}", "ключ Google"),
    (r"\bghp_[0-9A-Za-z]{20,}", "токен GitHub"),
    (r"\bAQVN[0-9A-Za-z_\-]{10,}", "ключ YC"),
    (r"\bsk-[0-9A-Za-z]{20,}", "ключ OpenAI-класса"),
]


def git(*args, check=True, env=None, stdin=None):
    """Запуск git. Текстовый режим; для списков файлов использовать git_z()."""
    e = dict(os.environ)
    if env:
        e.update(env)
    r = subprocess.run(("git",) + args, cwd=REPO, capture_output=True, text=True,
                       env=e, input=stdin)
    if check and r.returncode != 0:
        raise RuntimeError("git %s -> %s\n%s" % (" ".join(args), r.returncode, (r.stderr or "")[:400]))
    return (r.stdout or "").strip()


def git_z(*args):
    """Список путей через NUL — безопасно для имён с кавычками и пробелами."""
    r = subprocess.run(("git",) + args, cwd=REPO, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("git %s -> %s" % (" ".join(args), r.returncode))
    return [p.decode("utf-8", "surrogateescape") for p in r.stdout.split(b"\0") if p]


def git_remove_paths(paths, env):
    """Убрать пути из индекса через stdin -z (имена с кавычками не ломаются)."""
    if not paths:
        return
    payload = b"".join(p.encode("utf-8", "surrogateescape") + b"\0" for p in paths)
    e = dict(os.environ); e.update(env)
    r = subprocess.run(("git", "update-index", "--force-remove", "-z", "--stdin"),
                       cwd=REPO, capture_output=True, env=e, input=payload)
    if r.returncode != 0:
        raise RuntimeError("update-index: %s" % (r.stderr or b"")[:300])


def classify(tracked):
    """Разложить отслеживаемые файлы на публикуемые и служебные."""
    keep, drop = set(), []
    for line in tracked:
        top = line.split("/")[0]
        if top in KEEP_DIRS or line in KEEP_FILES:
            keep.add(line)
        elif top in DROP_DIRS or line in DROP_FILES or line in DROP_DATA_FILES:
            drop.append(line)
    unexpected = sorted(tracked - keep - set(drop))
    return keep, drop, unexpected


def scan_sensitive(keep, ref=BASE_REF):
    """Проверить публикуемый состав на чувствительное.

    Читает содержимое ИЗ КОММИТА (git show ref:path), а не из рабочего дерева:
    публикуется именно коммит, и проверять надо то, что уйдёт в публичный
    репозиторий. Иначе незакоммиченная правка в рабочем дереве прошла бы
    фильтр, но не попала в срез (или наоборот).
    """
    hits = []
    for line in sorted(keep):
        r = subprocess.run(("git", "show", "%s:%s" % (ref, line)), cwd=REPO,
                           capture_output=True)
        if r.returncode != 0:
            continue
        text = r.stdout.decode("utf-8", "ignore")
        for pat, label in SENSITIVE_PATTERNS:
            m = re.search(pat, text)
            if m:
                hits.append((line, label, m.group(0)[:40]))
    return hits


def main():
    print("Репозиторий: %s" % REPO)
    print("База среза:  %s (%s)" % (git("rev-parse", "--abbrev-ref", "HEAD"),
                                    git("rev-parse", "--short", BASE_REF)))
    print("Режим:       %s" % ("ПУБЛИКАЦИЯ" if APPLY else "сухой прогон"))
    print()

    if git("status", "--porcelain"):
        print("ВНИМАНИЕ: рабочее дерево не чистое — срез берётся от HEAD,")
        print("незакоммиченное в публикацию не попадёт:")
        for line in git("status", "--porcelain").splitlines()[:8]:
            print("  %s" % line)
        print()

    tracked = set(git_z("ls-files", "-z"))
    keep, drop, unexpected = classify(tracked)

    print("Состав:")
    print("  публикуется:          %d файлов" % len(keep))
    print("  убирается служебного: %d" % len(drop))
    if unexpected:
        print("  ВНЕ КЛАССИФИКАЦИИ:    %d — дополнить KEEP_*/DROP_*:" % len(unexpected))
        for u in unexpected[:15]:
            print("      %s" % u)
    print()

    print("Фильтр чувствительного (%d шаблонов):" % len(SENSITIVE_PATTERNS))
    hits = scan_sensitive(keep)
    if hits:
        print("  НАЙДЕНО %d совпадений — публикация заблокирована:" % len(hits))
        for f, label, frag in hits[:20]:
            print("    %-50s %-22s %s" % (f, label, frag))
        print("\nУстраните утечку или уточните состав, затем повторите.")
        return 1
    print("  чисто: 0 совпадений")
    print()

    if not APPLY:
        print("Сухой прогон завершён.")
        print("Публикация: APPLY=1 python3 scripts/publish_wiki.py")
        return 0

    # --- Сборка среза во временном индексе, без переключения ветки ---
    with tempfile.NamedTemporaryFile(prefix="pubidx_", delete=False) as tf:
        idx = tf.name
    try:
        os.unlink(idx)  # git создаст индекс сам
        env = {"GIT_INDEX_FILE": idx}
        # индекс = дерево базового коммита
        git("read-tree", BASE_REF, env=env)
        # убрать служебное из индекса (файлы в рабочем дереве не трогаются)
        git_remove_paths(drop, env)
        tree = git("write-tree", env=env)

        parent = git("rev-parse", BASE_REF)
        msg = "wiki: публикация базы знаний из %s" % git("rev-parse", "--short", BASE_REF)
        commit = git("commit-tree", tree, "-p", parent, "-m", msg)
        print("Срез собран: дерево %s, коммит %s" % (tree[:8], commit[:8]))

        print("Публикация...")
        out = git("push", PUBLIC_REMOTE, "%s:%s" % (commit, PUBLIC_BRANCH), "--force")
        print(out or "  (без вывода)")
    finally:
        if os.path.exists(idx):
            os.unlink(idx)

    print()
    print("Опубликовано: %d файлов" % len(keep))
    print("Сайт: https://lnrgitg.github.io/research-wiki/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
