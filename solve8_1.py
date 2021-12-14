from collections import defaultdict
import itertools


MASKS = [
    {'a', 'b', 'c', 'e', 'f', 'g'},
    {'c', 'f'},
    {'a', 'c', 'd', 'e', 'g'},
    {'a', 'c', 'd', 'f', 'g'},
    {'b', 'c', 'd', 'f'},
    {'a', 'b', 'd', 'f', 'g'},
    {'a', 'b', 'd', 'e', 'f', 'g'},
    {'a', 'c', 'f'},
    {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    {'a', 'b', 'c', 'd', 'f', 'g'},
]

LEN_RULES = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

def subsets(ss):
    return itertools.chain(*map(lambda x: itertools.combinations(ss, x), range(0, len(ss)+1)))


with open('input8.txt') as fp:
    c = 0

    while True:
        l = fp.readline()
        if not l:
            break

        a, b = l.split('|')

        segments = [set(n.strip()) for n in a.split(' ') if n]
        digits = [''.join(sorted(n.strip())) for n in b.split(' ') if n]

        opts = defaultdict(set)

        for s in segments:
            r = LEN_RULES.get(len(s))
            if r is not None:
                opts[r] = s

        for s in segments:
            if len(s) == 5:
                if len(s - opts[1]) == 3:
                    opts[3] = s
                elif len(s - opts[4]) == 2:
                    opts[5] = s
                else:
                    opts[2] = s
            elif len(s) == 6:
                if len(s - opts[4]) == 2:
                    opts[9] = s
                elif len(s - opts[1]) == 4:
                    opts[0] = s
                else:
                    opts[6] = s

        m = {''.join(sorted(v)): k for k, v in opts.items()}

        acc = 0

        for d in digits:
            acc = acc * 10 + m[d]

        c += acc

    print(c)
