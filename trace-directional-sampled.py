from pyx import *
import random

NOISE = 0.1
MIN_THRESHOLD = 0.
MAX_THRESHOLD = 0.1
HEIGHT = 100

class DirectionalTrace:
  def init_canvas(self):
    self.canvas = canvas.canvas()

  def get_line(self, base_x_pts):
    curr_x_pts = []
    direction = 1
    for i in range (0, len(base_x_pts)):
      curr_x_pt = base_x_pts[i + random.randrange(-3, 0)]
      next_rx_pt = min(max(MIN_THRESHOLD, random.uniform(0, direction * NOISE)), MAX_THRESHOLD)
      curr_x_pts.append(base_x_pts[i] + max(0, next_rx_pt))
      if (next_rx_pt >= MAX_THRESHOLD or next_rx_pt <= MIN_THRESHOLD):
        direction = -direction
    return curr_x_pts

  def draw_line(self, x_pts):
    p = path.path(path.moveto(x_pts[0], 0))
    for y in range(1, len(x_pts)):
      p.append(path.lineto(x_pts[y], y))
    self.canvas.stroke(p, [deformer.smoothed(0.3)])

  def draw(self):
    line = [0] * HEIGHT
    self.draw_line(line)
    for x in range(1, HEIGHT):
      next_line = self.get_line(line)
      self.draw_line(next_line)
      line = next_line

  def print_canvas(self):
    self.canvas.writePDFfile('trace-directional-sampled-3')

  def main(self):
    self.init_canvas()
    self.draw()
    self.print_canvas()


if __name__ == "__main__":
  DirectionalTrace().main()
