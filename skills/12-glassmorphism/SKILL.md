---
name: glassmorphism
description: Frosted glass panels: semi-transparent fills, backdrop blur, 1px light borders, and soft shadows layered over vibrant backgrounds.
tags: [glass, frosted, blur, transparency, depth]
related: [aurora-ui, class-morphism, claymorphism]
---

# UI/UX Skill: Glassmorphism

## 1. Definition

Glassmorphism is a style based on frosted glass panels: elements use semi-transparent backgrounds combined with background blur (`backdrop-filter: blur()`), a 1px light border, and soft shadows to create a "frosted glass sheet floating above content" feel. The style was foreshadowed by Windows Vista Aero and was popularized by Apple (iOS 7 Control Center, macOS Big Sur, visionOS) and Microsoft Fluent Design. Its core element is **multi-layered depth**: the colorful/blurred background sits behind, the glass panel is in the middle, and the content sits on top — glass is only truly effective when there is something vibrant behind it to blur.

## 2. Core Design Principles

- **Semi-transparent background:** glass panels use `rgba(255,255,255,0.10–0.40)` (light mode) or `rgba(20,20,30,0.30–0.50)` (dark mode) — enough to blur the background while maintaining readability.
- **Backdrop blur is mandatory:** `backdrop-filter: blur(10–30px)` (optionally combined with `saturate(180%)` to enhance the vibrancy of the content showing through) — no blur, no glass.
- **1px light border:** a thin border `rgba(255,255,255,0.3–0.6)` creates the "glass edge" that catches the light — this is the strongest identifier.
- **Vibrant background behind:** glass panels need to sit on a colorful gradient, image, or bokeh shapes; placing them on a flat white/gray background renders the effect invisible.
- **Light text:** white text with 90–100% opacity (plus a soft text-shadow if needed) to ensure contrast on the glass panel.
- **Hierarchy through transparency levels:** 2–3 transparency levels (e.g., 30% for main cards, 15% for secondary panels) to distinguish hierarchy without needing borders.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Background gradient 1 | `#667EEA` | Indigo — starting point of the background gradient |
| Background gradient 2 | `#764BA2` | Purple — gradient endpoint, accent color |
| Glass fill | `#FFFFFF` (10–20% opacity) | Glass card fill |
| Glass border | `#FFFFFF` (30–60% opacity) | 1px border creating the light-catching edge |
| Primary text | `#FFFFFF` (95–100% opacity) | White text on glass |
| Secondary text | `#FFFFFF` (60–75% opacity) | Meta, caption |
| Ambient shadow | `#1F2687` (20% opacity) | Soft dark purple shadow below the glass panel |

**Rule:** at least 1/3 of the viewport area must be a vibrant background (gradient/image) for the glass effect to be visible.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | Inter (or SF Pro Display) | H1: 40–64px / 600–700 |
| Body | Inter (or SF Pro Text) | 15–17px / 400–500, line-height 1.5 |
| Label | Inter | 12–14px / 500, letter-spacing 0.05em |

**Important:** all text on glass panels must be white (or near-white); dark text on glass with a light background will fail contrast requirements.

## 5. Signature Visual Elements

- Glass cards: `background: rgba(255,255,255,0.15); backdrop-filter: blur(20px) saturate(180%); border: 1px solid rgba(255,255,255,0.3); border-radius: 16–24px;`
- Floating layers: 2–3 layers of glass at different transparency/blur levels create a sense of depth.
- Colorful blobs behind: gradient color spots or large bokeh circles placed behind the glass panel.
- Soft shadow: `box-shadow: 0 8px 32px rgba(31,38,135,0.2)` — enough lift without breaking the "transparent" feel.
- Icons: white thin strokes or filled white; colored icons only on solid-colored buttons.
- Optional subtle noise/grain (2–4% opacity) to reduce gradient banding through the glass.

## 6. Real-World Use Cases

- **Media apps:** Apple Music, Spotify Now Playing, video players — the glass panel overlays artwork without destroying the image.
- **Weather / Maps apps:** widgets overlaying maps or sky imagery — glass keeps map context visible while remaining readable.
- **Hero sections / landing pages:** frosted glass cards floating over gradients — conveys a premium, modern feel.
- **Quick-setting panels:** control centers, notification centers, toolbar overlays — borrowing from the Apple visionOS/window system.

## 7. Combination Notes

- **Combining with Aurora UI:** the most natural pairing — glass cards floating over aurora create the "light passing through glass" effect.
- **Combining with Flat Design:** use flat content (text, solid-color icons) placed on top of the glass panel — the contrast between flat content and the blurred background creates clarity.
- **Combining with Claymorphism:** use glass as the backdrop and clay as the floating cards on top, creating multiple layers of depth.
- **Do not combine with Brutalism/Skeuomorphism:** glassmorphism requires smoothness and light; brutalism is raw and skeuomorphism is heavy-textured — they are completely opposite in depth philosophy.

## 8. Anti-Patterns

- **Glass on plain backgrounds:** placing glass panels over white/gray backgrounds removes any visible effect — the frosted glass requires a vibrant, detailed background behind it.
- **Nested glass panels:** stacking glass inside glass (panel within panel) doubles blur cost and muddies contrast — keep one glass layer per visual region.
- **Failing contrast:** transparency + blur reduces contrast; light gray or dark text on glass commonly fails WCAG AA (4.5:1) — always verify text contrast over the busiest background area.
- **Over-blurring everything:** applying `backdrop-filter: blur(40px+)` across many elements is GPU-expensive and causes jank on mobile — limit blur radius (10–30px) and the number of glass surfaces per screen.
