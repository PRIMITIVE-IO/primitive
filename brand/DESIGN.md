# Primitive relaunch 2026: design tokens

**Tagline:** Primitive is back. Agent Swarm control in cyberspace.

The same tokens are used by the landing site (`src/style.less` custom properties) and the GitHub README banner
(`PRIMITIVE-IO/primitive`, `brand/`). `tokens.json` is the source of truth; keep all three in sync.

## Palette: neon on dark

The accents are sampled from the existing brand assets, so the relaunch looks like the original film and logo.

| Token | Hex | Where it comes from | Use |
|---|---|---|---|
| `void` | `#04060B` | | Page background |
| `deep` | `#0A1020` | | Alternate sections |
| `panel` | `#0E1828` | | Cards, panels |
| `panel-hi` | `#132238` | | Featured card |
| `line` | `#1B3550` | | Hairlines, borders, 48px grid |
| `text` | `#E6F3F7` | | Headlines, body |
| `muted` | `#8DA2B5` | | Secondary text |
| `dim` | `#5B7088` | | Captions, HUD labels |
| `cyan` | `#00D2FD` | Logo circles (`Primitive.png`) | Primary accent: links, structure, focus rings |
| `blue` | `#09AFFF` | Prime Sequence background | Secondary accent: runtime, arcs, tags |
| `phosphor` | `#D8F8B8` | Glow of the original film title card (`caption.jpg`) | Headline emphasis, live status, primary buttons |
| `signal` | `#FF4FD8` | New | Agents and highlights only, used sparingly |

Glows: `0 0 24px rgba(0,210,253,.35)` (cyan), `0 0 18px rgba(216,248,184,.45)` (phosphor), `0 0 18px rgba(255,79,216,.45)` (signal).
Text contrast: `text` and `muted` on `void` are well above WCAG AA. Never set body text in `signal` or `blue`.

## Typography

- **Display:** system sans (`Segoe UI`, `Helvetica Neue`, Arial), weight 300, tracking -0.04em. This echoes the thin geometric logo wordmark without loading web fonts.
- **Body:** the same stack, weight 400, line-height 1.65.
- **HUD / mono:** `JetBrains Mono`, `Cascadia Code`, `SFMono-Regular`, Consolas. Uppercase, 11px, tracking 0.14em, for eyebrows, tags and captions.

## Motifs

- A faint 48px cyan grid ("cyberspace floor") behind the hero, swarm and closing sections, masked at the edges.
- Pulsing status dots: phosphor for live, signal for agents. Turned off under `prefers-reduced-motion`.
- Logos: `Primitive.png` (white wordmark plus cyan circles) on dark, and `logo_small.png` in the header and footer.
- Illustrations are labeled **Concept illustration**. Don't present them as screenshots.

## Voice

Short, declarative, second person. Name real things (Claude Code, Codex, OpenXR, islands, traces). Describe only what the
`primitive-proxy` / `primitive-env` READMEs state. No invented numbers, quotes or customers.
