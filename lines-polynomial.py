from pyx import *
from sets import Set
import random
import sys
import math

SEED = None

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(SEED or seed)

WIDTH = 600
HEIGHT = 30
INIT_M = 0.3
RATIO = .013
PRINT_DOTS = 0
PRINT_LINES = True

x = 0
current_x = 0
while current_x < WIDTH:
    used_x = x**(1.5)
    print used_x
    c.stroke(
        path.line(used_x, 1, used_x, HEIGHT)
    )
    current_x = used_x
    x += .5

c.writePDFfile("output/lines/lines-%d" % (seed));
