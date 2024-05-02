import sys
from collections import deque as dq
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
queue = dq([i for i in range(1, n+1)])
for i in range(n-1):
    for j in range(k-1):
        queue.append(queue.popleft())
    arr.append(queue.popleft())
print('<', end='')
for i in arr:
    print(i, end=', ')
print(queue[0], end='>')
