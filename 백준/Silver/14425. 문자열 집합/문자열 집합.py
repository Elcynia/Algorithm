import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().strip().split())
arr1 = {input().strip() for _ in range(N)}
arr2 = [input().strip() for _ in range(M)]
cnt = 0
for char in arr2:
  if char in arr1:
    cnt += 1
print (cnt)