with open('input6.txt') as fp:
    fishies = [0] * 9

    for f in fp.readline().split(','):
        fishies[int(f)] += 1

    for n in range(256):
        k = fishies[0]
        fishies = fishies[1:] + [0]
        fishies[8] += k
        fishies[6] += k

    print(sum(fishies))
