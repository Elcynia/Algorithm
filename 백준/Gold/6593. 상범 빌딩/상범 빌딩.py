import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0] # 위층, 아래층

def BFS(start):
  Q = deque([start])
  visited = [[[False]*C for _ in range(R)] for _ in range(L)]
  visited[start[0]][start[1]][start[2]] = True
  time = 0

  while Q:
    for _ in range(len(Q)):
      z, x, y = Q.popleft()
      
      if building[z][x][y] == 'E':
        return f"Escaped in {time} minute(s)."
      
      for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
          if not visited[nz][nx][ny] and building[nz][nx][ny] != '#':
            visited[nz][nx][ny] = True
            Q.append((nz, nx, ny))
    
    time += 1
  
  return "Trapped!"

while True:
  L, R, C = map(int, input().strip().split())
  if L == 0 and R == 0 and C == 0:
    break

  building = []
  start = 0

  for i in range(L):
    floor = [list(input().strip()) for _ in range(R)]
    building.append(floor)
    input()

    if not start:
      for j in range(R):
        for k in range(C):
          if building[i][j][k] == 'S':
            start = (i, j, k)
            break
        if start:
          break

  print(BFS(start))