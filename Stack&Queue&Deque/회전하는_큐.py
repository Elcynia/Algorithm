import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
pick = list(map(int, input().split()))
D = deque([i for i in range(1, n+1)])
cnt = 0

for i in pick:
  while True:
    if (D[0] == i):
      D.popleft()
      break
    else: 
      if D.index(i) < len(D)/2:
        while D[0] != i:
          D.rotate(-1) 
          cnt += 1
      else:
        D.rotate(1) 
        cnt += 1
print (cnt)
