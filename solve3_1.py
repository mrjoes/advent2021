from functools import reduce

with open('input3t.txt') as fp:
    l = fp.readlines()
    r = [[int(c) for c in s.strip()] for s in l]
    t = reduce(lambda a, b: [(x + y) for x, y in zip(a, b)], r)
    print(t)

    m = len(l) // 2

    gamma = reduce(lambda a, b: a << 1 | (b >= m), t, 0)
    eps = (~gamma) & ((1 << len(r[0])) - 1)
    print(gamma * eps)
