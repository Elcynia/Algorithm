import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().strip().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
board1 = [list(map(int, input().strip().split())) for _ in range(N)]
board2 = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def BFS(y, x):
  before = board1[y][x]
  after = board2[y][x]
  Q = deque([(y, x)])
  visited[y][x] = True
  changed = [(y, x)]
  
  while Q:
    curY, curX = Q.popleft()
    for i in range(4):
      ny, nx = curY + dy[i], curX + dx[i]
      if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and board1[ny][nx] == before:
        visited[ny][nx] = True
        Q.append((ny, nx))
        changed.append((ny, nx))
        if board2[ny][nx] != after:
          return False
  
  for cy, cx in changed:
    if board2[cy][cx] != after:
      return False
  
  return True

result = "YES"
cnt = 0

for i in range(N):
  for j in range(M):
    if board1[i][j] != board2[i][j] and not visited[i][j]:
      if not BFS(i, j):
        result = "NO"
        break
      cnt += 1
  if result == "NO":
    break

if result == "YES" and cnt > 1:
  result = "NO"

print(result)