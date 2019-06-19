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
points_list = []
while current_x < WIDTH:
    used_x = x**(1.5)
    num_dots = INIT_M**(used_x*RATIO) * 100
    y_coords = random.sample(range(1, HEIGHT, 2), min(HEIGHT/2, int(math.ceil(num_dots))))
    for y_coord in y_coords:
        if PRINT_DOTS:
            circle = path.circle(used_x, y_coord, 0.5)
            c.fill(circle)
        points_list.append((used_x, y_coord))
    current_x = used_x
    x += .5
r = path.rect(1, 1, current_x, HEIGHT - 2)
c.stroke(r,[style.linewidth(0.4)])

if PRINT_LINES:
    filled_points = Set(filter(lambda point: point[0] < 1**1.5, points_list))
    line_x = 0
    while line_x < x:
        line_used_x = line_x**(1.5)
        curr_points = filter(lambda point: point[0] == line_x**1.5, filled_points)
        eligible_points = filter(lambda point: point[0] > (line_x)**(1.5) and point[0] < (line_x + 3)**(1.5), points_list)
        print len(eligible_points)
        if len(eligible_points) == 0:
            break
        random.shuffle(curr_points)
        random.shuffle(eligible_points)
        for a in curr_points:
            points_to_connect = random.sample(eligible_points, min(len(eligible_points), 2))
            filled_points.update(points_to_connect)
            for b in points_to_connect:
                c.stroke(
                    path.line(a[0], a[1], b[0], b[1]),
                    [style.linecap.round, style.linewidth(0.75)],
                )

        line_x += .5

if PRINT_DOTS:
    for point in filled_points:
        circle = path.circle(point[0], point[1], 0.25)
        c.fill(circle)

c.writePDFfile("output/poly-3/poly-%d" % (seed));
