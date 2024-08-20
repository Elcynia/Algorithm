import sys
sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []

def dfs():
  if (len(s) == M):
    print (*s, sep=' ')
    return
  for i in range(N):
    if arr[i] not in s: # 중복 체크
      s.append(arr[i])
      dfs()
      s.pop()
    
dfs()