from itertools import chain
from math import log
from random import shuffle
from typing import Iterator, List, Optional, Tuple

from graph import Graph
from solution import Solution, random_solution

Step = Tuple[int, int]


def get_steps(source: Solution, target: Solution) -> List[Step]:
    positions = set()
    steps = []
    for i, node in enumerate(target.node_order):
        node_pos = source.inv_node_order[node]
        if source.node_order[i] != node and (i, node_pos) not in positions:
            steps.append((node, i))
            positions.add((node_pos, i))
    return steps


def do_path(source: Solution, steps: List[Step],
            order: Iterator[int]) -> Iterator[Solution]:
    solution = source
    for step in map(steps.__getitem__, order):
        solution = solution.swapped(*step)
        yield solution


def path_relinking(source: Solution, target: Solution,
                   tries: Optional[int] = None) -> Solution:
    steps = get_steps(source, target)

    if tries is None:
        tries = max(int(log(len(steps))), 1)

    checked = set()
    solutions = [[source, target]]
    order = list(range(len(steps)))
    while tries > 0:
        shuffle(order)
        order_key = tuple(order)
        if order_key not in checked:
            solutions.append(do_path(source, steps, order_key))
            checked.add(order_key)
            tries -= 1

    return min(chain.from_iterable(solutions), key=lambda s: s.colors_count)


def path_relinking_standalone(graph: Graph, **kwargs) -> Solution:
    return path_relinking(random_solution(graph), random_solution(graph))
