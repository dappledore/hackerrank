//https://www.hackerrank.com/challenges/counting-valleys/
//Count number of valleys , U is up and D is down, start end at sea level, D followed by same number of U is a valley

function countingValleys(n, s) {
  let arr = s.split("");
  let cnt = 0,
    res = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == "D") cnt--;
    else cnt++;
    if (cnt == 0 && arr[i] == "U") res++;
  }
  return res;
}

console.log(countingValleys(8, "UDDDUDUU"));
