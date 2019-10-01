import os
from concurrent.futures import as_completed, ProcessPoolExecutor
from itertools import chain, product
from time import perf_counter
from typing import Any, Callable, List

from graph import tuples_to_dict, Graph
from reader import read_graph
from solver import greedy2, NodeColors, Solver

FUNCTIONS = (greedy2,)


def loop(graph: Graph, filename: str, params: Any, func: Solver,
         iterations: int) -> List[str]:
    output = []
    for _ in range(iterations):
        start_time = perf_counter()
        _, colors = func(graph)
        diff = perf_counter() - start_time
        output.append(f'{os.path.basename(filename)}\t{params}\t'
                      f'{objective_function(colors)}\t{diff:.5f}')
    return output


def run_instance(filename: str, params: Any, func: Solver,
                 total_iterations: int = 100):
    graph = init_graph(filename)

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(loop, graph, filename, params, func,
                                   total_iterations // executor._max_workers)
                   for _ in range(total_iterations)]
        output = [f.result() for f in as_completed(futures)]

    with open(out_filename(filename, func), 'a') as file:
        file.write('\n'.join(chain.from_iterable(output)))
        file.write('\n')


def init_graph(filename: str) -> Graph:
    _, edges = read_graph(filename)
    vertex_neighbors = tuples_to_dict(edges)
    return vertex_neighbors


def out_filename(in_filename: str, func: Solver):
    basename = '.'.join(os.path.basename(in_filename).split(".")[:-1])

    return f'out/{basename}-{func.__name__}.txt'


def objective_function(colors: NodeColors) -> int:
    return max(colors.values()) + 1


def main():
    for filename, func in product(os.listdir('all-instances'), FUNCTIONS):
        print(filename)
        run_instance(f'all-instances/{filename}', None, func)


if __name__ == '__main__':
    main()
