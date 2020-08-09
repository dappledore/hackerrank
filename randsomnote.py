# https://www.hackerrank.com/challenges/ctci-ransom-note/

from collections import Counter


def ransom_note(magazine, ransom):
    return (Counter(ransom) - Counter(magazine)) == {}


print(ransom_note(["give", "give", "me", "one", "grand", "today", "night"],
                  ["give", "one", "grand", "today"]))
