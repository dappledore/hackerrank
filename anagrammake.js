//https://www.hackerrank.com/challenges/ctci-making-anagrams
//Return the number of deletes needed to make a string an anagram
//add letters on string a , then substract on string b any unbalance will be added total
function makeAnagram(a, b) {
  let counter = {};
  let total = 0;
  Array.from(a).forEach((c) => {
    counter[c] = counter[c] || 0;
    counter[c] += 1;
  });
  Array.from(b).forEach((c) => {
    counter[c] = counter[c] || 0;
    counter[c] -= 1;
  });
  Object.keys(counter).forEach((k) => {
    if (counter[k] !== 0) total += Math.abs(counter[k]);
  });
  return total;
}

console.log(makeAnagram("abc", "acbz"));
