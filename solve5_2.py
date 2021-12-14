import re
from functools import reduce
from math import copysign

with open('input5.txt') as fp:
    lines = [[int(n) for n in re.match('(\d+),(\d+) -> (\d+),(\d+)', r).groups()] for r in fp.readlines()]

    state = {}

    mx = 0
    my = 0

    def dot(x, y):
        global mx
        global my

        c = (x, y)
        v = state.get(c)
        v = v + 1 if v else 1
        state[c] = v

        if c[0] > mx:
            mx = c[0] + 1
        if c[1] > my:
            my = c[1] + 1

    for l in lines:
        x0, y0, x1, y1 = l

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        x, y = x0, y0

        sx = 0 if not dx else (x1 - x0) / dx
        sy = 0 if not dy else (y1 - y0) / dy

        s = dx if dx > dy else dy

        while s >= 0:
            dot(x, y)
            x += sx
            y += sy
            s -= 1

    if False:
        for y in range(my):
            for x in range(mx):
                print(state.get((x, y), 0), end='')
            print()

    cnt = reduce(lambda a, b: a + (1 if state[b] > 1 else 0), state, 0)
    print(cnt)
