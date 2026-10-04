#!/usr/bin/env python3
"""Поиск датасета ключевой ставки в универсальном API Банка России.

API: https://www.cbr.ru/dataservice/ — дерево публикаций, датасеты, меры.
Проверка сертификата отключена (питфолл российских источников).
Без записи в базу: только разведка.
"""
import json
import ssl
import urllib.request

BASE = "https://www.cbr.ru/dataservice"
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=60, context=CTX)
                      .read().decode("utf-8", "ignore"))


def walk(node, depth=0, out=None):
    """Обойти дерево публикаций и собрать узлы с 'ставк' в названии."""
    if out is None:
        out = []
    name = (node.get("name") or node.get("dataset_name") or node.get("title") or "")
    if any(w in name.lower() for w in ("ставк", "key rate", "ключев")):
        out.append({"id": node.get("id"), "name": name, "depth": depth,
                    "keys": sorted(node.keys())[:12]})
    for key in ("children", "items", "datasets", "publications"):
        for ch in (node.get(key) or []):
            walk(ch, depth + 1, out)
    return out


print("=== корень API ===")
try:
    root = get(f"{BASE}/publications")
    print("тип ответа:", type(root).__name__)
    if isinstance(root, list):
        print("узлов верхнего уровня:", len(root))
        for n in root[:15]:
            print("   ", n.get("id"), "|", (n.get("name") or "")[:60])
    elif isinstance(root, dict):
        print("ключи:", sorted(root.keys())[:12])
except Exception as e:
    print("ошибка:", str(e)[:200])

print("\n=== поиск по дереву ===")
try:
    found = walk(root if isinstance(root, (list, dict)) else {})
    if isinstance(root, list):
        found = []
        for n in root:
            walk(n, 0, found)
    for f in found[:20]:
        print(f"   id={f['id']} глубина={f['depth']} | {f['name'][:70]}")
        print(f"      поля: {f['keys']}")
except Exception as e:
    print("ошибка обхода:", str(e)[:200])