import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
acc = 0 # SUM
min_length = float('inf')

while True:
    if acc >= S:
        min_length = min(min_length, right - left)
        acc -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        acc += arr[right]
        right += 1

print(0 if min_length == float('inf') else min_length)