#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/ctci-coin-change/problem


def ways(n, coins):
    lookup = [1] + [0] * n
    for coin in coins:
        for i in range(1, n+1):
            if i < coin:
                continue
            lookup[i] += lookup[i-coin]
    return lookup[n]


print(ways(15, [4, 3]))
