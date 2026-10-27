# UI/UX Skill: Brutalism UI

## 1. Definition

Brutalism UI in web/digital design is a "raw, bare, unpolished" style — inspired by architectural brutalism (exposing raw concrete), but applied to digital interfaces. Elements are presented in their raw form: system fonts, basic background colors, gridless or very rough layouts, obvious hover states, and content displayed almost without processing. The goal is to break aesthetic conventions to create attention, uniqueness, and deliberate anti-design.

## 2. Core Design Principles

- **System or "raw" fonts:** use Arial, Courier New, Times New Roman, or dedicated brutalist fonts like Archivo Black, Monoton — not professionally designed "beautiful" fonts.
- **Unsophisticated basic colors:** bright yellow, light red, lime green, candy pink — usually unnatural colors, CSS color keywords like `yellow`, `red`, `blue`.
- **Intentional disorderly layout:** may use skewed arrangement, slight overlaps, imperfectly aligned elements; but there's a hidden visual logic.
- **Thick black borders:** 2–4px borders surrounding most blocks; this is the strongest identifier.
- **Obvious hover states:** background color change, color inversion, or white/black text highlighting.
- **No soft shadows:** if shadows exist, they are hard shadows (`4px 4px 0 #000`) or no shadows at all.
- **"Raw" navigation:** can be text link lists, DOS-style buttons, or the simplest possible menu.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background | `#FFFEF0` | Off-white — "paper" feel |
| Accent 1 | `#FFE600` | Bright yellow — large block backgrounds |
| Accent 2 | `#FF5C00` | Orange-red — CTAs |
| Accent 3 | `#FF00FF` | Bright magenta — hover states |
| Text | `#000000` | Absolute black |
| Accent | `#00FF00` | Terminal green — for highlights |

**Rule:** no gray colors — either #000 or #FFF. Color combinations must have high contrast, never use muted intermediate colors.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Display | Archivo Black (or Impact, Arial Black) | 48–120px / 900, uppercase |
| Body | Courier New (or Space Mono, Roboto Mono) | 16–18px / 400–700 |
| UI Label | Arial (or Helvetica) | 14–16px / 700 |

Monospace fonts (Courier New, Space Mono) are the most popular choice in brutalism UI because they create a "raw, unpolished" feel.

## 5. Signature Visual Elements

- 2–4px black borders around almost everything.
- Hard shadow: `box-shadow: 4px 4px 0px #000;`.
- "Raw" checkbox/button: browser-native interface, unstyled.
- Imperfect grid: blocks slightly misaligned, creating a "rushed" or "deliberately wrong" feel.
- Thick underlines for links: 3px underline, no hover underline.
- Marquee text, scrolling text, simple text animations.

## 6. Real-World Use Cases

- **Creative agency portfolios:** Balenciaga, Bloomberg (old version), design studios wanting to be completely different.
- **Tech startups / developer tooling:** developer tools (pages like old figma.com, glitch.me) — brutalism conveys "we don't care about appearance, function is what matters."
- **Rebellious brands / digital art:** streetwear brands, digital artists, NFTs — expressing strong personality.

## 7. Combination Notes

- **Combining with Maximalism:** most natural combination — both oppose design conventions, brutalism provides the structural backbone (layout/borders) and maximalism provides the flesh (graphics/patterns), but commit to a shared grid system.
- **Combining with Retro:** shares common DNA (system fonts, bold borders) — brutalism can be seen as "retro but modernized."
- **Do not combine with Neumorphism/Claymorphism/Aurora UI:** diametrically opposite in every element; the combination will produce an "indecisive mix."

## 8. Anti-Patterns

- **Confusing intentionality with negligence:** truly disordered layouts (randomly rotated everything, completely broken grids) may read as amateur mistakes rather than deliberate anti-design—some hidden logic must remain.
- **Usability sacrificed for shock value:** using tiny click targets, illegible type, or poor contrast under the guise of brutalism damages user experience without artistic justification.
- **Half-hearted boldness:** mixing bold brutalist elements with polished, refined ones creates indecision rather than tension—a committed brutalist approach is more effective.
- **Random interactivity:** adding marquees or scroll effects without purpose feels gimmicky; every "raw" element should have intentional function alongside its aesthetic.
