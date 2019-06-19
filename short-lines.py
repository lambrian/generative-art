from pyx import *
import random
import sys

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(seed)

WIDTH = 300
HEIGHT = 25
DENSITY = 1
RADIUS = 0.5

for x in range(1, int(WIDTH/DENSITY)):
    used_y = random.randrange(0, 100) * .02
    while used_y < HEIGHT:
        rc1 = rng.choice(range(int(WIDTH/DENSITY)))
        rc2 = rng.choice(range(int(WIDTH/DENSITY)))
        if rc1 > x and rc2 > x:
            p = path.line(
                x*DENSITY,
                used_y,
                x*DENSITY + DENSITY,
                random.randrange(-DENSITY, DENSITY*2)*.5 + used_y
            )
            c.stroke(p, [style.linewidth(0.4), style.linecap.round])
        used_y += random.randrange(100) * .02

c.writePDFfile("output/short-lines-output/short-lines-%d-%d-%f-%f-%d" % (WIDTH, HEIGHT, DENSITY, RADIUS, seed));
