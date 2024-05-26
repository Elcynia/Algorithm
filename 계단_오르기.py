import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
stair = [int(input()) for _ in range(n)]

def solution(n, stair):
    if n == 1:
        return stair[0]
    if n == 2:
        return stair[0] + stair[1]
    dp = [0] * n

    # 초기값 설정
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

    # 점화식을 이용하여 DP 테이블 채우기
    for i in range(3, n):
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

    # 마지막 계단까지 도달했을 때 얻을 수 있는 최대 점수 출력
    return dp[-1]

print(solution(n, stair))