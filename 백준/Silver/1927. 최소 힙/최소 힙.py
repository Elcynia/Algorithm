import sys, heapq
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
  digit = int(input())
  if digit == 0:
    if arr:
      print(heapq.heappop(arr))
    else:
      print(0)
  else:
    heapq.heappush(arr, digit)