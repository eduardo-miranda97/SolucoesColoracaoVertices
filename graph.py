from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product
from random import random
from typing import Any, Dict, Iterator, Set, Tuple

Edge = Tuple[int, int]
Graph = Dict[int, Set[int]]


def generate_graph(num_nodes: int, density: float):

    num_edges = 0
    graph = defaultdict(set)

    for i, j in combinations(range(1, num_nodes + 1), 2):
        if i != j and random() < float(density):
            num_edges += 1
            graph[i].add(j)
            graph[j].add(i)

    graph = dict(graph)

    return num_edges, graph


def export_col(num_nodes: int, num_edges: int, graph: Graph,
               extra: Dict[str, Any]) -> str:

    output = [f'c {k}: {v}' for k, v in extra.items()]

    output.append(f'\np edge {num_nodes} {num_edges}')

    for source, dest in dict_to_tuples(graph):
        output.append(f'e {source} {dest}')

    return '\n'.join(output)


def export_dot(graph: Graph) -> str:

    output = []
    for source, dest in dict_to_tuples(graph):
        output.append(f'{source} -- {dest}')

    node_params = '\n'.join(
        f'{i} [label={len(j)}]'
        for i, j in graph.items())

    return '\n'.join(('graph {', node_params, '\n'.join(output), '}'))


def tuples_to_dict(vertices: int, edges: Iterator[Edge]) -> Graph:

    missing = set(range(1, vertices + 1))
    graph = defaultdict(set)
    directions = ((0, 1), (1, 0))
    for edge, (i, j) in product(edges, directions):
        graph[edge[i]].add(edge[j])
        try:
            missing.remove(edge[i])
        except KeyError:
            pass

    for key in missing:
        graph[key]

    return dict(graph)


def dict_to_tuples(graph: Graph) -> Set[Edge]:

    edges = set()
    for node, neighbors in graph:
        for neighbor in neighbors:
            edges.add((node, neighbor) if node < neighbor
                      else (neighbor, node))

    return edges
