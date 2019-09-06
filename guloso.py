import sys
from itertools import product, count

E = set()

with open(sys.argv[1]) as f:
    for line in f:
        line = (line.replace('\n', '')).split(' ')
        if (line[0] == 'e'):
            E.add((line[1], line[2]))
        if (line[0] == 'p'):
            H = int(line[2])

vizinhos = dict()

for edge in E:
    vizinhos.setdefault(edge[0], set()).add(edge[1])
    vizinhos.setdefault(edge[1], set()).add(edge[0])

cores = dict()

for vertex, neighbors in vizinhos.items():
    for i in count():
        if all(cores.get(n, None) != i for n in neighbors):
            cores[vertex] = i
            break

print(cores)
print(max(cores.values()) + 1)

