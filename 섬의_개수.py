import sys
#sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

w, h = map(int, input().split())
while (w, h) != (0, 0):
    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1] # 상하좌우, 북서, 북동, 남서, 남동
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    cnt = 0
    def DFS(y, x):
        global visited, board
        visited[y][x] = 1
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= h or nx < 0 or nx >= w: # 범위 밖 필터링
                continue
            if not visited[ny][nx] and board[ny][nx]: # 아직 방문하지 않은 섬이면 탐색
                DFS(ny, nx)
    
    for i in range(h):
        for j in range(w):
            if board[i][j] and not visited[i][j]:
                DFS(i, j)
                cnt += 1
    print(cnt)
    w, h = map(int, input().split())

# [0]

# [0, 1]
# [1, 0]

# [1, 1, 1]
# [1, 1, 1]

# [1, 0, 1, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 1, 0, 1]
# [1, 0, 0, 1, 0]

# [1, 1, 1, 0, 1]
# [1, 0, 1, 0, 1]
# [1, 0, 1, 0, 1]
# [1, 0, 1, 1, 1]

# [1, 0, 1, 0, 1]
# [0, 0, 0, 0, 0]
# [1, 0, 1, 0, 1]
# [0, 0, 0, 0, 0]
# [1, 0, 1, 0, 1]