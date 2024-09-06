import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
rank = 1

for _ in range(N):
    country = list(map(int, input().split()))
    arr.append(country)

arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if i > 0 and arr[i][1:] != arr[i-1][1:]:
        rank = i + 1
    if arr[i][0] == K:
        print(rank)
        break