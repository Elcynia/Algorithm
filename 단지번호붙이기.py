import sys
#sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*(n) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
res = 0
cnt = 0
res2 = []

def dfs(y, x):
    global cnt
    cnt += 1
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[ny][nx] == 1 and not visited[ny][nx]:
            dfs(ny, nx)

for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            dfs(i, j)
            res += 1
            res2.append(cnt)
            cnt = 0

print(res)
for i in sorted(res2):
    print(i)
