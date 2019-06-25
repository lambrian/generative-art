from pyx import *
from sets import Set
import random
import sys
import math
import statistics

SEED = None

c = canvas.canvas()
seed = random.randrange(sys.maxsize)
rng = random.Random(SEED or seed)

WIDTH = 600
HEIGHT = 30
INIT_SOURCE_COUNT = 5
MAX_X_DELTA = 5.0
MAX_Y_DELTA = 2.0

# place initial sources
roots = map(lambda y: (0, y), random.sample(range(HEIGHT), INIT_SOURCE_COUNT))

i = 0
while len(filter(lambda root: root[0] < WIDTH, roots)) > 0:
    print "iteration %d" % i
    i += 1
    print "before roots: %d" % len(roots)
    roots = filter(lambda root: root[0] < WIDTH - 5, roots)
    print "after roots: %d" % len(roots)
    new_roots = []
    # randomly select some roots to kill
    for root in roots:
        curr_x = root[0]
        curr_y = root[1]
        if curr_x >= WIDTH:
            continue
        y_delta = random.uniform(
            min(-1, -1 * (MAX_Y_DELTA - MAX_Y_DELTA*curr_y/WIDTH)),
            max(1.0, MAX_Y_DELTA - MAX_Y_DELTA*curr_y/WIDTH),
        )
        new_x = min(
            root[0] + random.uniform(
                max((MAX_X_DELTA/WIDTH * (WIDTH - curr_x))/2, 1.0),
                MAX_X_DELTA/WIDTH * (WIDTH - curr_x)
            ),
            WIDTH,
        )
        new_y = max(min(root[1] + y_delta, HEIGHT), 0)
        c.stroke(
            path.line(curr_x, curr_y, new_x, new_y),
            [style.linecap.round, style.linewidth(1.0 / WIDTH * (WIDTH - curr_x))],
        )
        new_roots.append((new_x, new_y))
        if abs(y_delta) > .75 and random.random() > .98:
            new_x = min(root[0] + random.uniform(0.5, 2.0), WIDTH)
            new_y = new_y = max(min(root[1] + -1*y_delta, HEIGHT), 0)
            c.stroke(
                path.line(curr_x, curr_y, new_x, new_y),
                [style.linecap.round, style.linewidth(1.0 / WIDTH * (WIDTH - curr_x))],
            )
            new_roots.append((new_x, new_y))
    roots = new_roots
    if len(roots) > 0:
        mean_x = statistics.mean(map(lambda root: root[0], roots))
        print mean_x
        num_roots_to_kill = int(len(roots) - WIDTH / 30)
        print "# roots %d, mean_x %f, killing %d roots" % (len(roots), mean_x, num_roots_to_kill)
        random.shuffle(roots)
        roots = roots[0:len(roots) - num_roots_to_kill]

c.writePDFfile("output/roots/roots-%d" % (seed));
