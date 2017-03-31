#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def show_X(pc, **kw):
    pc.update_scalarmappable()
    ax = pc.get_axes()
    idx = np.where(pc.get_array() == 3)[0]
    x, y = pc.get_paths()[idx].vertices[:-2, :].mean(0)
    ax.text(x, y, 'X', ha="center", va="center", color=(1.0, 1.0, 1.0),
            fontsize=26, **kw)


def plot_keymap(A, team_name):
    colormap = ListedColormap(['#F0DC82', '#0000FF', '#FF0000', '#000000'])
    c = plt.pcolor(A, cmap=colormap, edgecolor='k', linewidth=4)
    c.get_axes().invert_yaxis()
    plt.axis('equal')
    plt.axis('off')
    plt.title('Key Map: ' + team_name + ' play first')
    show_X(c)
    plt.show()


def main():
    B = np.random.choice(25, 18, replace=False)
    first_team = np.random.randint(2)
    teams = {0: 'Reds', 1: 'Blues'}
    blues, reds, assassin = np.split(B, [8+first_team, 17])

    A = np.zeros((25,))
    A[blues] = 1
    A[reds] = 2
    A[assassin] = 3
    A = np.reshape(A, (5, 5))

    ## Alternative Implementation
    # first_team = np.random.choice(['B', 'R'],1)[0]
    # A = 'IIIIIIIBBBBBBBBRRRRRRRRA' + first_team
    # A = np.array(list(A))
    # np.random.shuffle(A)

    plot_keymap(A, teams[first_team])

if __name__ == "__main__":
    main()

