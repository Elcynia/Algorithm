import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
a, b = map(int, input().split())

while (not a == b):
  a += 1
  one = a * 2
  two = int(str(a) + str(1))
  print (two)
  print (a)