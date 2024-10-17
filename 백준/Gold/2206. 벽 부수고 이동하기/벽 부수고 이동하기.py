import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]
graph = [list(input().strip()) for _ in range(N)]

def BFS(start):
  Q = deque([(start[0], start[1], 0, 1)])  # y, x, 벽 부순 여부, 이동 거리
  visited[start[0]][start[1]][0] = True
  while Q:
    y, x, broken, dist = Q.popleft()
    if y == N-1 and x == M-1:
      return dist
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < N and 0 <= nx < M:
        if graph[ny][nx] == '0' and not visited[ny][nx][broken]:
          visited[ny][nx][broken] = True
          Q.append((ny, nx, broken, dist + 1))
        elif graph[ny][nx] == '1' and broken == 0:
          visited[ny][nx][1] = True
          Q.append((ny, nx, 1, dist + 1))
  return -1

print (BFS((0, 0)))