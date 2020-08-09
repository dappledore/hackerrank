# https://www.hackerrank.com/challenges/s10-mcq-3/problem
import itertools
from fractions import Fraction

X = ["b", "b", "b", "r", "r", "r", "r"]
Y = ["b", "b", "b", "b", "r", "r", "r", "r", "r"]
Z = ["b", "b", "b", "b", "r", "r", "r", "r"]

r = [(i)for i in itertools.product(X, Y, Z)]
e = list(map(lambda x: x.count('r') == 2 and x.count('b') == 1, r))
res = Fraction(e.count(True), len(e))
print(res)
