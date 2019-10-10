#!/usr/bin/env python

# Highly divisible triangular number

# Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

from functools import reduce
import math

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def natural_numbers():
    n = 1
    while True:
        n += 1
        yield n

@memoize
def triangle_number(n):
    if n == 1:
        return 1
    return triangle_number(n - 1) + n


def factors(n):
    def _add_factors(xs, y):
        if n / y != y:
            xs.append(n / y)
        xs.append(y)
        return xs
    return reduce(_add_factors, filter(lambda x: n % x == 0, xrange(1, int(math.sqrt(n)) + 1)), [])

def triangle_divisors(n):
    for i in natural_numbers():
        t = triangle_number(i)
        f = factors(t)
        cnt = len(f)
        if cnt > n:
            print(i, t, 'factors', f, 'cnt', cnt)
            return i

print(triangle_divisors(500))