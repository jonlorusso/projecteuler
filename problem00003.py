#!/usr/bin/env python

import math

#
# Largest prime factor

# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def odd_divisors(n):
    for i in xrange(int(math.sqrt(n)) - 1, 2, -1):
        if n % i == 0:
             yield i

def isprime(n):
    for i in xrange(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

#n = 13195
n = 600851475143
for i in odd_divisors(n):
    if isprime(i):
        print(i)
        break
