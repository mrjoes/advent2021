from collections import defaultdict
import re


with open('input14.txt') as fp:
    start = fp.readline().strip()
    fp.readline()
    rules = dict(re.match('(\w+) -> (\w+)', l).groups() for l in fp.readlines())

    pairs = defaultdict(int)

    # Add single letter to account for tail single letter
    start += ' '

    for a, b in zip(start, start[1:]):
        pairs[a + b] = 1

    for n in range(40):
        res = defaultdict(int)

        for p in pairs:
            if p in rules:
                res[p[0] + rules[p]] += pairs[p]
                res[rules[p] + p[1]] += pairs[p]
            else:
                res[p[0]] += 1

        pairs = res

        r = defaultdict(int)
        for p, v in pairs.items():
            r[p[0]] += v

    res = defaultdict(int)
    for p, v in pairs.items():
        res[p[0]] += v

    print(res)

    s = sorted(res.values())
    print(s[-1] - s[0])
