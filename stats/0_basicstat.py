# https://www.hackerrank.com/challenges/s10-basic-statistics/
n = int(input())
arr = list(map(int, input().rstrip().split()))

mean = 0
median = 0
mode = 0

for i in arr:
    mean += i
print(str(mean/n))

arr.sort()

pivot = int(n/2)-1
median = (arr[pivot] + arr[pivot+1]) / 2 if n % 2 == 0 else arr[pivot]
print(str(median))

counts = {}
freq = 0

for i in arr:
    counts[i] = counts.get(i, 0) + 1

for val, count in counts.items():
    if count > freq:
        mode = val
        freq = count
    if count == freq and val < mode:
        mode = val
print(mode)
