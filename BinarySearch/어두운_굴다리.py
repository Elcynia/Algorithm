import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input()) # 굴다리
M = int(input()) # 가로등 수
street_lamp_position = sorted(list(map(int, input().split())))
max_distance = 0

# 첫 굴다리 지점과 첫 가로등 사이의 거리
max_distance = max(max_distance, street_lamp_position[0])

# 인접한 가로등 사이의 거리
for i in range(1, M):
    distance = street_lamp_position[i] - street_lamp_position[i-1] # 2
    min_height =  (distance + 1) // 2 # 가로등 높이는 max_distance에서 최소 1/2 이상이 되어야 조건에 부합
    max_distance = max(max_distance, min_height)

# 굴다리 끝과 마지막 가로등 사이의 거리
max_distance = max(max_distance, N - street_lamp_position[-1])

print(max_distance)