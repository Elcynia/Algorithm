import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input()) # 금액
k = int(input()) # 동전의 가지 수
coins = [list(map(int, input().split())) for _ in range(k)]
dp = [0] * (T+1) # 1~20
dp[0] = 1

for coin, cnt in coins: # 5원, 10원, 1원 순회 ex) [5, 3], [10, 2] ...
  for money in range(T, 0, -1): # T원부터 내림차순으로 (중복 계산 방지) ex) 20, 19, 18...
    for i in range(1, cnt + 1): # 각 동전의 개수 순회 
      if money - coin * i >= 0: # 현재 금액에서 동전을 뺀 값이 0원 이상이면,
        dp[money] += dp[money - coin * i] # 경우의 수 추가
      else:
        break

print(dp[T])