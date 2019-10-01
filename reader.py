from __future__ import annotations

from typing import Tuple, Set


def read_graph(filename: str) -> Tuple[int, Set[Tuple[int, int]]]:

    edges = set()

    with open(filename) as file:
        for line in file:
            line = (line.replace('\n', '')).split()
            if line:
                if line[0] == 'e':
                    edges.add((int(line[1]), int(line[2])))
                if line[0] == 'p':
                    vertices = int(line[2])

    return vertices, edges
