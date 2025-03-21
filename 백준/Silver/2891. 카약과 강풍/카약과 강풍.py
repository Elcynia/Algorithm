import sys
input = sys.stdin.readline
N, S, R = map(int, input().strip().split()) # 팀 수, 손상된 팀 수, 여분 카약 팀 수
damaged = list(map(int, input().strip().split())) # 카약 손상 팀 목록
extra = list(map(int, input().strip().split())) # 카약 하나 더 가져온 팀 목록

# 각 팀의 카약 상태를 나타내는 배열 (1: 정상, 0: 손상, 2: 여분 있음)
status = [1] * (N + 1)  # 1-indexed로 사용

# 손상된 카약 반영
for team in damaged:
    status[team] -= 1

# 여분 카약 반영
for team in extra:
    status[team] += 1


# 앞뒤로 빌려주기
for i in range(1, N):
    if status[i] == 0 and status[i+1] == 2:
        status[i] = 1
        status[i+1] = 1
    elif status[i] == 2 and status[i+1] == 0:
        status[i] = 1
        status[i+1] = 1

# 출발할 수 없는 팀 수 계산 (카약이 0개인 팀)
result = sum(1 for s in status[1:] if s == 0)

print(result)