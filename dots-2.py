from pyx import *
import random
import sys

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(seed)

WIDTH = 600
HEIGHT = 100
DENSITY = 12
RADIUS = 0.5

x = WIDTH
while x > 1:
    used_y = 0
    while used_y < HEIGHT:
        rc1 = rng.choice(range(int(WIDTH)))
        rc2 = rng.choice(range(int(100)))
        if rc1 > x and rc2 > 1:
            circle = path.circle(x, used_y, 1)
            c.fill(circle)
        used_y += random.randrange(DENSITY, DENSITY * 2)
    x_d = random.randrange(DENSITY, DENSITY * 2)
    x = x - x_d

c.writePDFfile("poly-%d-%d-%f-%f-%d" % (WIDTH, HEIGHT, DENSITY, RADIUS, seed));
