# https://www.hackerrank.com/challenges/equality-in-a-array/problem
import os
from collections import Counter


def equalizeArray(arr):
    # alternative max(Counter(arr).values())
    c = Counter(arr).most_common(1)[0][1]
    return len(arr)-c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
