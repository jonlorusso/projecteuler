#!/usr/bin/env python

# Summation of primes

# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math
from itertools import takewhile

def isprime(n):
    if n == 1:
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
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def naturalnumbers():
    x = 0
    while True:
        x += 1
        yield x

def primenumbers():
    for x in naturalnumbers():
        if isprime(x):
            yield x

def take(iterable, n):
    return itertools.islice(my_list, n)

n=2000000
print(sum(takewhile(lambda x: x < n, primenumbers())))
