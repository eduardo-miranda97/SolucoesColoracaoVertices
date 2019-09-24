import builtins
from collections import defaultdict
from itertools import combinations, count
from random import random, seed

COLORS = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan', 'black',
          'brown', 'pink', 'white', 'grey', 'orange', 'crimson', 'cornsilk',
          'darksalmon', 'royalblue', 'seagreen1', 'slateblue', 'yellowgreen']


def generator(num_nodes: int, density: float, func_name: str, seed_: int):

    func = getattr(builtins, func_name)
    seed(seed_)

    # output = []
    neighbors = defaultdict(set)

    for i, j in combinations(range(int(num_nodes)), 2):
        if i != j and random() < float(density):
            neighbors[i].add(j)
            neighbors[j].add(i)
            # output.append(f'{i} -- {j}')

    inv_degree = defaultdict(list)
    for i, neighbors_ in neighbors.items():
        inv_degree[len(neighbors_)].append(i)

    colors = {}
    neighbor_colors = defaultdict(set)

    for degree_ in reversed(sorted(inv_degree.keys())):
        nodes = inv_degree[degree_]
        while nodes:
            node = func(nodes, key=lambda n: len(neighbor_colors[n]))
            color = next(c for c in count()
                         if c not in neighbor_colors[node])
            colors[node] = color
            for neighbor in neighbors[node]:
                neighbor_colors[neighbor].add(color)
            nodes.remove(node)

    # graph_params = f'labelloc="t";\nlabel="{max(colors.values()) + 1} colors"'

    # node_params = '\n'.join(
    #     f'{i} [label={len(j)} style=filled fillcolor={COLORS[colors[i]]}]'
    #     for i, j in neighbors.items())

    # print('\n'.join(('graph {', graph_params, node_params, '\n'.join(output), '}')))

    return max(colors.values()) + 1

