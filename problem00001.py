#!/usr/bin/env python

n = 10
def ifmultiple(i):
    if i % 3 == 0 or i % 5 == 0:
        return i
    return 0

print(sum(map(ifmultiple, range(1, n))))
