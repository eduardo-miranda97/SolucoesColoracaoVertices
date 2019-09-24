import sys
from itertools import count, islice, product

from reader import read_graph


def generate_mod(in_fname: str, out_fname: str):
    H, E = read_graph(in_fname)
    I = V = [i + 1 for i in range(H)]

    R = count()
    saida = []

    for v, i in product(V, I):
        saida.append(f'var x_{v}_{i} binary;')

    for i in I:
        saida.append(f'var w_{i} binary;')

    saida.append('minimize num_colors:')
    for i in I:
        saida.append(f'w_{i} +')

    saida[-1] = saida[-1].replace(' +', ';')

    saida.append('subject to')

    for v in V:
        saida.append(f'r{next(R)}: ' +
                     ' + '.join(f'x_{v}_{i}' for i in I) +
                     ' = 1;')

    for (u, v), i in product(E, I):
        saida.append(f'r{next(R)}: x_{u}_{i} + x_{v}_{i} <= w_{i};')

    for i in I:
        saida.append(f'r{next(R)}: w_{i} <= ' +
                     ' + '.join(f'x_{v}_{i}' for v in V) + ';')

    for i in islice(I, 1, None):
        saida.append(f'r{next(R)}: w_{i} <= w_{i - 1};')

    saida.append('solve;')
    saida.append('display ' + ' + '.join(f'w_{i}' for i in I) + ';')

    with open(out_fname, 'w') as f:
        f.write('\n'.join(saida))
        f.write('\n')


if __name__ == '__main__':
    generate_mod(*sys.argv[1:])
