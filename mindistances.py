# https://www.hackerrank.com/challenges/minimum-distances/problem

#!/bin/python3

from collections import Counter


def minimumDistances(a):
    c = Counter(a)
    m = 10000
    for k in c:
        if c[k] == 2:
            first = a.index(k)
            second = a.index(k, first+1)
            m = min(m, second-first)
    return m if m < 10000 else -1

  # def minimum_distance(n, A): #alternative that starts with distance 1 checking each index and keeps growing distance until min found or none
  #   for d in range(1, n):
  #       for i in range(n - d):
  #           if A[i] == A[i+d]:
  #               return d
  #   return -1


print(minimumDistances([7, 1, 3, 4, 1, 7]))
