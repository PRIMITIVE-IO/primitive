# Primitive relaunch 2026: design tokens

**Tagline:** Primitive is back. Agent Swarm control in cyberspace.

The identity is built on the **official Primitive logo**: a row of outlined circles (2, 3, 5, then 7 in a hex cluster) above
the PRIMITIVE wordmark, in navy on white. The landing site (`src/style.less`) and the GitHub README banner
(`PRIMITIVE-IO/primitive`, `brand/`) use the same tokens. `tokens.json` is the source of truth, and the files are identical in both repos.

## Logo

| File | Use |
|---|---|
| `primitive-logo.svg` | Primary lockup, navy `#000050` on white |
| `primitive-logo-reversed.svg` | White lockup on navy sections |
| `primitive-mark(-reversed).svg` | The circles only (favicon, small marks) |
| `primitive-wordmark(-reversed).svg` | Wordmark only (site header) |
| `primitive-logo.png` | The original artwork the SVGs were traced from |

The SVGs were vectorized with potrace from `primitive-logo.png`. Don't redraw, recolor (except navy or white), stretch, or add effects.
Keep clear space of at least one circle's height around the logo.

## Palette: navy on white, cyberspace as accent

| Token | Hex | Use |
|---|---|---|
| `navy` | `#000050` | **Primary.** Sampled from the logo. Logo, headlines, primary buttons, dark sections |
| `navy-deep` | `#00002E` | Gradients, illustration panel |
| `navy-hi` | `#14147A` | Hover on navy, cards on navy |
| `periwinkle` | `#3A3ACF` | Headline emphasis, links on white |
| `lavender` | `#B8BAF0` | Secondary text and emphasis on navy |
| `paper` | `#FFFFFF` | Page background |
| `mist` | `#F4F5FB` | Alternate light sections, cards |
| `line` | `#DCDEEE` | Hairlines |
| `text` | `#14143C` | Body text |
| `muted` | `#585B85` | Secondary text |
| `cyan` | `#00D2FD` | *Secondary accent:* grid, glow, live dots. Only on navy, never text on white |
| `signal` | `#FF4FD8` | *Secondary accent:* agents only, small marks |

Navy on white (and white on navy) passes WCAG AAA. Muted on white and lavender on navy pass AA.

## Typography

- **Quicksand** (self-hosted variable woff2, Latin subset, SIL OFL; see `src/fonts/Quicksand-OFL.txt`) is the closest thin,
  rounded geometric match to the wordmark.
  - Display: weight 300, tracking 0.01em.
  - Wordmark-style labels: weight 600, uppercase, 11-12px, tracking 0.28em.
  - Body: weight 500, line-height 1.7.
- Mono (`JetBrains Mono`, `Cascadia Code`, Consolas) for commands only.

## Cyberspace, as an accent

- The concept illustration sits in a **navy "cyberspace window"** with a faint cyan grid and glow, and it stays labeled *Concept illustration*.
  It is recolored with `brand/recolor_svg.py`: navy panels, periwinkle structure, cyan runtime, magenta for the phone.
- Navy sections (the swarm, closing) carry the same faint cyan grid. Agent marks use `signal`.
- Status dots pulse slowly, and stop under `prefers-reduced-motion`.

## Voice

Short, declarative, second person. Name real things (Claude Code, Codex, OpenXR, islands, traces). Describe only what the
`primitive-proxy` / `primitive-env` READMEs state. No invented numbers, quotes or customers.
