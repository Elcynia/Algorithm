import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
ans = 0

MAX = sum(arr)

for i in range(8):
  for j in range(i+1, 9):
    if (MAX - arr[i] - arr[j] == 100):
      a, b = arr[i], arr[j]
      break

arr.remove(a)
arr.remove(b)
for i in sorted(arr):
  print (i)