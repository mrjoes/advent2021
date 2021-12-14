from functools import reduce

with open('input1.txt') as fp:
    n = [int(v) for v in fp.readlines()]
    print(reduce(lambda a, b: a + int(b), (a < b for a, b in zip(n, n[1:]))))
