# https://www.hackerrank.com/challenges/s10-weighted-mean/

import math

n = int(input())
w = list(map(int, input().split()))
l = list(map(int, input().split()))

ltotal = sum(l)
total = 0

for i in range(n):
    total += w[i] * l[i]

print(round(total/ltotal, 1))
