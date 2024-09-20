import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]


# 첫 번째 행 초기화 (출발점 연료 소비량 계산)
for j in range(m):
    for k in range(3):
        dp[0][j][k] = graph[0][j]
        
# DP
for i in range(1, n):
    for j in range(m):
        if j > 0:  # 7시 방향 계산
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + graph[i][j]
            # 이전 행의 오른쪽 열에서 수직 또는 오른쪽 대각선으로 온 경우 중 최소값 + 현재 위치 연료
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + graph[i][j]  # 6시 방향 계산
        # 이전 행의 같은 열에서 왼쪽 대각선 또는 오른쪽 대각선으로 온 경우 중 최소값 + 현재 위치 연료
        if j < m-1:  # 5시 방향 계산
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + graph[i][j]
            # 이전 행의 왼쪽 열에서 왼쪽 대각선 또는 수직으로 온 경우 중 최소값 + 현재 위치 연료

result = min(min(dp[n-1][j]) for j in range(m))
print(result)