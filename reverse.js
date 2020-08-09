//let str = "hello".split("").reverse().join("");

let target = Array(100).fill("abc").join("");

let str = "";

// for (let i = target.length - 1; i >= 0; i--) {
//   str += target[i];
// }

let num = target.length;

while (num >= 0) {
  num--;
  str += target.charAt(num);
}

console.log(str);

// function reverse(str, num) {
//   if (num < 0) return "";

//   return str.charAt(num) + reverse(str, num - 1);
// }

// let str = Array(1000).fill("abc").join("");

// console.log(reverse(str, str.length));
