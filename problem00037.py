#!/usr/bin/env python

# Truncatable primes

# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from itertools import count, islice
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

n = 3797

def truncations(n):
    yield(n)
    s = str(n)
    for i in range(1, len(s)):
        yield int(s[:-i])
        yield int(s[i:])

def primenumbers(start=11):
    for x in count(start):
        if isprime(x):
            yield x

print(sum(islice((p for p in primenumbers() if all(map(isprime, truncations(p)))), 0, 11)))
