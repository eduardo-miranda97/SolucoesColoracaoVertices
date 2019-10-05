from __future__ import annotations

from solution import Solution

SWAP = 1
SHIFT = 2
DELETE_INSERT = 3


def annealing(solution: Solution, alpha: float, amount_neighboors: int,
              initial_temp: float, final_temp: float,
              reheat_times: int, neighboor_structure: int) -> Solution:
    best_solution = solution
    for _ in range(reheat_times):
        temperature = initial_temp
        while temperature > final_temp:
            temperature *= alpha
            for _ in range(amount_neighboors):
                n_solution = generate_neighboor(neighboor_structure,
                                                best_solution)
                # Calc do criterio de boltsman

    return best_solution


def generate_neighboor(neighboor_structure: int,
                       solution: Solution) -> Solution:
    if neighboor_structure == SWAP:
        return solution
    if neighboor_structure == SHIFT:
        return solution
    if neighboor_structure == DELETE_INSERT:
        return solution

    return None
