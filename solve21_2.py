import re
from itertools import product
from functools import lru_cache


with open('input21.txt') as fp:
    pos = [int(re.match('Player (\d+) starting position: (\d+)', l).groups()[1]) for l in fp.readlines()]

    rolls = [sum(n) for n in product(range(1, 4), repeat=3)]

    def calc(p, s, r):
        np = ((p - 1 + r) % 10) + 1
        ns = s + np
        return np, ns

    d = 0

    @lru_cache(maxsize=None)
    def play(player, p0, s0, p1, s1):
        global d
        d += 1
        if d % 100000:
            print(d)

        if s0 >= 21:
            return 1, 0
        elif s1 >= 21:
            return 0, 1

        wins = [0, 0]

        for r in rolls:
            if player == 0:
                np, ns = calc(p0, s0, r)
                w0, w1 = play(1, np, ns, p1, s1)
            else:
                np, ns = calc(p1, s1, r)
                w0, w1 = play(0, p0, s0, np, ns)

            wins[0] += w0
            wins[1] += w1

        return wins

    wins = play(0, pos[0], 0, pos[1], 0)
    print(wins)
