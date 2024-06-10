import sys
from collections import deque
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split()) # 가로, 세로
graph = [list(map(str, input().strip())) for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[0]*(N) for _ in range(M)]
def BFS(y, x):
  w = 0
  b = 0
  Q = deque()
  Q.append([y, x])
  visited[y][x] = 1

  while Q:
    y, x = Q.popleft()
    color = graph[y][x]
    if color == 'W':
      w += 1
    else:
      b += 1
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and graph[ny][nx] == color:
        visited[ny][nx] = 1
        Q.append([ny, nx])
  return w, b
        
total_w = 0 
total_b = 0

for i in range(M):
  for j in range(N):
    if not visited[i][j]:
      w_cnt, b_cnt = BFS(i, j)
      if w_cnt > 0:
        total_w += w_cnt ** 2
      else:
        total_b += b_cnt ** 2

print(total_w, total_b)