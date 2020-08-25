// https://www.hackerrank.com/challenges/js10-template-literals/problem

function readLine() {
  return inputString[currentLine++];
}

function sides(literals, ...expressions) {
  let a = expressions[0];
  let p = expressions[1];

  let m = (p ** 2 - 16 * a) ** 0.5;

  let s1 = (p + m) / 4;
  let s2 = (p - m) / 4;

  return [s1, s2].sort();
}

function main() {
  let s1 = +readLine();
  let s2 = +readLine();

  [s1, s2] = [s1, s2].sort();

  const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${
    2 * (s1 + s2)
  }.`;

  console.log(s1 === x ? s1 : -1);
  console.log(s2 === y ? s2 : -1);
}

main();
