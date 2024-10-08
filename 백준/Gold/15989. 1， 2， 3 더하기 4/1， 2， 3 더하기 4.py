import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())
dp = [1] * 10001
for i in range(2, 4):  # 2와 3에 대해 반복
  for j in range(i, 10001):
    dp[j] += dp[j-i]
for _ in range(T):
    N = int(input())
    print(dp[N])