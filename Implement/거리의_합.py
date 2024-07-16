import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
ans = 0
arr = list(map(int, input().split()))
for i in range(n):
  for j in range(n):
    ans += abs(arr[i] - arr[j])
print (ans)