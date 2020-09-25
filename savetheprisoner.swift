// https://www.hackerrank.com/challenges/save-the-prisoner/problem

func saveThePrisoner(n: Int, m: Int, s: Int) -> Int {
    let k = ((s - 1 + m - 1) % n) + 1
    return k
}

print(saveThePrisoner(n: 7, m: 19, s: 2))