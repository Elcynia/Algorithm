import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, B = input().split()
B = int(B)
res = int(N, B)

print(res)
