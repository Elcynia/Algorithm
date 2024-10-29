import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]
N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

def BFS():
  Q = deque()
  # 모든 아기 상어의 위치를 큐에 넣고 거리를 0으로 초기화
  for y in range(N):
    for x in range(M):
      if board[y][x] == 1:
        Q.append((y, x))
        dist[y][x] = 0
  
  while Q:
    curY, curX = Q.popleft()
    for i in range(8):
      ny, nx = curY + dy[i], curX + dx[i]
      if 0 <= ny < N and 0 <= nx < M and dist[ny][nx] == -1:
        dist[ny][nx] = dist[curY][curX] + 1
        Q.append((ny, nx))
  
  return max(max(row) for row in dist)

print(BFS())