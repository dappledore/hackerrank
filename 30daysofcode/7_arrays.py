# https://www.hackerrank.com/challenges/30-arrays/
# Day 7

import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in range(n-1, -1, -1):
        sys.stdout.write(str(arr[i]) + ' ')
