from collections import defaultdict
from itertools import count
from random import sample
from typing import Dict

from graph import tuples_to_dict_bi
from reader import read_graph


def greedy1(filename: str) -> Dict[int, int]:

    _, edges = read_graph(filename)
    vertex_neighbors = tuples_to_dict_bi(edges)

    colors = dict()
    for vertex, neighbors in sample(vertex_neighbors.items(),
                                    k=len(vertex_neighbors)):
        for i in count():
            if all(colors.get(n, None) != i for n in neighbors):
                colors[vertex] = i
                break

    return colors


def greedy2(filename: str) -> Dict[int, int]:

    _, edges = read_graph(filename)
    neighbors = tuples_to_dict_bi(edges)

    inv_degree = defaultdict(list)
    for i, neighbors_ in neighbors.items():
        inv_degree[len(neighbors_)].append(i)

    colors = {}
    neighbor_colors = defaultdict(set)

    for degree_ in reversed(sorted(inv_degree.keys())):
        nodes = inv_degree[degree_]
        for node in sample(nodes, k=len(nodes)):
            color = next(c for c in count()
                         if c not in neighbor_colors[node])
            colors[node] = color
            for neighbor in neighbors[node]:
                neighbor_colors[neighbor].add(color)

    return colors
