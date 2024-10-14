import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input())
types = list(map(int, input().strip().split())) # 0: queue, 1: stack
arr1 = list(map(int, input().strip().split()))
M = int(input())
arr2 = list(map(int, input().strip().split()))
Q = deque()
r = []

for i in range(N):
  if types[i] == 0:
    Q.append(arr1[i])

for x in arr2:
  Q.appendleft(x)
  print(Q.pop(), end=' ')