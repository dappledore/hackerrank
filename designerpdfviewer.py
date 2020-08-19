#!/bin/python3

# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
import os

# Complete the designerPdfViewer function below.


def designerPdfViewer(h, word):
    m = 0
    for w in word:
        m = max(h[ord(w) - 97], m)
    return m * len(word)

# without ord function , using dictionary
# def designerPdfViewer(h, word):
#     l = 'abcdefghijklmnopqrstuvwxyz'
#     d = dict(zip(l, h))
#     return len(word)*max([d[w] for w in word])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
