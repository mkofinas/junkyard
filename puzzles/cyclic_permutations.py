#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
from copy import deepcopy
from math import factorial as fac


def non_cyclic_permutations(X):
    Y = set(permutations(X))
    Z = deepcopy(Y)
    N = len(X)
    for y in Y:
        cyclic_perms = {tuple(y[i - j] for i in range(N)) for j in range(N)}
        Z -= cyclic_perms
        Z |= {tuple(y)}
    return Z


def remove_adjacent_girls(Z):
    S = deepcopy(Z)
    for z in Z:
        gender_sequence = ''.join(item[0] for item in z) + z[0][0]
        if 'GG' in gender_sequence:
            S -= {z}
    return S


boys = 4
girls = 4

X = ['B' + str(i) for i in range(1, boys + 1)] + \
    ['G' + str(i) for i in range(1, girls + 1)]

Z = non_cyclic_permutations(X)
S = remove_adjacent_girls(Z)

# for item in S:
    # print item
print len(S)

prediction = fac(boys - 1) * fac(boys) / fac(boys - girls)
print prediction

