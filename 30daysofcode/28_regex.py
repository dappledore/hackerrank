# https://www.hackerrank.com/challenges/30-regex-patterns/problem

#import re

if __name__ == '__main__':
    N = int(input())
    names = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        # can also actually use a regex re.search('@gmail\.com$', emailID): or  '@gmail.com' in emailID:
        if emailID.endswith("@gmail.com"):
            names.append(firstName)

    for name in sorted(names):
        print(name)
