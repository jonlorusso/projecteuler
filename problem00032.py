#!/usr/bin/env python

# Pandigital products

# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from functools import reduce

def ispandigital(n, a, b):
    c = a * b
    s = reduce(lambda x, y: x + y, map(str, [a, b, c]))

    if len(s) != n:
        return 0

    return c if ''.join(sorted(s)) == '123456789'[0:n] else 0

n = 9

#TODO figure out how to specify the ranges
print(sum(set([ispandigital(n, a, b) for a in range(1999) for b in range(1999)])))

