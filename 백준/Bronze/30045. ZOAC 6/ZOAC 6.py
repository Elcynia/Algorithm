import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    string = input().strip() 
    if '01' in string or 'OI' in string:
        cnt += 1

print(cnt)