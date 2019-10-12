#!/usr/bin/env

# Amicable numbers
   
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math

def divisors(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            x = n // i
            if x != i and x != n:
                yield x

d = lambda n: sum(divisors(n))

def amicable(a):
    b = d(a)
    return a != b and d(b) == a

print(sum(filter(amicable, range(1, 10000))))
