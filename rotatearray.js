//https://www.hackerrank.com/challenges/ctci-array-left-rotation/
//rotate an array left , d can be 10^5
function rotLeft(a, d) {
  let count = d % a.length;
  a.push.apply(a, a.splice(0, count)); // splice remove count from array and returns removed portion this then gets added onto end of array
  return a;
}

console.log(rotLeft([1, 2, 3, 4, 5], 0));
