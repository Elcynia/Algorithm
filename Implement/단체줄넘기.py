import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
height_count = {}

for i in arr:
  if i in height_count:
    height_count[i] = min(height_count[i] + 1, 2)
  else:
    height_count[i] = 1

res = sum(height_count.values())
print(res)