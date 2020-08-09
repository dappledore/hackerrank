var findMaxConsecutiveOnes = function (nums) {
  let cnt = 0,
    max = 0;
  for (i = 0; i < nums.length; i++) {
    if (nums[i] === 0) cnt = 0;
    else cnt++;
    max = Math.max(max, cnt);
  }
  return max;
};

console.log(findMaxConsecutiveOnes([1]));
