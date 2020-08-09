# https://www.hackerrank.com/challenges/mini-max-sum/problem
def miniMaxSum(arr):
    arr = sorted(arr)
    l = sum(arr[:4])
    h = sum(arr[-4:])
    print(f'{l} {h}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
