#!/usr/bin/env python3
"""
Verification script for academic paper translations.
Usage: python verify_translation.py <input.md> [backup.md]
Checks: Cyrillic ratio, garbled text, control chars, no weather-artifacts,
        no placeholders, terms preserved, tables/footnotes intact.
import re
import sys
import os
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <translated.md> [backup.md]", file=sys.stderr)
    sys.exit(1)
INPUT = sys.argv[1]
BACKUP = sys.argv[2] if len(sys.argv) > 2 else None
errors = []
warnings = []
with open(INPUT, 'r', encoding='utf-8') as f:
    content = f.read()
lines = content.split('\n')
# === NEW CHECKS (mandatory after PDF→.RU.md pipeline) ===
# 1. Cyrillic ratio >50%
cyrillic = sum(1 for c in content if '\u0400' <= c <= '\u04ff')
latin = sum(1 for c in content if c.isascii() and c.isalpha())
total_alpha = cyrillic + latin
ratio = cyrillic / max(total_alpha, 1)
print(f"Cyrillic ratio: {ratio:.1%} ({cyrillic} cyr / {latin} lat)")
if ratio < 0.5:
    errors.append(f"Cyrillic ratio {ratio:.1%} < 50% — file appears NOT translated")
# 2. Garbled shift-cipher scan (Caesar +3)
common_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had',
                'her', 'was', 'one', 'our', 'out', 'has', 'have', 'this', 'that', 'with',
                'from', 'they', 'been', 'said', 'each', 'which', 'their', 'will',
                'about', 'would', 'there', 'could', 'other', 'more', 'very', 'some',
                'these', 'those', 'only', 'also', 'than', 'then', 'when', 'what'}
garbled_count = 0
for line in lines:
    stripped = line.strip()
    if not stripped or len(stripped) < 20:
        continue
    # Try decoding shift -3
    decoded = ''.join(chr(ord(c) - 3) if 'A' <= c <= 'z' else c for c in stripped)
    words = [w.lower() for w in re.findall(r'[a-zA-Z]{4,}', decoded)]
    if words:
        english_hits = sum(1 for w in words if w in common_words)
        if english_hits > len(words) * 0.3 and len(words) >= 3:
            garbled_count += 1
if garbled_count > 5:
    errors.append(f"Found {garbled_count} garbled (shift-cipher) lines — PDF font encoding issue unresolved")
# 3. Control characters = 0 (except \n, \r, \t)
ctrl_chars = [c for c in content if ord(c) < 32 and c not in '\n\r\t']
if ctrl_chars:
    errors.append(f"Found {len(ctrl_chars)} control characters (ord<32, non-whitespace)")
# 4. Visual spot-check — print first/last 5 non-empty lines
print("\n=== First 5 non-empty lines ===")
non_empty = [l for l in lines if l.strip()]
for l in non_empty[:5]:
    print(f"  {l[:80]}")
print("\n=== Last 5 non-empty lines ===")
for l in non_empty[-5:]:
# === EXISTING CHECKS ===
# 5. Backup exists (if specified)
if BACKUP and not os.path.exists(BACKUP):
    errors.append("Missing .bak backup")
# 6. No weather-translation artifacts (common ML bug for 'nowcasting')
for artifact in ['текущей погоды', 'прогноз current weather', 'nowcast.current']:
    count = content.count(artifact)
    if count:
        errors.append(f"Found '{artifact}' {count} times — domain term corrupted")
# 7. No placeholder remnants
placeholders = set(re.findall(r'__[A-Z_]+__', content))
if placeholders:
    errors.append(f"Unresolved placeholders: {placeholders}")
# 8. Check key terms are present (customize per paper)
term_patterns = [
    (r'nowcast\w*', 'nowcasting'),
    (r'\bVAR\b', 'VAR'),
    (r'\bBVAR\b', 'BVAR'),
]
terms_missing = []
for pattern, name in term_patterns:
    if not re.search(pattern, content):
        terms_missing.append(name)
if terms_missing:
    warnings.append(f"Missing terms (may be OK if paper doesn't use them): {terms_missing}")
# 9. Tables preserved
table_lines = [l for l in lines if l.strip().startswith('|') and l.strip().endswith('|')]
if len(table_lines) < 10:
    warnings.append(f"Tables may be damaged ({len(table_lines)} lines)")
# 10. Blockquote footnotes preserved
bq_lines = [l for l in lines if l.strip().startswith('> ')]
if len(bq_lines) < 5:
    warnings.append(f"Blockquote footnotes may be damaged ({len(bq_lines)} lines)")
# 11. References intact
if 'References' not in content and 'Список литературы' not in content and 'Литература' not in content:
    warnings.append("References section may be missing or translated")
# === RESULT ===
if errors:
    print("\nFAILURES:", file=sys.stderr)
    for e in errors:
        print(f"  ✗ {e}", file=sys.stderr)
else:
    print("\nALL CHECKS PASSED ✓")
    if warnings:
        for w in warnings:
            print(f"  ⚠ {w}", file=sys.stderr)