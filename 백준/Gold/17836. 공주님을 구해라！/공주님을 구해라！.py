import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M, T = map(int, input().strip().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
board = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

def BFS(y, x):
  Q = deque([(y, x, 0, False)])  # y, x, time, has_sword
  visited[y][x][0] = True
  
  while Q:
    curY, curX, time, has_sword = Q.popleft()
    
    if time > T:
      continue
    
    if curY == N-1 and curX == M-1:  # 도착 시간
      return time
    
    for i in range(4):
      ny, nx = curY + dy[i], curX + dx[i]
      if 0 <= ny < N and 0 <= nx < M:
        if has_sword and not visited[ny][nx][1]:
          visited[ny][nx][1] = True
          Q.append((ny, nx, time+1, True))
        elif not has_sword:
          if board[ny][nx] == 0 and not visited[ny][nx][0]:
            visited[ny][nx][0] = True
            Q.append((ny, nx, time+1, False))
          elif board[ny][nx] == 2 and not visited[ny][nx][1]:
            visited[ny][nx][1] = True
            Q.append((ny, nx, time+1, True))
  
  return float('inf')

r = BFS(0, 0)
print (r if r <= T else 'Fail')