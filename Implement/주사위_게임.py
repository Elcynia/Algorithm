import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
res_a, res_b = 100, 100
for i in range(n):
  a, b = map(int, input().split())
  if (a > b):
    res_b -= a
  elif (a < b):
    res_a -= b
  else:
    continue
print (res_a, res_b, sep='\n')