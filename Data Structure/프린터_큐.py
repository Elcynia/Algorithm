import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
TC = int(input())

for _ in range(TC):
  N, M = map(int, input().split()) # 문서의 개수, 현재 Queue에서 몇 번째에 놓여 있는지 (맨왼쪽이 0번째)
  priority = list(map(int, input().split())) # 문서 중요도 (값이 높을 수록 중요함)
  Q = deque([(i, p) for i, p in enumerate(priority)])
  cnt = 0
  while True:
    if Q[0][1] == max(Q, key=lambda x: x[1])[1]:
      cnt += 1
      cleanup = Q.popleft()
      if cleanup[0] == M:
        print (cnt)
        break
    else:
      Q.append(Q.popleft())