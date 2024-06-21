import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

remainder = int(input()) % 8

if remainder == 1:
    res = 1
elif remainder == 0 or remainder == 2:
    res = 2
elif remainder == 3 or remainder == 7:
    res = 3
elif remainder == 4 or remainder == 6:
    res = 4
elif remainder == 5:
    res = 5

print(res)