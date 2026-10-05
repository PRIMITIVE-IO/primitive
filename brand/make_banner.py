"""Build the README relaunch banner from the shared design tokens and the existing logo.

    python3 brand/make_banner.py            # writes brand/banner.svg
    google-chrome --headless=new --hide-scrollbars --window-size=1280,400 \
      --force-device-scale-factor=2 --screenshot=images/relaunch-banner.png brand/banner.svg

Then optionally quantize to 256 colors (Pillow) to keep the PNG small.

No screenshots are used: the logo is images/Primitive.png and the illustration is the labeled concept
art brand/agent-world.svg (the same file as the landing site's src/rsc/agent-world.svg).
"""
import base64, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
t = {k: v["value"] for k, v in json.loads((root / "brand/tokens.json").read_text())["color"].items()}
b64 = lambda p, mime: f"data:{mime};base64," + base64.b64encode((root / p).read_bytes()).decode()
logo = b64("images/Primitive.png", "image/png")
art = b64("brand/agent-world.svg", "image/svg+xml")
W, H = 1280, 400
grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(0, W + 1, 48)) + \
       "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(0, H + 1, 48))
mono = "JetBrains Mono, Cascadia Code, DejaVu Sans Mono, Consolas, monospace"
sans = "Segoe UI, Helvetica Neue, Arial, Liberation Sans, sans-serif"
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="g1" cx="0.74" cy="0.5" r="0.55"><stop stop-color="{t['cyan']}" stop-opacity=".18"/><stop offset="1" stop-color="{t['cyan']}" stop-opacity="0"/></radialGradient>
    <radialGradient id="g2" cx="0.08" cy="0.1" r="0.4"><stop stop-color="{t['signal']}" stop-opacity=".10"/><stop offset="1" stop-color="{t['signal']}" stop-opacity="0"/></radialGradient>
    <linearGradient id="fade" x1="0" x2="0" y1="0" y2="1"><stop stop-color="#fff" stop-opacity="0"/><stop offset=".35" stop-color="#fff"/><stop offset=".75" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <mask id="m"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
    <filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="{W}" height="{H}" fill="{t['void']}"/>
  <rect width="{W}" height="{H}" fill="url(#g1)"/><rect width="{W}" height="{H}" fill="url(#g2)"/>
  <g stroke="{t['cyan']}" stroke-opacity=".07" mask="url(#m)">{grid}</g>
  <image href="{art}" x="700" y="-40" width="590" height="480"/>
  <image href="{logo}" x="56" y="44" width="220" height="64"/>
  <g transform="translate(56,140)">
    <rect width="190" height="30" rx="2" fill="{t['phosphor']}" fill-opacity=".06" stroke="{t['phosphor']}" stroke-opacity=".45"/>
    <circle cx="16" cy="15" r="3.5" fill="{t['phosphor']}" filter="url(#glow)"/>
    <text x="30" y="19.5" font-family="{mono}" font-size="11" letter-spacing="1.8" fill="{t['phosphor']}">PRIMITIVE IS BACK</text>
  </g>
  <text font-family="{sans}" font-weight="300" font-size="58" letter-spacing="-2">
    <tspan x="52" y="236" fill="{t['cyan']}" filter="url(#glow)">Agent Swarm</tspan><tspan fill="{t['text']}"> control</tspan>
    <tspan x="52" y="300" fill="{t['phosphor']}" filter="url(#glow)">in cyberspace.</tspan>
  </text>
  <text x="56" y="344" font-family="{sans}" font-size="16" fill="{t['muted']}">Claude Code and Codex, directed by voice, in one shared 3D world of your code.</text>
  <text x="56" y="372" font-family="{mono}" font-size="11" letter-spacing="1.5" fill="{t['dim']}">VR (OPENXR) · FLAT SCREEN · BROWSER · PRIMITIVE.IO</text>
  <text x="{W-24}" y="{H-18}" text-anchor="end" font-family="{mono}" font-size="10" letter-spacing="1.2" fill="{t['dim']}">CONCEPT ILLUSTRATION</text>
  <rect x=".5" y=".5" width="{W-1}" height="{H-1}" fill="none" stroke="{t['line']}"/>
</svg>
'''
(root / "brand/banner.svg").write_text(svg)
print("wrote brand/banner.svg")
