#!/bin/bash
# rosstat_industrial_job.sh — выведен из эксплуатации 16.10.2026.
#
# Была цепочка: prom_files_update → sezon_parse → refresh_staging → harmonize_6.
# Пункт 2 аудита убрал staging; 16.10.2026 удалены лендинг rosstat_construction.db
# и гармонайзер 6 — последний шаг, который доводил ряды до канона. Оставшиеся шаги
# писали бы в rosreestr_deals.db, который после удаления гармонайзера никто не
# читает: данные копились бы мимо канона. Поэтому джоб остановлен.
#
# Возврат: тег pre-del-construction-h6 (git), attic/harmonize_6_rosstat_extra.py.bak,
# attic/rosstat_construction_landing_tables.csv.gz.
set -u
echo "rosstat_industrial_job: выведен из эксплуатации 16.10.2026 — шаг к канону удалён" >&2
exit 0
