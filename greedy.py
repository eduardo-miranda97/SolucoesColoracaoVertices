from collections import defaultdict
from random import shuffle

from graph import Graph
from solution import Solution


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
