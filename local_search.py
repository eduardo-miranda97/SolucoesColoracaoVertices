from __future__ import annotations

from math import exp
from random import uniform, randint

from graph import Graph
from solution import Solution, random_solution

SWAP = 1
SHIFT = 2
DELETE_INSERT = 3


def annealing_standalone(graph: Graph, **kwargs) -> Solution:
    return local_search(random_solution(graph), **kwargs)


def local_search(solution: Solution, alpha: float = 0.9, amount_neighbors: int = 10,
              initial_temp: float = 100, final_temp: float = 10,
              reheat_times: int = 1, neighbor_structure: int = 1,
              annealing: bool = True) -> Solution:
    best_solution = solution
    current_solution = solution
    for _ in range(reheat_times):
        temperature = initial_temp
        while temperature > final_temp:
            for _ in range(amount_neighbors):
                n_solution = generate_neighbor(neighbor_structure,
                                                best_solution)
                delta = n_solution.colors_count - current_solution.colors_count

                if(delta < 0):

                        # Aceita de cara
                        current_solution = n_solution.copy()

                        # Verifica se é melhor do que a overall
                        if n_solution.colors_count < best_solution.colors_count:

                            # Atualiza a overall
                            best_solution = n_solution.copy()
                            #temperature
                            #print("\n\tUpdate Melhor em ", str(temperature), " com Obj = ", str(n_solution.colors_count), "\n")
                            #print(n_solution)

                else:
                    # Gera numero uniforme r ~ U(0,1)
                    if annealing:
                        r = uniform(0,1)

                        # Testa o criterio de Boltzmann
                        if r <= exp(-delta/temperature) :
                        # Aceita uma solucao pior
                           current_solution = n_solution.copy()

            # Decai a temperatura
            temperature = temperature * alpha

        #Reinicia a soluçaõ corrente para a melhor solução atual
        current_solution = best_solution.copy()

    return best_solution


def generate_neighbor(neighbor_structure: int,
                       solution: Solution) -> Solution:
    if neighbor_structure == SWAP:
        maximo = len(solution.graph)-1
        pos1 = randint(0,maximo)
        pos2 = pos1
        while (pos1 == pos2):
            pos2 = randint(0, maximo)

        return solution.swapped_by_position(pos1, pos2)

    if neighbor_structure == DELETE_INSERT:
        maximo = len(solution.graph)-1
        pos1 = randint(0,maximo)
        pos2 = pos1
        while (pos1 == pos2):
            pos2 = randint(0, maximo)

        return solution.delete_insert(pos1, pos2)

    if neighbor_structure == SHIFT:
        amount = randint(0, len(solution.graph)-1)
        return solution.shift_solution(amount)

    return None
