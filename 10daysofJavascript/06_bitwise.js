// https://www.hackerrank.com/challenges/js10-bitwise/problem

function getMaxLessThanK(n, k) {
  let m = 0;
  for (let a = 1; a <= n; a++) {
    for (let b = a + 1; b <= n; b++) {
      let r = a & b;
      if (r < k) m = Math.max(r, m);
    }
  }
  return m;
}
