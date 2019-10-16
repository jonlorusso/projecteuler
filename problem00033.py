#!/usr/bin/env python

# Digit cancelling fractions

# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# for d in range(10, 100):
#     for n in range(10, d):
#         if str(n)[1] == str(d)[0] and int(str(d)[1]) > 0 and (int(str(n)[0]) / int(str(d)[1]) == n/d):
#             print(str(n)[0], ' ', str(d)[1])
#             print('%d/%d' % (n, d))

from functools import reduce
from math import gcd

def isdigitalcancelling(n, d):
    if d % 10 == 0:
        return False

    return n % 10 == d // 10 and (n // 10) / (d % 10) == n / d

product = reduce(lambda t1, t2: (t1[0] * t2[0], t1[1] * t2[1]), [(n, d) for d in range(10, 100) for n in range(10, d) if isdigitalcancelling(n, d)])
print(product[1] // gcd(*product))
