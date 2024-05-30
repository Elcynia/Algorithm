import sys
from collections import deque
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
S = deque(map(int, input().split()))

def dessert(S):
    arr = deque()
    cur = 1

    while S:
        if S[0] == cur:
            S.popleft()
            cur += 1
        else:
            if arr and arr[-1] == cur:
                arr.pop()
                cur += 1
            else:
                arr.append(S.popleft())
    while arr:
        if arr[-1] == cur:
            arr.pop()
            cur += 1
        else:
            return False

    return True

if dessert(S):
    print("Nice")
else:
    print("Sad")