import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# bottom-up
for i in range(n-2, -1, -1):
    for j in range(len(arr[i])):
        arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])

print(arr[0][0])