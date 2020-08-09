//https://www.hackerrank.com/challenges/minimum-swaps-2/

function minimumSwaps(arr) {
  const arr2 = arr.slice().sort((a, b) => a - b);
  const indexes = new Map();
  arr.forEach((v, i) => indexes.set(v, i));
  let swaps = 0;
  //compare given array to sorted array
  arr.forEach((v, i) => {
    if (v !== arr2[i]) {
      swaps++;
      arr[indexes.get(arr2[i])] = v; //get index of sorted value
      arr[i] = arr2[i];
      indexes.set(v, indexes.get(arr2[i]));
    }
  });
  return swaps;
}

console.log(minimumSwaps([2, 1, 5, 4, 3]));
