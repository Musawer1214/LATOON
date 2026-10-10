def star(cv, x, y, r, col, a=1):
    cv.circ(x, y, r * 1.0, fill=mix(col, (0, 0, 0), .45), a=a)
    cv.circ(x - r * .08, y - r * .1, r * .88, fill=col, a=a)
    cv.circ(x - r * .3, y - r * .32, r * .3, fill=mix(col, WHT, .55), a=.6 * a)
def pulsar(cv, x, y, r, t, a=1):
    for k in range(3):
        q = (t * .9 + k / 3) % 1
        cv.circ(x, y, r * (1.2 + q * 2.6), fill=None, outline=PAPER, w=3, oa=.5 * (1 - q) * a)
    cv.circ(x, y, r, fill=PAPER, a=a); cv.circ(x, y, r * .55, fill=YEL, a=a)
def s0(cv, t, D):
    kinetic(cv, t, 300, "3 STARS", 130, INKC, -.2, "Black", .03)
    kinetic(cv, t, 430, "3 DESTINIES", 100, YEL, -.1, "Black", .03)
    img(cv, "art", 540, 1000, 1.0 + .03 * pr(t, 0, 4), eo(pr(t, .0, .6)))
    chip(cv, 200, 1370, 680, "BORN TOGETHER", RED, eo(pr(t, 1.6, 2.2)), INKC, 38)
def s1(cv, t, D):
    head(cv, t, "A PULSAR", "FAST telescope, found 2020", YEL)
    img(cv, "fast", 540, 880, 1.0 + .02 * pr(t, 0, 6), eo(pr(t, .0, .5)))
    q = eo(pr(t, 2.2, 2.8)); chip(cv, 140, 1260 + (1 - q) * 70, 800, "SPINS EVERY 3.2 MILLISECONDS", YEL, q, INK, 32, 76)
    cv.text(540, 1400, "a dead star, one turn faster than a blink", 30, MUTE, eo(pr(t, 3.8, 4.4)), "SemiBold")
def s2(cv, t, D):
    head(cv, t, "THE INNER PAIR", "one orbit every 8 days", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    cx, cy = 540, 970
    cv.circ(cx, cy, 250, fill=None, outline=mix(PAPER, INK, .3), w=3, oa=.8)
    a = t * 3.2
    pulsar(cv, cx + math.cos(a) * 70, cy + math.sin(a) * 70, 30, t)
    star(cv, cx - math.cos(a) * 220, cy - math.sin(a) * 220, 46, (236, 236, 226))
    cv.text(540, 1300, "pulsar + white dwarf", 34, INK, eo(pr(t, 1.2, 1.8)), "Black")
def s3(cv, t, D):
    head(cv, t, "A MYSTERY", "slowing ~100x too fast", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    n = int(100 * eo(pr(t, .5, 2.6)))
    cv.text(540, 800, f"{max(1, n)}x", 190, RED, 1, "Black")
    cv.text(540, 960, "faster slowdown than similar pulsars", 34, INK, eo(pr(t, 1.2, 1.8)), "Bold")
    cv.line([(220, 1100), (860, 1100)], mix(PAPER, INK, .4), 4)
    pulsar(cv, 330, 1210, 28, t)
    q = eo(pr(t, 2.6, 3.4)); 
    cv.text(640, 1215, "who is pulling?", 52, INK, q, "Black")
def s4(cv, t, D):
    head(cv, t, "THE THIRD STAR", "73.5-year orbit", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    cx, cy = 460, 970
    # elongated orbit e=.6
    pts = []
    for k in range(121):
        th = k / 120 * 2 * math.pi
        r = 150 / (1 - .6 * math.cos(th)) * .85
        pts.append((cx + r * math.cos(th) - 120, cy + r * math.sin(th) * .62))
    cv.line(pts, mix(PAPER, INK, .35), 4)
    pulsar(cv, cx - 120 + 0, cy, 14, t)
    th = t * 1.1 + 2.5
    r = 150 / (1 - .6 * math.cos(th)) * .85
    star(cv, cx + r * math.cos(th) - 120, cy + r * math.sin(th) * .62, 44, YEL)
    chip(cv, 230, 1270, 620, "ABOUT 1 SUN OF MASS", YEL, eo(pr(t, 1.8, 2.4)), INK, 32, 70)
def s5(cv, t, D):
    head(cv, t, "A HIDDEN HAND", "on the pulse clock", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    shift = math.sin(t * 2.2) * 30 * eo(pr(t, 1.0, 1.8))
    for k in range(12):
        x = 180 + k * 62 + shift * (k / 11)
        cv.line([(x, 880), (x, 1060)], mix(INK, PAPER, .1), 6)
    cv.line([(170, 1080), (900, 1080)], mix(PAPER, INK, .5), 4)
    cv.text(540, 760, "PULSES ARRIVE LATE, THEN EARLY", 34, INK, 1, "Black")
    cv.text(540, 1200, "gravity changes the timing", 38, RED, eo(pr(t, 1.2, 1.8)), "Black")
def s6(cv, t, D):
    kinetic(cv, t, 450, "THREE PATHS", 110, INKC, 0, "Black", .03)
    card(cv, 100, 560, 980, 1400, 34)
    rows = [("~20 SUNS", "supernova, now a pulsar", RED, 30), ("SEVERAL SUNS", "now a white dwarf", MUTE, 22), ("ABOUT 1 SUN", "still alive", YEL, 46)]
    for i, (a_, b_, c, r) in enumerate(rows):
        q = eo(pr(t, .3 + i * 1.9, .9 + i * 1.9)); y = 740 + i * 220
        star(cv, 220, y, r * q, c) if i != 0 else pulsar(cv, 220, y, 22, t, q)
        cv.text(630, y - 24, a_, 44, INK, q, "Black"); cv.text(630, y + 34, b_, 30, mix(INK, PAPER, .2), q, "Bold")
def s7(cv, t, D):
    head(cv, t, "SECOND EVER", "pulsar + star triple", YEL)
    card(cv, 100, 560, 980, 1380, 34)
    cv.text(540, 860, "2nd", 200, RED, eo(pr(t, .2, .8)), "Black")
    cv.text(540, 1020, "known pulsar triple", 46, INK, eo(pr(t, .6, 1.2)), "Black")
    chip(cv, 170, 1180, 740, "FIRST WITH A LIVING STAR", YEL, eo(pr(t, 1.6, 2.2)), INK, 34, 76)
def s8(cv, t, D):
    kinetic(cv, t, 760, "LATOON", 150, YEL, 0, "Black", .05)
    cv.text(540, 900, "Voyaging the unseen", 48, INKC, eo(pr(t, .6, 1.2)), "Bold")
    cv.text(540, 1000, "Follow for more", 40, MUTE, eo(pr(t, 1.1, 1.7)), "SemiBold")
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8]
