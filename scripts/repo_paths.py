#!/usr/bin/env python3
"""Определение рабочего репозитория вики — независимо от площадки.

**Зачем.** До 19.09.2026 тринадцать скриптов содержали жёсткий путь
`/home/lnr/research-wiki` (публичное зеркало, к тому же устаревшее после
разделения репозиториев). Пока скрипты запускались только на VPS под
пользователем `lnr`, это сходило с рук. На ВМ YC пользователь `ubuntu`,
главный репозиторий лежит в `~/research-wiki-private`, и такие скрипты
падали с `FileNotFoundError` либо — что опаснее — писали в зеркало, откуда
данные затираются следующим `publish_wiki.py`.

**Правило.** Корень определяется по порядку: переменная `WIKI_REPO` →
`~/research-wiki-private` → `~/research-wiki`. Проверка — наличие каталога
`papers/`, чтобы случайный пустой каталог не был принят за репозиторий.

Использование:

    from repo_paths import REPO, CACHE_DIR
    ...
    with open(os.path.join(REPO, "data", "x.json")) as fh:
        ...

При запуске как скрипта печатает найденный корень — удобно для проверки:

    python3 scripts/repo_paths.py
"""
import os
import sys

_CANDIDATES = [
    os.environ.get("WIKI_REPO"),
    os.path.expanduser("~/research-wiki-private"),
    os.path.expanduser("~/research-wiki"),
]


def find_repo():
    """Корень репозитория вики или None."""
    for p in _CANDIDATES:
        if p and os.path.isdir(os.path.join(p, "papers")):
            return os.path.abspath(p)
    return None


REPO = find_repo()

# Кэш веб-загрузок Hermes: путь тоже зависит от домашнего каталога
# пользователя (~/.hermes/cache/web), поэтому берём из HERMES_HOME, если задан.
HERMES_HOME = os.environ.get("HERMES_HOME") or os.path.expanduser("~/.hermes")
CACHE_DIR = os.path.join(HERMES_HOME, "cache", "web")


def require_repo():
    """Корень репозитория или завершение с понятным сообщением."""
    if REPO is None:
        sys.exit(
            "Не найден репозиторий вики. Задайте WIKI_REPO либо создайте "
            "~/research-wiki-private с каталогом papers/."
        )
    return REPO


if __name__ == "__main__":
    print("REPO      =", REPO or "(не найден)")
    print("CACHE_DIR =", CACHE_DIR,
          "(существует)" if os.path.isdir(CACHE_DIR) else "(нет)")
    print("кандидаты по порядку:")
    for c in _CANDIDATES:
        mark = "  <-- выбран" if c and REPO == os.path.abspath(c) else ""
        print("   ", c or "(пусто)", mark)
