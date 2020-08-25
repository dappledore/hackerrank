# https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    t = sum(bill[:k] + bill[k+1:])
    o = "Bon Appetit" if t / 2 == b else str(b - t // 2)
    print(o)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
