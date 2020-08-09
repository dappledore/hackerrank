function aclean(arr) {
  let words = new Map();
  for (let word of arr) {
    let sorted = word.split("").sort().join("").toLowerCase();
    words.set(sorted, word);
  }
  return [...words.values()];
}

let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

console.log(aclean(arr));
