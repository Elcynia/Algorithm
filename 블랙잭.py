import sys
# sys.stdin = open('./input.txt', 'rt')
N, M = map(int, input().split())
cards = list(map(int, input().split()))
r = 0

for i in range(N-2): # 첫번째 카드 픽 (세번째 카드까지 확인) 0 1 2
  for j in range(i+1, N-1): # 두번째 카드 픽 (첫번째 경우의 수 이후의 조합)  1 2 3, 2 3, 3
    for k in range(j+1, N): # 세번째 카드 픽 (두번째 경우의 수 이후의 조합)
      t = cards[i] + cards[j] + cards[k]
      if t <= M:
        r = max(r, t)
print (r)
      