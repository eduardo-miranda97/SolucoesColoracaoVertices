from __future__ import annotations
import random
from itertools import islice
from typing import List, Dict, Iterator
from collections import defaultdict

from solution import Solution
from graph import Graph


def grasp(graph: Graph, 
          max_iterations_without_improvements: int = 100) -> Solution:
    iterations = 0
    while iterations < max_iterations_without_improvements:
        solution = grasp_construction_phase(graph)
        print(solution.node_order)
        iterations += 1


def grasp_construction_phase(graph: Graph, rcl_size: int = 5,
                             lazy: bool = False) -> Solution:
    inv_degree = defaultdict(list)
    for i, neighbors_ in graph.items():
        inv_degree[len(neighbors_)].append(i)

    order = []
    for degree_ in rcl_iterator(graph, inv_degree, rcl_size):
        nodes = inv_degree[degree_]
        random.shuffle(nodes)
        order.extend(nodes)

    solution = Solution(graph, order)
    if not lazy:
        solution.calculate_colors_count()
    return solution


def rcl_iterator(graph: Graph, inv_degree: Dict[int, List[int]],
                 rcl_size: int) -> Iterator[int]:
    degrees = sorted(inv_degree.keys())
    while degrees:
        rcl = get_rcl(inv_degree, degrees, rcl_size)
        node = random.sample(rcl, 1)[0]
        yield node
        degree = len(graph[node])
        inv_degree[degree].remove(node)
        if not inv_degree[degree]:
            degrees.remove(degree)


def get_rcl(inv_degree: Dict[int, List[int]], degrees: List[int],
            number: int) -> List[int]:
    rcl = []
    remaining = number
    for degree in reversed(degrees):
        rcl.extend(islice(inv_degree[degree], remaining))
        remaining = number - len(rcl)
        if not remaining:
            break

    return rcl
