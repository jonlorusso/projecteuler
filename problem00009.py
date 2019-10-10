#!/usr/bin/env python

# Special Pythagorean triplet

# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def istriplet(a, b, c):
    return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)

for a in xrange(1, 1000):
    for b in xrange(a, 1000):
        c = 1000 - (a + b)
        if istriplet(a, b, c):
            print(a, b, c, (a * b * c))
