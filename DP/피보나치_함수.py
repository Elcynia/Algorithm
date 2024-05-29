import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
TC = int(input())

max_n = 0
test_cases = []

for _ in range(TC):
    n = int(input())
    test_cases.append(n)
    if n > max_n:
        max_n = n

dp = [[0, 0] for _ in range(max_n + 1)]

dp[0] = [1, 0]
if max_n > 0:
    dp[1] = [0, 1]

for i in range(2, max_n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

# 결과 출력
for n in test_cases:
    print(dp[n][0], dp[n][1])
