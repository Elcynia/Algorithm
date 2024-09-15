import sys
from collections import deque 
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
S = deque([])
ans = [0]*n

for i in range(n):
    while S and S[-1][1] < lst[i]:
        S.pop()
    if S:
        ans[i] = S[-1][0] + 1
    S.append((i, lst[i]))

print(*ans)