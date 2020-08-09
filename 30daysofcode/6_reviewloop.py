# https://www.hackerrank.com/challenges/30-review-loop/problem
# day 6
import sys

n = int(input())
for i in range(0, n):
    str = input()
    for j in range(0, len(str)):
        if j % 2 == 0:
            sys.stdout.write(str[j])
    sys.stdout.write(" ")
    for j in range(0, len(str)):
        if j % 2 == 1:
            sys.stdout.write(str[j])
    print('')
