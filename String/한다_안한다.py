import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
for i in range(n):
  s = input()
  print ('Do-it' if s[len(s)//2-1] == s[len(s)//2] else 'Do-it-Not')
