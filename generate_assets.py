"""Generates the pixel-style SVGs for the README.
Edit the CONTENT section, then run:  python generate_assets.py
"""
import random, html, textwrap

# ---------------- CONTENT (edit this) ----------------
NAME = "ARNABH KUSHWAHA"
TAGLINE = "FULL-STACK DEV / UI-UX DESIGNER / VISXH"
SECTIONS = [
    ("WHO I AM",
     "Hey, I'm Arnabh - a 19-year-old developer and designer from Lucknow. I'm the founder of "
     "Hubrave, a tech-driven digital agency, and I'm studying BCA (Data Science & AI) at SRMU."),
    ("WHAT I DO",
     "I build web products end to end - React / Next.js frontends, Supabase and Node backends - and "
     "AI automations for real businesses, like voice call assistants and lead-response systems. "
     "I design in Figma before I write code. My team Sentinels got selected in Smart India Hackathon 2026."),
    ("VISION",
     "Build products people actually use and pay for, and grow Hubrave into a company that matters "
     "- not just another agency."),
    ("BEYOND CODE",
     "Making music as Visxh, playing with my band Kaaya, gaming, and running BGMI scrim tournaments."),
]
# ---------------- STYLE ----------------
BG, PANEL_BORDER, TEXT = "#1c1f24", "#30363d", "#d0d7de"
GREENS = ["#0e4429", "#006d32", "#26a641", "#39d353", "#7ee787"]
CREAM, ACCENTS = "#e6dccb", ["#58a6ff", "#f0883e"]
W = 900
rng = random.Random(7)

FONT = {
 'A':[" ### ","#   #","#   #","#####","#   #","#   #","#   #"],
 'B':["#### ","#   #","#   #","#### ","#   #","#   #","#### "],
 'C':[" ### ","#   #","#    ","#    ","#    ","#   #"," ### "],
 'D':["#### ","#   #","#   #","#   #","#   #","#   #","#### "],
 'E':["#####","#    ","#    ","#### ","#    ","#    ","#####"],
 'F':["#####","#    ","#    ","#### ","#    ","#    ","#    "],
 'G':[" ### ","#   #","#    ","# ###","#   #","#   #"," ####"],
 'H':["#   #","#   #","#   #","#####","#   #","#   #","#   #"],
 'I':[" ### ","  #  ","  #  ","  #  ","  #  ","  #  "," ### "],
 'J':["  ###","   # ","   # ","   # ","   # ","#  # "," ##  "],
 'K':["#   #","#  # ","# #  ","##   ","# #  ","#  # ","#   #"],
 'L':["#    ","#    ","#    ","#    ","#    ","#    ","#####"],
 'M':["#   #","## ##","# # #","# # #","#   #","#   #","#   #"],
 'N':["#   #","##  #","# # #","#  ##","#   #","#   #","#   #"],
 'O':[" ### ","#   #","#   #","#   #","#   #","#   #"," ### "],
 'P':["#### ","#   #","#   #","#### ","#    ","#    ","#    "],
 'Q':[" ### ","#   #","#   #","#   #","# # #","#  # "," ## #"],
 'R':["#### ","#   #","#   #","#### ","# #  ","#  # ","#   #"],
 'S':[" ####","#    ","#    "," ### ","    #","    #","#### "],
 'T':["#####","  #  ","  #  ","  #  ","  #  ","  #  ","  #  "],
 'U':["#   #","#   #","#   #","#   #","#   #","#   #"," ### "],
 'V':["#   #","#   #","#   #","#   #","#   #"," # # ","  #  "],
 'W':["#   #","#   #","#   #","# # #","# # #","# # #"," # # "],
 'X':["#   #","#   #"," # # ","  #  "," # # ","#   #","#   #"],
 'Y':["#   #","#   #"," # # ","  #  ","  #  ","  #  ","  #  "],
 'Z':["#####","    #","   # ","  #  "," #   ","#    ","#####"],
 '/':["    #","    #","   # ","  #  "," #   ","#    ","#    "],
 '-':["     ","     ","     ","#####","     ","     ","     "],
 ' ':["     "]*7,
}

def pixel_text(s, x, y, scale, color):
    out, cx = [], x
    for ch in s.upper():
        for r, row in enumerate(FONT.get(ch, FONT[' '])):
            for c, v in enumerate(row):
                if v == '#':
                    out.append(f'<rect x="{cx+c*scale}" y="{y+r*scale}" width="{scale}" height="{scale}" fill="{color}"/>')
        cx += 6 * scale
    return "".join(out), cx - x - scale

def text_width(s, scale): return len(s) * 6 * scale - scale

def glitch_bar(x0, x1, y, h):
    out, x = [], x0
    while x < x1:
        w = rng.choice([2, 3, 4, 6, 8, 10, 14])
        if rng.random() < 0.7:
            col = rng.choices([*GREENS, CREAM, *ACCENTS, "#8b949e"], weights=[2,3,3,3,2,3,1,1,2])[0]
            out.append(f'<rect x="{x}" y="{y}" width="{min(w, x1-x)}" height="{h}" fill="{col}"/>')
        x += w + rng.choice([0, 0, 1, 2, 4])
    return "".join(out)

def svg(h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}">'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{h-1}" rx="6" fill="{BG}" stroke="{PANEL_BORDER}"/>'
            f'{body}</svg>')

# ---------- header ----------
def header():
    H, parts = 250, []
    t, _ = pixel_text(NAME, 24, 22, 4, "#f0f0f0"); parts.append(t)
    cell, top, rows, cols = 10, 70, 13, W // 10
    for j in range(rows):
        for i in range(cols):
            tpos = i / cols
            dens = 0.9 if tpos < 0.4 else max(0.06, 0.9 - 1.7 * (tpos - 0.4))
            if rng.random() > dens: continue
            r = rng.random()
            col = rng.choice(ACCENTS) if r < 0.02 else CREAM if r < 0.1 else rng.choice(GREENS)
            x, y = i * cell, top + j * cell
            if rng.random() < 0.05:   # a few pixels flicker
                d, b = rng.uniform(2, 5), rng.uniform(0, 4)
                parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{col}">'
                             f'<animate attributeName="opacity" values="1;0.15;1" dur="{d:.1f}s" begin="{b:.1f}s" repeatCount="indefinite"/></rect>')
            else:
                parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{col}"/>')
    for _ in range(9):  # big cream blocks
        s = rng.choice([2, 3, 4]) * cell
        x = rng.randrange(int(W * 0.4), int(W * 0.8), cell)
        y = rng.randrange(top, top + rows * cell - s + 1, cell)
        parts.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{CREAM}"/>')
    t, _ = pixel_text(TAGLINE, W - 24 - text_width(TAGLINE, 2), 218, 2, "#f0f0f0"); parts.append(t)
    return svg(H, "".join(parts))

# ---------- about card ----------
def about():
    parts, y, pad = [], 26, 28
    font = "font-family=\"'Courier New',Consolas,'DejaVu Sans Mono',monospace\" font-size=\"13.5\""
    for title, body in SECTIONS:
        t, tw = pixel_text(title, pad, y, 3, "#f0f0f0"); parts.append(t)
        parts.append(glitch_bar(pad + tw + 24, W - pad, y + 6, 9))
        ly = y + 21 + 24
        for line in textwrap.wrap(body, 98):
            parts.append(f'<text x="{pad}" y="{ly}" fill="{TEXT}" {font}>{html.escape(line)}</text>')
            ly += 19
        y = ly + 18
    return svg(y, "".join(parts))

def heading(title):
    t, tw = pixel_text(title, 24, 14, 3, "#f0f0f0")
    return svg(50, t + glitch_bar(24 + tw + 24, W - 24, 20, 9))

for name, content in [("header", header()), ("about", about()), ("skillset", heading("SKILL SET"))]:
    open(f"assets/{name}.svg", "w").write(content)
print("done")
