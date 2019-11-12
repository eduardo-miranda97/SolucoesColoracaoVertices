from __future__ import annotations

from collections import defaultdict
from copy import copy
from itertools import count
from random import shuffle
from typing import Dict, Iterator, List

from numpy import roll

from graph import Graph


class Solution:
    graph: Graph
    node_order: List[int]
    _inv_node_order: Dict[int, int]
    _node_colors: Dict[int, int]
    _colors_count: int

    def __init__(self, graph: Graph, node_order: Iterator[int]):
        self.graph = graph
        self.node_order = list(node_order)
        self._inv_node_order = None
        self._node_colors = None
        self._colors_count = None

    @property
    def inv_node_order(self) -> Dict[int, int]:
        if self._inv_node_order is None:
            self.calculate_inv_node_order()
        return self._inv_node_order

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

    def calculate_inv_node_order(self):
        self._inv_node_order = {n: i for i, n in enumerate(self.node_order)}

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

    def swap_by_position(self, position1: int, position2: int) -> Solution:
        self.node_order[position1], self.node_order[position2] = (
        self.node_order[position2] , self.node_order[position1])
        self._node_colors, self._colors_count = None, None

    def delete_insert(self, position1: int, position2: int) -> Solution:
        solution = self.copy()
        value = solution.node_order.pop(position1)
        solution.node_order.insert(position2, value)
        self._node_colors, self._colors_count = None, None
        return solution

    def swapped_by_position(self, position1: int, position2: int):
        solution = self.copy()
        solution.swap_by_position(position1, position2)
        return solution

    def shift_solution(self, amount:int) -> Solution:
        solution = self.copy()
        solution.node_order = roll(solution.node_order, amount)
        self._node_colors, self._colors_count = None, None
        return solution

    def swap(self, node: int, position: int):
        node_position = self.inv_node_order[node]
        other_node = self.node_order[position]
        self.node_order[node_position], self.node_order[position] = (
            self.node_order[position], self.node_order[node_position])
        self._inv_node_order[node] = position
        self._inv_node_order[other_node] = node_position
        self._node_colors, self._colors_count = None, None

    def copy(self) -> Solution:
        return Solution(self.graph, copy(self.node_order))

    def swapped(self, node: int, position: int) -> Solution:
        solution = self.copy()
        solution.swap(node, position)
        return solution


def solver(graph: Graph, lazy: bool = False) -> Solution:
    raise NotImplementedError()


def random_solution(graph: Graph) -> Solution:
    node_order = list(range(1, len(graph) + 1))
    shuffle(node_order)
    return Solution(graph, node_order)
