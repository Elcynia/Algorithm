import sys
input = sys.stdin.readline
n, k = map(int, input().split())
INF = float('inf')
dp = [INF] * (k+1)
dp[0] = 0
coins = [int(input()) for _ in range(n)]


for i in coins: 
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i] + 1) 

print(dp[k] if dp[k] != INF else -1)
