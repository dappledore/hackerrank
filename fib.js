// 1,1,2,3,5,8,13

// function fib(n) {
//   if (n <= 2) return 1;

//   return fib(n - 1) + fib(n - 2);
// }

let memo = [];

function fib(n, memo) {
  // memo = memo || {};
  if (memo[n]) return memo[n];
  if (n <= 2) return 1;
  let result = fib(n - 1, memo) + fib(n - 2, memo);
  memo[n] = result;
  return result;
}

function fib_bottomup(n) {
  if (n <= 2) return 1;
  bottom_up = [];
  bottom_up[1] = 1;
  bottom_up[2] = 1;
  for (let i = 3; i <= n; i++) {
    bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2];
  }
  return bottom_up[n];
}

function fibMat(n) {
  let arr = Array(n).fill(1);
  let I = [
    //indetity matrix
    [0, 0],
    [1, 0],
    [0, 1],
  ];
  let T = [
    //Transform matrix
    [0, 0],
    [0, 1],
    [1, 1],
  ];
  if (n <= 2) return arr[2];

  n -= 1;
  while (n) {
    if (n % 2 == 1) {
      mul(I, T, 2);
      n--;
    } else {
      mul(T, T, 2);
      n /= 2;
    }
  }
}

function mul(A, B, dim) {
  let res = [dim + 1];
}

console.log(fib(100, memo));
console.log(fib_bottomup(101));
