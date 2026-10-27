# UI/UX Skill: Neumorphism

## 1. Definition

Neumorphism (New + Skeuomorphism) creates an effect of elements "pushed out" or "pressed in" from the surface, mimicking the tactile feel of soft materials (rubber, smooth plastic, silicone) on a flat background. Unlike old skeuomorphism (which simulated real materials like wood, leather), neumorphism relies solely on soft shadows to create depth without complex textures or gradients. The background and elements typically share the same hue, differing only in lightness.

## 2. Core Design Principles

- **Background and elements share the same hue:** background, buttons, and cards all belong to the same color group, differing only in lightness by ±10%.
- **Symmetrical soft shadows:** one light shadow on the top-left corner and one dark shadow on the bottom-right corner, with equal blur and spread. This is the core technique.
- **No clear borders:** no border, no outline — boundaries are created entirely through shadow.
- **Prefers neutral backgrounds:** light gray background (light mode) is the most common environment; dark mode requires shadow inversion (lighter instead of darker).
- **Clear interaction feedback:** when pressed, shadows reverse (shadow becomes inner shadow) creating a "pressed in" feel; hover states need subtle transitions.
- **Consistent border-radius:** rounded corners of 16–24px uniformly across elements, creating a soft, tactile feel.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background (light) | `#E4E9F2` | Warm gray-white — most common background |
| Primary background (dark) | `#2D3748` | Dark gray — for dark mode |
| Element (light) | `#ECF0F3` | 5–8% lighter than background |
| Light shadow | `#FFFFFF` (70% opacity) | Top-left corner |
| Dark shadow | `#A3B1C6` (50% opacity) | Bottom-right corner |
| Accent color | `#6C63FF` | Soft purple — used for icons/active states |
| Primary text | `#4A5568` | Medium-dark gray, not too dark |

**Rule:** accent color is only for icons and active states; interactive elements (buttons, toggles) should maintain the background color.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | Poppins (or Nunito, Quicksand) | H1: 36–48px / 500–600; H2: 24–28px / 500 |
| Body | Poppins | 15–16px / 400, line-height 1.6 |
| UI Label | Poppins | 13–14px / 500 |

Rounded fonts like Poppins, Nunito, and Quicksand are the best fit for the soft, tactile feel of neumorphism.

## 5. Signature Visual Elements

- Soft UI: shadow blur 20–40px, spread 5–15px, no hard edges.
- Inner shadow on press: `inset` shadow instead of `drop` shadow.
- No thin-stroke icons — use solid (filled) icons so they "pop" from the background.
- Sliders, toggles, inputs: "embedded" style (sinking into the surface) instead of "raised."
- Cards may be slightly raised; list items are flat-inset style.

## 6. Real-World Use Cases

- **Fitness / wellness apps:** Apple Fitness+, meditation apps — soft, friendly feel, gentle on the eyes.
- **Personal tools:** smart home remote, IoT control app — the tactile "touchable" feel creates user affinity.
- **Lightweight portfolios:** personal pages, profile apps — creates a refined feel, distinct from flat design.

## 7. Combination Notes

- **Combining with Flat Design:** use flat design for main content (text, images) and neumorphism only for interactive components (buttons, switches, sliders) — clearly separate zones.
- **Combining with Glassmorphism:** limit this combination because both rely on shadows/blur; if necessary, place glass panel at the top layer with neumorphic buttons underneath, ensuring sufficient contrast.
- **Avoid in data-heavy dashboards:** neumorphism is unsuitable for data-dense interfaces because subtle shadows don't provide enough layer differentiation with many components.

## 8. Anti-Patterns

- **Background-element color convergence:** using background and element colors that differ by less than 5% makes interactive elements nearly invisible—legibility must take precedence over subtle aesthetics.
- **Inconsistent shadow values:** applying different blur, spread, or opacity values across buttons and cards breaks the unified soft-material illusion that defines neumorphism.
- **Low-contrast text:** pairing gray-on-gray elements with soft shadows results in text that fails accessibility standards—the neumorphic aesthetic requires deliberate contrast planning.
- **Static interfaces:** neumorphism relies on shadow transitions to communicate pressed/raised states; without clear interaction feedback, the tactile quality that distinguishes this style is lost.
