import sys
# sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v, cnt):
  global res, visited, graph, f2
  visited[v] = 1
  if v == f2:
    res = cnt
    return
  for i in range(1, n+1):
    if not visited[i] and graph[v][i] == 1:
      DFS(i, cnt+1)


n = int(input()) # 전체 사람의 수
f1, f2 = map(int, input().split()) # 찾고자 하는 두 사람의 번호
m = int(input()) # 부모 자식들의 관계의 수
res = -1
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1
DFS(f1, 0)
print (res)