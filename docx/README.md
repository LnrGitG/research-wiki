# Word-версии записок

Файлы собраны из markdown-записок каталога `queries/` конвертером pandoc:

```bash
PANDOC=~/.hermes/hermes-agent/venv/lib/python3.11/site-packages/pypandoc/files/pandoc
$PANDOC queries/<файл>.md -o docx/<имя>.docx --from markdown
```

| Файл Word | Источник |
|---|---|
| Прогноз-первичка-реформа-2026.docx | `queries/prognoz-pervichka-reforma-2026-scenarii.md` |
| Дизайн-прогноза-первичка-2026.docx | `queries/dizayn-prognoz-spros-pervichka-reforma-2026.md` |
| Бэктест-2024-и-эластичность.docx | `queries/bektest-dizayna-2024-i-elastichnost-pervichki.md` |
| Микросимуляция-когорт-2026.docx | `queries/mikrosimulyatsiya-kogort-reforma-2026.md` |
| Эффект-предвосхищения-2026.docx | `queries/effekt-predvoskhishcheniya-reforma-2026.md` |

Markdown остаётся источником правды: правки вносятся в `queries/*.md`, после чего
документ пересобирается командой выше. Word-версии — производные артефакты.