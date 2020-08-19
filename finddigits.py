#!/bin/python3

# https://www.hackerrank.com/challenges/find-digits/problem
import os


def findDigits(n):
    nl = map(int, str(n))
    return sum([1 for d in nl if d and n % d == 0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
