# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import os


def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    ly = year % 4 == 0 and year % 100 > 0 or (
        year % 100 == 0 and year % 400 == 0) if year > 1918 else year % 4 == 0
    return f'12.09.{year}' if ly else f'13.09.{year}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
