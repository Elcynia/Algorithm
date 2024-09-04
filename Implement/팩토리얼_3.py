import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())

def func(k):
  r = 1
  for i in range(2, k+1):
     r *= i
  return r

print (func(n))