// https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

func climbingLeaderboard(ranked: [Int], player: [Int]) -> [Int] {
  let ranked2 = Array(Set(ranked)).sorted(by: {$0 > $1}) //reverse array smallest values at end, no duplicates
  var l = ranked2.count
  var ranks = [Int]()
  //if p value is less than end value, we have found rank. Rank uses length of array.
  for p in player {
    while l > 0, p >= ranked2[l-1] {
      l = l - 1
    }
    ranks.append(l+1)
  }
  return ranks
}

print( climbingLeaderboard(ranked: [100, 90, 90, 80, 75, 60], player: [50, 65, 77, 90, 102]) )