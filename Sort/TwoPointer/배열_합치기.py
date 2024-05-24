import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
arr = []
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
j = 0
while i < n and j < m:
  if a[i] <= b[j]:
    arr.append(a[i])
    i += 1
  else:
    arr.append(b[j])
    j += 1
arr += a[i:]
arr += b[j:]
print(*arr)
