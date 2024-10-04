import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, Q = map(int, input().strip().split())
arr = [0] * N
for i in range(Q):
  L, I = map(int, input().strip().split())
  for j in range(L-1, N, I):
    arr[j] = 1
print (arr.count(0))