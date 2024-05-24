import sys
from collections import deque
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 빈 칸 위치 저장 리스트
empty_cells = []
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            empty_cells.append([y, x])  # 리스트로 저장

# 바이러스 확산 시뮬레이션 함수 (deque 기반 BFS)
def bfs(virus):
    while virus:
        y, x = virus.popleft()  # 큐에서 칸 하나 꺼냄

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = 2  # 바이러스로 감염
                virus.append([ny, nx])  # 큐에 추가

# 안전 영역 계산 함수
def count_safe_area():
    safe_area = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:  # 빈 칸
                safe_area += 1
    return safe_area

# 벽 설치 및 안전 영역 계산 함수
def install_wall(walls):
    # 벽 설치
    for y, x in walls:
        graph[y][x] = 1

    # 바이러스 확산 시뮬레이션 (BFS)
    virus = deque()
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 2:
                virus.append([y, x])
    bfs(virus)

    # 안전 영역 계산
    safe_area = count_safe_area()

    # 벽 제거
    for y, x in walls:
        graph[y][x] = 0

    return safe_area

# 최대 안전 영역 찾기
max_safe_area = 0
for walls in itertools.combinations(empty_cells, 3):
    max_safe_area = max(max_safe_area, install_wall(walls))

print(max_safe_area)