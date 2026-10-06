#!/usr/bin/env python3
"""Сбор данных trudvsem.ru (Работа в России) — резюме и средняя ЗП по регионам."""
import urllib.request, ssl, hashlib
import xml.etree.ElementTree as ET
import sys, os
sys.path.insert(0, os.path.expanduser("~/research-wiki-private/scripts"))
from db_tunnel import query, execute

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

SOURCE_ID = 31  # trudvsem


def normalize(name):
    """Нормализация названия региона для сравнения."""
    n = name.lower().strip()
    # Убираем типовые слова
    for word in ["республика", "область", "край", "автономный округ", "автономная область",
                 "город", "республика(", "народная республика"]:
        n = n.replace(word, "")
    n = n.replace("ё", "е").strip()
    # Разбиваем на слова и берём ключевое
    words = [w for w in n.split() if len(w) > 2]
    return words

def match_region(trudvsem_name, db_regions):
    """Найти region_id по названию trudvsem."""
    tv_words = set(normalize(trudvsem_name))
    if not tv_words:
        return None
    best_match = None
    best_score = 0
    for rid, db_name in db_regions:
        db_words = set(normalize(db_name))
        if not db_words:
            continue
        # Пересечение слов
        common = tv_words & db_words
        score = len(common) / max(len(tv_words), len(db_words))
        if score > best_score:
            best_score = score
            best_match = rid
    if best_score >= 0.3:
        return best_match
    return None

def main():
    # Проверить метрики
    metrics = {}
    for code in ["trudvsem_resumes_count_w", "trudvsem_avg_wage_w", "trudvsem_companies_count_w"]:
        r = query(f"SELECT metric_id FROM catalog.metric WHERE metric_code='{code}'")
        if r:
            metrics[code] = r[0][0]
            print(f"{code}: metric_id={r[0][0]}")
        else:
            print(f"{code}: NOT FOUND — creating")
            unit_id = 29 if "count" in code else 38
            execute(f"""INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id, frequency_id, status, is_active)
                VALUES ('{code}', 'trudvsem {code}', {unit_id}, {SOURCE_ID}, 15, 'active', true)
                ON CONFLICT (metric_code) DO NOTHING""")
            r = query(f"SELECT metric_id FROM catalog.metric WHERE metric_code='{code}'")
            metrics[code] = r[0][0]
            print(f"  created: metric_id={r[0][0]}")

    # Регионы
    regions_db = query("SELECT region_id, name_ru, oktmo FROM catalog.region WHERE is_active = true")
    print(f"Regions in DB: {len(regions_db)}")

    # Получить список версий stat-citizens
    meta_url = "https://opendata.trudvsem.ru/7710538364-stat-citizens"
    req = urllib.request.Request(meta_url, headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req, context=ctx, timeout=15)
    meta_data = resp.read().decode("utf-8")
    meta_root = ET.fromstring(meta_data)

    versions = []
    for dv in meta_root.findall(".//dataversion"):
        src = dv.find("source")
        created = dv.find("created")
        if src is not None:
            versions.append({"url": src.text, "created": created.text if created is not None else ""})

    print(f"stat-citizens versions: {len(versions)}")

    # Загрузить последние 5 версий
    for v in versions[-5:]:
        try:
            req = urllib.request.Request(v["url"], headers={"User-Agent": "Mozilla/5.0"})
            resp = urllib.request.urlopen(req, context=ctx, timeout=20)
            data = resp.read().decode("utf-8")
            root = ET.fromstring(data)

            date_str = v["created"][:8]
            period_start = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
            content_hash = hashlib.sha256(data.encode()).hexdigest()[:16]

            # Создать release
            execute(f"""INSERT INTO catalog.release (source_id, label, content_hash, status, ingested_at)
                VALUES ({SOURCE_ID}, 'trudvsem-stat-citizens-{v["created"]}', '{content_hash}', 'active', now())
                ON CONFLICT DO NOTHING""")
            rel = query(f"SELECT release_id FROM catalog.release WHERE content_hash='{content_hash}' AND source_id={SOURCE_ID}")
            release_id = rel[0][0] if rel else None

            obs_count = 0
            for reg in root.findall(".//region"):
                code_elem = reg.find("code")
                name_elem = reg.find("name")
                if code_elem is None:
                    continue
                stats = reg.find("statistics")
                if stats is None:
                    continue

                reg_code = code_elem.text
                reg_name = name_elem.text if name_elem is not None else ""
                if reg_code == "RUS":
                    rid = 1
                else:
                    rid = match_region(reg_name, [(r[0], r[1]) for r in regions_db])
                    if rid is None:
                        continue

                for stat in stats.findall("statistic"):
                    stat_name = stat.find("name")
                    stat_value = stat.find("value")
                    if stat_name is None or stat_value is None:
                        continue

                    if "количество" in stat_name.text.lower() and "резюме" in stat_name.text.lower():
                        mid = metrics["trudvsem_resumes_count_w"]
                        try:
                            val = int(stat_value.text)
                        except ValueError:
                            continue
                    elif "заработн" in stat_name.text.lower():
                        mid = metrics["trudvsem_avg_wage_w"]
                        try:
                            val = float(stat_value.text)
                        except ValueError:
                            continue
                    else:
                        continue

                    execute(f"""INSERT INTO data.observation
                        (metric_id, region_id, period_start, period_end, value, source_id, release_id, observation_status, assessment_type)
                        VALUES ({mid}, {rid}, '{period_start}', '{period_start}', {val}, {SOURCE_ID}, {release_id}, 'validated', 'final')
                        ON CONFLICT DO NOTHING""")
                    obs_count += 1

            print(f"  {v['created']}: {obs_count} obs, release_id={release_id}")
        except Exception as e:
            print(f"  {v['created']}: FAIL {e}")

    # Верификация
    total = query(f"SELECT count(*) FROM data.observation WHERE source_id={SOURCE_ID}")
    print(f"\nTotal trudvsem observations: {total[0][0]}")

    # КТ: средняя ЗП по РФ vs Росстат
    rus_wage = query(f"""SELECT value, period_start FROM data.observation
        WHERE metric_id={metrics['trudvsem_avg_wage_w']} AND region_id=1
        ORDER BY period_start DESC LIMIT 1""")
    if rus_wage:
        print(f"КТ: trudvsem средняя ЗП РФ = {rus_wage[0][0]} руб. ({rus_wage[0][1]})")
    rosstat_wage = query("""SELECT o.value, o.period_start FROM data.observation o
        JOIN catalog.metric m ON o.metric_id = m.metric_id
        WHERE m.metric_code='emiss_57824_wage_m' AND o.region_id=1
        ORDER BY o.period_start DESC LIMIT 1""")
    if rosstat_wage:
        print(f"КТ: Росстат среднемесячная ЗП = {rosstat_wage[0][0]} руб. ({rosstat_wage[0][1]})")

if __name__ == "__main__":
    main()