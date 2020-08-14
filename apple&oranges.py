# https://www.hackerrank.com/challenges/apple-and-orange/problem
def countApplesAndOranges(s, t, a, b, apples, oranges):
    alow, ahigh = s - a, t - a
    olow, ohigh = t - b, s - b
    ac = sum([1 for apple in apples if apple >= alow and apple <= ahigh])
    oc = sum([1 for orange in oranges if orange <= olow and orange >= ohigh])

    print(ac)
    print(oc)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
