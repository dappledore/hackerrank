// https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

func jumpingOnClouds(c: [Int], k: Int) -> Int {
  var score = 100, i = k, n = c.count
  while i % n != 0 {
    score = score - (c[i%n] == 0 ? 1 : 3)
    i+=k
  }
  return score - (1 + 2*c[0])
}

print(jumpingOnClouds(c:[1, 1, 1, 0, 1, 1, 0, 0, 0, 0],k:3))