# Разведка окружения mlcluster JupyterHub: что даёт под gabullinln

Записка 14.10.2026. Точечная проверка вычислительной площадки mlcluster изнутри —
ответ на раздел 7 плана переезда (`shared-context/infra/mlcluster-migration-plan.md`):
persistence, квоты, география выхода наружу, пригодность стека для переноса прогонов.
Все значения получены запуском кода **внутри пода** пользователя, а не из спецификаций.

## Как получен доступ

Прямой веб-вход невозможен: JupyterHub отдаёт только «Sign in with Keycloak»
(локальной формы логин/пароль нет). Рабочий канал — API-токен:

- `GET /hub/api/user` с токеном → 200, модель пользователя: `admin: false`,
  группы `NEW-MODELS`, `ddkp-gu-ep`, scopes `access:servers!server=gabdullinln/`,
  `read:users:activity`, `read:users:groups`, `read:users:name`, `users:activity`.
- `GET /user/gabdullinln/api/status` → 200 (`kernels: 0`, `connections: 0`,
  сервер стартовал 18:48:17Z).
- `DELETE /hub/api/users/gabdullinln/server` → **403: «requires any of [delete:servers]»**,
  `POST …/server` → **403: «requires [servers]»**. То есть токен даёт исполнение кода
  в уже запущенном сервере, но **не управляет жизненным циклом** — перезапуск только
  руками через Hub Control Panel.

Инструменты в репозитории: `scripts/mlcluster_probe.py` (паспорт окружения) и
`scripts/mlcluster_run.py` (выполнить произвольный Python-код в поде через
Jupyter Server API + WebSocket). Токен — в `~/.hermes/.env` как `JUPYTERHUB_TOKEN`,
в вывод и логи не попадает.

## Ресурсы пода

| Параметр | Значение | Источник |
|---|---|---|
| Образ | Ubuntu 24.04.4 LTS, Python 3.13.15, conda/mamba в `/opt/conda` | `cat /etc/os-release`, `sys.version` |
| Память | лимит cgroup **8 589 934 592 Б = 8,0 ГиБ**, занято 192 МБ | `cat /sys/fs/cgroup/memory.max` |
| CPU | `cpu.max = 200000 100000` → **квота 2 ядра**; `os.cpu_count()` = 16 (видимые ядра хоста) | `cat /sys/fs/cgroup/cpu.max` |
| GPU | **NVIDIA A100 80GB PCIe, MIG-инстанс `1g.10gb`** (≈10 ГБ видеопамяти) | `nvidia-smi -L` |
| Домашний диск | `/home/jovyan` — **Longhorn PVC, 4,9 ГБ** (`pvc-83c48e71-…`), занято 436 КБ | `df -h` |
| Корневой диск | overlay 450 ГБ, занято 156, свободно 276 — **эфемерный** | `df -h /` |
| nofiles | 4096 | `ulimit -a` |
| Права | uid 1000 (jovyan), **sudo заблокирован** («no new privileges»), root нет | `id`, `sudo -n true` |

Практический вывод по диску: домашний том — 4,9 ГБ при том, что исходники `raw/` (2,1 ГБ)
и дамп БД (380 МБ) в сумме занимают больше половины; под кэш датасетов в поде почти
не остаётся места. Крупные данные в поде работать не смогут — их место либо в
хранилище контура, либо в самом PostgreSQL.

## Что в стеке есть, а чего нет

В поде **183 пакета**, но из аналитического арсенала нет почти ничего:

- **отсутствуют** `numpy`, `pandas`, `scipy`, `statsmodels`, `linearmodels`, `polars`,
  `duckdb`, `scikit-learn`, `pyarrow`, `openpyxl`, `matplotlib`, `plotly`,
  `xgboost`, `lightgbm`, `torch`, `rpy2`, а также драйверы `psycopg`/`psycopg2`;
- **есть** `requests 2.34.2`, `SQLAlchemy 2.0.52`, `nbformat 5.11.0`, `jupyterlab 4.6.3`,
  `jupyterlab_git 0.54.1`;
- **нет R** (`R` и `Rscript` не найдены), нет `node`, `psql`, `pg_restore`, `tesseract`,
  `latex`/`xelatex`.

Установка возможна: `pip install` отработал (`six 1.17.0` поставлен), PyPI доступен.
Однако писать можно в `/home/jovyan` (PVC), `/tmp` и `/opt/conda` — при этом
`/opt/conda` лежит в **эфемерном** слое контейнера, то есть пакет, поставленный
в site-packages, при пересоздании пода исчезнет. Для повторяемости прогонов
нужен venv **внутри** `/home/jovyan` (или `pip install --user`), а не в conda-базе.

Отсюда прямое следствие для переезда: R-часть вычислений (`midasr`, `fixest` — сейчас
на ВМ) на этой площадке **не воспроизводится без отдельной установки R**, а GPU
(A100 MIG) простаивает, пока не поставлены CUDA-сборки библиотек.

## География выхода наружу — есть, и широкая

Проверено `urllib` из пода (код ответа HTTP):

| Ресурс | Результат | Комментарий |
|---|---|---|
| GitHub | 200 | внешний интернет открыт |
| PyPI | 200 | установка пакетов работает |
| HuggingFace | 200 | |
| google.com | 200 | |
| **ЕМИСС / fedstat.ru** | **200** | ключевой российский источник доступен |
| **cbr.ru** | **200** | |
| rosstat.gov.ru | обычный SSL → ошибка сертификата, **без проверки сертификата → 200** | та же известная проблема цепочки CA, лечится `ssl.CERT_NONE` |
| LiteLLM `litellm.mlcluster.ru/health` | 401 | сервис жив, нужен ключ |
| GitLab `gitlab.mlcluster.ru` | 200 | |
| api.openai.com | 403 | геоблок, как и ожидалось |
| api.anthropic.com | 403 | геоблок |

То есть гипотеза «внутренний контур не видит внешние источники» **не подтвердилась**:
из пода доступны и российские статистические площадки, и GitHub с PyPI. Блокируются
только те же зарубежные LLM-API, что и у нас. Риск из раздела 5 плана можно снимать.

## Внутренняя сеть: чего не видно с VPS

В окружении пода обнаружены адреса сервисов кластера (переменные `JUPYTERHUB_POSTGRESQL_*`):

- `10.96.56.156:5432` — RW-эндпоинт PostgreSQL;
- `10.96.24.71:5432` — R-эндпоинт; `10.96.51.94:5432` — RO-эндпоинт;
- `10.96.32.50:80` — pgAdmin.

Это сервисы служебной БД самого JupyterHub (`jupyterhub-postgresql`), а не наша
`research_wiki`, но факт важнее конкретного имени: **внутренние сервисы кластера
достижимы из пода и недостижимы с VPS** (адреса вида 10.96.x.x — cluster IP). Значит,
работа с БД целей переезда должна идти через под, а не с VPS: публичного DNS у
PostgreSQL mlcluster нет, имена `db`, `postgres`, `pg` не резолвятся. Роль
`scripts/mlcluster_run.py` здесь — не удобство, а единственный технический канал.

## Открытые пункты и следующий шаг

Не проверено по техническим причинам: **persistence не подтверждён эмпирически** —
перезапуск сервера требует scope `delete:servers`, которого у токена нет, а
разрушать сессию без явного согласия владельца не следовало. Косвенные признаки
сильные: `/home/jovyan` — выделенный Longhorn PVC, отдельный от overlay, то есть
по устройству переживает пересоздание пода; но проверить это опытом (маркер в home
до и после restart) можно только после ручного перезапуска через Hub Control Panel
или после выдачи токена с более широкими правами.

Ещё не закрыто: лимиты по CPU/GPU на уровне квот кластера (видно только факт
выделения), срок жизни PVC и политика очистки, срок жизни токенов JupyterHub,
а также хост/порт будущей `research_wiki` в контуре — их по-прежнему нужно
запросить у администраторов.

## Источники

1. Живые ответы API 14.10.2026: `GET /hub/api/user` → 200 (scopes, группы);
   `DELETE/POST /hub/api/users/gabdullinln/server` → 403 с требуемыми scope;
   `GET /user/gabdullinln/api/status` → 200.
2. Прогон `scripts/mlcluster_probe.py` (паспорт: cgroup, GPU, mounts, DNS, outbound)
   — отчёт `/tmp/mlcluster_probe.json`, 14.10.2026.
3. Прогон разведочного кода через `scripts/mlcluster_run.py` (стек, права, запись,
   `pip install`, проверки HTTP-доступности) — `/tmp/deep.out`, 14.10.2026.
4. `shared-context/infra/mlcluster-migration-plan.md`, `shared-context/infra/registry.yaml`
   — состояние проекта переезда.

Связанные материалы: [[jupyterlab-sandbox-vm]] (песочница на прежней ВМ),
[[sandbox-venv-r-python]] (состав окружения ВМ и R-стек),
[[pgadmin-scenarios-20260929]] (доступ к БД v2 через корпоративный pgAdmin).
