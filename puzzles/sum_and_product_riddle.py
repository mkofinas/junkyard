#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Δύο φοιτητές μαθηματικών, ο Άρης και ο Γιώργος, ενδιαφέρονται για την ίδια
συμφοιτήτριά τους τη Μαρία. Αυτή τους είπε πως θα τα φτιάξει με αυτόν που θα
αποδειχτεί πιο έξυπνος από τους δύο. Έβαλε στο μυαλό της δύο ακέραιους αριθμούς
από το 3 έως το 100 και ψιθύρισε στον Άρη το άθροισμά τους και στον Γιώργο το
γινόμενό τους. Τους εξήγησε τους κανόνες και τους είπε πως όποιος από τους δύο
καταφέρει να βρει τους δύο αριθμούς θα κερδίσει την καρδιά της. Τότε οι δύο
φοιτητές έκαναν μεταξύ τους τον παρακάτω διάλογο:

Άρης: Ξέρω πως δεν μπορείς να βρεις τους αριθμούς. Δυστυχώς ούτε κι εγώ μπορώ.
Γιώργος: Τώρα με αυτό που είπες τους βρήκα!
Άρης: Τώρα τους βρήκα κι εγώ!

Στο τέλος έμειναν κι οι δύο μπουκάλες γιατί ήρθαν ισοπαλία, αλλά τουλάχιστον
πήραν την ικανοποίηση πως έλυσαν το γρίφο της Μαρίας. Ποιοι ήταν οι δύο αριθμοί;

Σαν βοήθεια δίνεται η Εικασία του Goldbach, που λέει πως κάθε ζυγός αριθμός
μπορεί να γραφτεί σαν άθροισμα δύο πρώτων. Παρόλο που δεν έχει αποδειχτεί για
κάθε αριθμό, ισχύει στα σίγουρα μέσα στα όρια που θέτει το πρόβλημα.
"""

from __future__ import print_function
from __future__ import division

import operator

from collections import defaultdict
from collections import Counter

import numpy as np

prod = lambda x: reduce(operator.mul, x)

one_even_one_odd = lambda x, y: ((x % 2 == 0 and y % 2 != 0) or
                                 (x % 2 != 0 and y % 2 == 0))

S = lambda i, j: i + j
P = lambda i, j: i * j
sum_nums = np.fromfunction(S, (101, 101), dtype=np.int32)
prod_nums = np.fromfunction(P, (101, 101), dtype=np.int32)

adders = defaultdict(list)
divisors = defaultdict(list)
for i in xrange(3, 101):
    for j in xrange(3, i+1):
        adders[sum_nums[i, j]] += [(i, j)]
        divisors[prod_nums[i, j]] += [(i, j)]

# 1. Exclude single combinations from components
adders = {k: v for k, v in adders.iteritems() if len(v) > 1}
divisors = {k: v for k, v in divisors.iteritems() if len(v) > 1}

# Exclude even sums and odd products (Goldbach's Conjecture)
# Since A knows that P cannot conclude to a single pair, the sum should not be
# even, as this would mean that it can be factored as the sum of two primes,
# which in turn will create a product with unique factorization.
# Since sum is odd, it will be comprised of an even and an odd number, making
# the product even.
# adders = {k: v for k, v in adders.iteritems() if k % 2 != 0}
# divisors = {k: v for k, v in divisors.iteritems() if k % 2 == 0}
# Remove even multiplicand pairs
# for key, val in divisors.iteritems():
    # for i, v in enumerate(val):
        # if not one_even_one_odd(v[0], v[1]):
            # del divisors[key][i]

adder_products = {key: [prod(v) for v in val]
                  for key, val in adders.iteritems()}

product_frequencies = Counter(v for val in adder_products.values()
                                for v in val)

product_occurences = {key: [product_frequencies[v] for v in val]
                      for key, val in adder_products.iteritems()}

eligible_sums = [key
                 for key, val in product_occurences.iteritems()
                 if all(v > 1 for v in val)]

multiplicand_sums = {key: [sum(v) for v in val]
                     for key, val in divisors.iteritems()}

eligible_products = {key: val for key, val in multiplicand_sums.iteritems()
                              if any(v in eligible_sums for v in val)}

updated_adder_products = {key: [prod(v) for v in val]
                           for key, val in adders.iteritems()
                           if key in eligible_sums}
updated_product_frequencies = Counter(v for val in updated_adder_products.values()
                                        for v in val)
updated_product_occurences = {key: [updated_product_frequencies[v] for v in val]
                              for key, val in updated_adder_products.iteritems()}

final_components = [adders[key][[v == 1 for v in val].index(1)]
                    for key, val in updated_product_occurences.iteritems()
                    if sum(v == 1 for v in val) == 1]
assert len(final_components) == 1
final_component = final_components[0]
S = sum(final_component)
P = prod(final_component)

print('Components: {0}'.format(final_component))
print('Sum: {0} + {1} = {2}'.format(final_component[0], final_component[1], S))
print('Product: {0} * {1} = {2}'.format(final_component[0], final_component[1], P))


