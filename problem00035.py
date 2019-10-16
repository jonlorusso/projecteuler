#!/usr/bin/env python

# Circular primes
# Problem 35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

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


def iscircularprime(n):
    s = str(n)
    return all(map(isprime, [int(s[i:] + s[0:i]) for i in range(len(s))]))

print(sum([1 for i in range(1000000) if iscircularprime(i)]))
