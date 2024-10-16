import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
A, B = map(int, input().split())
M = (B - A) / 400
P = 1 / (1 + 10**M)
print(f"{P:.6f}")