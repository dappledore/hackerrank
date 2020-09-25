// https://www.hackerrank.com/challenges/append-and-delete/forum

// Complete the appendAndDelete function below.
func appendAndDelete(s: String, t: String, k: Int) -> String {
  let slen = s.count, tlen = t.count
  if slen + tlen < k {return "Yes"}
  
  var sameNum = min(slen,tlen)
  for i in 0..<sameNum {
    if s[s.index(s.startIndex,offsetBy: i)] != t[t.index(t.startIndex, offsetBy: i)] {
      sameNum = i
      break
    }
  }
  let diff = (slen - sameNum) + (tlen - sameNum)
  // diff is less than, equal k so enough changes and the changes needed are even number 
  // (delete and add) an odd number will fail (add or delete)
  if diff <= k && (diff-k) % 2 == 0 { 
    return "Yes"
  } else {
    return "No"
  }

}

print( appendAndDelete(s: "hackerhappy", t: "hackerrank", k: 9) ) // k of 9 will pass , k of 10 will fail since diff-k is an odd number