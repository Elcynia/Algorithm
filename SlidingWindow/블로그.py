import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, X  = map(int, input().split())
visitors = list(map(int, input().split()))

tmp = sum(visitors[:X])
mx_visitors = tmp
cnt = 1

for i in range(X, N):
  tmp = tmp + visitors[i] - visitors[i-X]
  if tmp > mx_visitors:
    mx_visitors = tmp
    cnt = 1
  elif tmp == mx_visitors:
    cnt += 1
    
if (mx_visitors == 0):
  print ('SAD')
else:
  print (mx_visitors)
  print (cnt)