// https://www.hackerrank.com/challenges/js10-switch/problem
function getLetter(s) {
  let letter;
  // Write your code here
  switch (true) {
    case /^[aeiou]/.test(s):
      letter = "A";
      break;
    case /^[bcdfg]/.test(s):
      letter = "B";
      break;
    case /^[hjklm]/.test(s):
      letter = "C";
      break;
    case /^[npqrstvwxyz]/.test(s):
      letter = "D";
      break;
  }
  return letter;
}
