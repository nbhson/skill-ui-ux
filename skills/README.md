# 🎨 Professional UI/UX Skill Set — 12 Design Styles

A professional reference guide for 12 UI/UX design styles, each with full coverage of: definition, design principles, color palette (hex), typography, visual elements, real-world applications, combination notes, and anti-patterns.

## 📂 Skill List

| # | Style | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Minimalism](./01-minimalism/skill.md) | 01-minimalism | Less is more — white space, single focal point, strict grid |
| 2 | [Maximalism](./02-maximalism/skill.md) | 02-maximalism | More is more — vibrant colors, patterns, bold typography |
| 3 | [Flat Design](./03-flat-design/skill.md) | 03-flat-design | Pure 2D — flat colors, no heavy gradients, no shadows |
| 4 | [Neumorphism](./04-neumorphism/skill.md) | 04-neumorphism | Soft UI — symmetrical shadows, same hue, soft tactile feel |
| 5 | [Claymorphism](./05-claymorphism/skill.md) | 05-claymorphism | Clay material — internal gradients, super-rounded, corner highlight |
| 6 | [Aurora UI](./06-aurora-ui/skill.md) | 06-aurora-ui | Aurora borealis — multi-layer gradients, high blur, smooth motion |
| 7 | [Brutalism UI](./07-brutalism-ui/skill.md) | 07-brutalism-ui | Raw, bare — thick black borders, system fonts, bright colors |
| 8 | [Collage Art](./08-collage-art/skill.md) | 08-collage-art | Cut-and-paste — multi-layer, textures, diverse typography |
| 9 | [Skeuomorphism](./09-skeuomorphism/skill.md) | 09-skeuomorphism | Mimic real materials — leather, wood, metal, clear depth |
| 10 | [Retro](./10-retro/skill.md) | 10-retro | Past decades — 50s/70s/80s/90s, era-specific palettes |
| 11 | [Class Morphism](./11-class-morphism/skill.md) | 11-class-morphism | Classic + Morphic — golden ratio, warm palette, serif typography |
| 12 | [Glassmorphism](./12-glassmorphism/skill.md) | 12-glassmorphism | Frosted glass — transparency, backdrop blur, 1px light border |

## 🤖 Machine-Readable Data

[`data.json`](./data.json) — the full skill set as structured JSON (definitions, principles, palettes, typography, combinations, anti-patterns, tags). Use it as a data source for AI agents, design linting, or design-token generation.

```json
{
  "styles": [{ "id": "neumorphism", "palette": [...], "combinations": {...}, "antiPatterns": [...] }]
}
```

## 🖼 References & Inspiration

[`assets/figma-references.md`](./assets/figma-references.md) — curated Figma Community search links, real-world reference sites, stock asset sources, and quick-start CSS tokens for each style.

## 🎯 How to Use

1. **Select a style:** use the summary table to choose the skill that fits your product/brand.
2. **Read skill.md:** each file follows 7 standard sections (definition → principles → colors → font → visual → applications → combinations).
3. **Apply:** use the hex palette + font pair + visual rules as standards when designing.

## 🔄 Quick Combination Matrix

| | Min | Max | Flat | Neu | Clay | Aurora | Brutal | Collage | Skeuo | Retro | Class | Glass |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Minimalism** | — | ❌ | ✅ | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ✅ |
| **Maximalism** | ❌ | — | ❌ | ❌ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | ✅ | ❌ | ⚠️ |
| **Flat Design** | ✅ | ❌ | — | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| **Neumorphism** | ⚠️ | ❌ | ⚠️ | — | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ✅ | ⚠️ |
| **Claymorphism** | ⚠️ | ⚠️ | ⚠️ | ❌ | — | ⚠️ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ✅ |
| **Aurora UI** | ✅ | ⚠️ | ✅ | ❌ | ⚠️ | — | ❌ | ⚠️ | ❌ | ❌ | ✅ | ✅ |
| **Brutalism UI** | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | — | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Collage Art** | ❌ | ✅ | ❌ | ❌ | ❌ | ⚠️ | ✅ | — | ❌ | ⚠️ | ❌ | ⚠️ |
| **Skeuomorphism** | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | — | ✅ | ⚠️ | ❌ |
| **Retro** | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ✅ | ⚠️ | ✅ | — | ⚠️ | ❌ |
| **Class Morphism** | ⚠️ | ❌ | ⚠️ | ✅ | ⚠️ | ✅ | ❌ | ❌ | ⚠️ | ⚠️ | — | ✅ |
| **Glassmorphism** | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ❌ | ⚠️ | ❌ | ❌ | ✅ | — |

**Legend:** ✅ = combines well · ⚠️ = conditional combination · ❌ = not recommended

## 📐 Standard Skill Structure

Each `skill.md` follows an 8-section standard:
1. **Definition** — 2–3 sentences on the core concept
2. **Core Design Principles** — mandatory rules to follow
3. **Suggested Color Palette** — hex codes + role of each color
4. **Typography** — font pair + reference sizes
5. **Signature Visual Elements** — shapes, effects, textures
6. **Real-World Use Cases** — suitable industries/product categories
7. **Combination Notes** — 2–3 tips for pairing with other styles
8. **Anti-Patterns** — common mistakes that look like the style but violate its principles
