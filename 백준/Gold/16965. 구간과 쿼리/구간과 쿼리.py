import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = []

def Move(a, b):
  return (b[0] < a[0] < b[1]) or (b[0] < a[1] < b[1])

def BFS(s, e):
  Q = deque([s])
  visited = [s]
  
  while Q:
    cur = Q.popleft()
    if cur == e:
      return 1
    
    for i in range(len(arr)):
      if i not in visited and Move(arr[cur], arr[i]):
        Q.append(i)
        visited.append(i)
  
  return 0

for _ in range(n):
  query = list(map(int, input().strip().split()))
  if query[0] == 1:
    arr.append((query[1], query[2]))
  else:
    if len(arr) < 2: # 구간이 2개 미만일 경우 0 출력 (비교하기 위해 최소 2개 구간이 필요하므로)
      print(0)
    else:
      print(BFS(query[1] - 1, query[2] - 1))