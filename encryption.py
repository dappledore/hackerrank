# https://www.hackerrank.com/challenges/encryption/problem
import math


def encryption(s):
    l = len(s.strip().replace(" ", ""))
    # r = math.floor(l ** 0.5)
    c = math.ceil(l ** 0.5)
    res = ""
    for i in range(c):
        # for j in range(c):
        # k = i+j*c
        res += s[i::c]
        res += " "
    return res


print(encryption("ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"))
