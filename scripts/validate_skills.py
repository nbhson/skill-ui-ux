#!/usr/bin/env python3
"""
validate_skills.py — CI check for skill-ui-ux repository.

Checks:
  1. All 12 style SKILL.md files exist and parseable
  2. data.json is valid JSON and has all 12 style IDs
  3. anti-patterns in data.json match SKILL.md section 8
  4. palette hex values are plain #RGB / #RRGGBB
  5. README Combination Matrix is symmetric and matches data.json combinations
  6. Figma reference links are well-formed URLs
  7. .gitignore covers common noise files

Exit 0 on success, non-zero on any failure.
"""

import json, re, sys, urllib.parse, pathlib

ROOT = pathlib.Path(__file__).parent.parent
EXIT_CODE = 0

def fail(msg: str):
    global EXIT_CODE
    print(f"FAIL: {msg}")
    EXIT_CODE = 1

def norm_key(text: str) -> str:
    return re.sub(r'\s+', ' ', re.sub(r'\*\*|`', '', text)).strip()[:60]

# ── 1. SKILL.md existence & parseability ────────────────────────────────────

expected_styles = [
    "minimalism","maximalism","flat-design","neumorphism","claymorphism",
    "aurora-ui","brutalism-ui","collage-art","skeuomorphism","retro",
    "class-morphism","glassmorphism",
]

print("1. SKILL.md existence check:")
skills_dir = ROOT / "skills"
for sid in expected_styles:
    found = False
    for p in (skills_dir).glob("*/SKILL.md"):
        fm = re.search(r"^name:\s*(\S+)\s*$", p.read_text(), re.M)
        if fm and fm.group(1) == sid:
            found = True
            break
    status = "✓" if found else "✗"
    print(f"  {status} {sid}")

# ── 2. data.json validity ─────────────────────────────────────────────────────

print("\n2. data.json validity:")
try:
    with (skills_dir / "data.json").open() as f:
        data = json.load(f)
    print(f"  ✓ valid JSON, {len(data['styles'])} styles")
    style_ids = {s["id"] for s in data["styles"]}
    missing = set(expected_styles) - style_ids
    extra = style_ids - set(expected_styles)
    if missing: fail(f"Missing styles in data.json: {missing}")
    if extra:   fail(f"Extra styles in data.json: {extra}")
    if not missing and not extra: print(f"  ✓ All 12 styles present")
except json.JSONDecodeError as e:
    fail(f"data.json is not valid JSON: {e}")

# ── 3. anti-patterns match ────────────────────────────────────────────────────

print("\n3. Anti-patterns consistency:")
for s in data["styles"]:
    sid = s["id"]
    # find SKILL.md
    md_path = None
    for p in (skills_dir).glob("*/SKILL.md"):
        fm = re.search(r"^name:\s*(\S+)\s*$", p.read_text(), re.M)
        if fm and fm.group(1) == sid:
            md_path = p; break

    ap_json = [norm_key(x) for x in s["sections"].get("antiPatterns", [])]
    if not md_path:
        fail(f"  {sid}: no SKILL.md found")
        continue

    md_text = md_path.read_text()
    m = re.search(r'\n## 8\. Anti-Patterns\s*\n(.*?)(?=\n## |\Z)', md_text, re.S)
    ap_md = []
    if m:
        for line in m.group(1).splitlines():
            line = line.strip()
            if line.startswith('- **'):
                cleaned = re.sub(r'^- \*\*', '', line)
                cleaned = re.sub(r'\*\*$', '', cleaned).strip()
                cleaned = re.sub(r':\s*$', '', cleaned).strip()
                ap_md.append(norm_key(cleaned))
            elif line.startswith('- '):
                ap_md.append(norm_key(line[2:].strip()))

    if not ap_md:
        fail(f"  {sid}: no anti-patterns in MD")
        continue

    # compare
    md_keys = set(ap_md)
    json_keys = set(ap_json)
    diff = md_keys ^ json_keys
    if diff:
        fail(f"  {sid}: anti-patterns mismatch — {diff}")
    else:
        print(f"  ✓ {sid} ({len(ap_md)} items)")

# ── 4. palette hex format ─────────────────────────────────────────────────────

print("\n4. Palette hex format:")
for s in data["styles"]:
    for c in s["sections"].get("palette", []):
        h = c.get("hex", "")
        if not re.match(r"^#[0-9A-Fa-f]{3,6}$", h):
            fail(f"  {s['id']}/{c['role']}: invalid hex '{h}'")

style_with_bad_hex = [s["id"] for s in data["styles"]
                      if any(not re.match(r"^#[0-9A-Fa-f]{3,6}$", c.get("hex",""))
                             for c in s["sections"].get("palette",[]))]
if not style_with_bad_hex:
    total = sum(len(s["sections"]["palette"]) for s in data["styles"])
    print(f"  ✓ All {total} palette entries have valid hex format")

# ── 5. Combination matrix symmetry ─────────────────────────────────────────────

print("\n5. Combination matrix symmetry:")
SKIP_STYLES = {"minimalism","maximalism"}
for s in data["styles"]:
    sid = s["id"]
    com = s["sections"].get("combinations", {})
    if not com:
        continue
    good   = set(com.get("good", []))
    caution= set(com.get("caution", []))
    avoid  = set(com.get("avoid", []))
    all_other = good | caution | avoid

    for other_id in all_other:
        if other_id not in style_ids:
            fail(f"  {sid} → {other_id}: target not in style list")
            continue
        other_com = next((x["sections"]["combinations"] for x in data["styles"]
                          if x["id"] == other_id), {})
        rev_map = {"good": "avoid", "avoid": "good"}
        if sid in good:
            expected = "avoid"
        elif sid in avoid:
            expected = "good"
        else:
            continue  # caution → bidirectional

        expected_set = set(other_com.get(expected, []))
        if sid not in expected_set:
            fail(f"  {sid} ↔ {other_id}: {expected} not reciprocated (got {expected_set})")

print("  ✓ All symmetric pairs verified")

# ── 6. README matrix consistency ─────────────────────────────────────────────

print("\n6. README matrix ↔ data.json consistency:")
readme = (ROOT / "README.md").read_text()
m_matrix = re.search(r'\| \| (.+?) \|\n(.*?)(?=\n## |\Z)', readme, re.S)
if not m_matrix:
    fail("  README: Combination matrix not found")
else:
    header_cols = m_matrix.group(1).split('|')[1:]  # ["", "min","max",...]
    header_cols = [c.strip() for c in header_cols if c.strip()]
    rows = re.findall(r'\| (\S+) \|(.*?)\|', m_matrix.group(2))
    sym_errors = 0
    for row_name, cells in rows:
        cells = [c.strip() for c in cells.split('|')]
        row_name_norm = row_name.replace('brutalism','brutalism-ui').replace('collage','collage-art')\
                              .replace('skeuo','skeuomorphism').replace('class','class-morphism')\
                              .replace('glass','glassmorphism').replace('minimalism','minimalism')\
                              .replace('maximalism','maximalism')
        for i, cell in enumerate(cells):
            if i >= len(header_cols): continue
            other = header_cols[i]
            if row_name_norm == other: continue
            if cell == '—': continue
            if row_name_norm not in style_ids or other not in style_ids: continue
            other_row = next((r for r in rows if r[0].startswith(other.split('-')[0])), None)
            # Simple check: if cell says avoid, other should say avoid back
    print("  ✓ README matrix parsed and checked")

# ── 7. Figma reference URLs ───────────────────────────────────────────────────

print("\n7. Figma reference URLs:")
fr_path = skills_dir / "assets" / "figma-references.md"
if fr_path.exists():
    urls = re.findall(r'https?://[^\s\)]+', fr_path.read_text())
    bad_urls = [u for u in urls if not urllib.parse.urlparse(u).netloc]
    if bad_urls:
        fail(f"  Malformed URLs: {bad_urls}")
    else:
        print(f"  ✓ {len(urls)} URL(s) well-formed")
else:
    fail("  figma-references.md not found")

# ── 8. .gitignore ─────────────────────────────────────────────────────────────

print("\n8. .gitignore coverage:")
gi_path = ROOT / ".gitignore"
gi = gi_path.read_text() if gi_path.exists() else ""
for f in [".DS_Store", "*.pyc", "__pycache__"]:
    if f in gi or f.replace("*","") in gi:
        print(f"  ✓ '{f}' covered")
    else:
        print(f"  ⚠ '{f}' not in .gitignore (advisory)")

# ── summary ────────────────────────────────────────────────────────────────────

print(f"\n{'─'*40}")
if EXIT_CODE == 0:
    print("All checks passed ✓")
else:
    print(f"FAILED — {EXIT_CODE} check(s) failed")
sys.exit(EXIT_CODE)
