import os
from concurrent.futures import as_completed, ProcessPoolExecutor
from itertools import product
from time import perf_counter
from typing import Any, Callable, Tuple

from graph import tuples_to_dict, Graph
from reader import read_graph
from solver import greedy1, greedy2, NodeColors, NodeOrder

FUNCTIONS = greedy1, greedy2


def single_run(graph, filename, params, func) -> str:
    start_time = perf_counter()
    _, colors = func(graph)
    diff = perf_counter() - start_time
    return (f'{os.path.basename(filename)}\t'
            f'{params}\t'
            f'{objective_function(colors)}\t'
            f'{diff}')


def run_instance(filename: str, params: Any,
                 func: Callable[[Graph], Tuple[NodeOrder, NodeColors]],
                 run_count: int = 100):
    graph = init_graph(filename)

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(single_run, graph, filename, params, func)
                   for _ in range(run_count)]
        output = [f.result() for f in as_completed(futures)]

    with open(out_filename(filename, func), 'a') as file:
        file.write('\n'.join(output))


def init_graph(filename: str) -> Graph:
    _, edges = read_graph(filename)
    vertex_neighbors = tuples_to_dict(edges)
    return vertex_neighbors


def out_filename(in_filename: str, func: Callable):
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
