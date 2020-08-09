# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Day 8
n = int(input())

pb = {}

for i in range(n):
    line = input().split(' ')
    pb[line[0]] = line[1]

# name_numbers = [input().split() for _ in range(n)]
# pb = {k: v for k,v in name_numbers}

name = ''
while True:
    try:
        name = input()
        if name in pb:
            print('{}={}'.format(name, pb[name]))
        else:
            print('Not found')
    except EOFError:
        break
