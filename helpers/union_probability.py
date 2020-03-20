#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def union_prob(p, n):
    return 1 - (1-p) ** n


def dice_union(min_roll, num_dice):
    prob = (7 - min_roll) / 6
    return union_prob(prob, num_dice)


def main(args):
    m = int(args[0])
    n = int(args[1])
    print(dice_union(m, n))


if __name__ == "__main__":
    main(sys.argv[1:])
