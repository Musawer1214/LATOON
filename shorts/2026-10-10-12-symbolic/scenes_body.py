def dotfield(cv, t, x0, y0, x1, y1, p, seed=3, step=44):
    rs = random.Random(seed)
    cols = [CORAL, MUST, TEAL, PAPER, mix(CORAL, MUST, .5), (90, 120, 150)]
    i = 0
    for yy in range(int(y0), int(y1), step):
        for xx in range(int(x0), int(x1), step):
            i += 1
            a = eo(pr(p, (i % 37) / 37 * .5, (i % 37) / 37 * .5 + .4))
            cv.circ(xx + rs.randint(-8, 8), yy + rs.randint(-8, 8), rs.randint(8, 15), fill=cols[rs.randint(0, 5)], a=a)
def s0(cv, t, D):
    kinetic(cv, t, 300, "NO WORDS INSIDE", 92, INKC, -.2, "Black", .02)
    kinetic(cv, t, 410, "ChatGPT", 56, MUST, .3, "Bold", .03)
    rs = random.Random(5)
    card(cv, 60, 480, 1020, 1260, 30, mix(BG1, PAPER, .08), eo(pr(t, .2, .6)))
    for r in range(11):
        for c in range(9):
            a = eo(pr(t, .5 + (r * 9 + c) * .008, .8 + (r * 9 + c) * .008))
            v = rs.uniform(-1, 1)
            txt = "%+.2f" % v
            cv.text(125 + c * 100, 540 + r * 62, txt, 30, CORAL if v < 0 else MUST, a * .9, "Bold")
    chip(cv, 110, 1300, 860, "HOW DOES IT FOLLOW GRAMMAR?", PAPER, eo(pr(t, 3.4, 3.9)), INK, 42, 96)
def s1(cv, t, D):
    kinetic(cv, t, 300, "PARIS, 1884", 104, INKC, -.2, "Black", .03)
    photo(cv, "seurat", 70, 450, 1010, 1100, t / D, 1.0, 1.3, .5, .6)
    brackets(cv, 70, 450, 1010, 1100, PAPER, eo(pr(t, .3, .8)) * .9)
    credit(cv, "Georges Seurat, A Sunday on La Grande Jatte (public domain)", 1130, eo(pr(t, .8, 1.3)))
    chip(cv, 110, 1200, 860, "THOUSANDS OF TINY DOTS", MUST, eo(pr(t, 2.2, 2.7)), INK, 46, 96)
def s2(cv, t, D):
    kinetic(cv, t, 300, "ZOOM IN, ZOOM OUT", 84, INKC, -.2, "Black", .02)
    z = eio(pr(t, 1.2, 3.4))
    photo(cv, "dots", 150, 450, 930, 1230, 0, 1.0, 1.0, .5, .5, a=1 - z)
    photo(cv, "seurat", 90, 520, 990, 1170, t / D, 1.0, 1.1, .5, .6, a=z)
    cv.text(540, 1300, "one dot: no meaning" if z < .5 else "together: a Sunday in the park", 44, MUST, 1, "Black")
def s3(cv, t, D):
    kinetic(cv, t, 300, "YALE STUDY", 110, INKC, -.2, "Black", .03)
    cv.text(540, 410, "Tom McCoy, linguist", 44, MUST, eo(pr(t, .3, .8)), "Bold")
    card(cv, 70, 500, 1010, 1020, 30, PAPER, eo(pr(t, .5, 1.0)))
    a = eo(pr(t, .9, 1.4))
    cv.text(540, 600, "LLM numbers", 40, INK, a, "Black")
    cv.text(540, 700, "[0.31, -0.84, 0.07, ...]", 44, mix(INK, PAPER, .25), a, "Bold")
    arrow(cv, 540, 760, 540, 860, CORAL, 9, eo(pr(t, 1.6, 2.1)))
    b = eo(pr(t, 2.1, 2.6))
    cv.text(540, 930, "hidden structure?", 54, CORAL, b, "Black")
    chip(cv, 110, 1100, 860, "arXiv preprint, Oct 2026", mix(PAPER, BG1, .2), eo(pr(t, 3.2, 3.7)), INKC, 38, 84)
def s4(cv, t, D):
    kinetic(cv, t, 300, "ROLES + FILLERS", 94, INKC, -.2, "Black", .02)
    words = ["cats", "chase", "dogs"]; roles = ["SUBJECT", "VERB", "OBJECT"]; cols = [MUST, CORAL, TEAL]
    for i in range(3):
        a = eo(pr(t, .4 + i * .9, .9 + i * .9))
        x = 70 + i * 320
        chip(cv, x, 520, 300, words[i], cols[i], a, INK, 52, 110)
        yy = 700 + (1 - a) * -40
    for i in range(3):
        a = eo(pr(t, 3.4 + i * .8, 3.9 + i * .8))
        x = 70 + i * 320
        cv.line([(x + 150, 640), (x + 150, 760)], PAPER, 5, a)
        card(cv, x, 770, x + 300, 920, 22, PAPER, a)
        cv.text(x + 150, 845, roles[i], 36, INK, a, "Black")
    q = eo(pr(t, 6.4, 7.0))
    cv.text(540, 1060, "the same trick, for fractions:", 36, MUST, q, "Bold")
    frac(cv, 330, 1210, "3", "4", 100, INKC, q)
    cv.text(540, 1160, "", 10, INKC, 0)
    cv.text(690, 1160, "numerator", 34, TEAL, q, "Black")
    cv.text(690, 1260, "denominator", 34, CORAL, q, "Black")
    cv.text(540, 1390, "7 large models tested", 34, ASH, eo(pr(t, 8.2, 8.7)), "SemiBold")
def s5(cv, t, D):
    kinetic(cv, t, 300, "THE TEST", 110, INKC, -.2, "Black", .03)
    a = eo(pr(t, .3, .8))
    cv.text(540, 440, "behavior barely changed", 46, MUST, a, "Bold")
    card(cv, 70, 520, 1010, 760, 30, PAPER, a)
    cv.text(540, 600, "the clever doctor helped a lawyer", 40, INK, a, "Black")
    cv.text(540, 680, "clever", 40, CORAL, a, "Black")
    # edit
    e = eio(pr(t, 3.4, 4.8))
    card(cv, 70, 840, 1010, 1080, 30, PAPER, eo(pr(t, 3.0, 3.5)))
    cv.text(540, 900, "edit one role inside the model", 34, mix(INK, PAPER, .3), eo(pr(t, 3.2, 3.7)), "Bold")
    cv.text(540, 990, "the doctor helped a clever lawyer", 40, INK, eo(pr(t, 4.6, 5.1)), "Black")
    cv.text(540, 1040, "", 10, INK, 0)
    arrow(cv, 540, 1090, 540, 1170, CORAL, 9, eo(pr(t, 5.0, 5.5)))
    chip(cv, 110, 1210, 860, "MODEL ACTS AS IF IT SAW THAT", MUST, eo(pr(t, 5.5, 6.0)), INK, 40, 96)
def s6(cv, t, D):
    kinetic(cv, t, 300, "PREPRINT", 120, INKC, -.2, "Black", .03)
    cv.text(540, 420, "not peer-reviewed yet", 44, MUST, eo(pr(t, .3, .8)), "Bold")
    a = eo(pr(t, .8, 1.3))
    card(cv, 70, 520, 1010, 1020, 30, PAPER, a)
    cv.text(540, 640, "\u201cOur work only scratches", 44, INK, a, "Black")
    cv.text(540, 710, "the surface\u2026\u201d", 44, INK, a, "Black")
    cv.text(540, 830, "Tom McCoy", 38, CORAL, a, "Black")
    cv.text(540, 890, "Yale University, Oct 8 2026", 28, mix(INK, PAPER, .35), a, "SemiBold")
    dotfield(cv, t, 100, 1100, 980, 1400, eo(pr(t, 1.2, 2.8)), 4, 56)
def s7(cv, t, D):
    p = eio(pr(t, 0, 1.6))
    dotfield(cv, t, 100, 1020, 980, 1420, p, 9, 60)
    kinetic(cv, t, 740, "LATOON", 150, INKC, -.1, "Black", .05)
    cv.text(540, 880, "Voyaging the unseen", 52, MUST, eo(pr(t, .9, 1.5)), "SemiBold")
    chip(cv, 280, 1110, 520, "FOLLOW", MUST, eo(pr(t, 1.6, 2.2)), INK, 44, 90)
SCENES = [s0, s1, s2, s3, s4, s5, s6, s7]
