import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
s = input().strip() 
if (s == s[::-1]):
  print ('true')
else:
  print ('false')