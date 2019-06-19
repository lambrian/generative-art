from pyx import *
import random
import sys

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(seed)

WIDTH = 600
HEIGHT = 30
DENSITY = .8

c.stroke(
    path.rect(1, 0, WIDTH, HEIGHT)
)

for x in range(1, (int)(WIDTH/DENSITY)):
    rc = rng.choice(range(int(WIDTH/DENSITY)))
    if rc > x:
        p = path.line(x*DENSITY, 0, x*DENSITY, HEIGHT)
        c.stroke(p, [style.linewidth(0.6)])

c.writePDFfile("output/lines/lines-%d-%d-%d-%d" % (WIDTH, HEIGHT, DENSITY, seed));


