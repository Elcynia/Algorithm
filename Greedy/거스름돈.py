import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
coins = [500, 100, 50, 10, 5, 1]
money = 1000 - n
res = 0

for i in coins:
  res += money // i  # 해당 동전으로 거스름돈을 최대한 주기
  money %= i  # 남은 거스름돈 계산
print (res)