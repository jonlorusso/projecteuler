#!/usr/bin/env python

# Sum square difference

# Problem 6
# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def sum_of_squares(n):
    return sum(map(lambda x: math.pow(x, 2), list(range(1, n+1))))

def square_of_sum(n):
    return math.pow(sum(list(range(1, n+1))), 2)

n=100
su=sum_of_squares(n)
sq=square_of_sum(n)
print(su, sq, sq - su)
