import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
res = 0
for i in range(n):
  res = sum(a * b for a, b in zip(A, B))
print(res)