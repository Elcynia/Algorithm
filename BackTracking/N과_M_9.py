import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * (N)
arr.sort()
ans = []

def func(start):
  if start == M:
    print(*ans)
    return
  prev = 0
  for i in range(N):
    if not visited[i] and prev != arr[i]:
      visited[i] = True
      ans.append(arr[i])
      prev = arr[i]
      func(start + 1)
      visited[i] = False
      ans.pop()
  
func(0)