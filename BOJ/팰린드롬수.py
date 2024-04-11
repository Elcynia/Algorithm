import sys
sys.stdin = open('./input.txt', 'r')
n = int(sys.stdin.readline())
while(n != 0):
  if n == int(str(n)[::-1]):
    print('yes')
  else:
    print('no')
  n = int(sys.stdin.readline())  