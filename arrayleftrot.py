# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
def rotLeft(a, d):
    return a[d:] + a[:d]
    # for _ in range(d): #if you need to use a loop
    #   a.append(a.pop(0))


print(rotLeft([1, 2, 3, 4, 5], 4))
