//https://www.hackerrank.com/challenges/ctci-ransom-note/
//Are all notes words contained in magazine words
const print = function (d) {
  process.stdout.write(d + "\n");
};

function checkMagazine(magazine, note) {
  let words = {};
  magazine.map((word) => {
    words[word] = words[word] || 0;
    words[word] += 1;
  });
  for (let i = 0; i < note.length; i++) {
    if (!words[note[i]] || words[note[i]] <= 0) {
      print("No");
      return;
    }
    words[note[i]] -= 1;
  }
  print("Yes");
}

checkMagazine(
  ["give", "me", "one", "grand", "today", "night"],
  ["give", "give", "one", "grand", "today"]
);
