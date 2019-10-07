#!/usr/bin/env python

def fib():
    x = 1
    y = 2

    yield x
    yield y

    while True:
        z = x + y
        x, y = y, z
        yield z

result = 0
for x in fib():
    if x <= 4000000:
        if x % 2 == 0:
            result += x
    else:
        break

print(result)

