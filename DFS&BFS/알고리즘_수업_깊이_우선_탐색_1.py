import sys
sys.stdin = open('./input.txt', 'r')
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
  
n, m, r = map(int, input().split()) # 정점, 간선, 시작 정점
res = [0] * (n+1)
visited = [0] * (n+1) # 방문 여부
order = 1 # 방문 순서
graph = [[]*(n+1) for _ in range(n+1)] # 인접 리스트 생성
for _ in range(m): # 간선 정보 입력 
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1,n+1):
  graph[i].sort()

DFS(r)

for i in range(1,n+1):
  print (res[i])

