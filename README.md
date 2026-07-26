# 🏠 Research Wiki — Экономика жилья, ипотека, недвижимость

База знаний по экономике жилищного рынка: научные статьи, концепты, аналитические записки. Формат — Obsidian-совместимый markdown, синхронизация через Git (чтение с телефона).

📖 **Точка входа:** [index.md](index.md) | 📐 **Схема данных:** [SCHEMA.md](SCHEMA.md) | 📝 **Журнал работы:** [log.md](log.md)

---

## 📂 Структура репозитория

```
research-wiki/
├── index.md                  # Главная страница, навигация по wiki
├── SCHEMA.md                 # Схема организации знаний (типы страниц, теги)
├── log.md                    # Журнал изменений и история работы
│
├── papers/                   # 📄 Статьи в markdown (105 файлов)
│   │                         # Конвертировано из PDF через pymupdf4llm
│   ├── Yildirim-2025-...md   #   — Турция, Bayesian SVAR цены жилья
│   ├── Suh-2023-...md        #   — Корея, региональные жилищные циклы
│   ├── Bernanke-2003-...md   #   — FAVAR (классика)
│   └── ...                   #   FAVAR/BVAR, прогнозирование цен,
│                             #   монетарная политика → жильё, nowcasting
│
├── concepts/                 # 💡 Концепт-страницы (14 файлов)
│   │                         # Обобщение методов и теорий со ссылками на статьи
│   ├── econometric-models-housing-market.md  # 17 методов: FAVAR, DFM,
│   │                         #   ECM, DSGE, spatial, ML, nowcasting, GaR...
│   ├── transmisionnyi-mehanizm-dkp-zhile.md  # Трансмиссия ДКП → жильё
│   ├── regionalnaya-differenciaciya.md       # Региональные различия
│   ├── macroprudentialnaya-politika-rynok-zhilya.md
│   └── ...
│
├── queries/                  # 🔍 Аналитические записки (5 файлов)
│   │                         # Ответы на исследовательские вопросы
│   ├── monetarnaya-politika-i-rynok-zhilya-kompleksnaya-bibliografiya.md
│   ├── sintez-monetarnaya-politika-i-rynok-zhilya.md
│   └── ...
│
├── entities/                 # 🏛️ Сущности (2 файла)
│   ├── bank-rossii.md        # Банк России
│   └── lgotnaya-ipoteka.md   # Льготная ипотека
│
├── comparisons/              # ⚖️ Сравнительные таблицы (1 файл)
│
├── raw/                      # 🗄️ Исходники (не в git, см. .gitignore)
│   ├── papers/               #   PDF-бинарники статей (~250 файлов)
│   ├── articles/             #   Сырые тексты статей
│   ├── assets/               #   Изображения, графики
│   └── transcripts/          #   Расшифровки (видео, лекции)
│
├── scripts/                  # 🛠️ Скрипты обработки (конвертация PDF → MD)
├── templates/                # 📋 Шаблоны страниц (concept.md и др.)
└── _archive/                 # 📦 Архив устаревших материалов (не в git)
```

## 📊 Содержание коллекции papers/

| Тематический кластер | Примеры |
|---|---|
| 🏠 Прогнозирование цен на жильё | Rapach, Gupta, Das, Plakandaras, Bork, Mattera |
| 💰 Монетарная политика → жильё | Eickmeier, Jarocinski, Negro, Fischer, Nsafoah |
| 📊 FAVAR/BVAR методология | Bernanke 2003, Eickmeier 2011, Lin, Mumtaz, Paccagnini |
| 🌍 Международная трансмиссия | Bandt, Hirata, Corsetti, Cepni |
| 🇷🇺 Российские работы | Zubarev (наукастинг MFBVAR), Garmider (FAVAR РФ), Стерник |
| 🏦 Центробанки | Angelini 2025 (ECB), Soares, Dees, RBNZ |
| 🤖 ML-подходы | Qiongwei-Ye 2024, Hao, Rogoff-Yang 2026 (LLM sentiment) |

## 🔄 Рабочий процесс

1. **PDF** → `raw/papers/` (scp/Яндекс.Диск, не попадает в git)
2. **Конвертация** → `papers/*.md` (pymupdf4llm, frontmatter + title)
3. **Концепты** → обобщение в `concepts/` со ссылками на статьи
4. **Записки** → синтез в `queries/`
5. **Git push** → чтение на телефоне через Obsidian

## ⚙️ Технические детали

- **`.gitignore`**: PDF-бинарники (`*.pdf`), `_archive/`, workspace-файлы Obsidian — исключены, чтобы репозиторий не раздувался для мобильной синхронизации
- **Конвенция имён**: `Автор-Год-Краткое-название.md`
- **Frontmatter**: YAML-заголовок с `title`, `type`, `created`/`updated`, `tags`
- **Репозиторий приватный** — доступ по GitHub token
