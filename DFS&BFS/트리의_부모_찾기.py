import sys
# sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
res = [0]*(n+1)

def DFS(v):
  global visited, graph, res
  visited[v] = 1
  for i in graph[v]:
    if not visited[i]:
      res[i] = v
      DFS(i)


for _ in range(n-1):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

# for row in graph:
#   print (row)

DFS(1)
for i in range(2, n+1):
  print (res[i])