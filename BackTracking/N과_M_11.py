import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []

def func(start):
  if (len(s) == M):
    print (*s)
    return
  prev = -1
  for i in range(N):
    if prev != arr[i]:
      s.append(arr[i])
      func(i)
      prev = arr[i]
      s.pop()

func(0)