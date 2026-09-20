# Реестр спецификаций — конвенция

Формат: YAML + JSON Schema `schema.json` (рядом). Каждый файл — одна спецификация.

## Поля
- `name`: slug, уникален (nowcast-s6a, panel-fe-elasticity, ...)
- `version`: int, инкремент при правках
- `kind`: model | slice | filter
- `model`: ols | fe | re | midas | bridge | midasml | ardl
- `metrics`: список metric_id или metric_code из core.metric
- `filters`: {frequency, region_id, sub_dimension, period_start/end, release: final|first}
- `lags`: {high: N, low: N} — для mixed-frequency
- `oos`: {start, end} — окно out-of-sample
- `target`: зависимая переменная (например, yoy СМР)

## Прогон
- Результаты: derived.spec_runs (params, rmse/mae/r2, статус)
- Репорты: notebooks/reports/<name>-v<N>.qmd → quarto render
- Прогон создаёт строку в spec_runs c params=весь YAML

## Интерфейсы запуска
1. Telegram-кнопки (утверждение предложений) — agent пишет spec в файл и запускает
2. ipywidgets-формы в JupyterLab (свободная разведка) — spec_form.ipynb
3. CLI: `python3 scripts/spec_cli.py run <name> --grid lags=1..6`

## Пример
```yaml
name: nowcast-s6a
version: 1
kind: model
model: bridge
target: {metric_code: smr_yoy, frequency: m}
features:
  - {metric_code: escrow_vol_m, lags: [1,2]}
  - {metric_code: ddu_count_m, lags: [1]}
sample: {start: 2016-01, end: 2025-12}
oos: {start: 2024-01}
```