# https://www.hackerrank.com/challenges/time-conversion/problem
def timeConversion(s):
    hr = s[:2]
    if hr == "12":
        hr = "00"
    return str(int(hr)+12) + s[2:-2] if s[-2:] == "PM" else hr + s[2:-2]
