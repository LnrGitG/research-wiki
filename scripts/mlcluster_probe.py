#!/usr/bin/env python3
"""Разведка окружения mlcluster JupyterHub (шаг 6 переезда, см. infra/mlcluster-migration-plan.md).

Токен читается из окружения JUPYTERHUB_TOKEN или из ~/.hermes/.env (строка JUPYTERHUB_TOKEN=...).
Токен НИКОГДА не печатается.

Уровень A (Hub API): состояние сервера пользователя, активность, признаки квот.
Уровень B (ядро внутри пода через /user/<name>/api): файловая система, cgroup-лимиты,
исходящий интернет, версии стека, достижимость БД и сервисов контура.

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 scripts/mlcluster_probe.py [--json out.json]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

import requests

HUB = "https://jupyterhub.mlcluster.ru"
USER = "gabdullinln"
SERVER = f"{HUB}/user/{USER}"
ENV_FILES = [Path.home() / ".hermes" / ".env", Path.home() / ".env"]
SKIP = {"JUPYTERHUB_TOKEN", "TOKEN"}


def load_token() -> str | None:
    tok = os.environ.get("JUPYTERHUB_TOKEN")
    if tok:
        return tok.strip()
    for f in ENV_FILES:
        if not f.exists():
            continue
        for line in f.read_text(errors="ignore").splitlines():
            line = line.strip()
            if line.startswith("JUPYTERHUB_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def hdr(tok: str) -> dict:
    return {"Authorization": f"token {tok}"}


def get(url: str, tok: str, **kw):
    try:
        r = requests.get(url, headers=hdr(tok), timeout=30, **kw)
        return r.status_code, r.text[:2000]
    except Exception as e:  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


# ---------------------------------------------------------------- уровень A
def tier_a(tok: str, out: dict) -> None:
    A = out["hub_api"] = {}
    code, body = get(f"{HUB}/hub/api/user", tok)
    A["self_user"] = {"code": code, "body": body}
    try:
        A["self_user_json"] = json.loads(body)
    except Exception:  # noqa: BLE001
        pass

    code, body = get(f"{HUB}/hub/api/users/{USER}", tok)
    A["user_admin_view"] = {"code": code, "body": body}

    code, body = get(f"{HUB}/hub/api/user/server", tok)
    A["own_server"] = {"code": code, "body": body}

    code, body = get(f"{SERVER}/api/status", tok)
    A["server_status"] = {"code": code, "body": body}
    if code == 200:
        try:
            A["server_status_json"] = json.loads(body)
        except Exception:  # noqa: BLE001
            pass


# ---------------------------------------------------------------- уровень B
PY_PROBE = r'''
import json, os, platform, shutil, socket, subprocess, sys, urllib.request

res = {}
res["python"] = sys.version.split()[0]
res["user"] = os.environ.get("JUPYTERHUB_USER") or os.environ.get("USER")
res["home"] = os.path.expanduser("~")
res["cwd"] = os.getcwd()
res["hostname"] = socket.gethostname()


def sh(cmd):
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=25)
        return (p.stdout or p.stderr).strip()[:600]
    except Exception as e:
        return f"ERR {type(e).__name__}: {e}"


# persistence: маркер в домашней папке + содержимое
marker = os.path.join(res["home"], "persistence_probe.txt")
try:
    with open(marker, "a") as f:
        f.write("probe\n")
    res["persistence_marker_lines"] = sum(1 for _ in open(marker))
except Exception as e:
    res["persistence_marker_lines"] = f"ERR {e}"
res["home_listing"] = sh("ls -la ~ | head -25")
res["mounts"] = sh("df -h | head -15")

# квоты/ресурсы
res["cgroup_memory_max"] = sh("cat /sys/fs/cgroup/memory.max 2>/dev/null || cat /sys/fs/cgroup/memory/memory.limit_in_bytes 2>/dev/null")
res["cgroup_memory_current"] = sh("cat /sys/fs/cgroup/memory.current 2>/dev/null")
res["cgroup_cpu_max"] = sh("cat /sys/fs/cgroup/cpu.max 2>/dev/null")
res["nproc"] = os.cpu_count()
res["nvidia_smi"] = sh("nvidia-smi -L 2>/dev/null | head -5")
res["ulimit"] = sh("ulimit -a")

# исходящий интернет (что видно из пода)
targets = {
    "github_com": "https://github.com",
    "pypi_org": "https://pypi.org/simple/",
    "rosstat": "https://rosstat.gov.ru",
    "emiss": "https://www.fedstat.ru",
    "gitlab_internal": "https://gitlab.mlcluster.ru",
    "litellm_internal": "https://litellm.mlcluster.ru/health",
    "anthropic": "https://api.anthropic.com",
}
net = {}
for k, u in targets.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "probe"})
        with urllib.request.urlopen(req, timeout=8) as r:
            net[k] = f"{r.status}"
    except Exception as e:
        net[k] = f"ERR {type(e).__name__}: {str(e)[:120]}"
res["outbound"] = net
res["dns"] = {}
for h in ["github.com", "rosstat.gov.ru", "litellm.mlcluster.ru", "db", "postgres", "pg"]:
    try:
        res["dns"][h] = socket.gethostbyname(h)
    except Exception as e:
        res["dns"][h] = f"ERR {type(e).__name__}"

# стек
res["pip"] = sh("pip list --format=freeze 2>/dev/null | wc -l")
res["key_pkgs"] = sh("pip list --format=freeze 2>/dev/null | grep -iE '^(pandas|numpy|statsmodels|linearmodels|scikit-learn|polars|duckdb|psycopg|sqlalchemy|jupyterlab|rpy2)' ")
res["R"] = sh("R --version 2>/dev/null | head -2")
res["du_home"] = sh("du -sh ~ 2>/dev/null")
print("@@PROBE@@" + json.dumps(res, ensure_ascii=False))
'''


async def tier_b(tok: str, out: dict) -> None:
    """Создать ядро в поде пользователя и выполнить разведочный код через WebSocket."""
    import websockets

    B = out["kernel"] = {}
    try:
        r = requests.post(f"{SERVER}/api/kernels", headers=hdr(tok),
                          json={"name": "python3"}, timeout=60)
    except Exception as e:  # noqa: BLE001
        B["error"] = f"create kernel: {type(e).__name__}: {e}"
        return
    B["create_code"] = r.status_code
    if r.status_code not in (200, 201):
        B["create_body"] = r.text[:800]
        return
    kid = r.json()["id"]
    B["kernel_id"] = kid
    B["kernel_name"] = r.json().get("name")
    ws_url = (SERVER + f"/api/kernels/{kid}/channels").replace("https://", "wss://")
    code = PY_PROBE
    try:
        async with websockets.connect(ws_url, additional_headers=hdr(tok),
                                      max_size=2 ** 24, open_timeout=45) as ws:
            await ws.send(json.dumps({
                "header": {"msg_id": f"probe-{int(time.time())}", "username": USER,
                           "session": "probe", "msg_type": "execute_request",
                           "version": "5.3"},
                "parent_header": {}, "metadata": {},
                "content": {"code": code, "silent": False,
                            "store_history": False, "user_expressions": {},
                            "allow_stdin": False, "stop_on_error": True},
                "buffers": [], "channel": "shell"}))
            deadline = time.time() + 240
            while time.time() < deadline:
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=30)
                except asyncio.TimeoutError:
                    continue
                msg = json.loads(raw)
                mt = msg.get("header", {}).get("msg_type")
                if mt == "stream":
                    txt = msg["content"].get("text", "")
                    if "@@PROBE@@" in txt:
                        B["raw"] = txt
                elif mt == "execute_result":
                    data = msg["content"].get("data", {})
                    txt = data.get("text/plain", "")
                    if "@@PROBE@@" in txt:
                        B["raw"] = txt
                elif mt == "error":
                    B["kernel_error"] = msg["content"].get("evalue")
                elif mt == "execute_reply":
                    break
    except Exception as e:  # noqa: BLE001
        B["ws_error"] = f"{type(e).__name__}: {e}"
    if B.get("raw"):
        line = B.pop("raw")
        for chunk in line.splitlines():
            if "@@PROBE@@" in chunk:
                try:
                    B["result"] = json.loads(chunk.split("@@PROBE@@", 1)[1])
                except Exception as e:  # noqa: BLE001
                    B["parse_error"] = str(e)
                break
    try:
        requests.delete(f"{SERVER}/api/kernels/{kid}", headers=hdr(tok), timeout=30)
    except Exception:  # noqa: BLE001
        pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None, help="куда сохранить отчёт")
    ap.add_argument("--skip-kernel", action="store_true")
    ap.add_argument("--restart", action="store_true",
                    help="перезапустить сервер и проверить persistence маркера")
    args = ap.parse_args()

    tok = load_token()
    out: dict = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "hub": HUB, "user": USER}
    if not tok:
        out["error"] = ("JUPYTERHUB_TOKEN не найден: нет ни переменной окружения, "
                        "ни строки в ~/.hermes/.env")
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 2
    out["token_present"] = True

    tier_a(tok, out)
    if not args.skip_kernel:
        asyncio.run(tier_b(tok, out))

    print(json.dumps(out, ensure_ascii=False, indent=2)[:20000])
    if args.json:
        Path(args.json).write_text(json.dumps(out, ensure_ascii=False, indent=2))
        print(f"\n[saved] {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
