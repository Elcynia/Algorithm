import sys
# sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ans = 0

def DFS(y, x, h):
  visited[y][x] = True
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and board[ny][nx] > h:
      DFS(ny, nx, h)

for h in range(max(map(max, board))):
  visited = [[False]*(n) for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if board[i][j] > h and not visited[i][j]:
        DFS(i, j, h)
        cnt += 1
  ans = max(ans, cnt)
print (ans)