import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
r = 0
while (True):
  a, b = map(int,input().split())
  if (a == b == 0):
    break
  else:
    print (2*a-b)
  