import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

def func(start, idx):
  if start == M:
    print (*ans)
    return
  prev = -1
  for i in range(idx, N):
    if prev != arr[i]:
      ans.append(arr[i])
      func(start + 1, i)
      prev = arr[i]
      ans.pop()

func(0, 0)
