# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    ta, tb = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            ta += 1
        elif b[i] > a[i]:
            tb += 1
    return [ta, tb]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
