# -*- coding: utf-8 -*-
"""Проверка доступности Yandex embeddings API с VPS (эндпоинт как в build_yandex_embeddings.py)."""
import json
import subprocess

KEY = None
for line in open("/home/lnr/.hermes/.env", encoding="utf-8"):
    if line.startswith("YANDEX_CLOUD_API_KEY="):
        KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
assert KEY, "нет ключа"

body = json.dumps({
    "modelUri": "emb://b1gpe14c599s44v5dacm/text-search-doc/latest",
    "text": "проверка доступности API эмбеддингов с VPS во Франкфурте",
}, ensure_ascii=False)

r = subprocess.run(
    ["curl", "-s", "-m", "30", "-X", "POST",
     "https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding",
     "-H", "Authorization: Api-Key " + KEY,
     "-H", "Content-Type: application/json",
     "--data-binary", "@-"],
    input=body, capture_output=True, text=True)

try:
    v = json.loads(r.stdout)
    emb = v.get("embedding", [])
    print("OK, dim:", len(emb), "| keys:", list(v.keys())[:4])
except Exception:
    print("RAW:", r.stdout[:200], "| ERR:", r.stderr[:200])