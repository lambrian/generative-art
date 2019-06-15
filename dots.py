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

for x in range(1, (int)(WIDTH/DENSITY)):
    used_y = 0
    while used_y < HEIGHT:
        rc1 = rng.choice(range(int(WIDTH/DENSITY)))
        rc2 = rng.choice(range(int(WIDTH/DENSITY)))
        if rc1 > x and rc2 > x:
            circle = path.circle(x*DENSITY, used_y, 0.1)
            c.fill(circle)
        used_y += random.randrange(25, 100) * .01

c.writePDFfile("dots-%d-%d-%f-%f-%d" % (WIDTH, HEIGHT, DENSITY, RADIUS, seed));
