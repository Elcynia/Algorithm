import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
A, B, N, M = map(int, input().strip().split()) # 힘A, 힘B, 동규 현위치, 주미 현위치
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
graph = [list(input().strip()) for _ in range(N)]
def BFS(A, B, N, M):
  queue = deque([(N, 0)])  # (현재 위치, 이동 횟수)
  visited = set([N])
  mx = 100000  

  while queue:
    current, moves = queue.popleft()
    
    if current == M:
      return moves  
    
    next_positions = [
      current - 1, current + 1,
      current - A, current + A,
      current - B, current + B,
      current * A, current * B
    ]
    
    for next_pos in next_positions:
      if 0 <= next_pos <= mx and next_pos not in visited:
        visited.add(next_pos)
        queue.append((next_pos, moves + 1))
  
  return -1  # 도달할 수 없는 경우

print(BFS(A, B, N, M))