#!/usr/bin/env python

from functools import reduce
from itertools import permutations
from math import sqrt, ceil

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def isprime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5
    if n % 7 == 0:
        return n == 7
    if n % 13 == 0:
        return n == 13
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def trianglenumber(n):
    return (n * (n + 1)) // 2

def sum_triangle_row(n):
    return (n * n * n + n) // 2

def istrianglenumber(n):
    x = int(sqrt(2 * n))
    return (2 * n) == (x * (x + 1))

def pandigitals(start=1, end=9, r=9):
    for i in permutations('1234567890'[start:end + 1], r):
        yield int(''.join(i))

def factors(n):
    def _add_factors(xs, y):
        if n / y != y:
            xs.append(n / y)
        xs.append(y)
        return xs
    return reduce(_add_factors, filter(lambda x: n % x == 0, range(1, int(sqrt(n)) + 1)), [])
