#!/usr/bin/env python

import math

# Largest palindrome product

# Problem 4
# A palindromic numbzr reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def max_n_digit(n):
    return pow(10, n) - 1

def ispalindrome(n):
    l = math.floor(math.log10(n))
    for i in xrange(0, int(l/2) + 1):
        if nth_digit(n, l - i) != nth_digit(n, i):
            return False
    return True

def nth_digit(x, n):
    return x // math.pow(10, n) % 10

def max_palindrome(ndigit):
    max = 0
    for x in xrange(max_n_digit(ndigit), max_n_digit(ndigit - 1), -1):
        for y in xrange(x, max_n_digit(ndigit - 1), -1):
            p = x * y
            if ispalindrome(p) and p > max:
                max = p
    return max

print(max_palindrome(3))
