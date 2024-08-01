import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = [-1] + list(map(int, input().split())) # 1-indexed
dp = [0] * (n+1)
dp[1] = arr[1]
for i in range(2, n+1):
  dp[i] = arr[i]
  for j in range(1, i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + arr[i])
print (max(dp))