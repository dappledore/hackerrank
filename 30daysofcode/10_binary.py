# https://www.hackerrank.com/challenges/30-binary-numbers/problem

if __name__ == '__main__':
    n = int(input())
    x = bin(n)[2:]
    cnt = 0
    m = 0
    for i in x:
        if i == '1':
            cnt += 1
            m = max(m, cnt)
        else:
            cnt = 0
    print(m)
