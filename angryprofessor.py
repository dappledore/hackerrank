# https://www.hackerrank.com/challenges/angry-professor/problem
import os


def angryProfessor(k, a):
    c = sum([1 for i in a if i < 1])
    return "NO" if c >= k else "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
