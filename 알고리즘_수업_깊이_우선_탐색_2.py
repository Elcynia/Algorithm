import sys
# sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v):
  global visited, graph, res, order
  visited[v] = 1
  res[v] = order
  order += 1
  for i in graph[v]:
    if not visited[i]:
      DFS(i)
    

n,m,r = map(int, input().split())
visited = [0] * (n+1)
res = [0] * (n+1)
order = 1
graph = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1,n+1):
  graph[i].sort(reverse=True)

DFS(r)
for i in range(1, n+1):
  print (res[i])