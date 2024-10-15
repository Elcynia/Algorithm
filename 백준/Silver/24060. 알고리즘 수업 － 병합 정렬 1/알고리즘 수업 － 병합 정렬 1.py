import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().strip().split()))

cnt = 0  
result = -1

def merge_sort(A, p, r):
  if p < r:
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
  global cnt, result, K
  tmp = []
  i, j = p, q + 1

  while i <= q and j <= r:
    if A[i] <= A[j]:
      tmp.append(A[i])
      i += 1
    else:
      tmp.append(A[j])
      j += 1
    cnt += 1
    if cnt == K:
      result = tmp[-1]

  while i <= q:
    tmp.append(A[i])
    i += 1
    cnt += 1
    if cnt == K:
      result = tmp[-1]

  while j <= r:
    tmp.append(A[j])
    j += 1
    cnt += 1
    if cnt == K:
      result = tmp[-1]

  for i in range(len(tmp)):
    A[p + i] = tmp[i]

merge_sort(arr, 0, len(arr) - 1)
print(result)