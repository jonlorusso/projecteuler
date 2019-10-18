#!/usr/bin/env python

# Coded triangle numbers

# Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

from projecteuler import trianglenumber, istrianglenumber

filename = 'p042_words.txt'

def wordvalue(s):
    return sum(map(int, map(lambda c: ord(c) - 64, filter(lambda c: c.isalpha(), s))))

with open(filename) as file: # Use file to refer to the file object
    print(len([w for w in filter(istrianglenumber, map(wordvalue, file.read().split(',')))]))
