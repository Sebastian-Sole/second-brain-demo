from PIL import Image, ImageDraw, ImageFilter
import math
import os
import random


SIZE = 1200
OUT_DIR = "assets/objects-transparent"
random.seed(42)


def jitter_points(points, amount=8):
    return [(x + random.uniform(-amount, amount), y + random.uniform(-amount, amount)) for x, y in points]


def line(draw, points, width=18, passes=3, jitter=5):
    for _ in range(passes):
        pts = jitter_points(points, jitter)
        draw.line(pts, fill=(8, 8, 7, 245), width=width + random.randint(-3, 3), joint="curve")


def polygon(draw, points, width=18, passes=3, jitter=5):
    pts = points + [points[0]]
    line(draw, pts, width=width, passes=passes, jitter=jitter)


def curve(draw, points, width=18, passes=3, jitter=5):
    for _ in range(passes):
        pts = jitter_points(points, jitter)
        draw.line(pts, fill=(8, 8, 7, 245), width=width + random.randint(-3, 3), joint="curve")


def rough_ellipse_points(cx, cy, rx, ry, start=0, end=math.tau, n=80, wobble=0.08):
    pts = []
    for i in range(n + 1):
        t = start + (end - start) * i / n
        rr_x = rx * (1 + random.uniform(-wobble, wobble))
        rr_y = ry * (1 + random.uniform(-wobble, wobble))
        pts.append((cx + math.cos(t) * rr_x, cy + math.sin(t) * rr_y))
    return pts


def hatch(draw, bbox, count=70, width=3):
    x0, y0, x1, y1 = bbox
    for _ in range(count):
        x = random.uniform(x0, x1)
        y = random.uniform(y0, y1)
        length = random.uniform(20, 90)
        angle = random.uniform(-0.7, 0.7)
        pts = [(x, y), (x + math.cos(angle) * length, y + math.sin(angle) * length)]
        draw.line(pts, fill=(8, 8, 7, random.randint(35, 95)), width=width)


def save(name, draw_fn):
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img, "RGBA")
    draw_fn(draw)
    img = img.filter(ImageFilter.GaussianBlur(0.25))
    os.makedirs(OUT_DIR, exist_ok=True)
    img.save(os.path.join(OUT_DIR, name))


def coffee(draw):
    top = rough_ellipse_points(600, 330, 190, 58, wobble=0.12)
    line(draw, top, width=19, passes=4, jitter=4)
    curve(draw, [(420, 330), (435, 410), (455, 475), (485, 875), (555, 910), (690, 895), (742, 468), (778, 400), (785, 332)], width=20, passes=4, jitter=7)
    curve(draw, rough_ellipse_points(602, 423, 205, 45, start=0.03, end=math.pi - 0.05, n=40, wobble=0.11), width=18, passes=3, jitter=4)
    curve(draw, rough_ellipse_points(600, 896, 110, 25, start=0.05, end=math.pi - 0.05, n=35, wobble=0.13), width=18, passes=3, jitter=4)
    curve(draw, [(738, 390), (752, 438), (742, 500), (730, 540)], width=25, passes=3, jitter=5)
    draw.ellipse((674, 300, 735, 335), fill=(8, 8, 7, 235))
    hatch(draw, (430, 300, 790, 905), count=95, width=4)


def keys(draw):
    curve(draw, rough_ellipse_points(600, 315, 180, 155, n=90, wobble=0.16), width=19, passes=4, jitter=5)
    curve(draw, rough_ellipse_points(437, 435, 55, 75, n=60, wobble=0.18), width=18, passes=3, jitter=5)
    curve(draw, rough_ellipse_points(608, 505, 70, 82, n=60, wobble=0.2), width=18, passes=3, jitter=5)
    curve(draw, rough_ellipse_points(770, 455, 62, 78, n=60, wobble=0.18), width=18, passes=3, jitter=5)
    line(draw, [(430, 500), (375, 715), (330, 900)], width=21, passes=4, jitter=8)
    polygon(draw, [(342, 892), (438, 918), (462, 862), (412, 842)], width=18, passes=3, jitter=7)
    line(draw, [(612, 585), (596, 788), (575, 955)], width=21, passes=4, jitter=8)
    line(draw, [(585, 795), (525, 815)], width=18, passes=3, jitter=6)
    line(draw, [(590, 852), (538, 892)], width=18, passes=3, jitter=6)
    line(draw, [(770, 530), (824, 685), (888, 850)], width=21, passes=4, jitter=8)
    line(draw, [(842, 735), (902, 710)], width=18, passes=3, jitter=6)
    line(draw, [(865, 795), (926, 802)], width=18, passes=3, jitter=6)
    polygon(draw, [(280, 520), (390, 455), (480, 610), (340, 690)], width=18, passes=3, jitter=8)
    hatch(draw, (285, 250, 915, 935), count=100, width=4)


def checklist(draw):
    polygon(draw, [(350, 185), (824, 240), (780, 918), (292, 870)], width=20, passes=4, jitter=9)
    curve(draw, [(350, 185), (332, 395), (315, 585), (292, 870)], width=20, passes=3, jitter=10)
    polygon(draw, [(420, 320), (500, 326), (492, 405), (410, 395)], width=17, passes=3, jitter=6)
    polygon(draw, [(405, 520), (488, 510), (500, 596), (415, 610)], width=17, passes=3, jitter=6)
    polygon(draw, [(395, 705), (478, 712), (468, 800), (385, 787)], width=17, passes=3, jitter=6)
    line(draw, [(430, 365), (462, 392), (542, 296)], width=19, passes=3, jitter=7)
    line(draw, [(423, 555), (458, 585), (535, 496)], width=19, passes=3, jitter=7)
    for y in (345, 390, 545, 590, 735, 785):
        line(draw, [(590 + random.randint(-12, 12), y), (785 + random.randint(-15, 15), y + random.randint(-8, 8))], width=14, passes=2, jitter=5)
    curve(draw, [(665, 915), (700, 828), (780, 818)], width=18, passes=3, jitter=7)
    hatch(draw, (305, 190, 810, 900), count=60, width=3)


def envelope(draw):
    polygon(draw, [(285, 430), (900, 400), (925, 830), (315, 865)], width=20, passes=4, jitter=9)
    line(draw, [(295, 435), (598, 665), (908, 405)], width=18, passes=3, jitter=8)
    line(draw, [(315, 855), (595, 665), (922, 825)], width=18, passes=3, jitter=8)
    polygon(draw, [(430, 250), (765, 290), (785, 560), (570, 650), (410, 520)], width=20, passes=3, jitter=10)
    curve(draw, [(420, 255), (516, 270), (655, 268), (760, 292)], width=17, passes=3, jitter=9)
    line(draw, [(505, 430), (650, 420)], width=15, passes=3, jitter=5)
    line(draw, [(530, 485), (700, 475)], width=15, passes=3, jitter=5)
    hatch(draw, (290, 250, 920, 860), count=80, width=3)


if __name__ == "__main__":
    save("coffee-cup-v2.png", coffee)
    save("keyring-v2.png", keys)
    save("checklist-v2.png", checklist)
    save("envelope-v2.png", envelope)

    def coffee_v3(draw):
        curve(draw, rough_ellipse_points(600, 330, 168, 46, n=56, wobble=0.1), width=18, passes=2, jitter=3)
        curve(draw, rough_ellipse_points(598, 390, 188, 38, start=0, end=math.pi, n=34, wobble=0.12), width=17, passes=2, jitter=4)
        line(draw, [(430, 350), (458, 612), (486, 870), (565, 900), (696, 882), (752, 350)], width=18, passes=2, jitter=7)
        line(draw, [(455, 500), (735, 508)], width=14, passes=2, jitter=5)
        draw.ellipse((680, 302, 730, 328), fill=(8, 8, 7, 230))
        curve(draw, [(735, 392), (750, 435), (738, 494)], width=19, passes=2, jitter=4)
        hatch(draw, (475, 520, 710, 860), count=18, width=3)

    def keys_v3(draw):
        curve(draw, rough_ellipse_points(608, 305, 150, 122, n=70, wobble=0.11), width=17, passes=2, jitter=4)
        curve(draw, rough_ellipse_points(454, 430, 45, 55, n=38, wobble=0.14), width=16, passes=2, jitter=4)
        curve(draw, rough_ellipse_points(615, 458, 50, 56, n=38, wobble=0.14), width=16, passes=2, jitter=4)
        curve(draw, rough_ellipse_points(762, 430, 48, 58, n=38, wobble=0.14), width=16, passes=2, jitter=4)
        line(draw, [(455, 480), (386, 700), (345, 845)], width=17, passes=2, jitter=7)
        line(draw, [(348, 845), (415, 865), (436, 815), (388, 800)], width=15, passes=2, jitter=6)
        line(draw, [(615, 515), (610, 705), (582, 905)], width=17, passes=2, jitter=7)
        line(draw, [(600, 735), (545, 752)], width=14, passes=2, jitter=5)
        line(draw, [(596, 805), (548, 836)], width=14, passes=2, jitter=5)
        line(draw, [(762, 490), (815, 660), (880, 835)], width=17, passes=2, jitter=7)
        line(draw, [(830, 705), (886, 690)], width=14, passes=2, jitter=5)
        line(draw, [(854, 770), (912, 782)], width=14, passes=2, jitter=5)
        polygon(draw, [(305, 500), (395, 462), (456, 580), (340, 650)], width=15, passes=2, jitter=7)
        hatch(draw, (320, 250, 900, 880), count=24, width=3)

    def checklist_v3(draw):
        polygon(draw, [(380, 230), (805, 260), (760, 880), (335, 845)], width=18, passes=2, jitter=8)
        for y in (355, 545, 735):
            polygon(draw, [(430, y), (505, y + 6), (498, y + 76), (420, y + 65)], width=14, passes=2, jitter=5)
        line(draw, [(438, 392), (466, 418), (535, 334)], width=16, passes=2, jitter=6)
        line(draw, [(435, 580), (466, 615), (542, 522)], width=16, passes=2, jitter=6)
        for y in (370, 410, 560, 605, 750, 795):
            line(draw, [(590, y), (755 + random.randint(-18, 18), y + random.randint(-10, 10))], width=12, passes=2, jitter=5)
        line(draw, [(690, 878), (728, 806), (760, 800)], width=16, passes=2, jitter=6)
        hatch(draw, (365, 260, 775, 850), count=18, width=3)

    def envelope_v3(draw):
        polygon(draw, [(315, 420), (870, 405), (900, 800), (340, 830)], width=18, passes=2, jitter=8)
        line(draw, [(328, 430), (590, 650), (865, 410)], width=16, passes=2, jitter=7)
        line(draw, [(342, 820), (590, 650), (898, 795)], width=16, passes=2, jitter=7)
        polygon(draw, [(438, 282), (750, 315), (760, 550), (590, 650), (420, 520)], width=17, passes=2, jitter=8)
        curve(draw, [(440, 282), (525, 296), (640, 298), (748, 315)], width=15, passes=2, jitter=7)
        line(draw, [(520, 435), (650, 426)], width=12, passes=2, jitter=5)
        line(draw, [(540, 490), (690, 480)], width=12, passes=2, jitter=5)
        hatch(draw, (340, 430, 880, 800), count=16, width=3)

    save("coffee-cup-v3.png", coffee_v3)
    save("keyring-v3.png", keys_v3)
    save("checklist-v3.png", checklist_v3)
    save("envelope-v3.png", envelope_v3)
