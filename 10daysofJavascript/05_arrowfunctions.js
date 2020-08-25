// https://www.hackerrank.com/challenges/js10-arrows/problem

function modifyArray(nums) {
  return nums.map((a) => (a % 2 ? a * 3 : a * 2));
}
