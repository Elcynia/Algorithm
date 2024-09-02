import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input()) # 도시
m = int(input()) # 한 도시에서 출발하여 다른 도시에 도착하는 버스 수
INF = float('inf')
graph = [[INF] * (n) for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in graph:
    result = []
    for x in i:
        if x == INF:
            result.append(0)
        else:
            result.append(x)
    print(*result)