import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().strip().split()))

count = {}
start = 0
end = 0
mx_length = 0

while end < N:
    # 현재 숫자의 개수를 증가
    if arr[end] in count:
        count[arr[end]] += 1
    else:
        count[arr[end]] = 1
    
    # 현재 숫자의 개수가 K를 초과하면 start를 이동
    while count[arr[end]] > K:
        count[arr[start]] -= 1
        start += 1
    
    # 최대 길이 갱신
    mx_length = max(mx_length, end - start + 1)
    end += 1

print(mx_length)