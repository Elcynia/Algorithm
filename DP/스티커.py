import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  n = int(input())
  arr = [list(map(int, input().split())) for _ in range(2)]
  dp = [[0] * (n+1) for _ in range(2)]
  # 초기값 설정
  dp[0][0], dp[1][0] = arr[0][0], arr[1][0]
  dp[0][1] = arr[1][0] + arr[0][1]
  dp[1][1] = arr[0][0] + arr[1][1]
  
  for i in range(2, n):
    dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
    # 이전 열의 아래쪽 스티커를(dp[1][i-1]) 선택한 경우와 전전 열의 아래쪽 스티커를 선택한 경우 (dp[1][i-2]), 현재 열의 위쪽 스티커 점수(arr[0][i])
    dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]
    # 이전 열의 위쪽 스티커를(dp[1][i-1]) 선택한 경우와 전전 열의 위쪽 스티커를 선택한 경우 (dp[1][i-2]), 현재 열의 아래쪽 스티커 점수(arr[1][i])
  print (max(dp[0][n-1], dp[1][n-1]))
  