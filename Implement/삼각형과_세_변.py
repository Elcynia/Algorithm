import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
while True:
  a, b, c = map(int, input().split())
  if (a == b == c == 0): break
  if (max(a, b, c) >= (a+b+c - max(a,b,c))): print ('Invalid')
  else:
    if (a == b == c): print ('Equilateral')
    elif ((a == b) or (a == c) or (b == c)): print ('Isosceles')
    elif ((a != b) and (a != c)): print ('Scalene')