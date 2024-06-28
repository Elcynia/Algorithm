import sys, re
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
for i in range(n):
  s = input()
  if (re.match(r'^.{6,9}$', s)):
    print ("yes")
  else:
    print ("no")
  