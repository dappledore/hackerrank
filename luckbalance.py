# https://www.hackerrank.com/challenges/luck-balance/problem
def luckBalance(k, contests):
    luck = 0
    for l, i in sorted(contests, reverse=True):
        if not i:
            luck += l
        elif k > 0:
            luck += l
            k -= 1
        else:
            luck -= l
    return luck


arr = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luckBalance(3, arr))
