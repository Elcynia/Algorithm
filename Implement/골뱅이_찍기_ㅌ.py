import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input())
for _ in range(N): print('@@@@@'*N)
for _ in range(N): print('@'*N)
for _ in range(N): print('@@@@@'*N)
for _ in range(N): print('@'*N)
for _ in range(N): print('@@@@@'*N)