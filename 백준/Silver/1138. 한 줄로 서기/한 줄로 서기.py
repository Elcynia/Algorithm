import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

r = [0] * n
for i in range(1, n+1):
    left_people = arr[i-1]
    cnt = 0
    for j in range(n):
        if cnt == left_people and r[j] == 0:
            r[j] = i
            break
        elif r[j] == 0:
            cnt += 1

print(*r)