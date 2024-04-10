import sys
sys.stdin = open('./input.txt', 'r')
n, m = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10**6)

def DFS(idx):
    global visited, graph
    visited[idx] = 1
    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]:
            DFS(i)
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
ans = 0
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1
for i in range(1, n+1):
    if not visited[i]:
        DFS(i)
        ans += 1
print (ans)