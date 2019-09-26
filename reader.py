from __future__ import annotations

from typing import Tuple, Set


def read_graph(filename: str) -> Tuple[int, Set[Tuple[int, int]]]:
    edges = set()
    with open(filename) as f:
        for line in f:
            line = (line.replace('\n', '')).split(' ')
            if line[0] == 'e':
                edges.add((line[1], line[2]))
            if line[0] == 'p':
                vertices = int(line[2])
    return vertices, edges
