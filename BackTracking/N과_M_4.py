import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
s = []

def dfs(start):
  if len(s) == M: # M개 고르면 종료
    print (*s, sep=' ')
    return
    
  for i in range(start, N + 1):
    s.append(i)
    dfs(i)
    s.pop()

dfs(1)