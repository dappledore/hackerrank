# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    cnt = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            cnt += 1
    return cnt


print(birthday([1, 2, 1, 3, 4, 5], 3, 2))
