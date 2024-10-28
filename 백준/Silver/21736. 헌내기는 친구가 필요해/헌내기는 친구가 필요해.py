import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().strip().split())
board = [input().strip() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(y, x):
  Q = deque([(y, x)])
  visited[y][x] = True
  cnt = 0

  while Q:
    curY, curX = Q.popleft()
    for i in range(4):
      ny, nx = curY + dy[i], curX + dx[i]
      if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
        if board[ny][nx] != 'X':
          visited[ny][nx] = True
          Q.append((ny, nx))
          if board[ny][nx] == 'P':
            cnt += 1

  return cnt

# i 탐색
start_y, start_x = None, None
for i in range(N):
  for j in range(M):
    if board[i][j] == 'I':
      start_y, start_x = i, j
      break
  if start_y != None:
    break

result = BFS(start_y, start_x)

print(result if result > 0 else "TT")