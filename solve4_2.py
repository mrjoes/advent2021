#!/usr/bin/env python3
import re
import os

with open('input4.txt') as fp:
    # Read data
    draws = [int(x) for x in fp.readline().split(',')]

    def read_board():
        board = []

        fp.readline()

        for _ in range(5):
            l = [int(x) for x in re.split('\s+', fp.readline()) if x]
            if not l:
                return None

            board.append(l)

        return board

    boards = []

    while True:
        b = read_board()
        if not b:
            break

        boards.append(b)

    # Solve
    def solve():
        indexes = [{c: (x, y) for y, r in enumerate(b) for x, c in enumerate(r)} for b in boards]
        state_x = [[0, 0, 0, 0, 0] for _ in range(len(boards))]
        state_y = [[0, 0, 0, 0, 0] for _ in range(len(boards))]

        num_boards = len(indexes)

        for d in draws:
            for b, i in enumerate(indexes):
                if not i:
                    continue

                m = i.get(d)
                if m:
                    del(i[d])

                    x, y = m

                    state_x[b][x] += 1
                    state_y[b][y] += 1

                    if state_x[b][x] == 5 or state_y[b][y] == 5:
                        if num_boards == 1:
                            return indexes[b], d

                        indexes[b] = None
                        num_boards -= 1

    index, d = solve()
    print(sum(index.keys()) * d)
