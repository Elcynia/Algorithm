import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
v = int(input())
ans = 0
for i in range(n):
    if arr[i] == v:
        ans += 1

print (ans)