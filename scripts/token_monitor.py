#!/usr/bin/env python3
"""Token context monitor for Hermes Agent.

Reads state.db + hermes prompt-size to give a full picture of:
- Static context breakdown (system prompt, skills, tools, memory, profile)
- Per-session token usage and cache efficiency
- Per-model cumulative costs
- Memory budget tracking with fill forecast
- Context effectiveness (output/input ratio)

Usage:
    python3 token_monitor.py [--days 7] [--limit 20] [--json]
"""
import argparse
import json
import sqlite3
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERMES_HOME = Path.home() / ".hermes"
STATE_DB = HERMES_HOME / "state.db"
MEMORY_FILE = HERMES_HOME / "memories" / "MEMORY.md"
USER_FILE = HERMES_HOME / "memories" / "USER.md"


def get_prompt_size():
    """Run hermes prompt-size --json and return parsed result."""
    try:
        result = subprocess.run(
            ["hermes", "prompt-size", "--json"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        pass
    return None


def get_db_stats(days=7, limit=20):
    """Read token stats from state.db."""
    db = sqlite3.connect(str(STATE_DB))
    cur = db.cursor()

    since = (datetime.now(timezone.utc) - timedelta(days=days)).timestamp()

    # Per-session stats
    cur.execute("""
        SELECT id, model, input_tokens, output_tokens, cache_read_tokens,
               cache_write_tokens, reasoning_tokens, api_call_count,
               estimated_cost_usd, message_count, tool_call_count,
               billing_provider, started_at, last_activity_at
        FROM sessions
        WHERE last_activity_at > ?
        ORDER BY last_activity_at DESC
        LIMIT ?
    """, (since, limit))
    sessions = cur.fetchall()

    # Per-model aggregated
    cur.execute("""
        SELECT model, billing_provider,
               SUM(api_call_count), SUM(input_tokens), SUM(output_tokens),
               SUM(cache_read_tokens), SUM(cache_write_tokens),
               SUM(reasoning_tokens), SUM(estimated_cost_usd),
               COUNT(DISTINCT session_id)
        FROM session_model_usage
        WHERE last_seen > ?
        GROUP BY model, billing_provider
        ORDER BY SUM(input_tokens) DESC
    """, (since,))
    model_usage = cur.fetchall()

    # Total counts
    cur.execute("""
        SELECT SUM(input_tokens), SUM(output_tokens), SUM(cache_read_tokens),
               SUM(api_call_count), COUNT(*)
        FROM sessions WHERE last_activity_at > ?
    """, (since,))
    totals = cur.fetchone()

    # System prompt sizes
    cur.execute("SELECT hash, LENGTH(prompt) FROM system_prompts ORDER BY LENGTH(prompt) DESC LIMIT 10")
    system_prompts = cur.fetchall()

    db.close()
    return sessions, model_usage, totals, system_prompts


def format_tokens(n):
    """Format token count compactly."""
    if n is None or n == 0:
        return "0"
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)


def format_cost(n):
    """Format USD cost."""
    if n is None:
        return "—"
    if n < 0.01:
        return f"${n:.4f}"
    return f"${n:.2f}"


def print_report(days, limit, as_json=False):
    """Main report."""
    prompt = get_prompt_size()
    sessions, model_usage, totals, sys_prompts = get_db_stats(days, limit)

    # Memory files
    mem_size = MEMORY_FILE.stat().st_size if MEMORY_FILE.exists() else 0
    usr_size = USER_FILE.stat().st_size if USER_FILE.exists() else 0

    if as_json:
        report = {
            "prompt_size": prompt,
            "totals": {
                "input_tokens": totals[0],
                "output_tokens": totals[1],
                "cache_read_tokens": totals[2],
                "api_calls": totals[3],
                "sessions": totals[4],
            },
            "memory_bytes": mem_size,
            "user_profile_bytes": usr_size,
            "model_usage": [
                {
                    "model": m[0], "provider": m[1], "calls": m[2],
                    "input": m[3], "output": m[4], "cache_read": m[5],
                    "cost_usd": m[8], "sessions": m[9]
                } for m in model_usage
            ]
        }
        print(json.dumps(report, indent=2))
        return

    # === Header ===
    print("╔══════════════════════════════════════════════════════════╗")
    print("║              📊 Hermes Token Context Monitor            ║")
    print(f"║              Last {days} days · {limit} sessions max              ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()

    # === 1. Static Context Breakdown ===
    if prompt:
        print("📦 STATIC CONTEXT (prompt-size)")
        print("─" * 56)
        sp = prompt.get("system_prompt", {})
        sk = prompt.get("skills_index", {})
        mm = prompt.get("memory", {})
        up = prompt.get("user_profile", {})
        tl = prompt.get("tools", {})

        print(f"  System prompt:      {sp.get('chars', 0):>8,} chars  {sp.get('bytes', 0):>8,} bytes")
        print(f"  Skills index:       {sk.get('chars', 0):>8,} chars  {sk.get('bytes', 0):>8,} bytes")
        print(f"  Memory:             {mm.get('chars', 0):>8,} chars  {mm.get('bytes', 0):>8,} bytes")
        print(f"  User profile:       {up.get('chars', 0):>8,} chars  {up.get('bytes', 0):>8,} bytes")
        print(f"  Tool schemas ({tl.get('count', '?')}): {tl.get('json_bytes', 0):>8,} bytes")

        total_chars = sp.get("chars", 0) + sk.get("chars", 0) + mm.get("chars", 0) + up.get("chars", 0)
        total_bytes = sp.get("bytes", 0) + sk.get("bytes", 0) + mm.get("bytes", 0) + up.get("bytes", 0) + tl.get("json_bytes", 0)
        est_tokens = total_bytes // 4  # rough: 4 bytes per token for mixed content
        print(f"  ────────────────────────────────────────")
        print(f"  Total:              {total_chars:>8,} chars  {total_bytes:>8,} bytes  ~{format_tokens(est_tokens)} tokens")

        # Sections for caching
        sections = prompt.get("sections", [])
        if sections:
            print()
            print("  Caching sections:")
            for name, chars, bts in sections:
                print(f"    {name:<40} {chars:>6,} chars  {bts:>8,} bytes")

        # Top skills by weight
        skills = prompt.get("skills_breakdown", [])
        if skills:
            top_skills = sorted(skills, key=lambda s: s.get("skill_md_bytes", 0), reverse=True)[:8]
            print()
            print("  🏋️ Top 8 skills by SKILL.md weight:")
            for s in top_skills:
                print(f"    {s['name']:<35} {s['skill_md_bytes']:>6,} bytes")

        # Toolsets breakdown
        toolsets = prompt.get("toolsets_breakdown", [])
        if toolsets:
            print()
            print("  🔧 Tool schemas by toolset:")
            for ts in toolsets:
                print(f"    {ts['toolset']:<20} {ts['tool_count']:>2} tools  {ts['json_bytes']:>6,} bytes")
    else:
        print("  ⚠️  prompt-size unavailable (hermes CLI not found or errored)")

    # === 2. Aggregated Stats ===
    print()
    print("📈 TOKEN USAGE SUMMARY")
    print("─" * 56)
    total_in = totals[0] or 0
    total_out = totals[1] or 0
    total_cache = totals[2] or 0
    total_calls = totals[3] or 0
    total_sessions = totals[4] or 0

    cache_pct = (total_cache / total_in * 100) if total_in > 0 else 0
    effectiveness = (total_out / total_in * 100) if total_in > 0 else 0

    print(f"  Sessions:           {total_sessions}")
    print(f"  Input tokens:       {format_tokens(total_in)}")
    print(f"  Output tokens:      {format_tokens(total_out)}")
    print(f"  Cache read:         {format_tokens(total_cache)}  ({cache_pct:.1f}% of input)")
    print(f"  API calls:          {total_calls:,}")
    print(f"  Effectiveness:      {effectiveness:.1f}% output/input ratio")

    # === 3. Per-Model ===
    print()
    print("🤖 PER-MODEL USAGE")
    print("─" * 56)
    print(f"  {'Model':<35} {'Calls':>7} {'Input':>8} {'Output':>8} {'Cache%':>7} {'Cost':>8}")
    for m in model_usage[:15]:
        model, provider = m[0], m[1]
        calls = m[2] or 0
        inp = m[3] or 0
        out = m[4] or 0
        cr = m[5] or 0
        cost = m[8] or 0
        cpct = (cr / inp * 100) if inp > 0 else 0
        print(f"  {model:<35} {calls:>7,} {format_tokens(inp):>8} {format_tokens(out):>8} {cpct:>6.1f}% {format_cost(cost):>8}")

    # === 4. Memory Budget ===
    print()
    print("🧠 MEMORY BUDGET")
    print("─" * 56)
    mem_limit = 5000
    mem_rendered = prompt.get("memory", {}).get("chars", 0) if prompt else mem_size
    mem_pct = mem_rendered / mem_limit * 100
    remaining = mem_limit - mem_rendered
    # Estimate days until full (based on last 7 days growth)
    print(f"  Memory:       {mem_rendered:>5,} / {mem_limit:,} chars  ({mem_pct:.0f}%)  — {remaining:,} remaining")
    print(f"  User profile: {usr_size:>5,} / 2,500 chars")

    if prompt:
        mem_bytes = prompt.get("memory", {}).get("bytes", 0)
        print(f"  Memory bytes: {mem_bytes:,}  (UTF-8 on disk: {mem_size:,})")

    # === 5. System Prompt Variants ===
    if sys_prompts:
        print()
        print("📜 SYSTEM PROMPT VARIANTS (top 10 by size)")
        print("─" * 56)
        for h, length in sys_prompts:
            print(f"  {h[:24]}...  {length:>6,} chars")

    # === 6. Recent Sessions ===
    print()
    print(f"📋 RECENT SESSIONS (last {min(limit, len(sessions))})")
    print("─" * 56)
    print(f"  {'Model':<30} {'In':>8} {'Out':>7} {'Cache%':>7} {'Calls':>6} {'Msgs':>5}")
    for s in sessions[:15]:
        model = (s[1] or "?")[:29]
        inp = s[2] or 0
        out = s[3] or 0
        cr = s[4] or 0
        calls = s[7] or 0
        msgs = s[10] or 0
        cpct = (cr / inp * 100) if inp > 0 else 0
        print(f"  {model:<30} {format_tokens(inp):>8} {format_tokens(out):>7} {cpct:>6.1f}% {calls:>5} {msgs:>5}")


def main():
    parser = argparse.ArgumentParser(description="Hermes token context monitor")
    parser.add_argument("--days", type=int, default=7, help="Lookback period")
    parser.add_argument("--limit", type=int, default=20, help="Max sessions to show")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()
    print_report(args.days, args.limit, args.json)


if __name__ == "__main__":
    main()