from pyx import *
import random
import sys

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(seed)

WIDTH = 500
HEIGHT = 50
DENSITY = .25

for x in range(1, (int)(WIDTH/DENSITY)):
    rc = rng.choice(range(int(WIDTH/DENSITY)))
    if rc > x:
        p = path.line(x*DENSITY, 0, x*DENSITY, HEIGHT)
        c.stroke(p)

c.writePDFfile("lines-%d-%d-%d-%d" % (WIDTH, HEIGHT, DENSITY, seed));


