# https://www.hackerrank.com/challenges/30-scope/problem
class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    maximumDifference = 0

    def computeDifference(self):
        l, h = 101, 0
        for el in self.__elements:
            l = min(l, el)
            h = max(h, el)
        self.maximumDifference = (h - l)
        return self.maximumDifference

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
