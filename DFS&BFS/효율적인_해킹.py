import sys
from collections import deque
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
max_cnt = 0
res = []

def BFS(v):
    global cnt
    visited[v] = 1
    cnt = 1
    Q = deque([v])
    while Q:
      node = Q.popleft()
      for i in graph[node]:
        if not visited[i]:
          visited[i] = 1
          cnt += 1
          Q.append(i)
    return cnt

for _ in range(M): # 연결 정보 입력
    A, B = map(int, input().split())
    graph[B].append(A)

for i in range(1, N+1):
    visited = [0] * (N+1)
    cnt = BFS(i)
    if cnt > max_cnt:
        max_cnt = cnt
        res = [i]
    elif cnt == max_cnt:
        res.append(i)

for r in res:
    print(r, end=' ')
