#!/usr/bin/env bash
# Воспроизведение пересчёта H-007 (queries/h007-recheck-20261028.md).
# Вход — CSV задачи-предшественника t_e9cfa6d6; можно переопределить через H007_INPUTS.
# Пример: H007_INPUTS=/path/to/h007_inputs_quarterly.csv bash scripts/h007_recheck/run_all.sh
set -euo pipefail
PY="${PY:-$HOME/.hermes/hermes-agent/venv/bin/python3}"
HERE="$(cd "$(dirname "$0")" && pwd)"
export H007_INPUTS="${H007_INPUTS:-/home/lnr/.hermes/kanban/boards/research/attachments/t_e9cfa6d6/h007_inputs_quarterly.csv}"
export HERMES_KANBAN_WORKSPACE="${HERMES_KANBAN_WORKSPACE:-$(mktemp -d)}"
test -f "$H007_INPUTS" || { echo "нет входного CSV: $H007_INPUTS" >&2; exit 1; }
for f in h007_recheck.py h007_sens.py h007_sens2.py h007_stats.py h007_oos_extra.py; do
  [ -f "$HERE/$f" ] || { echo "нет скрипта: $f" >&2; exit 1; }
  echo "===== $f ====="
  "$PY" "$HERE/$f"
done
echo "артефакты: $HERMES_KANBAN_WORKSPACE"
