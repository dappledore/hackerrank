# https://www.hackerrank.com/challenges/kangaroo/problem
# x1 + y * v1 = x2 + y * v2 when two kangaroos position are same, y is number of jumps
# reduces to (x1-x2) / (v2 - v1) , when the two divide no remainder they are at same position
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:  # x1 will not catchup
        return "NO"
    return "YES" if ((x1 - x2) % (v2 - v1) == 0) else "NO"
