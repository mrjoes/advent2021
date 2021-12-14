class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


with open('input12.txt') as fp:
    graph = {'start': Node('start'), 'end': Node('end')}

    for l in fp.readlines():
        f, t = l.strip().split('-')

        fn = graph.get(f)
        if not fn:
            fn = Node(f)
            graph[f] = fn

        tn = graph.get(t)
        if not tn:
            tn = Node(t)
            graph[t] = tn

        fn.neighbours.append(tn)
        tn.neighbours.append(fn)

    queue = [graph['start']]
    paths = [[False, graph['start']]]

    final = []

    while True:
        new_paths = []

        count = 0

        for p in paths:
            for k in p[-1].neighbours:
                if k.name == 'start':
                    continue

                if k.name == 'end':
                    final.append(p + [k])
                    continue

                flag = p[0]

                if k.name.islower():
                    c = p.count(k)

                    if c > 0:
                        if p[0]:
                            continue
                        elif c == 1:
                            flag = True

                new_paths.append([flag] + p[1:] + [k])
                count += 1

        paths = new_paths

        if not count:
            break

    print(len(final))
