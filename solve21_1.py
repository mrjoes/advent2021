import re

with open('input21.txt') as fp:
    pos = [int(re.match('Player (\d+) starting position: (\d+)', l).groups()[1]) for l in fp.readlines()]
    scores = [0] * len(pos)

    r = 0
    c = 0

    def rnd():
        global r, c

        v = r
        c += 1
        r = (r + 1) % 100

        return v + 1

    won = None

    while won is None:
        for i in range(len(pos)):
            k = 0

            for n in range(3):
                k += rnd()

            pos[i] += k
            while pos[i] > 10:
                pos[i] -= 10

            scores[i] += pos[i]

            print(i, pos[i], scores[i], k)

            if scores[i] >= 1000:
                won = i
                break

    print(won, scores[0], scores[1], c)
    print(scores[len(scores) - won - 1] * c)
