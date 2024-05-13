import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  s = input().strip()
  print(s[0],  s[-1], sep='')