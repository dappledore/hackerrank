# https://www.hackerrank.com/challenges/plus-minus/problem

# Complete the plusMinus function below.
def plusMinus(arr):
    p, n, z, l = 0, 0, 0, len(arr)
    for v in arr:
        if v > 0:
            p += 1
        elif v < 0:
            n += 1
        elif v == 0:
            z += 1
    print(round(p/l, 6))
    print(round(n/l, 6))
    print(round(z/l, 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
