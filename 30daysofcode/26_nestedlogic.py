# https://www.hackerrank.com/challenges/30-nested-logic/problem
ad, am, ay = list(map(int, input().split(' ')))
ed, em, ey = list(map(int, input().split(' ')))


def calcFine(ad, am, ay, ed, em, ey):
    # no fine, could use a default of zero to avoid first and conditions
    if (ad <= ed and am <= em and ay <= ey) or ay < ey:
        return 0
    elif ad > ed and am == em and ay == ey:
        return 15 * (ad-ed)
    elif am > em and ay == ey:
        return 500 * (am - em)
    elif ay > ey:
        return 10000


print(calcFine(ad, am, ay, ed, em, ey))
