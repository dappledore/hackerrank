# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())


def isPrime(v):
    if v == 1:
        return "Not prime"
    for i in range(2, int(v**0.5)+1):
        if v % i == 0:
            return "Not prime"
    return "Prime"


for i in range(n):
    num = int(input())
    print(isPrime(num))
