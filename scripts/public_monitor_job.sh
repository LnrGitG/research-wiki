#!/bin/bash
# Публичный монитор жилья: снапшот из PostgreSQL -> GitHub Pages.
# Cron (05:00 МСК = 02:00 UTC). Ручной запуск безопасен: без изменений
# ничего не коммитится и не публикуется.
#
# Публикуем в отдельный служебный клон ~/research-wiki-publish, а не через
# publish_wiki.py: тот делает force-push всего дерева и, во-первых, падает на
# фильтре чувствительного (IP в log.md), во-вторых, затирал бы коммиты
# соседнего джоба monitor: snapshot, который пишет в тот же репозиторий.
set -euo pipefail

REPO="/home/lnr/research-wiki-private"
PUB="/home/lnr/research-wiki-publish"
PUB_URL="https://github.com/LnrGitG/research-wiki.git"
PY="/home/lnr/.hermes/hermes-agent/venv/bin/python3"
cd "$REPO"

echo "[1/5] сборка среза"
"$PY" scripts/build_public_monitor.py

echo "[2/5] проверка контракта витрины"
"$PY" scripts/check_public_monitor.py

echo "[3/5] коммит в приватный репозиторий"
git add docs/public-monitor.json docs/public-monitor.html scripts/build_public_monitor.py scripts/check_public_monitor.py
if git diff --cached --quiet; then
  echo "  данных нет изменений — публикация не нужна"
  PRIVATE_CHANGED=0
else
  git commit -q -m "Публичный монитор: автообновление среза $(date -u +%Y-%m-%d)"
  git push private main
  PRIVATE_CHANGED=1
  echo "  приватный обновлён"
fi

echo "[4/5] синхронизация служебного клона"
if [ ! -d "$PUB/.git" ]; then
  git clone -q "$PUB_URL" "$PUB"
fi
cd "$PUB"
git fetch -q origin
git reset -q --hard origin/main
cp "$REPO/docs/public-monitor.html" "$REPO/docs/public-monitor.json" docs/

# ссылка на витрину в оглавлении публичного сайта (идемпотентно)
"$PY" - <<'PY'
import re
p = '/home/lnr/research-wiki-publish/docs/index.html'
h = open(p, encoding='utf-8').read()
if 'public-monitor.html' in h:
    print('  ссылка уже есть')
else:
    anchor = re.search(r'<a href="metrics-catalog\.html"[^>]*>.*?</a>', h)
    if not anchor:
        print('  ВНИМАНИЕ: якорь каталога метрик не найден, ссылку не добавил')
    else:
        link = ('\n<a href="public-monitor.html" style="display:inline-block;padding:10px 24px;'
                'background:#1a1d29;border:1px solid #2a2d3a;border-radius:8px;color:#4fc3f7;'
                'font-size:0.9rem;text-decoration:none">📈 Публичный монитор</a>')
        h = h[:anchor.end()] + link + h[anchor.end():]
        open(p, 'w', encoding='utf-8').write(h)
        print('  ссылка добавлена')
PY

echo "[5/5] публикация"
if git diff --quiet && git diff --cached --quiet && [ "${PRIVATE_CHANGED}" = "0" ]; then
  echo "  публичный репозиторий без изменений"
  exit 0
fi
git add docs/public-monitor.html docs/public-monitor.json docs/index.html
git commit -q -m "Публичный монитор: срез $(date -u +%Y-%m-%dT%H:%MZ)"
git push origin main
echo "готово: https://lnrgitg.github.io/research-wiki/public-monitor.html"
