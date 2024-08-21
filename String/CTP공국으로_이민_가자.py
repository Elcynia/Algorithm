import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())

for k in range(T):
  M, S = input().split()
  if (S == 'C'):
    arr = list(input().split())
    for char in arr:
      print (ord(char) - (ord('A')-1), end=' ')
    print()
  else:
    arr = list(map(int, input().split()))
    for char in arr:
      print (chr(char + ord('A')-1), end=' ')
    print()