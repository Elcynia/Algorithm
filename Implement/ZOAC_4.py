import sys, math
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
H, W, N, M = map(int, input().split())
rows = math.ceil(H / (N + 1))
cols = math.ceil(W / (M + 1))
r = rows * cols
print (r)