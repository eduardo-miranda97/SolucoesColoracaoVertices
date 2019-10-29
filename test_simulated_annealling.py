from random import shuffle

from graph import generate_graph
import annealling as ann
from solution import Solution

VERTEXES = 2000
DENSITY = 0.6
ALPHA = 0.6
AMOUNT_NEIGHBORS = 7
INITIAL_TEMP = 100
FINAL_TEMP = 10
REHEAT_TIMES = 2
NEIGHBOR_STRUCTURE = ann.SHIFT


def test_simulated_annealling():
    _, graph = generate_graph(VERTEXES, DENSITY)
    order = list(range(VERTEXES))
    shuffle(order)
    solution1 = Solution(graph, order)

    best_solution = ann.annealing(solution1, ALPHA, AMOUNT_NEIGHBORS,
    INITIAL_TEMP, FINAL_TEMP, REHEAT_TIMES, NEIGHBOR_STRUCTURE)

    print('Inicial solution = ' + str(solution1.colors_count))
    print('Best solution = ' + str(best_solution.colors_count))


if __name__ == '__main__':
    test_simulated_annealling()
