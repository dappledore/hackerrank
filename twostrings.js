//https://www.hackerrank.com/challenges/two-strings/
//2 strings have same substring, substring can be one character

function twoStrings(s1, s2) {
  let s = {};
  s1.split("").map((str) => {
    s[str] = true;
  });

  for (i = 0; i < s2.length - 1; i++) {
    if (s[s2[i]]) return "YES";
  }
  return "NO";
}

console.log(twoStrings("hello", "cat"));
