# https://www.hackerrank.com/challenges/30-conditional-statements/
# Day 3
N = 20
print(N)
if N % 2 == 1:
    print("Weird")
elif N in range(2, 5+1):
    print("Not Weird")
elif N in range(6, 20+1):
    print("Weird")
elif N > 20:
    print("Not Weird")
