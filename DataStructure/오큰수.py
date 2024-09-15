import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = [int(i) for i in input().split()]
S = []
res = [-1] * n

for i in range(n):
  while S and arr[S[-1]] < arr[i]:
    p = S.pop()
    res[p] = arr[i]
  S.append(i)
print (*res)