import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())
dp = [[0] * (N+1) for _ in range(K+1)]
dp[0][0] = 1
 
for i in range(1, K+1):
    cur = [0] * (N+1)
    cur[0] = dp[i-1][0]

    for n in range(1, N+1):
        cur[n] = cur[n-1] + dp[i-1][n]

    for n in range(N+1):
        dp[i][n] = cur[n] % 1000000000

print(dp[K][N])