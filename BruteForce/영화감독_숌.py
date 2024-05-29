import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
number = 666
while n:
    if '666' in str(number):
        n -= 1
    number += 1
print(number-1)
