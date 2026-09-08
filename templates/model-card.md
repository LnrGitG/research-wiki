# Шаблон карточки модели

> Копировать при создании `models/<model-class>/<slug>.md`.
> Имя файла: lowercase, hyphens, например `models/nowcasting/midas-wordstat-smr.md`.

```markdown
---
title: Название модели
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: model
model_class: DSGE | BVAR | FAVAR | MIDAS | U-MIDAS | RF/ML | survival
status: draft | estimated | production | archived
hypotheses: [H-XXX]          # связка с hypotheses.yaml
tags: [from taxonomy]
sources: [data inputs, papers]
confidence: high | medium | low
---

# Название модели

## Назначение
Что моделирует, для какой гипотезы (relates_to из hypotheses.yaml), горизонт и целевая переменная.

## Спецификация
- Переменные и частоты (для mixed-frequency: список блоков и лагов)
- Идентификация: ограничения, инструменты (LaTeX при необходимости: $y_t = ...$)
- Априорные распределения / калибровка (если BVAR/DSGE)

## Код и данные
- Код: путь в scripts/ или URL репозитория
- Данные: файлы в data/ или research-data (path + диапазон)
- Воспроизводимость: команда запуска, версия окружения

## Результаты
- Ключевые оценки (с числами и датой прогона)
- Графики: ссылки на assets или таблицы
- Валидация: бенчмарк, RMSE/MAE, out-of-sample

## Обновление
- next_check: что перекатить на новые данные (синхронно с гипотезой)
- Владелец: @user
```

## Правила
1. Карточка обязана ссылаться хотя бы на одну запись hypotheses.yaml (поле `hypotheses:`) — иначе модель осиротела.
2. Код, которого нет — не обещать: писать `status: draft` и путь planned.
3. Результаты — только с датой прогона; устаревшие значения не удалять, а дополнять прогоном от новой даты.