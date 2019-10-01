from __future__ import annotations

from collections import defaultdict
from itertools import count
from random import sample
from typing import Dict, List, Tuple

from graph import Graph

NodeOrder = List[int]
NodeColors = Dict[int, int]


def greedy1(vertex_neighbors: Graph) -> Tuple[NodeOrder, NodeColors]:

    order = []
    colors = {}
    for vertex, neighbors in sample(vertex_neighbors.items(),
                                    k=len(vertex_neighbors)):
        for i in count():
            if all(colors.get(n, None) != i for n in neighbors):
                colors[vertex] = i
                order.append(vertex)
                break

    return order, colors


def greedy2(vertex_neighbors: Graph) -> Tuple[NodeOrder, NodeColors]:

    inv_degree = defaultdict(list)
    for i, neighbors_ in vertex_neighbors.items():
        inv_degree[len(neighbors_)].append(i)

    order = []
    colors = {}
    neighbor_colors = defaultdict(set)

    for degree_ in reversed(sorted(inv_degree.keys())):
        nodes = inv_degree[degree_]
        for node in sample(nodes, k=len(nodes)):
            color = next(c for c in count()
                         if c not in neighbor_colors[node])
            colors[node] = color
            order.append(node)
            for neighbor in vertex_neighbors[node]:
                neighbor_colors[neighbor].add(color)

    return order, colors
