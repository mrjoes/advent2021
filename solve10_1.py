TOKENS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

INCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

with open('input10t.txt') as fp:
    lines = [l.strip() for l in fp.readlines()]

    score = 0

    for l in lines:
        def process(l, s, e):
            global score

            k = l[s]
            if k not in TOKENS:
                return -2

            s += 1
            if s >= e:
                return -1

            while l[s] in TOKENS:
                s = process(l, s, e)
                if s < 0:
                    return s
                if s >= e:
                    return -1

            if l[s] != TOKENS[k]:
                score += SCORES[l[s]]
                return -2

            return s + 1

        process(l, 0, len(l) - 1)

    print(score)
