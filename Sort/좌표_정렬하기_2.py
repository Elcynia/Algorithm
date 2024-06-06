import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  a, b = map(int, input().split())
  arr.append([a,b])
  
arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
  print(i[0], i[1])
  
  