from collections import Counter


def number_needed(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())


print(number_needed("ddd", "dcd"))
