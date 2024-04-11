import sys
sys.stdin = open('./input.txt', 'r')
def DFS(idx):
    global visited, ans, graph
    visited[idx] = 1
    ans += 1
    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]: # 연결 여부 체크
            DFS(i)

n = int(sys.stdin.readline()) # pc 개수
m = int(sys.stdin.readline()) # 연결된 pc 쌍의 개수
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
ans = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

DFS(1)
print (ans - 1)