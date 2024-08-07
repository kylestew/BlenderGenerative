# %%
import geom.data as dat
import geom.ops as ops

import numpy as np

import geom_cairo as ctx


def make_line(x_pos, y_pos, height):
    line = dat.Line((x_pos, y_pos), (x_pos, y_pos + height))
    line.attribs = {ctx.STROKE: [0, 0, 0, 0.3]}
    return line


COUNT = 512

y_pos = 0.0
height = 0.18

xs = np.random.uniform(0, 1, size=COUNT)
lines = [make_line(x, y_pos, height) for x in xs]


poly = dat.Polygon([[0, 0], [1, 0], [1, 1]])

count = 10_000

pts = ops.scatter_pts(poly, count)

print("PTS CREATED:", len(pts))


# %%
## == DISPLAY ===================================================================
ctx.setup(900, 900, clear_color=[0, 0, 100], range=[-0.1, 1.1])

ctx.draw(lines, attribs={ctx.STROKE: [0.0, 0.0, 0.0, 0.5], ctx.LINE_WIDTH: 0.01})

ctx.draw(poly, attribs={ctx.STROKE: [1.0, 0.0, 0.0, 0.5], ctx.LINE_WIDTH: 1.0})
ctx.draw(pts, attribs={ctx.STROKE: [1, 1, 1, 0.8]})

ctx.display()
