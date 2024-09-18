import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(input().strip())
cnt = 0
for i in range(N):
  if (arr[i] == 'P'):
    for j in range(max(0, i-K), min(N, i+K+1)): # K 범위 내 햄버거 범위만
      if arr[j] == 'H':
        arr[j] = '-'
        cnt += 1
        break
print (cnt)