# https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree(n):
    height = 0
    for i in range(n+1):
        if i % 2:
            height = height * 2
        else:
            height += 1
    return height


result = utopianTree(4)
print(result)
