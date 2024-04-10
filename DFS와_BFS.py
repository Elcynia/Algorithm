import sys
# sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(idx):
  global visited1, graph
  visited1[idx] = 1
  print (idx, end=' ')
  for i in range(1, n+1):
    if not visited1[i] and graph[idx][i] == 1:
      DFS(i)

def BFS(idx):
  global visited2, graph
  queue = [idx]
  while queue: # queue가 빌 때까지
    visited2[idx] = 1
    x = queue.pop(0)
    print (x, end=' ')
    for i in range(1, n+1):
      if not visited2[i] and graph[x][i] == 1:
        queue.append(i)
        visited2[i] = 1

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited1 = [0]*(n+1)
visited2 = [0]*(n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1


DFS(v)
print()
BFS(v)
