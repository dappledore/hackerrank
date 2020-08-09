function isPalindrome(str) {
  for (let i = 0, len = str.length; i < len / 2; i++) {
    if (str[i] != str[len - 1 - i]) return false;
  }
  return true;
}

console.log(isPalindrome("lllllllllllllkghlllllllllllll"));
