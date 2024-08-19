import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, S = map(int, input().split())
arr = list(map(int,input().split()))
cnt = 0
def func(k, total):
  global cnt
  if (k == N):
    if (total == S):
      cnt += 1
    return
  func(k+1, total)
  func(k+1, total+arr[k])
  
func(0, 0)
if (S == 0):
  cnt -= 1
print (cnt)