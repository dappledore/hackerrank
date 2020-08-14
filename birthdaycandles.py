# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(ar):
    ar = sorted(ar, reverse=True)
    h = ar[0]
    total = 0
    for a in ar:
        if a == h:
            total += 1
        else:
            break
    return total
