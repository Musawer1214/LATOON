
def ring(cv, x, y, t, col=MINT, n=3, maxr=200, a=1, w=4):
    for k in range(n):
        u = (t * .7 + k / n) % 1
        cv.circ(x, y, 30 + u * maxr, outline=col, w=w, oa=a * (1 - u) * .8)

def tokw(cv, txt, size): return cv.tw(txt, size, "Black") + size * .7

def tokchip(cv, cx, cy, txt, size, col, a=1, sc=1.0, txtcol=None):
    w = tokw(cv, txt, size) * sc; h = size * 1.35 * sc
    if w < 4 or a <= .01: return
    cv.rrect(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, size * .28 * sc, fill=col, a=a)
    cv.text(cx, cy + size * .02, txt, size * sc, txtcol or INK, a, "Black")

def row(cv, cy, toks, size, gap, cols=None, a=None, cx=540, sc=None):
    ws = [tokw(cv, x, size) for x in toks]
    tot = sum(ws) + gap * (len(toks) - 1); x = cx - tot / 2; out = []
    for i, (tk, w) in enumerate(zip(toks, ws)):
        c = (cols or TCOL)[i % len(cols or TCOL)]
        out.append((x + w / 2, w))
        tokchip(cv, x + w / 2, cy, tk, size, c, 1 if a is None else a[i], 1 if sc is None else sc[i])
        x += w + gap
    return out

# ---- S0 hook: ChatGPT never saw a letter
def s0(cv, t, D):
    chip(cv, 540, 290, "HOW CHATGPT ACTUALLY READS", 28, INK, MINT, 1)
    kinetic(cv, t, 440, "NEVER SAW", 150, WHT, -.3, "Black", .02)
    kinetic(cv, t, 600, "A LETTER", 150, MINT2, -.2, "Black", .02)
    ring(cv, 540, 960, t, MINT, 3, 230)
    z = 1 + .04 * math.sin(t * 3)
    img(cv, "logo", 540, 960, .48 * z, 1)
    for i, ch in enumerate("HELLO"):
        x = 540 + (i - 2) * 150; y = 1270
        p = eback(pr(t, .1 + i * .08, .5 + i * .08), 2)
        cv.text(x, y + (1 - p) * 40, ch, 120, WHT, cl(p), "Black")
        q = eo(pr(t, .9 + i * .28, 1.2 + i * .28))
        if q > 0:
            cv.line([(x - 52, y + 38), (x - 52 + 104 * q, y - 38)], RED, 12, 1)

# ---- S1 chopped into tokens
def s1(cv, t, D):
    kinetic(cv, t, 330, "TOKENS", 130, MINT2, 0, "Black", .04)
    cv.text(540, 440, "your sentence gets chopped", 38, CREAM, eo(pr(t, .3, .7)), "SemiBold")
    toks = ["Chat", "GPT", "reads", "your", "words"]
    size = 50
    sweep = eio(pr(t, .45, 1.6))
    ws = [tokw(cv, x, size) for x in toks]
    gaps = [eback(pr(t, .55 + i * .2, .95 + i * .2), 2) for i in range(4)]
    tot = sum(ws) + 22 * sum(gaps)
    x = 540 - tot / 2; cy = 860
    for i, (tk, w) in enumerate(zip(toks, ws)):
        up = math.sin(cl((t - (.6 + i * .2)) * 3, 0, 3.14)) * 18 if t > .6 else 0
        tokchip(cv, x + w / 2, cy - up, tk, size, TCOL[i], eo(pr(t, 0, .3)))
        x += w + (22 * gaps[i] if i < 4 else 0)
    if 0 < sweep < 1:
        sx = lerp(540 - tot / 2 - 40, 540 + tot / 2 + 40, sweep)
        cv.line([(sx, cy - 110), (sx, cy + 110)], WHT, 6, .9)
        cv.circ(sx, cy - 118, 12, fill=WHT, a=.9)
    n = int(cl((t - .6) / .2, 0, 5) + .0001)
    n = min(5, max(0, int((t - .55) / .2) + 1)) if t > .55 else 0
    q = eback(pr(t, 1.9, 2.4), 2)
    chip(cv, 540, 1160, f"{n if t < 1.6 else 5} TOKENS", 52, INK, YEL, q)
    cv.text(540, 1275, "pieces of text, not letters", 34, MINT2, eo(pr(t, 2.4, 2.9)), "SemiBold")

# ---- S2 common vs rare
def s2(cv, t, D):
    cv.text(540, 330, "COMMON  vs  RARE", 66, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 580, "COMMON WORDS", 36, MINT2, eo(pr(t, .2, .6)), "Black")
    row(cv, 700, ["the", "water", "house"], 78, 36, [MINT, SKY, YEL], a=[eo(pr(t, .4 + i * .2, .8 + i * .2)) for i in range(3)])
    cv.text(540, 815, "one piece each", 34, CREAM, eo(pr(t, 1.2, 1.6)), "SemiBold")
    cv.text(540, 1010, "RARE WORDS", 36, PINK, eo(pr(t, 1.5, 1.9)), "Black")
    # quokka splits
    q = eo(pr(t, 2.0, 2.4)); g = eback(pr(t, 2.2, 2.9), 2)
    if t < 2.4:
        cv.text(540, 1150, "quokka", 120, WHT, eo(pr(t, 1.7, 2.1)) * (1 - q), "Black")
    row(cv, 1150, ["qu", "ok", "ka"], 92, 26 * g, [PINK, VIO, ORG], a=[q] * 3)
    cv.text(540, 1275, "split into smaller chunks", 34, CREAM, eo(pr(t, 3.0, 3.4)), "SemiBold")
    cv.text(540, 1335, "illustrative splits: real tokenizers differ", 24, MUT, .9 * eo(pr(t, 3.2, 3.6)), "Medium")

# ---- S3 unbelievably
def s3(cv, t, D):
    cv.text(540, 330, "ONE WORD,", 62, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 410, "THREE PIECES", 62, MINT2, eo(pr(t, .2, .6)), "Black")
    segs = ["un", "believ", "ably"]
    q = eo(pr(t, 1.0, 1.4))
    if q < .99:
        cv.text(540, 880, "unbelievably", 128, WHT, eo(pr(t, .1, .5)) * (1 - q), "Black")
    g = eback(pr(t, 1.2, 1.9), 2)
    row(cv, 880 - 30 * g, segs, 100, 30 * g, [MINT, YEL, PINK], a=[q] * 3)
    for i in range(3):
        p = eback(pr(t, 2.0 + i * .35, 2.5 + i * .35), 2)
        x = 540 + (i - 1) * 300
        cv.circ(x, 1090, 46 * p, fill=mix(CARDC, TCOL[i], .25), a=1, outline=TCOL[i], w=5)
        cv.text(x, 1092, str(i + 1), 56 * p, TCOL[i], cl(p), "Black")
    chip(cv, 540, 1240, "3 TOKENS", 50, INK, YEL, eback(pr(t, 3.3, 3.8), 2))
    cv.text(540, 1335, "illustrative split: real tokenizers differ", 24, MUT, .9 * eo(pr(t, 3.5, 3.9)), "Medium")

# ---- S4 BPE merging
STATES = [["t", "h", "e", "r", "e"], ["th", "e", "r", "e"], ["the", "r", "e"], ["the", "re"]]
MERGE_T = [1.0, 2.0, 3.0]
def s4(cv, t, D):
    cv.text(540, 330, "HOW CHUNKS ARE LEARNED", 54, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 395, "merge the most common pair", 38, MINT2, eo(pr(t, .3, .7)), "SemiBold")
    k = sum(1 for m in MERGE_T if t >= m)
    toks = STATES[k]
    cols = {0: [SKY] * 5, 1: [MINT, SKY, SKY, SKY], 2: [MINT, SKY, SKY], 3: [MINT, YEL]}[k]
    size = 110
    ws = [tokw(cv, x, size) for x in toks]; gap = 18
    tot = sum(ws) + gap * (len(toks) - 1); x = 540 - tot / 2; cy = 860
    # pulse on the pair about to merge
    nxt = MERGE_T[k] if k < 3 else None
    for i, (tk, w) in enumerate(zip(toks, ws)):
        sc = 1.0
        if nxt is not None and nxt - .7 < t < nxt and i in (0, 1) and k < 3:
            sc = 1 + .08 * math.sin((t - (nxt - .7)) * 14)
        c = cols[i]
        if nxt is not None and nxt - .7 < t < nxt and i in (0, 1) and k < 3:
            c = YEL
        pop = 1.0
        if k > 0 and i == (0 if k < 3 else 1) and t - MERGE_T[k - 1] < .4:
            pop = 1 + .25 * (1 - eo(pr(t, MERGE_T[k - 1], MERGE_T[k - 1] + .4)))
        if k == 3 and i == 0 and False: pass
        tokchip(cv, x + w / 2, cy, tk, size, c, 1, sc * pop)
        x += w + gap
    if nxt is not None and nxt - .7 < t < nxt:
        cv.text(540, 1020, "MOST FREQUENT PAIR", 36, YEL, eo(pr(t, nxt - .7, nxt - .4)), "Black")
    for i in range(3):
        on = t >= MERGE_T[i]
        cv.circ(340 + i * 200, 1170, 36, fill=mix(CARDC, MINT, .35) if on else CARDC, a=1, outline=MINT if on else DIMC, w=4)
        cv.text(340 + i * 200, 1172, f"{i + 1}", 36, INK if False else (MINT2 if on else DIMC), 1, "Black")
    cv.text(540, 1270, "merges  ·  repeated thousands of times", 32, CREAM, eo(pr(t, 2.9, 3.4)), "SemiBold")
DIMC = (40, 90, 92)

# ---- S5 IDs
IDS = ["31842", "38", "9301", "502", "7716"]
def s5(cv, t, D):
    cv.text(540, 320, "EACH PIECE GETS", 58, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 395, "A NUMBER", 72, MINT2, eo(pr(t, .2, .6)), "Black")
    toks = ["Chat", "GPT", "reads", "your", "words"]
    for i, tk in enumerate(toks):
        y = 590 + i * 135; s0_ = .3 + i * .28
        p = eback(pr(t, s0_, s0_ + .4), 1.8)
        tokchip(cv, 320, y, tk, 56, TCOL[i], cl(p), p)
        a2 = eo(pr(t, s0_ + .25, s0_ + .5))
        cv.line([(470, y), (560 + 40 * a2, y)], CREAM, 6, a2 * .8)
        cv.poly([(560 + 40 * a2, y - 16), (590 + 40 * a2, y), (560 + 40 * a2, y + 16)], CREAM, a2 * .8)
        # number scramble then resolve
        res = pr(t, s0_ + .45, s0_ + .95)
        if res > 0:
            txt = IDS[i]
            if res < 1:
                rng = (int(t * 30) * 7919 + i * 131) % 99999
                txt = "".join(str((rng // (10 ** k)) % 10) for k in range(len(txt)))
            cv.rrect(690, y - 44, 1000, y + 44, 22, fill=CARDC, a=1, outline=MINT, w=3, oa=.7)
            cv.text(845, y + 2, txt, 56, MINT2 if res >= 1 else CREAM, 1, "Black")
    chip(cv, 540, 1320, "A VOCABULARY OF TENS OF THOUSANDS", 28, INK, YEL, eback(pr(t, 2.6, 3.1), 2))
    cv.text(540, 1385, "example IDs, not real ones", 24, MUT, .9 * eo(pr(t, 2.9, 3.3)), "Medium")

# ---- S6 only numbers
def s6(cv, t, D):
    cv.text(540, 330, "INSIDE THE MODEL", 56, WHT, eo(pr(t, .05, .4)), "Black")
    img(cv, "logo", 540, 790, .5, 1)
    ring(cv, 540, 790, t, MINT, 2, 200, .8)
    for c in range(9):
        x = 150 + c * 100
        for r in range(7):
            u = ((t * .9 + c * .21 + r / 7.0) % 1)
            y = 450 + u * 200
            rng = (c * 977 + r * 31 + int(t * 3 + c) * 53) % 10
            cv.text(x, y, str(rng), 40, MINT, .6 * math.sin(u * math.pi), "Black")
    kinetic(cv, t, 1150, "ONLY NUMBERS", 104, MINT2, .3, "Black", .03)
    cv.text(540, 1260, "never the letters inside", 38, CREAM, eo(pr(t, 1.4, 1.9)), "SemiBold")

# ---- S7 strawberry
def s7(cv, t, D):
    kinetic(cv, t, 360, "HOW MANY R's", 100, WHT, 0, "Black", .03)
    cv.text(540, 460, "in  strawberry ?", 56, YEL, eo(pr(t, .4, .8)), "Black")
    toks = ["str", "aw", "berry"]
    ids = ["496", "675", "15717"]
    ws = [tokw(cv, x, 100) for x in toks]; gap = 26
    tot = sum(ws) + gap * 2; x = 540 - tot / 2; cy = 860
    for i, (tk, w) in enumerate(zip(toks, ws)):
        p = eback(pr(t, .6 + i * .15, 1.0 + i * .15), 2)
        m = eio(pr(t, 1.3 + i * .15, 1.9 + i * .15))
        tokchip(cv, x + w / 2, cy, tk, 100, TCOL[i + 1], cl(p) * (1 - m), p)
        if m > 0:
            cv.rrect(x, cy - 68, x + w, cy + 68, 28, fill=CARDC, a=m, outline=TCOL[i + 1], w=4, oa=m)
            cv.text(x + w / 2, cy + 2, ids[i], 56, TCOL[i + 1], m, "Black")
        x += w + gap
    q = eback(pr(t, 2.1, 2.6), 2.5)
    cv.text(540, 1100, "?", 190 * q, YEL, cl(q), "Black")
    cv.text(540, 1255, "the R's are hidden inside the pieces", 34, CREAM, eo(pr(t, 2.3, 2.8)), "SemiBold")
    cv.text(540, 1320, "illustrative split and IDs", 24, MUT, .9 * eo(pr(t, 2.5, 2.9)), "Medium")

# ---- S8 limits counted in tokens
def s8(cv, t, D):
    cv.text(540, 330, "CONTEXT LIMITS", 62, WHT, eo(pr(t, .05, .4)), "Black")
    cv.text(540, 400, "are counted in", 38, MINT2, eo(pr(t, .3, .7)), "SemiBold")
    x0, x1, y0, y1 = 100, 980, 640, 820
    cv.rrect(x0, y0, x1, y1, 30, fill=CARDC, a=1, outline=MINT, w=4, oa=.8)
    f = eio(pr(t, .3, 1.9)); n = 15
    for i in range(n):
        if i / n <= f:
            cx = x0 + 28 + i * ((x1 - x0 - 56) / n) + 24
            cv.rrect(cx - 24, y0 + 28, cx + 24, y1 - 28, 12, fill=TCOL[i % 6], a=.95)
    cv.text(540, 910, "context window", 32, MUT, eo(pr(t, .4, .8)), "SemiBold")
    q = eback(pr(t, 1.2, 1.7), 2)
    tokchip(cv, 330, 1130, "TOKENS", 66, MINT, cl(q), q)
    cv.text(330, 1250, "✓", 90, MINT, cl(q), "Black")
    q2 = eback(pr(t, 1.5, 2.0), 2)
    tokchip(cv, 760, 1130, "words", 66, mix(CARDC, WHT, .25), cl(q2), q2, txtcol=(130, 150, 150))
    cv.line([(660, 1130), (860, 1130)], RED, 8, eo(pr(t, 2.0, 2.3)))
    cv.text(760, 1250, "✗", 90, RED, eo(pr(t, 2.0, 2.3)), "Black")

# ---- S9 outro
def s9(cv, t, D):
    p = eo(pr(t, .1, .9))
    for k in range(5):
        u = (t * .35 + k / 5) % 1
        cv.circ(540, 640, 60 + u * 330, outline=MINT, w=4, oa=(1 - u) * .7 * p)
    img(cv, "logo", 540, 640, .5 * p, p)
    kinetic(cv, t, 1010, "LATOON", 150, WHT, .2, "Black", .06)
    cv.text(540, 1120, "Voyaging the Unseen", 46, YEL, eo(pr(t, 1.0, 1.5)), "SemiBold")
    cv.text(540, 1210, "now you read the way it does.", 32, MINT2, eo(pr(t, 1.8, 2.3)), "Medium")
    cv.text(540, 1290, "ChatGPT logo: OpenAI (public domain, Wikimedia Commons)", 20, MUT, .8 * eo(pr(t, 2.0, 2.5)), "Medium")

SCENES = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
