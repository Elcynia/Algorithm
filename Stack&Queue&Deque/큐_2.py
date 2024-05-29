import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
Q = deque()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        Q.append(cmd[1])
    elif cmd[0] == 'pop':
        print(Q.popleft() if Q else -1)
    elif cmd[0] == 'size':
        print(len(Q))
    elif cmd[0] == 'empty':
        print(0 if Q else 1)
    elif cmd[0] == 'front':
        print(Q[0] if Q else -1)
    elif cmd[0] == 'back':
        print(Q[-1] if Q else -1)
    else:
        pass