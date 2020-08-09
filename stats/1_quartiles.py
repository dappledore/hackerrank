n = int(input())
a = sorted(map(int, input().split()))


def median(a):
    if len(a) % 2 == 0:
        return(a[len(a) // 2] + a[len(a) // 2 - 1]) // 2
    else:
        return a[len(a) // 2]


if len(a) % 2 == 0:
    q2 = median(a)
    q1 = median(a[: len(a) // 2])
    q3 = median(a[len(a) // 2:])
else:
    q2 = median(a)
    q1 = median(a[: a.index(q2)])
    q3 = median(a[a.index(q2) + 1:])

print(q1)
print(q2)
print(q3)
