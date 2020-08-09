# https://www.hackerrank.com/challenges/30-2d-arrays/problem


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # this -64 is important for minus totals, max minus value is -63 (7x-9)
    m = -64

    for i in range(6-2):
        for j in range(6-2):
            cnt = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i +
                                                              1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            m = max(m, cnt)

    print(m)
