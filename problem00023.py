#!/usr/bin/env python

# Non-abundant sums

# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
import itertools

ABUNDANT_SUM_LIMIT=28124

def divisors(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            x = n // i
            if x != i and x != n:
                yield x

def isabundant(n):
    return sum(divisors(n)) > n

abundant_numbers = filter(isabundant, range(1, ABUNDANT_SUM_LIMIT))
abundant_sums = [a + b for a, b in itertools.combinations_with_replacement(abundant_numbers, 2)]
abundant_sums_map = { a: 1 for a in abundant_sums }

print(sum(filter(lambda x: abundant_sums_map.get(x) is None, range(1, ABUNDANT_SUM_LIMIT))))
