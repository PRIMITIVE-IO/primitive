"""Build the README relaunch banner from the shared design tokens and the official logo.

    python3 brand/make_banner.py            # writes brand/banner.svg
    google-chrome --headless=new --hide-scrollbars --window-size=1280,400 \
      --force-device-scale-factor=2 --screenshot=images/relaunch-banner.png brand/banner.svg

Then optionally quantize to 256 colors (Pillow) to keep the PNG small.

No screenshots are used. The logo is images/brand/primitive-logo.svg (potrace vectorization of the official
images/brand/primitive-logo.png), the type is Quicksand (brand/quicksand-latin.woff2, SIL OFL, embedded), and the
illustration is the labeled concept art brand/agent-world.svg (the same file as the landing site's src/rsc/agent-world.svg).
"""
import base64, json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
t = {k: v["value"] for k, v in json.loads((root / "brand/tokens.json").read_text())["color"].items()}
b64 = lambda p, mime: f"data:{mime};base64," + base64.b64encode((root / p).read_bytes()).decode()
logo = b64("images/brand/primitive-logo.svg", "image/svg+xml")
art = b64("brand/agent-world.svg", "image/svg+xml")
font = b64("brand/quicksand-latin.woff2", "font/woff2")
W, H = 1280, 400
PX, PY, PW, PH = 724, 28, 528, 344          # navy "cyberspace window"
grid = "".join(f'<line x1="{x}" y1="{PY}" x2="{x}" y2="{PY+PH}"/>' for x in range(PX, PX + PW + 1, 32)) + \
       "".join(f'<line x1="{PX}" y1="{y}" x2="{PX+PW}" y2="{y}"/>' for y in range(PY, PY + PH + 1, 32))
lgrid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(0, W + 1, 48)) + \
        "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(0, H + 1, 48))
q = "Quicksand"
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <style>@font-face {{ font-family:"Quicksand"; src:url({font}) format("woff2"); font-weight:300 700; }}</style>
    <linearGradient id="win" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{t['navy']}"/><stop offset="1" stop-color="{t['navy-deep']}"/></linearGradient>
    <radialGradient id="glow" cx="0.55" cy="0.6" r="0.6"><stop stop-color="{t['cyan']}" stop-opacity=".18"/><stop offset="1" stop-color="{t['cyan']}" stop-opacity="0"/></radialGradient>
    <linearGradient id="fade" x1="0" x2="1"><stop stop-color="#fff"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <mask id="lm"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
    <clipPath id="wc"><rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="18"/></clipPath>
  </defs>
  <rect width="{W}" height="{H}" fill="{t['paper']}"/>
  <g stroke="{t['navy']}" stroke-opacity=".05" mask="url(#lm)">{lgrid}</g>
  <image href="{logo}" x="56" y="40" width="230" height="95"/>
  <g transform="translate(56,160)">
    <rect width="196" height="30" rx="15" fill="{t['paper']}" stroke="{t['navy']}" stroke-opacity=".25"/>
    <circle cx="18" cy="15" r="3.5" fill="{t['cyan']}"/>
    <text x="32" y="19.5" font-family="{q}" font-weight="700" font-size="10.5" letter-spacing="2.9" fill="{t['navy']}">PRIMITIVE IS BACK</text>
  </g>
  <text font-family="{q}" font-weight="300" font-size="52" letter-spacing="1">
    <tspan x="52" y="250" fill="{t['navy']}" font-weight="400">Agent Swarm</tspan><tspan fill="{t['navy']}"> control</tspan>
    <tspan x="52" y="310" fill="{t['periwinkle']}">in cyberspace.</tspan>
  </text>
  <text x="56" y="350" font-family="{q}" font-weight="500" font-size="15.5" fill="{t['muted']}">Claude Code and Codex, directed by voice, in one shared 3D world of your code.</text>
  <text x="56" y="376" font-family="{q}" font-weight="700" font-size="10" letter-spacing="2.6" fill="{t['muted']}">VR (OPENXR) · FLAT SCREEN · BROWSER · PRIMITIVE.IO</text>
  <g clip-path="url(#wc)">
    <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="url(#win)"/>
    <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="url(#glow)"/>
    <g stroke="{t['cyan']}" stroke-opacity=".08">{grid}</g>
    <image href="{art}" x="{PX + 34}" y="{PY - 18}" width="460" height="374"/>
    <text x="{PX + 20}" y="{PY + PH - 16}" font-family="{q}" font-weight="700" font-size="9" letter-spacing="2.4" fill="{t['lavender']}">CONCEPT ILLUSTRATION</text>
  </g>
</svg>
'''
(root / "brand/banner.svg").write_text(svg)
print("wrote brand/banner.svg")
