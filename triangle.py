# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
def maximumPerimeterTriangle(sticks):
    sticks = sorted(sticks, reverse=True)
    found = -1
    for i in range(len(sticks)-2):
        if sticks[i+1]+sticks[i+2] > sticks[i]:
            found = i
            break
    if found == -1:
        print('-1')
    else:
        print(sticks[found+2], sticks[found+1], sticks[i])


maximumPerimeterTriangle([1, 1, 3, 3])
