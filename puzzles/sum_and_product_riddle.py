#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
X and Y are two different whole numbers in the range [3, 100].
S and P are two mathematicians.
S knows the sum X + Y, while P knows the product X * Y.
The following conversation occurs:
Both S and P know all the information in this paragraph.

S: I know you cannot find the numbers. Unfortunately, I cannot either.
P: Now I know X and Y!
S: Now I also know X and Y!

What are X and Y?

Hint: You may find Goldbach's Conjecture useful.
"""

from __future__ import print_function
from __future__ import division

from builtins import range

import operator

from collections import defaultdict
from collections import Counter

import numpy as np

def main():
    low_limit = 3
    high_limit = 100
    sum_limit = 200
    array_shape = (high_limit+1, high_limit+1)
    sum_nums = np.fromfunction(lambda i, j: i + j, array_shape, dtype=np.int32)
    # prod_nums = np.fromfunction(lambda i, j: i * j, array_shape, dtype=np.int32)

    adders = defaultdict(list)
    # divisors = defaultdict(list)
    for i in range(low_limit, high_limit+1):
        for j in range(low_limit, i+1):
            if sum_limit and i + j <= sum_limit:
                adders[sum_nums[i, j]] += [(i, j)]
                # divisors[prod_nums[i, j]] += [(i, j)]

    # Exclude single combinations from components
    adders = {k: v for k, v in adders.iteritems() if len(v) > 1}
    # divisors = {k: v for k, v in divisors.iteritems() if len(v) > 1}

    # Exclude even sums and odd products (Goldbach's Conjecture) Since A knows
    # that P cannot conclude to a single pair, the sum should not be even, as
    # this would mean that it can be factored as the sum of two primes, which in
    # turn will create a product with unique factorization.  Since sum is odd,
    # it will be comprised of an even and an odd number, making the product
    # even.

    # adders = {k: v for k, v in adders.iteritems() if k % 2 != 0}
    # divisors = {k: v for k, v in divisors.iteritems() if k % 2 == 0}
    # Remove even multiplicand pairs
    # one_even_one_odd = lambda x, y: ((x % 2 == 0 and y % 2 != 0) or
                                        # (x % 2 != 0 and y % 2 == 0))
    # for key, val in divisors.iteritems():
            # for i, v in enumerate(val):
                # if not one_even_one_odd(v[0], v[1]):
                    # del divisors[key][i]
    prod = lambda x: reduce(operator.mul, x)

    adder_products = {key: [prod(v) for v in val]
                      for key, val in adders.iteritems()}

    product_frequencies = Counter(v for val in adder_products.values()
                                    for v in val)

    product_occurences = {key: [product_frequencies[v] for v in val]
                          for key, val in adder_products.iteritems()}

    eligible_sums = [key
                     for key, val in product_occurences.iteritems()
                     if all(v > 1 for v in val)]

    updated_adder_products = {key: val
                              for key, val in adder_products.iteritems()
                              if key in eligible_sums}

    updated_product_frequencies = Counter(
            v for val in updated_adder_products.values() for v in val)

    updated_product_occurences = {
            key: [updated_product_frequencies[v] for v in val]
            for key, val in updated_adder_products.iteritems()}

    final_components = [adders[key][[v == 1 for v in val].index(1)]
                        for key, val in updated_product_occurences.iteritems()
                        if sum(v == 1 for v in val) == 1]

    assert len(final_components) == 1, 'Solution must be unique'
    final_component = final_components[0]
    S = sum(final_component)
    P = prod(final_component)

    print('Components: {0}'.format(final_component))
    print('Sum: {0} + {1} = {s}'.format(*final_component, s=S))
    print('Product: {0} * {1} = {p}'.format(*final_component, p=P))


if __name__ == "__main__":
    main()

