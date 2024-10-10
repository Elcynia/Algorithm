import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
r = list(range(1, N+1))
for _ in range(M):
  i, j = map(int, input().strip().split())
  r[i-1:j] = r[i-1:j][::-1]

print (*r)
