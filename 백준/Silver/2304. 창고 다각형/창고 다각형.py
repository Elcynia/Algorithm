import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
roof = []

for _ in range(n):
    l, h = map(int, input().split())
    roof.append((l, h))
roof.sort()

# 가장 높은 막대를 찾음
max_height = 0
mx_idx = 0
for i in range(n):
    if roof[i][1] > max_height:
        max_height = roof[i][1]
        mx_idx = i

# 왼쪽에서부터 가장 높은 막대까지 면적 계산
area = 0
left_mx_height = roof[0][1]
for i in range(mx_idx):
    if roof[i][1] > left_mx_height:
        left_mx_height = roof[i][1]
    area += left_mx_height * (roof[i+1][0] - roof[i][0])

# 오른쪽에서부터 가장 높은 막대까지 면적 계산
right_mx_height = roof[-1][1]
for i in range(n-1, mx_idx, -1):
    if roof[i][1] > right_mx_height:
        right_mx_height = roof[i][1]
    area += right_mx_height * (roof[i][0] - roof[i-1][0])

area += max_height
print(area)
