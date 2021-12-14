from functools import reduce


def flt(s, inv):
    res = s

    for i in range(len(s[0])):
        if len(res) == 1:
            return res[0]

        t = reduce(lambda a, b: [(x + y) for x, y in zip(a, b)], res)
        m = len(res) / 2
        b = [int(x >= m) for x in t]

        res = list(filter(lambda n: n[i] == b[i] ^ inv, res))

    return res[0]


def tobin(t):
    return reduce(lambda a, b: a << 1 | b, t, 0)


with open('input3.txt') as fp:
    l = fp.readlines()
    r = [[int(c) for c in s.strip()] for s in l]

    oxy = tobin(flt(r, 0))
    co2 = tobin(flt(r, 1))

    print(oxy * co2)
