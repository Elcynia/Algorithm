import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, M, R = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)

for _ in range(M):  # 양방향 그래프 연결
  e, v = map(int, input().strip().split())
  graph[e].append(v)
  graph[v].append(e)

# 각 정점의 인접 리스트를 내림차순으로 정렬
for i in range(1, N+1):
  graph[i].sort(reverse=True)

def BFS(start):
  queue = deque([start])
  visited[start] = 1
  order = 1

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        order += 1
        visited[i] = order

BFS(R)

for i in range(1, N+1):
  print(visited[i])