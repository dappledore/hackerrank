// https://www.hackerrank.com/challenges/repeated-string/
//how many times "a" appears in repeated string "s" of "n" size , n can be 10^12 , s 1 to 100

// //too slow O(n) for large numbers
// function repeatedString(s, n) {
//   let cnt = 0,
//     arr = s.split("");
//   for (let i = 0, len = arr.length; i <= n; i++) {
//     if (arr[i % len] == "a") cnt++;
//   }
//   return cnt;
// }

function repeatedString(s, n) {
  let cnt = 0,
    cnt2 = 0;
  let arr = s.split("");
  if (arr.length == 0) return 0;
  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] == "a") cnt++;
    if (i < n % arr.length && arr[i] == "a") cnt2++;
  }
  return cnt * Math.floor(n / arr.length) + cnt2;
}

console.log(repeatedString("", 1000));
