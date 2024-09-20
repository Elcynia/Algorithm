import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
L, R = 1, n
arr = []
while L < R:
    arr.extend([R, L])
    L += 1
    R -= 1

if L == R:
    arr.append(L)

print(*arr)