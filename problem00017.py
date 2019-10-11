#!/usr/bin/env python

# Number letter counts

# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

# FIXME it does not affect the result, but this code is generating an extra - when there is no value in the units place:
# eg., nine hundred and seventy-
def in_words(n):
    result = ''

    thousand = n / 1000
    if thousand > 0:
        result += 'one thousand '
    n %= 1000

    hundred = n / 100
    if hundred > 0:
        result += words[hundred] + ' hundred'
    n %= 100

    if len(result) > 0 and  n > 0:
        result += ' and '

    if n < 20 and n > 10:
        result += words[n]
    else:
        tens = n / 10
        if tens > 0:
            result += words[tens * 10] + '-'
        n %= 10

        if n > 0:
            result += words[n]

    return result

def char_count(n):
    s = in_words(n)
    print(s)
    return sum([1 for c in s if c.isalpha()])

print(sum(map(char_count, xrange(1, 1001))))
