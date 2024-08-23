import sys
sys.stdin = open('./input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []

def func(start):
  if (len(s) == M):
    print (*s)
    return
  for i in range(start, N):
      s.append(arr[i])
      func(i+1)
      s.pop()
    
func(0)