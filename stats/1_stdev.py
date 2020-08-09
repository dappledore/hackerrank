import math

n = int(input())
arr = list(map(int, input().rstrip().split()))

mean = sum(arr) / n

a = math.sqrt(sum([(i-mean) ** 2 for i in arr]) / n)

print(round(a, 1))
