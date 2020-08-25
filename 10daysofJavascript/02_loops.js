// https://www.hackerrank.com/challenges/js10-loops/problem

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
  for (let v of s) {
    if (/^[aeiou]/.test(v)) console.log(v); //could also use "aeiou".includes(v)
  }
  for (let c of s) {
    if (/^[^aeiou]/.test(c)) console.log(c);
  }
}
