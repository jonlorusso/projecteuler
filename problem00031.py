#!/usr/bin/env python

# Coin sums

# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

#   1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

#from itertools import starmap
#from math import prod

n = 200
coins = [200,100,50,20,10,5,2,1]

def pence(weights):
    return sum(map(lambda x,y: x * y, coins, weights))

# def rangeP(weights, size=1):
#     global n
#     return range(int((n - pence(weights)) / size) + 1)

# count = 0

# for L2 in range(2):
#     for L in rangeP([L2], size=100):
#         for fifty in rangeP([L2, L], size=50):
#             for twenty in rangeP([L2, L, fifty], size=20):
#                 for ten in rangeP([L2, L, fifty, twenty], size=10):
#                     for five in rangeP([L2, L, fifty, twenty, ten], size=5):
#                         for two in rangeP([L2, L, fifty, twenty, ten, five], size=2):
#                             for one in rangeP([L2, L, fifty, twenty, ten, five, two]):
#                                 p = pence([L2, L, fifty, twenty, ten, five, two, one])
#                                 if p == n:
#                                     count += 1

#print(count)

def coin_combinations(total, coins):
    if total < 0 or len(coins) <= 0:
        return 0

    if total == 0:
        return 1

    return coin_combinations(total, coins[:-1]) + coin_combinations(total - coins[-1], coins)


print(coin_combinations(n, coins))
