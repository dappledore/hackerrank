# https: // www.hackerrank.com/challenges/sherlock-and-valid-string
from collections import Counter


def isValid(s):
    freq = [v for k, v in Counter(s).items()]
    pivot = freq[0]
    different_freqs = []
    for i in freq[1::]:
        if(pivot != i):
            different_freqs.append(i)
    if(len(different_freqs) > 1):
        return 'NO'
    else:
        return 'YES'


print(isValid("aabbccdd"))
