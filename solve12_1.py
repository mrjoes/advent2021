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
    paths = [[graph['start']]]

    final = []

    while True:
        new_paths = []

        count = 0

        for p in paths:
            for k in p[-1].neighbours:
                if k.name.islower() and k in p:
                    continue

                if k.name == 'end':
                    final.append(p + [k])
                    continue

                new_paths.append(p + [k])
                count += 1

        paths = new_paths

        if not count:
            break

    print(len(final))
