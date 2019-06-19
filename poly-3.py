from pyx import *
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
PRINT_DOTS = 1
PRINT_LINES = True

c.stroke(path.rect(0, 0, WIDTH + 1, HEIGHT + 1))

r = path.rect(1, 1, WIDTH, HEIGHT)
c.stroke(r,[style.linewidth(0.4)])
x = 0
current_x = 0
points_list = []
while current_x < WIDTH:
    used_x = x**(1.5)
    num_dots = INIT_M**(used_x*RATIO) * 100
    y_coords = random.sample(range(HEIGHT), min(HEIGHT, int(math.ceil(num_dots))))
    for y_coord in y_coords:
        if PRINT_DOTS:
            circle = path.circle(used_x, y_coord, 0.5)
            c.fill(circle)
        points_list.append((used_x, y_coord))
    current_x = used_x
    x += .5

line_x = 0
while line_x < x:
    line_used_x = line_x**(1.5)
    curr_points = filter(lambda point: point[0] == line_x**1.5, points_list)
    print "---"
    print curr_points
    eligible_points = filter(lambda point: point[0] == (line_x + .5)**(1.5), points_list)
    print eligible_points
    if len(eligible_points) == 0:
        break
    random.shuffle(curr_points)
    random.shuffle(eligible_points)
    for i in range(len(curr_points)):
        curr_point = curr_points[i]
        point_to_match = eligible_points[i % len(eligible_points)]
        c.stroke(
            path.line(curr_point[0], curr_point[1], point_to_match[0], point_to_match[1]),
            [style.linecap.round, style.linewidth(0.4)],
        )
    line_x += .5

c.writePDFfile("output/poly-3/poly-%d" % (seed));
