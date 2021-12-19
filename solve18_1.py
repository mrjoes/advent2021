import json
import math


class Value:
    is_value = True

    def __init__(self, p, i, v):
        self.parent = p
        self.idx = i
        self.value = v

    def __str__(self):
        return str(self.value)


class Node:
    is_value = False

    def __init__(self, p, i):
        self.parent = p
        self.idx = i
        self.nodes = [None, None]

    def __str__(self):
        return '[%s, %s]' % (self.nodes[0], self.nodes[1])


def tree(n):
    def walk(p, i, v):
        t = Node(p, i)
        t.nodes = [walk(t, i, k) if isinstance(k, list) else Value(t, i, k) for i, k in enumerate(v)]
        return t

    return walk(None, 0, n)


def add(a, b):
    n = Node(None, 0)

    n.nodes[0] = a
    a.parent = n
    a.idx = 0

    n.nodes[1] = b
    b.parent = n
    b.idx = 1

    return n


def add_left(r, i, v):
    while i >= 0:
        if r.nodes[i].is_value:
            r.nodes[i].value += v
            return True
        elif add_left(r.nodes[i], 1, v):
            return True

        i -= 1

    if r.parent:
        return add_left(r.parent, r.idx - 1, v)

    return False


def add_right(r, i, v):
    while i <= 1:
        if r.nodes[i].is_value:
            r.nodes[i].value += v
            return True
        elif add_right(r.nodes[i], 0, v):
            return True

        i += 1

    if r.parent:
        return add_right(r.parent, r.idx + 1, v)

    return False


def explode(r, d=0):
    if r.nodes[0].is_value and r.nodes[1].is_value and d >= 4:
        r.parent.nodes[r.idx] = Value(r.parent, r.idx, 0)

        add_left(r.parent, r.idx - 1, r.nodes[0].value)
        add_right(r.parent, r.idx + 1, r.nodes[1].value)

        return True

    for n in r.nodes:
        if not n.is_value:
            if explode(n, d + 1):
                return True

    return False


def split(r):
    for n in r.nodes:
        if n.is_value:
            if n.value > 9:
                nn = Node(n.parent, n.idx)
                nn.nodes[0] = Value(nn, 0, math.floor(n.value / 2))
                nn.nodes[1] = Value(nn, 1, math.ceil(n.value / 2))
                n.parent.nodes[n.idx] = nn
                return True
        else:
            if split(n):
                return True

    return False


def reduce(r):
    while True:
        if explode(r):
            print('exp', r)
            continue

        if split(r):
            print('spl', r)
            continue

        break


def magnitude(r):
    c = (r.nodes[0].value if r.nodes[0].is_value else magnitude(r.nodes[0])) * 3
    c += (r.nodes[1].value if r.nodes[1].is_value else magnitude(r.nodes[1])) * 2
    return c


with open('input18.txt') as fp:
    lines = fp.readlines()

    t = None

    for l in lines:
        j = json.loads(l)
        if not t:
            t = tree(j)
        else:
            t = add(t, tree(j))

        reduce(t)

    print(t)
    print(magnitude(t))
