import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
P = int(input())
for _ in range(P):
  arr = list(map(int, input().split()))
  T = arr[0]
  arr = arr[1:]
  total = 0
  r = []
  for i in arr:
    tmp = 0
    for j in range(len(r)-1, -1, -1):
      if r[j] > i:
        tmp += 1
      else:
        break
    r.insert(len(r)-tmp, i)
    total += tmp
  print (T, total) 