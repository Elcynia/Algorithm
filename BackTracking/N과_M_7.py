import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []

def func():
  if (len(s) == M):
    print (*s)
    return
  for i in range(N):
    s.append(arr[i])
    func()
    s.pop()
    
func()