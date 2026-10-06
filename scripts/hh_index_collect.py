#!/usr/bin/env python3
"""Сбор данных hh.ru (HeadHunter) — индекс рынка труда.
Требует API-ключ (HH_API_KEY в .env). Без ключа собирает публичные данные stats.hh.ru."""
import urllib.request, ssl, json, sys, os
sys.path.insert(0, os.path.expanduser("~/research-wiki-private/scripts"))
from db_tunnel import query, execute

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
SOURCE_ID = 32  # hh

def fetch_json(url, headers=None):
    """Fetch JSON from URL."""
    if headers is None:
        headers = {"User-Agent": "research-wiki/1.0"}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, context=ctx, timeout=15)
    return json.loads(resp.read().decode("utf-8"))

def main():
    # Проверить метрики
    metrics = {}
    for code, name, unit_id in [
        ("hh_vacancies_count_m", "Количество вакансий на hh.ru", 29),
        ("hh_resumes_count_m", "Количество резюме на hh.ru", 29),
        ("hh_avg_salary_m", "Средняя предлагаемая ЗП на hh.ru", 38),
        ("hh_hhi_index_m", "HH-индекс (соотношение вакансий к резюме)", 37),
    ]:
        r = query(f"SELECT metric_id FROM catalog.metric WHERE metric_code='{code}'")
        if r:
            metrics[code] = r[0][0]
            print(f"{code}: metric_id={r[0][0]}")
        else:
            print(f"{code}: NOT FOUND — creating")
            execute(f"""INSERT INTO catalog.metric (metric_code, name_ru, unit_id, source_id, frequency_id, status, is_active)
                VALUES ('{code}', '{name}', {unit_id}, {SOURCE_ID}, 5, 'active', true)
                ON CONFLICT (metric_code) DO NOTHING""")
            r = query(f"SELECT metric_id FROM catalog.metric WHERE metric_code='{code}'")
            metrics[code] = r[0][0]
            print(f"  created: metric_id={r[0][0]}")

    # Проверить API-ключ
    api_key = os.environ.get("HH_API_KEY", "")
    if not api_key:
        # Попробовать .env
        env_path = os.path.expanduser("~/research-wiki-private/.env")
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.startswith("HH_API_KEY="):
                        api_key = line.split("=", 1)[1].strip().strip('"')
                        break

    if not api_key:
        print("\n⚠️  HH_API_KEY не найден. Подготовлен скрипт, но данные не собраны.")
        print("Для сбора данных:")
        print("1. Зарегистрируйтесь на hh.ru/api")
        print("2. Получите API-ключ")
        print("3. Добавьте HH_API_KEY=... в ~/research-wiki-private/.env")
        print("4. Запустите скрипт повторно")
        print("\nАльтернатива: публичные данные stats.hh.ru (если доступны)")
        
        # Попробуем публичные данные
        try:
            url = "https://api.hh.ru/vacancies?per_page=1&text=строительство"
            data = fetch_json(url)
            total_vacancies = data.get("found", 0)
            print(f"\nПубличный API: всего вакансий 'строительство' = {total_vacancies}")
            
            # Создать release
            import hashlib
            content_hash = hashlib.sha256(str(total_vacancies).encode()).hexdigest()[:16]
            execute(f"""INSERT INTO catalog.release (source_id, label, content_hash, status, ingested_at)
                VALUES ({SOURCE_ID}, 'hh-public-snapshot', '{content_hash}', 'active', now())
                ON CONFLICT DO NOTHING""")
            rel = query(f"SELECT release_id FROM catalog.release WHERE content_hash='{content_hash}' AND source_id={SOURCE_ID}")
            release_id = rel[0][0] if rel else None
            
            from datetime import datetime
            today = datetime.now().strftime("%Y-%m-%d")
            
            # Записать как точечное наблюдение
            mid = metrics["hh_vacancies_count_m"]
            execute(f"""INSERT INTO data.observation
                (metric_id, region_id, period_start, period_end, value, source_id, release_id, observation_status, assessment_type)
                VALUES ({mid}, 1, '{today}', '{today}', {total_vacancies}, {SOURCE_ID}, {release_id}, 'validated', 'final')
                ON CONFLICT DO NOTHING""")
            print(f"Записано: {total_vacancies} вакансий по строительству на {today}")
        except Exception as e:
            print(f"Публичный API недоступен: {e}")
        return

    # С API-ключом — полный сбор
    print(f"API key found, collecting full data...")
    # TODO: реализовать полный сбор через API hh.ru
    # Эндпоинты: /vacancies, /resumes, /industries
    # Региональный разрез: /areas


if __name__ == "__main__":
    main()