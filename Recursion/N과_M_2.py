import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
visited = [False] * (n+1)
arr = []

def DFS(v, cnt):
  if cnt == m:
    print (' '.join(map(str, arr)))
    return
  for i in range(v, n+1):
    if not visited[i]:
      visited[i] = True
      arr.append(i)
      DFS(i, cnt+1)
      visited[i] = False
      arr.pop()
    
DFS(1, 0)