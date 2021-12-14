from functools import reduce

with open('input1.txt') as fp:
    n = [int(v) for v in fp.readlines()]
    sums = [sum(v) for v in zip(n, n[1:], n[2:])]
    print(reduce(lambda a, b: a + int(b), (a < b for a, b in zip(sums, sums[1:]))))
