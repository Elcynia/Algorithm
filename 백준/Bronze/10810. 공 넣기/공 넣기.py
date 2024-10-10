import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
r = [0] * N
for i in range(M):
  i, j, k = map(int, input().strip().split())
  for ball in range(i-1, j):
   r[ball] = k

print (*r)