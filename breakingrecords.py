# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
import os


def breakingRecords(scores):
    low, high = scores[0], scores[0]
    lc, hc = 0, 0
    for s in scores:
        if s < low:
            low = s
            lc += 1
        if s > high:
            high = s
            hc += 1
    return [hc, lc]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
