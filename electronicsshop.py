# https://www.hackerrank.com/challenges/electronics-shop/problem
# O(n*m)
def getMoneySpent(keyboards, drives, b):
    m = -1
    for k in keyboards:
        for d in drives:
            if d + k <= b:
                m = max(d+k, m)
    return m
