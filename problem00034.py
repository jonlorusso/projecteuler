#!/usr/bin/env python

# Digit factorials

# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fact(s):
    return factorial(int(s))

@memoize
def digitfactorial(s):
    if len(s) <= 0:
        return 0

    return digitfactorial(s[1:]) + fact(s[0])

print(sum([i for i in range(3, 10000000) if  i == digitfactorial(str(i))]))
