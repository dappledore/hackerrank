# https://www.hackerrank.com/challenges/picking-numbers/problem
import os


def pickingNumbers(a):
    a.sort()
    current = None
    cnt = m = 1
    for i in range(len(a)-1):
        if current is None:
            current = a[i]
        if a[i+1] - current <= 1:
            cnt += 1
            m = max(m, cnt)
        else:
            current = a[i+1]
            cnt = 1
    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
