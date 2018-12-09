from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from builtins import range

import numpy as np

T = 10000
N = 100
num_correct = 0

for _ in range(T):
    doors = np.zeros(N, dtype=np.int32)
    correct_door = np.random.randint(0, N, 1)[0]
    doors[correct_door] = 1
    choice = np.random.randint(0, N, 1)[0]
    X = list(set(range(N)) - set([choice]) - set([correct_door]))
    open_doors = np.random.choice(X, N - 2, replace=False)
    doors[open_doors] = -1
    remaining_doors = np.where(np.isin(doors, [0, 1]))[0]
    other_door = list(set(remaining_doors) - set([choice]))[0]

    new_choice = other_door
    if correct_door == new_choice:
        num_correct += 1

print(num_correct / T)
