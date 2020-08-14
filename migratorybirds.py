# https://www.hackerrank.com/challenges/migratory-birds/problem
from collections import Counter


def migratoryBirds(arr):
    cnt = Counter(arr)
    m = 0
    keys = []
    for k, v in cnt.most_common():
        if v < m:
            break
        keys.append(k)
        m = v
    return sorted(keys)[0]


print(migratoryBirds([1, 2, 2, 3, 3, 3, 4, 5]))
