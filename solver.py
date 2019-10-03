from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from itertools import count
from random import shuffle
from typing import Callable, Dict, List

from graph import Graph


@dataclass
class Solution:
    graph: Graph
    node_order: List[int]
    _node_colors: Dict[int, int] = field(init=False, default=None)
    _colors_count: int = field(init=False, default=None)

    @property
    def node_colors(self) -> Dict[int, int]:
        if self._node_colors is None:
            self.calculate_node_colors()
        return self._node_colors

    @property
    def colors_count(self) -> int:
        if self._colors_count is None:
            self.calculate_colors_count()
        return self._colors_count

    def calculate_node_colors(self):
        colors = {}
        neighbor_colors = defaultdict(set)
        for node in self.node_order:
            color = next(c for c in count()
                         if c not in neighbor_colors[node])
            colors[node] = color
            for neighbor in self.graph[node]:
                neighbor_colors[neighbor].add(color)
        self._node_colors = colors

    def calculate_colors_count(self):
        self._colors_count = max(self.node_colors.values()) + 1


Solver = Callable[[Graph, bool], Solution]


def greedy1(graph: Graph, lazy: bool = False) -> Solution:
    order = list(graph.keys())
    shuffle(order)
    solution = Solution(graph, order)
    if not lazy:
        solution.calculate_colors_count()
    return solution


def greedy2(graph: Graph, lazy: bool = False) -> Solution:

    inv_degree = defaultdict(list)
    for i, neighbors_ in graph.items():
        inv_degree[len(neighbors_)].append(i)

    order = []
    for degree_ in reversed(sorted(inv_degree.keys())):
        nodes = inv_degree[degree_]
        shuffle(nodes)
        order.extend(nodes)

    solution = Solution(graph, order)
    if not lazy:
        solution.calculate_colors_count()
    return solution
