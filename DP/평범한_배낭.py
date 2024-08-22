import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
ans = []
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
      
for i in range(1, N + 1):
  for j in range(1, K + 1):
    W, V = arr[i]
    if j < W: # 현재 물건의 무게가 j보다 크면 이전 물건 할당
      dp[i][j] = dp[i-1][j]
    else: # 그게 아니면 현재 물건과 넣지 않은 경우 둘 중 더 큰 값 선택
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)
            
print(dp[N][K])