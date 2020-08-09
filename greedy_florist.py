import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.


def getMinimumCost(k, c):
    c = sorted(c, reverse=True)
    total = 0
    mul = 1
    j = k
    for i in c:
        total += i * mul
        j -= 1
        if j == 0:
            mul += 1
            j = k

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
