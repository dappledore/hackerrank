# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
def catAndMouse(x, y, z):
    cata = abs(z-x)
    catb = abs(z-y)
    if catb == cata:
        return "Mouse C"
    return "Cat A" if cata < catb else "Cat B"


print(catAndMouse(4, 2, 3))
