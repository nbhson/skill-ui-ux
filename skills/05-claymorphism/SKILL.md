---
name: claymorphism
description: 3D rounded, soft, squeezable clay-like UI with internal gradients, super-rounded corners, and floating multi-layer shadows.
tags: [3d, rounded, clay, floating, apple-style]
related: [neumorphism, aurora-ui, glassmorphism]
---

# UI/UX Skill: Claymorphism

## 1. Definition

Claymorphism is a variant of Neumorphism but with the "material" characterized by clay — creating a 3D rounded, soft, slightly squeezable feel. This style rose from Apple's design trend (clearly visible from iOS 14 onward, especially iOS 15 widgets and macOS Big Sur icons). Unlike Neumorphism: (1) it typically uses internal gradients instead of simple shadows, (2) much larger border-radius, (3) often includes a sharp corner highlight, and (4) colors can be more diverse.

## 2. Core Design Principles

- **Internal gradient (inner gradient):** each block has a subtle gradient from top to bottom (or from a corner outward) simulating light on a curved surface; distinct from a flat background.
- **Super-rounded corners:** border-radius of 24–48px or fully circular (50%) — creating shapes like molded clay pieces.
- **Multi-layer shadows:** typically 2 shadows: one small soft shadow (near shadow) and one large blurred shadow (far shadow) to create a strong "floating" effect.
- **Corner highlight:** a bright white/muted zone at the top or center-top, simulating reflected light on a curved surface.
- **More saturated colors than Neumorphism:** not required to share hue with the background; can use multiple color groups, but each block has an internal gradient.
- **Thin borders:** often a 1px transparent or subtle border creating a "curved edge" look-through effect, especially when blocks overlap.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background | `#E8EEF5` | Light blue-gray — common Apple-ish background |
| Clay block 1 | `#7C3AED` → `#8B5CF6` | Purple gradient, 32px border-radius |
| Clay block 2 | `#F472B6` → `#FB7185` | Pink-coral gradient |
| Clay block 3 | `#34D399` → `#6EE7B7` | Mint green gradient |
| Highlight | `#FFFFFF` (40–60% opacity) | Light zone at the top |
| Near shadow | `#000000` (10% opacity) | Small, sharp shadow |
| Far shadow | `#6366F1` (15% opacity) | Large, blurred shadow, subtle purple tint |

**Rule:** each clay block needs exactly 3 layers: inner gradient + corner highlight + outer shadow.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | SF Pro Rounded (or Nunito, Poppins) | H1: 36–48px / 600–700 |
| Body | SF Pro Rounded | 15–17px / 400, line-height 1.5 |
| Label | SF Pro Rounded | 12–14px / 500 |

**Important:** use only rounded fonts; non-rounded fonts will create visual conflict with rounded clay blocks.

## 5. Signature Visual Elements

- Icons: filled style, large rounded corners, often placed inside fully circular clay containers.
- Buttons: 50% border-radius, top-corner highlight, light shadow underneath.
- Cards/Widgets: larger blocks, 24–40px border-radius, more prominent internal gradients.
- Input fields: transparent border but inner shadow creating a "pressed-in" feel.
- Borders are typically absent — boundaries are created by shadow alone.

## 6. Real-World Use Cases

- **iOS/macOS widgets & app icons:** this is the most natural environment for claymorphism.
- **Fitness/Health apps:** exercise icons, calorie trackers, habit trackers — creates a fun, colorful, youth-friendly feel.
- **Lightweight dashboards:** small widgets on smart dashboards, not for large data tables.

## 7. Combination Notes

- **Combining with Glassmorphism:** both share blur/transparent elements — use glass as the backdrop and clay for floating cards on top, creating rich depth.
- **Combining with Neon/Gradient UI:** naturally paired because the saturated palette of claymorphism harmonizes with neon gradients — can use a soft gradient background behind clay blocks.
- **Do not combine with pure Neumorphism:** too similar, and mixing their shadows creates inconsistency; if needed, apply them to completely separate zones.

## 8. Anti-Patterns

- **Forgetting the inner gradient:** clay blocks without internal gradients look like flat rounded rectangles rather than 3D clay pieces—the inner gradient is what creates the squeezable illusion.
- **Uniform rounding everywhere:** applying 50%+ border-radius to every single element turns the interface into a blob—vary the rounding to maintain visual hierarchy and interest.
- **Lone elements without overlap:** clay blocks that float in isolation miss the tactile, connected quality of the style; subtle overlaps between blocks reinforce the "molded clay" feel.
- **Overloaded color palette:** using too many saturated colors across multiple clay blocks fragments the cohesive effect—limit to 2-3 prominent color families for harmony.
