# https://www.hackerrank.com/challenges/30-loops/problem
# day 5

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, n*i))
