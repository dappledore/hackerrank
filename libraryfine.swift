// https://www.hackerrank.com/challenges/library-fine/problem

func libraryFine(d1: Int, m1: Int, y1: Int, d2: Int, m2: Int, y2: Int) -> Int {
  if y1 < y2 {
    return 0
  }
  if y1>y2 {
    return 10000
  }
  if m1<m2 {
    return 0
  }
  if m1>m2 {
      return (m1-m2)*500
  }
  return (d1 > d2) ?  (d1-d2)*15 : 0
}

print(libraryFine(d1: 6, m1: 7, y1: 2020, d2: 6, m2: 6, y2: 2020))
