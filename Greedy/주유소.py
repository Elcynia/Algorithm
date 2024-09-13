import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input()) # 도시 수
roads = list(map(int, input().split())) # 두 도시를 연결하는 도로 길이
oils = list(map(int, input().split())) # 리터 당 가격
min_cost = float('inf')
total = 0

for i in range(N-1):
  min_cost = min(min_cost, oils[i])
  total += min_cost * roads[i]
   
print(total)