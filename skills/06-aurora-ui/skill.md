# UI/UX Skill: Aurora UI

## 1. Definition

Aurora UI is a style that uses dynamic, soft light like the aurora borealis — multi-layered gradients overlapping, seamlessly transitioning colors, often combined with shimmer effects, high blur, and smooth motion. This style is closely associated with Apple (macOS Sonoma, iOS 17 animated wallpapers, visionOS) and high-end tech brands wanting to convey a futuristic, magical, and living feel. The core element is "light that feels real" — gradients are not flat, they have depth and motion.

## 2. Core Design Principles

- **Multi-layer gradients:** at least 2–3 overlapping gradients at different angles, creating a "light layer" with depth.
- **High blur (Bokeh effect):** bright areas are often heavily blurred (40–80px) to create "light orb" effects similar to photography.
- **Smooth motion:** gradients/light move slowly (8–20s cycle), using CSS animation or Lottie; transitions are subtle, not attention-grabbing.
- **Natural yet vibrant colors:** blues, purples, pinks, greens — colors reminiscent of real aurora.
- **Avoid hard contrast:** no thick black lines, no heavy dark text on aurora backgrounds — use white text with soft shadow instead.
- **Backdrop blur for content:** when placing content over aurora, use `backdrop-filter: blur()` or glass panels.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Background layer 1 | `#0F0C29` | Deep purple-black — creates depth |
| Background layer 2 | `#302B63` | Dark purple |
| Light layer 1 | `#6366F1` | Indigo — central light area |
| Light layer 2 | `#06B6D4` | Cyan — cool light area |
| Light layer 3 | `#A855F7` | Purple-pink — warm alternating area |
| Accent | `#22D3EE` | Bright cyan — icons, highlights |
| Text | `#FFFFFF` (90% opacity) | Soft white, light shadow |

**Note:** gradients typically combine radial + linear, not linear alone.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Display | SF Pro Display (or Geist, Inter) | 48–72px / 600–700, soft text-shadow |
| Header | SF Pro Display | 28–36px / 600 |
| Body | SF Pro Text (or Inter) | 15–17px / 400–500, 85–90% opacity |
| Label | SF Pro Text | 12–14px / 500, letter-spacing 0.05em |

Use sharp, non-serif fonts (Apple/tech style) to contrast with the soft light behind — creating a visual anchor point.

## 5. Signature Visual Elements

- **Animated background:** slow-moving gradients, infinite loop.
- **Light orbs:** blurred circles floating on the background.
- **Glass cards:** transparent frosted panels (`backdrop-filter: blur(20px)`, `background: rgba(255,255,255,0.1)`) placed over aurora.
- **Shimmer effect:** a light streak running across a surface to simulate "real light."
- **Icons:** white thin strokes or filled white — never dark colors on aurora backgrounds.

## 6. Real-World Use Cases

- **Operating systems & devices:** macOS Sonoma, iOS 17+, visionOS, Android 12+ dynamic color — aurora is a platform-level trend.
- **Streaming / gaming apps:** Spotify (new version), Discord (dark mode), Epic Games launcher — creates a living space for younger users.
- **Premium Web3/AI/Fintech brands:** landing pages for high-end tech products wanting to convey innovation and the future.

## 7. Combination Notes

- **Combining with Glassmorphism:** most natural pairing — glass cards floating over aurora create the "light passing through glass" effect, visually stunning.
- **Combining with Flat Design:** can use flat elements (text, monochrome icons) over aurora — this is the most common combination (e.g., macOS widgets).
- **Limitations:** do not place detailed photographs or live video directly over aurora due to visual conflict; use a glass overlay as an intermediary.

## 8. Anti-Patterns

- **Jarring or distracting motion:** fast, abrupt gradient animations defeat the ethereal quality of aurora—the gentle, slow movement is what makes the effect feel magical.
- **Sharp photographs on soft gradients:** placing detailed images or videos directly over aurora backgrounds creates visual conflict; always use a glass intermediary layer.
- **Dark text on bright aurora:** dark text on vibrant gradient backgrounds is difficult to read—white text with soft shadow is non-negotiable for accessibility.
- **Over-blurring:** applying excessive bokeh blur (80px+) everywhere creates an unfocused, inaccessible interface; blur should enhance depth, not obscure content.
