# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    dif = 0
    m = 2 * 10**9
    for i in range(len(arr)-1):
        dif = arr[i+1] - arr[i]
        m = min(dif, m)
    print(m)


minimumAbsoluteDifference([1, -3, 71, 68, 17])
