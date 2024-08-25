import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
mx = 0

LIS = [1] * N
for i in range(1, N):
  for j in range(i):
    if arr[i] > arr[j] and LIS[i] < LIS[j] + 1:
      LIS[i] = LIS[j] + 1

LDS = [1] * N
for i in range(N-2, -1, -1):
  for j in range(N-1, i, -1):
    if arr[i] > arr[j] and LDS[i] < LDS[j] + 1:
      LDS[i] = LDS[j] + 1

for i in range(N):
    mx = max(mx, LIS[i] + LDS[i] - 1)

print(mx)