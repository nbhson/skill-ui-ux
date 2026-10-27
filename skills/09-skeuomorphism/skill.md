# UI/UX Skill: Skeuomorphism

## 1. Definition

Skeuomorphism is a design style that mimics real-world objects in digital interfaces: the interface looks like real materials (leather, wood, metal) or real objects (calculators, notebooks, radios). This was the most popular style from 2007–2012 (Apple iOS before iOS 7, Windows Vista/7, Apple apps before 2013), before being replaced by Flat Design. Today, skeuomorphism is used selectively for contexts that need to create familiarity or a nostalgic feeling.

## 2. Core Design Principles

- **Mimic real materials:** leather (texture), wood (grain), metal (heavy gradient + highlight), paper (soft shadow).
- **Clear depth:** multiple shadow layers creating depth — drop shadow + bottom shadow + top highlight.
- **Bevel and Emboss:** create raised/pressed effects using border gradients (light on top = raised, dark on top = pressed).
- **Repeating textures:** material patterns (leather, linen, wood grain) as background, visible even on areas without content.
- **Physical buttons:** buttons have raised shapes, with clear "pressed-down" states using inner shadow and gradient.
- **Physical interaction feedback:** when pressed, buttons sink; volume sliders have grooves; switches have obvious on/off states.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Brown leather background | `#8B5A2B` | Leather brown |
| Black leather | `#3D3D3D` | Black leather (iPod classic) |
| Light wood | `#C4A574` | Light wood yellow |
| Silver metal | `#C0C0C0` → `#E8E8E8` | Metal gradient |
| Gold metal | `#D4AF37` → `#FFD700` | Brass/gold |
| Highlight | `#FFFFFF` (30% opacity) | Light on the surface |
| Dark shadow | `#000000` (30–50% opacity) | Drop shadow |

**Rule:** texture is the dominant element; color is secondary in skeuomorphism because material already provides color.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | Georgia (or Palatino, Rockwell) | H1: 32–48px / 700, bold serif |
| Body | Trebuchet MS (or Verdana) | 15–17px / 400, readable |
| Digital display | Digital-7 Mono (or LCD mono) | 24–48px — for LED/digital screens |

Serif fonts (Georgia, Palatino) or "soft" sans-serif (Trebuchet) fit the realistic material feel better than modern pure fonts.

## 5. Signature Visual Elements

- Background textures: leather, linen, wood, metal — used as background for the entire interface or for specific panels.
- Bevel border: 1px gradient border with light on top and dark on bottom to create a raised effect.
- Multi-layer drop shadow: outer shadow + inner shadow combined.
- Complex gradients: instead of flat colors, use multi-stop gradients to simulate light on a 3D surface.
- 3D icons: icons with depth, shadow, and highlight — not 2D glyphs.

## 6. Real-World Use Cases

- **Music/audio apps:** music players, guitar tuners, DJ apps — mimicking audio equipment (equalizers, cassette players, turntables) creates familiarity.
- **Game UI / Immersive apps:** mobile games, simulator apps (flight simulators, racing dashboards) — skeuomorphism creates a "touchable" feel.
- **Nostalgic/retro products:** notebook-style note apps, virtual garden apps — creates emotional connection.

## 7. Combination Notes

- **Combining with Retro:** very natural — many retro products can combine skeuomorphism to enhance the nostalgic feel.
- **Combining with Flat Design:** can use skeuomorphism for elements needing emphasis (key features) and flat for the rest — called "flat skeuomorphism hybrid" (e.g., iOS Calculator).
- **Do not combine with Neumorphism/Glassmorphism/Aurora UI:** both use shadows but with completely different principles; mixing them creates chaotic, inconsistent depth.

## 8. Anti-Patterns

- **Texture everything:** covering every surface with leather, wood, and metal textures overwhelms the interface and makes it feel cluttered rather than tactile—the "real material" should be applied selectively.
- **Mismatched metaphors:** applying skeuomorphic styling to contexts where the physical metaphor doesn't fit (e.g., a banking app designed as a leather notebook) creates confusion rather than familiarity.
- **Texture over readability:** heavy material patterns behind text or icons diminish legibility—the real-world metaphor should enhance, not obstruct, usability.
- **Stuck in 2010:** continuing to use heavy skeuomorphism (deep gradients, prominent bevels) when modern design has moved toward subtlety makes the interface appear dated rather than nostalgic.
