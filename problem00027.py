#!/usr/bin/env python

# Quadratic primes

# Problem 27
# Euler discovered the remarkable quadratic formula:

#     n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

#     n2+an+b, where |a|<1000 and |b|≤1000

#     where |n| is the modulus/absolute value of n
#     e.g. |11|=11 and |−4|=4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

from math import pow, sqrt, ceil
from itertools import count, takewhile, product

def quadratic(a, b):
    return lambda n: pow(n, 2) + (a * n) + b

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

def countprimes(q):
    return len(list(takewhile(isprime, map(q, count()))))

maxprimes= 0
result = 0

for p in product(range(-1000, 1000), range(-1000, 1001)):
    primes = countprimes(quadratic(*p))
    if primes > maxprimes:
        maxprimes, result = primes, (lambda a, b: a * b)(*p)

print(result)
