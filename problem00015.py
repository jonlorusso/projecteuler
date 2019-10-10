#!/usr/bin/env python

# Lattice paths

# Problem 15
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# https://en.wikipedia.org/wiki/Central_binomial_coefficient

import math

n = 20
numerator = math.factorial(2 * n)
denominator = math.pow(math.factorial(n), 2)

print(int(numerator/denominator))
