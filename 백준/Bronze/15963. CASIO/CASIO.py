import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
print(1 if N == M else 0)