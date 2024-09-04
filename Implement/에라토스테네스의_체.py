import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
arr = [True] * (N + 1)
cnt = 0

for i in range(2, N+1):
  for j in range(i, N+1, i):
    if arr[j]:
      arr[j] = False
      cnt += 1
      if cnt == K:
        print (j)
        break
      
      
# arr = [i for i in range(2, N+1)]
# for i in range(len(arr)):
#   p = arr[i]
#   if p != 0:
#     for j in range(i, len(arr)):
#       if arr[j] != 0 and arr[j] % p == 0:
#         cnt += 1
#         if cnt == K:
#           print(arr[j])
#           break
#         arr[j] = 0 