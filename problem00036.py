#!/usr/bin/env python

# Double-base palindromes

# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

n = 585

def tobinary(n):
    return "{0:b}".format(n)

def ispalindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and ispalindrome(s[1:-1])

print(sum(i for i in range(1, 1000000) if ispalindrome(str(i)) and ispalindrome(tobinary(i))))

