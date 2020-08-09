# https://www.hackerrank.com/challenges/maximum-element/problem

n = int(input())

stack = [0]

for i in range(n):
    l = list(map(int, input().split()))
    if l[0] == 1:
        num = l[1]
        stack.append(max(num, stack[-1]))  # set max element
    elif l[0] == 2:
        stack.pop()
    elif l[0] == 3:
        print(stack[-1])
