# https://www.hackerrank.com/challenges/30-sorting/problem

def sort(a, n):
    numSwaps = total = 0
    for i in range(n):
        numSwaps = 0
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
                total += 1
        if numSwaps == 0:
            break
    print(f'Array is sorted in {total} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[n-1]}')


sort([3, 4, 3], 3)
