import sys
#sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

MAX = 50
n, m = map(int, input().split()) # 세로, 가로
board = [['']*(m+2) for _ in range(n+2)]
visited = [[False]*(m+2) for _ in range(n+2)]
res = 0


def DFS(y, x):
  global visited,board
  visited[y][x] = True
  if board[y][x] == '-' and board[y][x+1] == '-':
    DFS(y, x+1)
  elif board[y][x] == '|' and board[y+1][x] == '|':
    DFS(y+1, x)

for i in range(1, n+1):
  row = input()
  for j in range(1, m+1):
    board[i][j] = row[j-1]

for i in range(1, n+1):
  for j in range(1, m+1):
    if not visited[i][j]:
      DFS(i, j)
      res += 1

print (res)
