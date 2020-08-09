//https://www.hackerrank.com/challenges/mark-and-toys/

function maximumToys(prices, k) {
  let s = prices.sort((a, b) => a - b),
    cnt = 0,
    sum = 0;
  s.some((i) => {
    sum += i;
    if (sum <= k) cnt++;
    else return false;
  });
  return cnt;
}

console.log(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50));
