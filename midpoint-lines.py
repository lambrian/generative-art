from pyx import *
import random
import sys

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(seed)

WIDTH = 600
HEIGHT = 50
DENSITY = 1
RADIUS = 0.5
LENGTH = 20

r = path.rect(1, -1, WIDTH, HEIGHT + 2)
c.stroke(r,[style.linewidth(0.4)])

for x in range(1, int(WIDTH/DENSITY)):
    used_y = random.randrange(0, 5) * .25
    while used_y < HEIGHT:
        rc1 = rng.choice(range(int(WIDTH/DENSITY)))
        rc2 = rng.choice(range(int(WIDTH/DENSITY)))
        if rc1 > x and rc2 > x:
            p = path.line(
                max(x*DENSITY - LENGTH/2, 1),
                used_y,
                min(x*DENSITY + LENGTH/2, WIDTH),
                used_y,
            )
            c.stroke(p, [style.linewidth(0.4), style.linecap.round])
        used_y += random.randrange(0, 10) * .5

c.writePDFfile("output/midpoint-lines/midpoint-lines-%d" % (seed));
