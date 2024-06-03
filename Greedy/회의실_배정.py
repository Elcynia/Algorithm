import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  a, b = map(int, input().split())
  arr.append([a, b])
  
arr.sort(key=lambda x: (x[1], x[0]))
  
count = 0
last_end_time = 0

for start, end in arr:
    if start >= last_end_time:
        last_end_time = end
        count += 1

print(count)