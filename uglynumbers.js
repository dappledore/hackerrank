let args = process.argv.slice(2);
let n = args[0] || 112;

function maxDivide(a, b) {
  while (a % b == 0) a = a / b;
  return a;
}

function isUgly(no) {
  no = maxDivide(no, 2);
  console.log(no);
  no = maxDivide(no, 3);
  console.log(no);
  no = maxDivide(no, 5);
  console.log(no);

  return no == 1;
}

console.log(isUgly(n));
