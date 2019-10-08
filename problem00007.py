#!/usr/bin/env

# 10001st prime

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math
from itertools import islice

def isprime(n):
    if n == 1:
        return False
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

# from itertools recipes
def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

nth_prime=lambda n: nth(primenumbers(), n)

n=10001
print(nth_prime(n))
