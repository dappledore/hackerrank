# https://www.hackerrank.com/challenges/extra-long-factorials/problem
import os


def extraLongFactorials(n):
    if n == 1:
        return 1
    return n * extraLongFactorials(n-1)


if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
