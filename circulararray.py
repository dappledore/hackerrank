# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
    l = len(a)
    if k > l:
        k %= l
    a = a[len(a)-k:] + a[0:len(a)-k]
    result = []
    for q in queries:
        result.append(a[q])
    return result


print(circularArrayRotation([1, 2, 3, 4], 2, [0, 1]))
