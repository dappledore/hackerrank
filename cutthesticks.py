
# https://www.hackerrank.com/challenges/cut-the-sticks/problem
import os


def cutTheSticks(arr):
    arr.sort()
    l = []
    while len(arr):
        l.append(len(arr))
        arr = [i - arr[0] for i in arr if i - arr[0] > 0]
        #    arr = [x for x in arr if x != min(arr)] #alternative without subtraction just use min value
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
