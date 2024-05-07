import sys
from collections import deque
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
TC = int(input()) # 테스트 케이스의 개수
dy = [-2, -2, 2, 2, -1, -1, 1, 1]
dx = [1, -1, 1, -1, 2, -2, 2, -2]

def BFS(y, x, ty, tx):
  Q = deque()
  Q.append([y, x])
  graph[y][x] = 1
  while Q:
    y, x = Q.popleft()
    
    if (y == ty) and (x == tx):
      return graph[y][x] - 1
    
    for i in range(8):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < l and 0 <= nx < l and graph[ny][nx] == 0:
        graph[ny][nx] = graph[y][x] + 1
        Q.append([ny, nx])
  return -1


for i in range(TC):
  l = int(input()) # 체스판의 한 변의 길이
  currentY, currentX = map(int, input().split()) # 나이트의 현재 위치
  targetY, targetX = map(int, input().split()) # 나이트가 이동하려는 위치
  graph = [[0] * (l+1) for _ in range(l+1)]
  print(BFS(currentY, currentX, targetY, targetX))