from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product
from random import random
from typing import Any, Dict, Iterator, Set, Tuple

Edge = Tuple[int, int]
Graph = Dict[int, Set[int]]


def generate_graph(num_nodes: int, density: float):

    num_edges = 0
    neighbors = defaultdict(set)

    for i, j in combinations(range(int(num_nodes)), 2):
        if i != j and random() < float(density):
            num_edges += 1
            neighbors[i].add(j)

    return num_edges, neighbors


def export_col(num_nodes: int, num_edges: int,
               uni_neighbors: Graph,
               extra: Dict[str, Any]) -> str:

    output = [f'c {k}: {v}' for k, v in extra.items()]

    output.append(f'\np edge {num_nodes} {num_edges}')

    for source, dests in uni_neighbors:
        for dest in dests:
            output.append(f'e {source} {dest}')

    return '\n'.join(output)


def export_dot(uni_neighbors: Graph) -> str:

    output = []
    for source, dests in uni_neighbors:
        for dest in dests:
            output.append(f'{source} -- {dest}')

    bi_neighbors = uni_to_bi(uni_neighbors)

    node_params = '\n'.join(
        f'{i} [label={len(j)}]'
        for i, j in bi_neighbors.items())

    return '\n'.join(('graph {', node_params, '\n'.join(output), '}'))


def tuples_to_dict(edges: Iterator[Edge]) -> Graph:

    vertex_neighbors = {}
    for edge, (i, j) in product(edges, ((0, 1), (1, 0))):
        vertex_neighbors.setdefault(edge[i], set()).add(edge[j])

    return vertex_neighbors


def uni_to_bi(graph: Graph) -> Graph:

    result = {}

    for source, dests in graph:
        for dest in dests:
            result[dest] = source

    result.update(graph)

    return result
