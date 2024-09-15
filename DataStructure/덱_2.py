import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
S = deque()

def Add1(x):
    S.appendleft(x)
    
def Add2(x):
    S.append(x)

def Remove1():
    if len(S) == 0:
        print(-1)
    else:
        print(S.popleft())
        
def Remove2():
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

def Front1():
    if len(S) == 0:
        print(-1)
    else:
        print(S[0])
        
def Front2():
    if len(S) == 0:
        print(-1)
    else:
        print(S[-1])

n = int(input())

for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        Add1(cmd[1])
    elif cmd[0] == 2:
        Add2(cmd[1])
    elif cmd[0] == 3:
        Remove1()
    elif cmd[0] == 4:
        Remove2()
    elif cmd[0] == 5:
        Size()
    elif cmd[0] == 6:
        Empty()
    elif cmd[0] == 7:
        Front1()
    elif cmd[0] == 8:
        Front2()
