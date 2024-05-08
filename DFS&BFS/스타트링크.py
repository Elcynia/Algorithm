import sys
from collections import deque
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
'''
F: 총 층수
S: 현재 층
G: 가야하는 층
U: 위로 U층
D: 아래로 D층
'''
F, S, G, U, D = map(int, input().split()) 
floor = [0 * (F+1) for _ in range(F+1)]

def BFS():
  Q = deque()
  Q.append(S)
  floor[S] = 1
  while Q:
    now = Q.popleft()
    if (now == G):
      return floor[now] - 1
    for i in [now + U, now - D]:
      if 1 <= i <= F and floor[i] == 0:
        floor[i] = floor[now] + 1
        Q.append(i)
  return "use the stairs"

print(BFS())
