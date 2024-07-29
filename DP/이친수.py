import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1][0] = 1

for i in range(2, n+1):
  for j in range(2):
    dp[i][j] = dp[i-1][j] + dp[i-2][j]
    
print (sum(dp[n]))
  