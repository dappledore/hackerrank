function alternatingCharacters(s) {
  let arr = s.split("");
  let str = arr[0];

  for (let i = 1; i < arr.length; i++) {
    if (str[str.length - 1] != arr[i]) str += arr[i];
  }
  return s.length - str.length;
}

console.log(alternatingCharacters("AAAAAAAA"));
