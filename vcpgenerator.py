import sys
from itertools import product, count

E = set()
r = count()

with open(sys.argv[1]) as f:
    for line in f:
        line = (line.replace('\n', '')).split(' ')
        if (line[0] == 'e'):
            E.add((line[1], line[2]))
        if (line[0] == 'p'):
            H = int(line[2])

I = [i+1 for i in range(H)]
V = [i+1 for i in range(H)]

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
    saida.append(f'r{next(r)}: ' + ' + '.join(f'x_{v}_{i}' for i in I) + ' = 1;')

for (u, v), i in product(E, I):
    saida.append(f'r{next(r)}: x_{u}_{i} + x_{v}_{i} <= w_{i};')

saida.append('solve;')

for i in I:
    saida.append('display ' + ' + '.join(f'w_{i}' for i in I) + ';') 

with open(sys.argv[2], 'w') as f:
    f.write('\n'.join(saida))
    f.write('\n')

