import sys, copy
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
graph = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
wall = 0


def BFS():
  Q = deque([])
  tmp = copy.deepcopy(graph)
  for i in range(N):
    for j in range(M):
      if tmp[i][j] == 2:
        Q.append((i, j))
  
  while Q:
    curY, curX = Q.popleft()
    for i in range(4):
      ny, nx = curY + dy[i], curX + dx[i]
      if 0 <= ny < N and 0 <= nx < M and tmp[ny][nx] == 0: 
        tmp[ny][nx] = 2
        Q.append((ny, nx))
  
  safe_area = sum(row.count(0) for row in tmp)
  return safe_area

def set_wall(wall):
  if wall == 3:
    return BFS()
  
  max_safe = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0:
        graph[i][j] = 1
        max_safe = max(max_safe, set_wall(wall + 1))
        graph[i][j] = 0
  
  return max_safe

print(set_wall(0))