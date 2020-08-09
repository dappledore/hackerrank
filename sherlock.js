//https://www.hackerrank.com/challenges/sherlock-and-valid-string
function isValid(s) {
  let cnts = {};
  let difs = [];
  Array.from(s).forEach((c) => {
    cnts[c] = cnts[c] || 0;
    cnts[c]++;
  });
  let pivot;
  Object.keys(cnts).forEach((k) => {
    if (!pivot) pivot = cnts[k];
    if (pivot != cnts[k]) difs.push(cnts[k]);
  });
  return difs.length > 1 ? "NO" : "YES";
}

console.log(isValid("abdddde"));
