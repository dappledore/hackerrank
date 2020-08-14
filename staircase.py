def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n - i), end='')
        print('#' * i)

        # j = n-i
        # while j: #manual way
        #     print(' ', end='')
        #     j -= 1
        # j = i
        # while j:
        #     print('#', end='')
        #     j -= 1
        # print()


staircase(4)
