// https://www.hackerrank.com/challenges/js10-arrays/problem
function getSecondLargest(nums) {
  return [...new Set(nums)].sort((a, b) => b - a)[1];
}

console.log(getSecondLargest([1, 2, 3, 4, 5, 5, 6]));
