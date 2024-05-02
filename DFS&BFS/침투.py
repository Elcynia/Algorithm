import sys
sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(y, x):
  global visited, board, res, M, N
  if y == M:
    res = 1
    return
    
  visited[y][x] = 1
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny < 1 or ny > M or nx < 1 or nx > N:
      continue
    if board[ny][nx] and not visited[ny][nx]:
      DFS(ny, nx)


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

M, N = map(int, input().split()) # 5 6
board = [[0] * (N+1) for _ in range(M+1)]
visited = [[0] * (N+1) for _ in range(M+1)]
res = 0

for i in range(1, M+1):
  row = input()
  for j in range(1, N+1):
    if (row[j - 1] == "0"):
      board[i][j] = 1

for j in range(1, N + 1):
    if board[1][j]:
      DFS(1, j)


if (res == 1):
  print("YES")
else:
  print ("NO")

for i in board:
  print (i)
