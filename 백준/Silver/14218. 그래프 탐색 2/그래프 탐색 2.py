import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  u, v = map(int, input().strip().split())
  graph[u].append(v)
  graph[v].append(u)

Q = int(input())
roads = [list(map(int, input().strip().split())) for _ in range(Q)]

def BFS():
  distances = [-1] * (N+1)
  Q = deque([1])
  distances[1] = 0
  
  while Q:
    cur = Q.popleft()
    for i in graph[cur]:
      if distances[i] == -1:
        distances[i] = distances[cur] + 1
        Q.append(i)
  
  return distances[1:]

for u, v in roads:
  graph[u].append(v)
  graph[v].append(u)
  print(*BFS())