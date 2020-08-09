let arr = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 33, 3];

arr = Array.from(new Set(arr)); //using Set , prob best method

// arr = arr.filter((v, i) => arr.indexOf(v) == i); //using filter

// arr = arr.reduce(
//   (acc, item) => (acc.includes(item) ? acc : [...acc, item]),
//   []
// ); //use reduce

// let newArr = [];

// arr.map((v) => {
//   if (!newArr[v]) {
//     newArr[v] = v;
//   }
// });

//using associative array
// useAssociative = (arr) => {
//   let uniq = [];
//   for (const val of arr) {
//     uniq[val] = 0;
//   }
//   return Object.keys(uniq);
// };

// console.log(useAssociative(arr));

// //using array
// useIncludes = (arr) => {
//   let uniq = [];
//   for (const val of arr) {
//     if (!arr.includes(val)) uniq.push(val);
//   }
//   return uniq;
// };

var removeDuplicates = function (nums) {
  //inplace removal
  for (let i = nums.length - 1; i > 0; i--) {
    if (nums[i] == nums[i - 1]) nums.splice(i, 1);
  }
};

// console.log(useIncludes(arr));

console.log(arr);
