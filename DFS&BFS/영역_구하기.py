import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
M, N, K = map(int, input().split())
graph = [[0] * (M) for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
cnt = 0
answer = []

def BFS(y, x):
  global cnt
  Q = deque()
  Q.append([y, x])
  graph[y][x] = 1
  while Q:
    y, x = Q.popleft()
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
        graph[ny][nx] = 1
        Q.append([ny, nx])
        cnt += 1
      
        
for _ in range(K):
  y1, x1, y2, x2 = map(int, input().split())
  for i in range(y1, y2): # range(y1, y2)로 하면 y1부터 y2-1까지
    for j in range(x1, x2): # range(x1, x2)로 하면 x1부터 x2-1까지 
      graph[i][j] = 1
      
# for i in graph:
#   print (i)

for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      cnt = 1
      BFS(i, j)
      answer.append(cnt)
print (len(answer))
print (*sorted(answer))
      

