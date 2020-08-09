//5! = 5x4x3x2x1
//5 5*24
//4 4*6
//3 3*2
//2 2*1
//1 1
function fact(n) {
  if (n == 1) return 1;
  return n * fact(n - 1);
}

console.log(fact(5));
