#!/usr/bin/env python

# Digit fifth powers

# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import math

n = 5

digit_powers = dict(map(lambda i: (i, int(math.pow(i, n))), range(10)))
max = n * int(math.pow(9, n))

# the horror!
print(sum(map(lambda t: t[0], filter(lambda t: t[0] == t[1], map(lambda i: (i, sum([digit_powers[int(c)] for c in str(i)])), range(2, max + 1))))))
