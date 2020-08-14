# https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonalDifference(arr):
    lr, rl = 0, 0
    for i in range(len(arr)):
        lr += arr[i][i]
        rl += arr[i][-(i+1)]
    return abs(rl-lr)


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

print(diagonalDifference(arr))
