from random import shuffle
from timeit import timeit

from graph import tuples_to_dict
from local_search import simulated_annealing
from solution import Solution
from reader import read_graph

# VERTEXES = 2000
# DENSITY = 0.6
# ALPHA = 0.6
# AMOUNT_NEIGHBORS = 7
# INITIAL_TEMP = 100
# FINAL_TEMP = 10
# REHEAT_TIMES = 2
# NEIGHBOR_STRUCTURE = lc.SHIFT


def test_simulated_annealling():
    vertices, edges = read_graph('benchmarks/le450_25d.col')
    graph = tuples_to_dict(vertices, edges)
    order = list(range(1, len(graph) + 1))
    shuffle(order)
    solution1 = Solution(graph, order)
    best_solution = simulated_annealing(solution1)

    print('Inicial solution = ' + str(solution1.colors_count))
    print('Best solution = ' + str(best_solution.colors_count))


if __name__ == '__main__':
    print(timeit(test_simulated_annealling, number=1))
