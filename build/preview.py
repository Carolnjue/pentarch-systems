"""Local preview harness: wraps each block in a fake WordPress page."""
import os, re, sys, glob
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build import OUT as PLUG
PV = os.environ.get("PSS_PREVIEW") or os.path.join(HERE, ".preview")
IMG = os.path.join(PLUG, "assets", "img")
os.makedirs(os.path.join(PV, "img"), exist_ok=True)

I = {  # simple 24px stroke icons, for the preview only (the plugin's pss_icon supplies the real ones)
    "arrow": "M5 12h14M13 6l6 6-6 6", "ne": "M7 17L17 7M9 7h8v8", "chev": "M6 9l6 6 6-6", "menu": "M4 7h16M4 12h16M4 17h16", "x": "M6 6l12 12M18 6L6 18",
    "up": "M12 19V5M6 11l6-6 6 6", "check": "M5 12l5 5 9-10", "call": "M5 4h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 6a2 2 0 0 1 2-2z",
    "mail": "M3 6h18v12H3zM3 7l9 6 9-6", "pin": "M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",
    "wa": "M4 20l1.5-4A8 8 0 1 1 8 18.5zM9 9c0 3 3 6 6 6l1-2-2-1-1 1c-1-.5-2-1.5-2.5-2.5l1-1-1-2z", "health": "M12 20s-8-5-8-11a4 4 0 0 1 8-1 4 4 0 0 1 8 1c0 6-8 11-8 11zM9 11h6M12 8v6",
    "school": "M2 9l10-5 10 5-10 5zM6 11v5c3 2 9 2 12 0v-5", "scissor": "M6 6a3 3 0 1 0 0 .1M6 18a3 3 0 1 0 0 .1M8.5 7.5L20 18M8.5 16.5L20 6", "cart": "M3 4h2l2.5 11h11L21 7H6.5M9 20a1 1 0 1 0 0 .1M18 20a1 1 0 1 0 0 .1",
    "pen": "M4 20l1-5L16 4l4 4L9 19zM14 6l4 4", "book": "M4 5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2zM4 19V5", "web": "M3 5h18v14H3zM3 9h18M7 7h.1", "map": "M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3zM9 3v15M15 6v15",
    "chart": "M4 20V10M10 20V4M16 20v-7M22 20H2", "wifi": "M2 9a15 15 0 0 1 20 0M5 13a10 10 0 0 1 14 0M8.5 16.5a5 5 0 0 1 7 0M12 20h.1", "offline": "M2 9a15 15 0 0 1 6-3M22 9a15 15 0 0 0-9-3.5M5 13a10 10 0 0 1 4-2.4M3 3l18 18M12 20h.1",
    "phone": "M8 2h8v20H8zM11 18h2", "shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM9 12l2 2 4-4", "lock": "M5 11h14v10H5zM8 11V7a4 4 0 0 1 8 0v4", "users": "M9 11a4 4 0 1 0 0-.1M2 21a7 7 0 0 1 14 0M17 11a3 3 0 1 0 0-.1M22 20a5 5 0 0 0-5-5",
    "server": "M4 4h16v6H4zM4 14h16v6H4zM8 7h.1M8 17h.1", "cloud": "M7 18a5 5 0 1 1 1-9.9A6 6 0 0 1 19 10a4 4 0 0 1-1 8z", "cash": "M2 6h20v12H2zM12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 9v6M18 9v6",
    "box": "M3 7l9-4 9 4v10l-9 4-9-4zM3 7l9 4 9-4M12 11v10", "scan": "M4 8V4h4M16 4h4v4M20 16v4h-4M8 20H4v-4M7 12h10", "print": "M7 8V3h10v5M5 8h14v8H5zM7 14h10v7H7z", "monitor": "M3 4h18v12H3zM8 20h8M12 16v4",
    "battery": "M3 8h16v8H3zM21 11v2M6 11h6", "lab": "M9 3h6M10 3v6L4 19a1 1 0 0 0 1 2h14a1 1 0 0 0 1-2L14 9V3M7 15h10", "bed": "M3 18V6M3 13h18v5M21 13a3 3 0 0 0-3-3H10v3M7 11a1.5 1.5 0 1 0 0-.1",
    "pill": "M4.5 13.5l9-9a4.2 4.2 0 0 1 6 6l-9 9a4.2 4.2 0 0 1-6-6zM9 9l6 6", "cal": "M4 5h16v16H4zM4 10h16M9 3v4M15 3v4", "star": "M12 3l2.8 5.8 6.2.9-4.5 4.4 1 6.2L12 17.4 6.5 20.3l1-6.2L3 9.7l6.2-.9z",
    "layers": "M12 3l9 5-9 5-9-5zM3 13l9 5 9-5", "code": "M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16", "search": "M11 18a7 7 0 1 0 0-14 7 7 0 0 0 0 14zM21 21l-5-5",
    "globe": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18", "cog": "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1",
    "spark": "M12 3v5M12 16v5M3 12h5M16 12h5M6 6l3 3M15 15l3 3M6 18l3-3M15 9l3-3", "handshake": "M2 12l4-4 4 2 4-3 4 1 4 4-6 6-3-2-2 2-3-2zM10 10l3 3", "clock": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 7v5l3 2",
    "play": "M7 4l13 8-13 8z",
}


def svg(n):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{I[n]}"/></svg>'


def placeholder(name):
    p = os.path.join(PV, "img", name)
    if os.path.exists(p):
        return
    W, H = 1366, 854
    im = Image.new("RGB", (W, H), (244, 245, 248)); d = ImageDraw.Draw(im)
    h = sum(map(ord, name))
    d.rectangle([0, 0, 220, H], fill=(10, 21, 48))
    for k in range(7):
        d.rounded_rectangle([24, 90 + k * 52, 196, 120 + k * 52], 8, fill=(238, 75, 59) if k == h % 7 else (31, 46, 84))
    d.rectangle([220, 0, W, 64], fill=(255, 255, 255)); d.line([220, 64, W, 64], fill=(225, 229, 236), width=2)
    for k in range(4):
        x = 250 + k * 270
        d.rounded_rectangle([x, 96, x + 250, 196], 12, fill=(255, 255, 255), outline=(225, 229, 236))
        d.rectangle([x + 20, 120, x + 110, 132], fill=(200, 205, 214)); d.rectangle([x + 20, 146, x + 150, 172], fill=[(10, 127, 123), (31, 60, 122), (201, 48, 31), (185, 122, 0)][(k + h) % 4])
    d.rounded_rectangle([250, 226, W - 30, H - 30], 12, fill=(255, 255, 255), outline=(225, 229, 236))
    for r in range(11):
        y = 270 + r * 48
        d.line([270, y + 30, W - 50, y + 30], fill=(238, 240, 244), width=2)
        d.rectangle([280, y, 280 + 120 + (h * r) % 200, y + 12], fill=(190, 196, 206))
        d.rounded_rectangle([900, y - 4, 1010, y + 18], 10, fill=[(212, 240, 239), (253, 236, 200), (225, 230, 242)][(r + h) % 3])
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 22)
    except Exception:
        f = None
    d.text((250, 22), "preview placeholder: " + name, fill=(100, 110, 130), font=f)
    im.save(p, quality=80)


FORM = '''<form class="tf" id="pss-form"><label>What would you like to see?<select name="product"><option>Pentarch MediCore (health facilities)</option><option>Pentarch POS (point of sale)</option><option>Something else</option></select></label>
<label>Organisation or business name<input name="org" placeholder="e.g. Upendo Pharmacy"></label>
<div class="r2"><label>Your name<input name="name"></label><label>Phone or WhatsApp<input name="phone" inputmode="tel"></label></div>
<label>When suits you?<select name="when"><option>This week</option><option>Next week</option></select></label>
<label>Anything we should know?<textarea name="message"></textarea></label><div class="hp"><input name="website"></div><div class="err"></div>
<button class="go" type="submit">BUTTON</button><p>We use your details only to arrange the demo.</p></form>'''

FONT_CSS = ""
for fam, pkg, ws in [("Bricolage Grotesque", "bricolage-grotesque", (400, 500, 600, 700, 800)), ("DM Sans", "dm-sans", (400, 500, 600, 700)), ("JetBrains Mono", "jetbrains-mono", (400, 500, 600))]:
    for wt in ws:
        f = glob.glob(os.path.join(HERE, "fonts", f"fontsource-{pkg}-*", "package", "files", f"{pkg}-latin-{wt}-normal.woff2"))
        if f:
            FONT_CSS += f'@font-face{{font-family:"{fam}";font-weight:{wt};font-display:block;src:url("file://{f[0]}") format("woff2")}}\n'


def render(html):
    html = html.replace(' loading="lazy"', '')
    html = re.sub(r'<meta http-equiv="refresh"[^>]*>', '', html).replace("data-redirect=", "data-redirect-preview=")  # stay on the page in the preview
    html = re.sub(r"\{\{icon:([a-z]+)\}\}", lambda m: svg(m.group(1)), html)

    def med(m):
        name = os.path.basename(m.group(1).strip())
        real = os.path.join(IMG, name)
        if os.path.exists(real):  # the real image the plugin imports into the Media Library
            return "file://" + real
        placeholder(name); return "img/" + name
    html = re.sub(r"\{\{media:([^}]+)\}\}", med, html)
    html = re.sub(r'\[pss_lead_form[^\]]*button="([^"]+)"[^\]]*\]', lambda m: FORM.replace("BUTTON", m.group(1)), html)
    return html


def main():
    hd = open(os.path.join(PLUG, "blocks", "global-header.html")).read()
    ft = open(os.path.join(PLUG, "blocks", "global-footer.html")).read()
    for f in sorted(glob.glob(os.path.join(PLUG, "blocks", "*.html"))):
        slug = os.path.basename(f)[:-5]
        if slug.startswith("global-"):
            continue
        body = open(f).read()
        doc = f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{slug}</title>
<style>{FONT_CSS}body{{margin:0}}</style><script>document.documentElement.className+=' js';</script>
<link rel="stylesheet" href="file://{PLUG}/assets/pss.css"></head><body class="page-template-pss-canvas">
{render(hd)}<main class="wp-site-blocks">{render(body)}</main>{render(ft)}
<script src="file://{PLUG}/assets/pss.js"></script></body></html>'''
        open(os.path.join(PV, slug + ".html"), "w").write(doc)
    print("preview ok")


if __name__ == "__main__":
    main()
