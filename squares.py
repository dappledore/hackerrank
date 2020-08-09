import math


def solution(area):
    ints = []
    while True:
        panel = getSquare(area)
        area = area-panel*panel
        if panel < 1:
            break
        ints.append(panel*panel)

    return ints


def getSquare(area):
    # could of used area**0.5 , area to power of 0.5 finds square and no need for library
    panel = int(math.sqrt(area))
    return panel


print(solution(17))
