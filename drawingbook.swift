// https://www.hackerrank.com/challenges/drawing-book/problem
func pageCount(n: Int, p: Int) -> Int {
    let totalTurns = n/2
    let turnsFromFront = p / 2
    return min(turnsFromFront,totalTurns - turnsFromFront)
}

print(pageCount(n: 6, p: 4))