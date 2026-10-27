---
name: minimalism
description: A 'less is more' philosophy where only essential elements remain and white space is an active design component.
tags: [minimal, clean, whitespace]
related: [flat-design, aurora-ui]
---

# UI/UX Skill: Minimalism

## 1. Definition

Minimalism is a design philosophy that emphasizes simplicity: retaining only elements truly essential to function and message, eliminating all superfluous decoration. The core tenet is "Less is more" — every pixel, every word, every color must justify its existence. White space (negative space) is treated as an active design element, not merely empty area.

## 2. Core Design Principles

- **White space is priority one:** generous padding and line-height guide the eye; content density is deliberately low.
- **One focal point per screen:** only one primary action/content is emphasized; everything else assumes a supporting role.
- **Strict grid alignment:** build layouts on an 8pt grid, with perfect alignment; no element should "float" outside the grid.
- **Limited color palette:** maximum 2–3 colors, with a single accent color.
- **Typography as the visual anchor:** hierarchy is created through size and weight, not borders, backgrounds, or icons.
- **Eliminate non-functional decoration:** no decorative shadows, no meaningless gradients, no texture for its own sake; icons are used only when they improve recognition.
- **Concise content:** microcopy is succinct, copy is trimmed to the minimum needed for comprehension.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background | `#FFFFFF` | Pure white, clean feel |
| Secondary background | `#F7F7F7` | Very light gray for alternating sections |
| Primary text | `#111111` | Near-absolute black, high contrast |
| Secondary text | `#6B7280` | Medium gray for meta and captions |
| Single accent | `#2563EB` | Blue 600 — used for CTA, links, active states |

**Dark variant:** background `#0A0A0A`, text `#FAFAFA`, accent `#3B82F6`.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | Inter (or Helvetica Now) | H1: 48–64px / 600–700; H2: 32–40px / 600 |
| Body | Inter (or SF Pro Text) | 16–18px / 400, line-height 1.6 |
| Caption | Inter | 12–14px / 400, secondary color |

Hierarchy is created primarily through **size and weight**, limiting font families to 1–2 maximum.

## 5. Signature Visual Elements

- No heavy borders, no bold shadows; if shadows exist they are extremely subtle (`0 1px 2px rgba(0,0,0,.05)`).
- Border-radius is small or absent (0–8px), and consistent throughout.
- Thin line-style icons (1.5–2px stroke), consistent with typographic weight.
- High-quality images with ample breathing room, no heavy filters.
- Dividers: thin 1px lines or white space alone.

## 6. Real-World Use Cases

- **SaaS / B2B:** dashboards, tech landing pages (Linear, Notion, Stripe style) — minimalism helps users focus on data and tasks.
- **Fintech:** banking apps, e-wallets — minimalism conveys reliability and makes numerical data easy to read.
- **Premium brands / design studios:** portfolio, agency intro pages — minimalism reflects sophistication and expertise.

## 7. Combination Notes

- **Combining with Glassmorphism/Aurora UI:** allow only one effect layer (one gentle gradient block or one frosted panel), keep everything else pure minimal — otherwise the "single focal point" principle breaks.
- **Combining with Neumorphism/Claymorphism:** minimize strictly; if unavoidable, apply only to one component group (e.g., toggles, buttons) to avoid diluting the overall cleanliness.

## 8. Anti-Patterns

- **Removing too much:** stripping away essential elements like navigation labels, progress indicators, or status cues leaves users without the context they need to make decisions.
- **Unintentional imbalance:** excessive whitespace can make layouts feel disconnected, while too little creates visual crowding—white space must serve a purpose, not merely exist.
- **No hierarchy:** without typography or color to establish focal points, users cannot discern what matters most on the screen.
- **Grayscale for the wrong reasons:** avoiding color entirely when a single accent would improve navigation and user experience is a missed opportunity, not a virtue.
