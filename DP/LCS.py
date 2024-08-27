import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
a = list(input().strip())
b = list(input().strip())
n = len(a)
n2 = len(b)
dp = [[0] * (n2+1) for _ in range(n+1)]
# print (dp)
for i in range(1, n+1):
  for j in range(1, n2+ 1):
    if a[i-1] == b[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1 # 두 값이 동일하면 이전 값 대입
    else: # 다르면 이전에 있는 lcs 중 더 큰 값 대입
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      
print (dp[n][n2])