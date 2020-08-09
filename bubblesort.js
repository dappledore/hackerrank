function countSwaps(a) {
  let n = a.length,
    cnt = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - 1; j++) {
      if (a[j] > a[j + 1]) {
        // let temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp;
        [a[j], a[j + 1]] = [a[j + 1], a[j]]; //ES6 way of swap
        cnt++;
      }
    }
  }
  return a;
}

console.log(countSwaps([3, 2, 1, 1, 2, 2, 3, 5, 7, 8]));
