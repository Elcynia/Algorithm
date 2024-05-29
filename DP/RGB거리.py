import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
r,g,b = map(int, input().split())
dp = [[0]*3 for _ in range(n)]
dp[0] = [r,g,b]
print (dp)
for i in range(1,n):
    r,g,b = map(int, input().split())
    dp[i][0] = r + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = g + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = b + min(dp[i-1][0], dp[i-1][1])
print(min(dp[n-1]))
