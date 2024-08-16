import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)] # 1-indexed
dp = [[0] * (N + 1) for _ in range(N + 1)]

# 2차원 누적합 배열
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]
        # dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i][j]
        # 현재 좌표 기준으로 위쪽 (dp[i-1][j]) + 왼쪽 (dp[i][j-1]) - 왼쪽대각선(dp[i-1][j-1]을 하면 현재 좌표 [i][j]를 포함하는 영역의 합)
        # but, 이 누적합 과정에서 dp[i-1][j-1]의 좌표가 두번 합산되므로 중복 제거를 위해 - dp[i-1][j-1]
        # 현재 위치의 값 + arr[i][j]

# 구간 합
for x1, y1, x2, y2 in [map(int, input().split()) for _ in range(M)]:
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)