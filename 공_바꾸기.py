import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(range(n+1))
for i in range(m):
  a, b = map(int, input().split())
  arr[a], arr[b] = arr[b], arr[a]
  
print(*arr[1:])