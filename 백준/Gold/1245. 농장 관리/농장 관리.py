import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().strip().split())
farm = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

def BFS(y, x):
  Q = deque([(y, x)])
  visited[y][x] = 1
  height = farm[y][x]
  top = True
  
  while Q:
    curY, curX = Q.popleft()
    for i in range(8):
      ny, nx = curY + dy[i], curX + dx[i]
      if 0 <= ny < N and 0 <= nx < M:
        if farm[ny][nx] > height:
          top = False
        elif farm[ny][nx] == height:
          if not visited[ny][nx]:
            visited[ny][nx] = 1
            Q.append((ny, nx))
  
  return top

cnt = 0
for i in range(N):
  for j in range(M):
    if farm[i][j] > 0 and not visited[i][j]:
      if BFS(i, j):
        cnt += 1

print(cnt)