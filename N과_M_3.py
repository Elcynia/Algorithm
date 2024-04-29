import sys
#sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []

def DFS(v, n, m):
  if v == m:
    print (' '.join(map(str, arr)))
    return
  for i in range(1, n+1):
      arr.append(i)
      DFS(v+1, n, m)
      arr.pop()

DFS(0, n, m)