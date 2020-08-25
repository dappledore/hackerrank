# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def beautifulDays(i, j, k):
    # convert number to string reverse, get absolute value , all divisible by k included in generator , sum array
    return sum([1 for n in range(i, j+1) if abs(n - int(str(n)[::-1])) % k == 0])


print(beautifulDays(20, 23, 6))
