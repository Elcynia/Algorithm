import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]
shortcuts.sort(key=lambda x: x[0])
dp = [i for i in range(D+1)]  

for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1] + 1)  # 1km 전진
    
    for start, end, length in shortcuts:
        if i == start and end <= D:
            dp[end] = min(dp[end], dp[i] + length)

print(dp[D])