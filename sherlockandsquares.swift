// https://www.hackerrank.com/challenges/sherlock-and-squares/problem

//iterative solution
func squares(a: Int, b: Int) -> Int {
  var s = Int(Double(a).squareRoot())
  var nums = [Int]()
  while(true) {
    if s * s > b {break}
    if s * s >= a { nums.append(s*s) }
    s += 1
  }
  return nums.count
}

//math solution
func squares2(a: Int, b: Int) -> Int {
  let bb = Int(Double(b).squareRoot())
  let aa = Int(Double(a).squareRoot()+1)
  return bb - aa + 1
}

print( squares(a: 24, b: 49) )
print( squares2(a: 24, b: 70) )