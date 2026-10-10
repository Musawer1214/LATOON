from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, sys
sys.path.insert(0, "src")
FD = "/workspace/latoon/template/inter/extras/ttf/Inter-%s.ttf"
def f(w, s): return ImageFont.truetype(FD % w, s)
SER = "/workspace/latoon/branding/fonts/PlayfairDisplay.ttf"
CREAM = (250, 244, 230); OX = (176, 52, 42); INK = (33, 30, 28); AMB = (255, 196, 64)
W, H = 1920, 1080
def cover(im, cx=.5, cy=.5, z=1.0):
    r = max(W / im.width, H / im.height) * z; im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x0 = int((im.width - W) * cx); y0 = int((im.height - H) * cy); return im.crop((x0, y0, x0 + W, y0 + H))
def ot(d, xy, t, font, fill, sw=8, anchor="lm", stroke=(18, 15, 12)):
    d.text(xy, t, font=font, fill=fill, stroke_width=sw, stroke_fill=stroke, anchor=anchor)
def stampbox(im, xy, txt, size, rot, col=OX):
    fnt = f("Black", size); tw = int(fnt.getlength(txt)); pad = int(size * .45)
    m = Image.new("L", (tw + 2 * pad, int(size * 1.25) + 2 * pad), 0); dd = ImageDraw.Draw(m)
    dd.text((m.width / 2, m.height / 2), txt, font=fnt, fill=255, anchor="mm")
    dd.rounded_rectangle((6, 6, m.width - 6, m.height - 6), int(size * .18), outline=255, width=max(4, size // 12))
    rng = np.random.default_rng(3); a = np.asarray(m, np.float32) / 255 * np.where(rng.random((m.height, m.width)) < .1, .3, 1.0)
    m = Image.fromarray((a * 245).astype(np.uint8)).rotate(rot, Image.BICUBIC, expand=True)
    im.paste(Image.new("RGB", m.size, col), (int(xy[0] - m.width / 2), int(xy[1] - m.height / 2)), m)
def grade(im, warm=.1):
    a = np.asarray(im.convert("RGB"), np.float32); g = a.mean(2, keepdims=True); a = a * .85 + g * .15
    a = a * (1 - warm) + np.array([255, 232, 196]) * (a / 255) * warm; return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
def leftdark(im, k=.78):
    g = Image.new("L", (W, H)); gd = ImageDraw.Draw(g)
    for x in range(W): gd.line([(x, 0), (x, H)], fill=int(max(0, 235 * (1 - x / (W * k)))))
    return Image.composite(Image.new("RGB", (W, H), (20, 16, 13)), im, g)
def save(im, name):
    im = im.resize((1280, 720), Image.LANCZOS); im.save(name, optimize=True)
# A: real machine + A≠A
im = leftdark(grade(cover(Image.open("img/machine_rama.jpg"), .75, .5, 1.05)), .7)
d = ImageDraw.Draw(im)
ot(d, (90, 300), "ENIGMA'S", f("Black", 120), CREAM)
ot(d, (90, 440), "FATAL FLAW", f("Black", 132), AMB)
stampbox(im, (430, 700), "A \u2260 A", 150, -7, (214, 70, 54))
d.text((1840, 1040), "LATOON", font=f("Black", 40), fill=CREAM, anchor="rm")
save(im, "thumb_A.png")
# B: the missing L on paper
from lib import background
import lib
bg = background().convert("RGB"); d = ImageDraw.Draw(bg)
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mono = ImageFont.truetype("/usr/share/fonts/opentype/urw-base35/NimbusMonoPS-Bold.otf", 92)
for i, ch in enumerate(letters):
    r, c = divmod(i, 9); x = 360 + c * 150; y = 230 + r * 170
    if ch == "L":
        d.rounded_rectangle((x - 58, y - 70, x + 58, y + 70), 10, fill=(232, 220, 196), outline=OX, width=6)
        d.ellipse((x - 105, y - 105, x + 105, y + 105), outline=OX, width=10)
        d.text((x, y), "L", font=mono, fill=(214, 170, 160), anchor="mm")
    else:
        d.rounded_rectangle((x - 58, y - 70, x + 58, y + 70), 10, fill=(247, 243, 233), outline=(198, 185, 160), width=3)
        d.text((x, y), ch, font=mono, fill=INK, anchor="mm")
ot(d, (960, 880), "THE MISSING LETTER", f("Black", 120), CREAM, 10, "mm")
d.text((1840, 1040), "LATOON", font=f("Black", 40), fill=(80, 72, 64), anchor="rm")
save(bg, "thumb_B.png")
# C: Rejewski before Turing
bg = background().convert("RGB")
def card(base, path, cx, cy, w, h, rot):
    p = grade(Image.open(path)); r = max(w / p.width, h / p.height); p = p.resize((int(p.width * r) + 1, int(p.height * r) + 1), Image.LANCZOS)
    x0 = (p.width - w) // 2; y0 = max(0, (p.height - h) // 4); p = p.crop((x0, y0, x0 + w, y0 + h))
    c = Image.new("RGBA", (w + 36, h + 36), (247, 243, 233, 255)); c.paste(p, (18, 18)); c = c.rotate(rot, Image.BICUBIC, expand=True)
    sh = Image.new("RGBA", (c.width + 80, c.height + 80), (0, 0, 0, 0)); m = Image.new("L", sh.size, 0); m.paste(c.split()[3].point(lambda v: v * 0.45), (40, 40))
    sh.putalpha(m.filter(ImageFilter.GaussianBlur(16))); base.paste(sh, (int(cx - sh.width / 2 + 14), int(cy - sh.height / 2 + 20)), sh)
    base.paste(c, (int(cx - c.width / 2), int(cy - c.height / 2)), c)
card(bg, "img/machine_milan.jpg", 1470, 560, 560, 620, 4)
card(bg, "img/rejewski.jpg", 1000, 520, 470, 600, -4)
d = ImageDraw.Draw(bg)
ot(d, (90, 380), "BROKEN", f("Black", 150), CREAM, 10)
ot(d, (90, 560), "BEFORE", f("Black", 150), CREAM, 10)
ot(d, (90, 740), "TURING", f("Black", 150), AMB, 10)
stampbox(bg, (1020, 900), "1932", 80, -6)
d.text((1840, 1040), "LATOON", font=f("Black", 40), fill=(80, 72, 64), anchor="rm")
save(bg, "thumb_C.png")
