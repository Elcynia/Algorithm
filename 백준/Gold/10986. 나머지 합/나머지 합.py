import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
result = [0] * (N+1)
cnt = [0] * M  # M으로 나눈 나머지의 개수
cnt[0] = 1  # 초기 누적합(0)의 나머지는 0
answer = 0

for i in range(1, N+1):
    result[i] = (result[i-1] + arr[i-1]) % M
    # 현재까지의 누적합과 같은 나머지를 가진 이전 누적합들과 쌍을 이루면
    # 그 구간의 합이 M으로 나누어 떨어짐
    answer += cnt[result[i]]
    cnt[result[i]] += 1

print(answer)