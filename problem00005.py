#!/usr/bin/env python

range_max=21
nums=list(xrange(1,range_max))

result=0
while True:
    result += 20
    if all(map(lambda x: result % x == 0, nums)):
        break

print(result)
