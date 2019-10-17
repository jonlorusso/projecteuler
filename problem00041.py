#!/usr/bin/env python

# Pandigital prime

# Problem 41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

from projecteuler import isprime
from itertools import permutations

print(max(filter(isprime, map(lambda xs: int(''.join(xs)), [xs for x in range(2,10) for xs in permutations('123456789'[:x], x)]))))
