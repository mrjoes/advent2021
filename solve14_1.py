import re
from collections import Counter


with open('input14.txt') as fp:
    start = fp.readline().strip()
    fp.readline()
    rules = dict(re.match('(\w+) -> (\w+)', l).groups() for l in fp.readlines())

    for n in range(10):
        res = ''

        for p, c in zip(start, start[1:]):
            v = p + c
            res = res[:-1] + p + rules[v] + c

        start = res

        print(n)

    s = sorted(dict(Counter(start)).values())
    print(s[-1] - s[0])
