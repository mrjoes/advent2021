TOKENS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

INCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

with open('input10.txt') as fp:
    lines = [l.strip() for l in fp.readlines()]

    scores = []

    for l in lines:
        score = 0

        def process(l, s, e):
            global score

            k = l[s]
            if k not in TOKENS:
                return -2

            s += 1

            if s < e:
                while l[s] in TOKENS:
                    s = process(l, s, e)
                    if s < 0:
                        if s == -1:
                            score = score * 5 + INCOMPLETE[TOKENS[k]]
                            return s
                        else:
                            return s

                    if s >= e:
                        break

            if s >= e:
                score = score * 5 + INCOMPLETE[TOKENS[k]]
                return -1

            if l[s] != TOKENS[k]:
                return -2

            return s + 1

        e = len(l)
        s = 0

        while s < e:
            s = process(l, s, e)
            if s < 0:
                break

        scores.append(score)

    a = sorted(s for s in scores if s)

    print(a[len(a) // 2])
