import sys
from itertools import count, product
from random import sample

from reader import read_graph

H, E = read_graph(sys.argv[1])

vertex_neighbors = dict()
for edge, (i, j) in product(E, ((0, 1), (1, 0))):
    vertex_neighbors.setdefault(edge[i], set()).add(edge[j])

colors = dict()
for vertex, neighbors in sample(vertex_neighbors.items(),
                                k=len(vertex_neighbors)):
    for i in count():
        if all(colors.get(n, None) != i
               for n in sample(neighbors, k=len(neighbors))):
            colors[vertex] = i
            break

print(colors)
print(max(colors.values()) + 1)
