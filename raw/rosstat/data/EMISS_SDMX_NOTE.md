

## pandaSDMX установлен (29.08.2026)

pandaSDMX 1.10.0 в venv (+ requests-cache). Назначение: нативный разбор SDMX-ответов ЕМИСС.

Контекст: у fedstat.ru (ЕМИСС) есть SDMX-эндпоинт — POST /indicator/data.do?format=sdmx
(его использует и fedstatAPIr с data_format="sdmx"). Excel-формат проще, но SDMX
структурированнее: pandasdmx.ReadResponse → pandas DataFrame одной строкой.

Источник EMISS зарегистрирован кастомно через pandasdmx.source.add_source
(в комплекте пакета ЕМИСС нет — только IMF, ECB, EUROSTAT, OECD и пр.).

Рабочая связка (оживёт с резидентного IP):
1. fedstatAPIr (R, ~/rlibs) — сборка data_ids с фильтрами → POST → sdmx
2. pandasdmx.read_sdmx(BytesIO(blob), format='str') — парсинг в pandas
3. Либо чистый python-port emiss_client.py (уже в scripts/)

Проверка на VPS ограничена 403 IP-блоком — SDMX-парсер прогнать на живом ответе можно
будет только с резидентного IP (Mac Studio после 22.09.2026).
