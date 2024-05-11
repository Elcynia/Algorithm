import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split()) # 종류, 합
arr = sorted([int(input()) for _ in range(N)], reverse=True)
ans = 0

for i in range(N):
  ans += K // arr[i]
  K %= arr[i]
print (ans)