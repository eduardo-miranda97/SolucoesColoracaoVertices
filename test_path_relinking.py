from random import shuffle

from graph import generate_graph
from path_relinking import path_relinking
from solution import Solution

VERTEXES = 100
DENSITY = 0.5


def test_path_relinking():
    _, graph = generate_graph(VERTEXES, DENSITY)
    order = list(range(VERTEXES))
    shuffle(order)
    solution1 = Solution(graph, order)
    shuffle(order)
    solution2 = Solution(graph, order)
    best = path_relinking(solution1, solution2)
    for sol in (solution1, solution2, best):
        print(sol.colors_count, sol.node_order)


if __name__ == '__main__':
    test_path_relinking()
