import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())

for i in range(n):
  print ('*'*(n-i))