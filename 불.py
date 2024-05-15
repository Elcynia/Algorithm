import sys
from collections import deque
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def Fire_BFS(): # 불의 이동 시간
  Q = deque()
  for i in range(h):
    for j in range(w):
      if graph[i][j] == '*':
        Q.append((i, j))
        fire_time[i][j] = 0
  while Q:
    y, x = Q.popleft()
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < h and 0 <= nx < w and fire_time[ny][nx] == -1 and graph[ny][nx] != '#': # 벽 제외하고 방문하지 않은 곳 탐색
        fire_time[ny][nx] = fire_time[y][x] + 1
        Q.append((ny, nx))

def Move_BFS(): # 상근이의 이동 시간
  Q = deque()
  for i in range(h):
    for j in range(w):
      if graph[i][j] == '@':
        Q.append((i, j))
        sanggeun_time[i][j] = 0
      
  while Q:
    y, x = Q.popleft()
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if sanggeun_time[ny][nx] == -1 and graph[ny][nx] != '#': # 벽 제외하고 방문하지 않은 곳 탐색하는데
        # 불이 없거나 불이 있어도 상근이가 더 빠르게 도착할 수 있는 곳이라면
        if fire_time[ny][nx] == -1 or sanggeun_time[y][x] + 1 < fire_time[ny][nx]: 
          sanggeun_time[ny][nx] = sanggeun_time[y][x] + 1 # 상근이의 이동 시간 갱신
          Q.append((ny, nx)) 
        if ny == 0 or ny == h-1 or nx == 0 or nx == w-1: # 상근이가 끝자락에 도달하면 이동 시간 반환
          return sanggeun_time[ny][nx] + 1

  return "IMPOSSIBLE" # 상근이가 끝자락에 도달하지 못하면 IMPOSSIBLE 반환

for _ in range(T): 
    w, h = map(int, input().split()) # w: 가로, h: 세로 
    graph = [input().strip() for _ in range(h)] 
    fire_time = [[-1] * w for _ in range(h)]
    sanggeun_time = [[-1] * w for _ in range(h)]
    Fire_BFS()
    result = Move_BFS()
    print(result)
