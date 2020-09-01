# https://www.hackerrank.com/challenges/strange-advertising/problem

def viralAdvertising(n):
    person = 5
    count = 0
    while n > 0:
        interested = person // 2
        person = interested * 3
        count += interested
        n -= 1
    return count


print(viralAdvertising(5))
