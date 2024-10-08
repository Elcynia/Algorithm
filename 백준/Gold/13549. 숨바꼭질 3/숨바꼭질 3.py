from collections import deque
import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 100001

def BFS(N, K):
  dist = [-1] * MAX  # 각 위치까지의 최소 시간을 저장
  Q = deque()
  Q.append(N)
  dist[N] = 0

  while Q:
    x = Q.popleft()
    if x == K:
      return dist[x]
    
    # 순간이동 (0초 소요)
    if 0 <= 2*x < MAX and dist[2*x] == -1: # 아직 방문하지 않은 곳 중에서 텔포 시도
      dist[2*x] = dist[x]
      Q.appendleft(2*x)  # 텔포한 것부터(0s) 우선 처리를 위해 큐의 앞에 추가 (최단 시간 보장)
    
    # 걷기 (1초 소요)
    for nx in (x-1, x+1):
      if 0 <= nx < MAX and dist[nx] == -1:
        dist[nx] = dist[x] + 1
        Q.append(nx)

print(BFS(N, K))