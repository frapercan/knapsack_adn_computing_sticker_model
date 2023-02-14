import itertools
import math
from itertools import chain, combinations
import numpy as np
import pandas as pd

p = 3  # Número de objetos distintos en el inventario para meter en la mochila
s = 20  # Capacidad Mochila
posiciones = [a for a in range(0, p)]  # Índices del inventario

values = np.array([1, 2, 3])  # Valores en cada posición del inventario dado el índice A
weights = np.array([4, 5, 1])  # Pesos en cada posición del inventario dado el índice A

A = np.zeros([2 ** p, p]) #Inicializamos
index = 0
for solution_length in range(p):
    for solution_index, combinations in enumerate(list(itertools.combinations(posiciones, solution_length + 1))):
        combinations = np.array(combinations)
        A[index][combinations if combinations.size else []] = 1
        index += 1

L = A * [weights]
R = A * [values]

print('A\n', A)
print('L\n', L)
print('R\n', R)

T_0 = pd.DataFrame(np.concatenate([A, L, R], axis=1),
                   columns=np.concatenate([[f's_{i + 1}' for i in range(p)], [f'l_{i}' for i in range(p)],
                                           [f'r_{i + 1}' for i in range(p)]]))  # p-biblioteca rellena

print(T_0)


def cardinal_sort(T, l, k):
    pass


def filling_paralell():
    pass
