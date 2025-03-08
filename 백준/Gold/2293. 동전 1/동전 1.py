import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, k = map(int, input().split())

dp = [0] * (k + 1)
dp[0] = 1  # 0원을 만드는 경우

for i in range(1, n + 1):
    coin = int(input())
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]

print(dp[k])
