import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
D = deque([(i+1, num) for i, num in enumerate(arr)])
result = []
while D:
  idx, move = D.popleft()
  result.append(idx)
  if not D:
    break
  if move > 0:
    D.rotate(-(move-1))
  else:
    D.rotate(-move)

print(*result)