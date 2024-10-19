import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
board = [list(map(int, input().strip().split())) for _ in range(N)]
group_id = [[0]*M for _ in range(N)]

def BFS(y, x, id):
  size = 0
  Q = deque([(y, x)])
  group_id[y][x] = id
  while Q:
    cy, cx = Q.popleft()
    size += 1
    for i in range(4):
      ny, nx = cy + dy[i], cx + dx[i]
      if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1 and group_id[ny][nx] == 0:
        group_id[ny][nx] = id
        Q.append((ny, nx))
  return size

def find_max_shape():
  group_sizes = {}
  cur_id = 1
  for y in range(N):
    for x in range(M):
      if board[y][x] == 1 and group_id[y][x] == 0:
        group_sizes[cur_id] = BFS(y, x, cur_id)
        cur_id += 1
  
  max_size = max(group_sizes.values()) if group_sizes else 0
  
  for y in range(N):
    for x in range(M):
      if board[y][x] == 0:
        neighbor_groups = set()
        for i in range(4):
          ny, nx = y + dy[i], x + dx[i]
          if 0 <= ny < N and 0 <= nx < M and group_id[ny][nx] != 0:
            neighbor_groups.add(group_id[ny][nx])
        size = 1 + sum(group_sizes[g] for g in neighbor_groups)
        max_size = max(max_size, size)
  
  return max_size

print(find_max_shape())