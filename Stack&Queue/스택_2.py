import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
S = deque()

def Add(x):
    S.append(x)

def Remove():
    if len(S) == 0:
        print(-1)
    else:
        print(S.pop())

def Size():
    print(len(S))

def Empty():
    if len(S) == 0:
        print(1)
    else:
        print(0)

def Front():
    if len(S) == 0:
        print(-1)
    else:
        print(S[-1])

n = int(input())

for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        Add(cmd[1])
    elif cmd[0] == 2:
        Remove()
    elif cmd[0] == 3:
        Size()
    elif cmd[0] == 4:
        Empty()
    elif cmd[0] == 5:
        Front()
